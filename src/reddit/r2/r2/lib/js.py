#!/usr/bin/env python
# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
#
# The Original Code is reddit.
#
# The Original Developer is the Initial Developer.  The Initial Developer of
# the Original Code is reddit Inc.
#
# All portions of the code written by reddit are Copyright (c) 2006-2014 reddit
# Inc. All Rights Reserved.
###############################################################################

import inspect
import sys
import os.path
from subprocess import Popen, PIPE
import re
import json

from r2.lib.translation import (
    extract_javascript_msgids,
    get_catalog,
    iter_langs,
    validate_plural_forms,
)
from r2.lib.plugin import PluginLoader
from r2.lib.permissions import ModeratorPermissionSet


try:
    from pylons import g, c, config
except ImportError:
    STATIC_ROOT = None
else:
    REDDIT_ROOT = config["pylons.paths"]["root"]
    STATIC_ROOT = config["pylons.paths"]["static_files"]

# STATIC_ROOT will be None if pylons is uninitialized
if not STATIC_ROOT:
    REDDIT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_ROOT = os.path.join(os.path.dirname(REDDIT_ROOT), "build/public")


script_tag = '<script type="text/javascript" src="{src}"></script>\n'
inline_script_tag = '<script type="text/javascript">{content}</script>'


class ClosureError(Exception): pass


class ClosureCompiler(object):
    def __init__(self, jarpath):
        self.jarpath = jarpath
        self.args = [
            "--jscomp_off=internetExplorerChecks",
        ]

    def _run(self, data, out=PIPE, args=None, expected_code=0):
        args = args or []
        p = Popen(["java", "-jar", self.jarpath] + self.args + args,
                stdin=PIPE, stdout=out, stderr=PIPE)
        out, msg = p.communicate(data)
        if p.returncode != expected_code:
            raise ClosureError(msg)
        else:
            return out, msg

    def compile(self, data, dest, args=None):
        """Run closure compiler on a string of source code `data`, writing the
        result to output file `dest`. A ClosureError exception will be raised if
        the operation is unsuccessful."""
        return self._run(data, dest, args)[0]


class Source(object):
    """An abstract collection of JavaScript code."""
    def get_source(self):
        """Return the full JavaScript source code."""
        raise NotImplementedError

    def use(self):
        """Return HTML to insert the JavaScript source inside a template."""
        raise NotImplementedError

    @property
    def dependencies(self):
        raise NotImplementedError

    @property
    def outputs(self):
        raise NotImplementedError


class FileSource(Source):
    """A JavaScript source file on disk."""
    def __init__(self, name):
        self.name = name

    def get_source(self):
        with open(self.path) as f:
            return f.read()

    @property
    def path(self):
        """The path to the source file on the filesystem."""

        from r2.lib.static import locate_static_file

        try:
            g.plugins
        except TypeError:
            # g.plugins isn't available. this means we're in the build system.
            # we can safely find all files in one place in this case since the
            # build system copies them in from plugins first.
            pass
        else:
            # this is in-request. we should check all the plugin directories
            return locate_static_file(os.path.join("static", "js", self.name))

        return os.path.join(STATIC_ROOT, "static", "js", self.name)

    def use(self):
        from r2.lib.template_helpers import static
        path = [g.static_path, self.name]
        if g.uncompressedJS:
            path.insert(1, "js")
        return script_tag.format(src=static(os.path.join(*path)))

    @property
    def dependencies(self):
        return [self.path]


class Module(Source):
    """A module of JS code consisting of a collection of sources."""
    def __init__(self, name, *sources, **kwargs):
        self.name = name
        self.should_compile = kwargs.get('should_compile', True)
        self.wrap = kwargs.get('wrap')
        self.sources = []
        sources = sources or (name,)
        for source in sources:
            if not isinstance(source, Source):
                if 'prefix' in kwargs:
                    source = os.path.join(kwargs['prefix'], source)
                source = FileSource(source)
            self.sources.append(source)

    def get_source(self):
        return ";".join(s.get_source() for s in self.sources)

    def extend(self, module):
        self.sources.extend(module.sources)

    @property
    def path(self):
        """The destination path of the module file on the filesystem."""
        return os.path.join(STATIC_ROOT, "static", self.name)

    def build(self, closure):
        with open(self.path, "w") as out:
            source = self.get_source()
            if self.wrap:
                source = self.wrap.format(content=source, name=self.name)

            if self.should_compile:
                print >> sys.stderr, "Compiling {0}...".format(self.name),
                closure.compile(source, out)
            else:
                print >> sys.stderr, "Concatenating {0}...".format(self.name),
                out.write(source)
        print >> sys.stderr, " done."

    def use(self):
        from r2.lib.template_helpers import static
        if g.uncompressedJS:
            return "".join(source.use() for source in self.sources)
        else:
            return script_tag.format(src=static(self.name))

    @property
    def dependencies(self):
        deps = []
        for source in self.sources:
            deps.extend(source.dependencies)
        return deps

    @property
    def outputs(self):
        return [self.path]


class DataSource(Source):
    """A generated source consisting of wrapped JSON data."""
    def __init__(self, wrap, data=None):
        self.wrap = wrap
        self.data = data

    def get_content(self):
        return self.data

    def get_source(self):
        content = self.get_content()
        json_data = json.dumps(content)
        return self.wrap.format(content=json_data) + "\n"

    def use(self):
        from r2.lib.filters import SC_OFF, SC_ON, websafe_json
        escaped_json = websafe_json(self.get_source())
        return (SC_OFF + inline_script_tag.format(content=escaped_json) +
                SC_ON + "\n")

    @property
    def dependencies(self):
        return []


class PermissionsDataSource(DataSource):
    """DataSource for PermissionEditor configuration data."""

    def __init__(self, permission_sets):
        self.permission_sets = permission_sets

    @classmethod
    def _make_marked_json(cls, obj):
        """Return serialized psuedo-JSON with translation support.

        Strings are marked for extraction with r.N_. Dictionaries are
        serialized to JSON objects as normal.

        """
        if isinstance(obj, dict):
            props = []
            for key, value in obj.iteritems():
                value_encoded = cls._make_marked_json(value)
                props.append("%s: %s" % (key, value_encoded))
            return "{%s}" % ",".join(props)
        elif isinstance(obj, basestring):
            return "r.N_(%s)" % json.dumps(obj)
        else:
            raise ValueError, "unsupported type"

    def get_source(self):
        permission_set_info = {k: v.info for k, v in
                               self.permission_sets.iteritems()}
        permissions = self._make_marked_json(permission_set_info)
        return "r.permissions = _.extend(r.permissions || {}, %s)" % permissions

    @property
    def dependencies(self):
        dependencies = set(super(PermissionsDataSource, self).dependencies)
        for permission_set in self.permission_sets.itervalues():
            dependencies.add(inspect.getsourcefile(permission_set))
        return list(dependencies)


class TemplateFileSource(DataSource, FileSource):
    """A JavaScript template file on disk."""
    def __init__(self, name, wrap="r.templates.set({content})"):
        DataSource.__init__(self, wrap)
        FileSource.__init__(self, name)
        self.name = name

    def get_content(self):
        from r2.lib.static import locate_static_file
        name, style = os.path.splitext(self.name)
        path = locate_static_file(os.path.join('static/js', self.name))
        with open(path) as f:
            return [{
                "name": name,
                "style": style.lstrip('.'),
                "template": f.read()
            }]


class LocaleSpecificSource(object):
    def get_localized_source(self, lang):
        raise NotImplementedError


class StringsSource(LocaleSpecificSource):
    """Translations sourced from a gettext catalog."""

    def __init__(self, keys):
        self.keys = keys

    invalid_formatting_specifier_re = re.compile(r"(?<!%)%\w|(?<!%)%\(\w+\)[^s]")
    def _check_formatting_specifiers(self, string):
        if not isinstance(string, basestring):
            return

        if self.invalid_formatting_specifier_re.search(string):
            raise ValueError("Invalid string formatting specifier: %r" % string)

    def get_localized_source(self, lang):
        catalog = get_catalog(lang)

        # relies on pyx files, so it can't be imported at global scope
        from r2.lib.utils import tup

        data = {}
        for key in self.keys:
            key = tup(key)[0]  # because the key for plurals is (sing, plur)
            self._check_formatting_specifiers(key)
            msg = catalog[key]

            if not msg or not msg.string:
                continue

            # jed expects to ignore the first value in the translations array
            # so we'll just make it null
            strings = tup(msg.string)
            data[key] = [None] + list(strings)
        return "r.i18n.addMessages(%s)" % json.dumps(data)


class PluralForms(LocaleSpecificSource):
    def get_localized_source(self, lang):
        catalog = get_catalog(lang)
        validate_plural_forms(catalog.plural_expr)
        return "r.i18n.setPluralForms('%s')" % catalog.plural_expr


class LocalizedModule(Module):
    """A module that generates localized code for each language.

    Strings marked for translation with one of the functions in i18n.js (viz.
    r._, r.P_, and r.N_) are extracted from the source and their translations
    are built into the compiled source.

    """

    def __init__(self, *args, **kwargs):
        self.localized_appendices = kwargs.pop("localized_appendices", [])
        Module.__init__(self, *args, **kwargs)

    @staticmethod
    def languagize_path(path, lang):
        path_name, path_ext = os.path.splitext(path)
        return path_name + "." + lang + path_ext

    def build(self, closure):
        Module.build(self, closure)

        with open(self.path) as f:
            reddit_source = f.read()

        localized_appendices = self.localized_appendices
        msgids = extract_javascript_msgids(reddit_source)
        if msgids:
            localized_appendices = localized_appendices + [StringsSource(msgids)]

        print >> sys.stderr, "Creating language-specific files:"
        for lang, unused in iter_langs():
            lang_path = LocalizedModule.languagize_path(self.path, lang)

            # make sure we're not rewriting a different mangled file
            # via symlink
            if os.path.islink(lang_path):
                os.unlink(lang_path)

            with open(lang_path, "w") as out:
                print >> sys.stderr, "  " + lang_path
                out.write(reddit_source)
                for appendix in localized_appendices:
                    out.write(appendix.get_localized_source(lang) + ";")

    def use(self):
        from pylons.i18n import get_lang
        from r2.lib.template_helpers import static
        from r2.lib.filters import SC_OFF, SC_ON

        if g.uncompressedJS:
            if c.lang == "en" or c.lang not in g.all_languages:
                # in this case, the msgids *are* the translated strings and we
                # can save ourselves the pricey step of lexing the js source
                return Module.use(self)

            msgids = extract_javascript_msgids(Module.get_source(self))
            localized_appendices = self.localized_appendices + [StringsSource(msgids)]

            lines = [Module.use(self)]
            for appendix in localized_appendices:
                line = SC_OFF + inline_script_tag.format(
                    content=appendix.get_localized_source(c.lang)) + SC_ON
                lines.append(line)
            return "\n".join(lines)
        else:
            langs = get_lang() or [g.lang]
            url = LocalizedModule.languagize_path(self.name, langs[0])
            return script_tag.format(src=static(url))

    @property
    def outputs(self):
        for lang, unused in iter_langs():
            yield LocalizedModule.languagize_path(self.path, lang)


class JQuery(Module):
    versions = {
        1: "1.11.1",
        2: "2.1.1",
    }

    def __init__(self, cdn_url="http://ajax.googleapis.com/ajax/libs/jquery/{version}/jquery", major_version=1):
        self.jquery_src = FileSource("lib/jquery-{0}.min.js".format(self.versions[major_version]))
        Module.__init__(self, "jquery-{0}.min.js".format(self.versions[major_version]), self.jquery_src, should_compile=False)
        self.cdn_src = cdn_url.format(version=self.versions[major_version])

    def use(self):
        from r2.lib.template_helpers import static
        if c.secure or (c.user and c.user.pref_local_js):
            return Module.use(self)
        else:
            ext = ".js" if g.uncompressedJS else ".min.js"
            return script_tag.format(src=self.cdn_src+ext)


module = {}


module["jquery1x"] = JQuery(major_version=1)
module["jquery2x"] = JQuery(major_version=2)


module["html5shiv"] = Module("html5shiv.js",
    "lib/html5shiv.js",
    should_compile=False
)

catch_errors = "try {{ {content} }} catch (err) {{ r.sendError('Error running module', '{name}', ':', err) }}"

module["reddit-init"] = LocalizedModule("reddit-init.js",
    "lib/es5-shim.js",
    "lib/json2.js",
    "lib/underscore-1.4.4.js",
    "lib/store.js",
    "lib/jed.js",
    "base.js",
    "preload.js",
    "logging.js",
    "client-error-logger.js",
    "jquery.html-patch.js",
    "uibase.js",
    "i18n.js",
    "utils.js",
    "analytics.js",
    "jquery.reddit.js",
    "reddit.js",
    "spotlight.js",
    localized_appendices=[
        PluralForms(),
    ],
    wrap=catch_errors,
)

module["reddit"] = LocalizedModule("reddit.js",
    "lib/jquery.cookie.js",
    "lib/jquery.url.js",
    "lib/backbone-1.0.0.js",
    "templates.js",
    "scrollupdater.js",
    "timetext.js",
    "ui.js",
    "login.js",
    "flair.js",
    "interestbar.js",
    "visited.js",
    "wiki.js",
    "apps.js",
    "gold.js",
    "multi.js",
    "recommender.js",
    "saved.js",
    PermissionsDataSource({
        "moderator": ModeratorPermissionSet,
        "moderator_invite": ModeratorPermissionSet,
    }),
    wrap=catch_errors,
)

module["admin"] = Module("admin.js",
    # include Backbone so it is available early to render admin bar fast.
    "lib/backbone-1.0.0.js",
    "adminbar.js",
)

module["mobile"] = LocalizedModule("mobile.js",
    module["reddit"],
    "lib/jquery.lazyload.js",
    "compact.js"
)


module["button"] = Module("button.js",
    "lib/jquery.cookie.js",
    "jquery.reddit.js",
    "blogbutton.js"
)


module["policies"] = Module("policies.js",
    "policies.js",
)


module["sponsored"] = Module("sponsored.js",
    "lib/ui.core.js",
    "lib/ui.datepicker.js",
    "sponsored.js"
)


module["timeseries"] = Module("timeseries.js",
    "lib/jquery.flot.js",
    "lib/jquery.flot.time.js",
    "timeseries.js",
)


module["timeseries-ie"] = Module("timeseries-ie.js",
    "lib/excanvas.min.js",
    module["timeseries"],
)


module["traffic"] = LocalizedModule("traffic.js",
    "traffic.js",
)


module["qrcode"] = Module("qrcode.js",
    "lib/jquery.qrcode.min.js",
    "qrcode.js",
)


module["highlight"] = Module("highlight.js",
    "lib/highlight.pack.js",
    "highlight.js",
)

module["less"] = Module('less.js',
    'lib/less-1.4.2.js',
    should_compile=False,
)

def use(*names):
    return "\n".join(module[name].use() for name in names)


def load_plugin_modules(plugins=None):
    if not plugins:
        plugins = PluginLoader()
    for plugin in plugins:
        plugin.add_js(module)


commands = {}
def build_command(fn):
    def wrapped(*args):
        load_plugin_modules()
        fn(*args)
    commands[fn.__name__] = wrapped
    return wrapped


@build_command
def enumerate_modules():
    for name, m in module.iteritems():
        print name


@build_command
def dependencies(name):
    for dep in module[name].dependencies:
        print dep


@build_command
def enumerate_outputs(*names):
    if names:
        modules = [module[name] for name in names]
    else:
        modules = module.itervalues()

    for m in modules:
        for output in m.outputs:
            print output


@build_command
def build_module(name):
    closure = ClosureCompiler("r2/lib/contrib/closure_compiler/compiler.jar")
    module[name].build(closure)


if __name__ == "__main__":
    commands[sys.argv[1]](*sys.argv[2:])

module["navbar"] = LocalizedModule("navbar.js",
    "vendor/bootstrap.js",
    "vendor/sb-admin.js",
    "signForm.js"
)
