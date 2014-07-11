# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402179425.867361
_template_filename='/home/jliao/src/reddit/r2/r2/templates/pagenamenav.html'
_template_uri='/pagenamenav.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['domain', 'help', 'nomenu', 'subreddits', 'subreddit', 'newpagelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f8c8daac210', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8daac210')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daac210')._populate(_import_ns, [u'plain_link', u'_md'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n')
        # SOURCE LINE 61
        __M_writer(u'\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n')
        # SOURCE LINE 71
        __M_writer(u'\n\n')
        # SOURCE LINE 75
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_domain(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daac210')._populate(_import_ns, [u'plain_link', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n  <div id="sr-name-box">\n    <span class="hover pagename redditname">\n      ')
        # SOURCE LINE 37
        __M_writer(mako_websafe(plain_link(getattr(c.site, "idn", c.site.name), c.site.path, _sr_path=False)))
        __M_writer(u'\n')
        # SOURCE LINE 38
        if hasattr(thing, "title"):
            # SOURCE LINE 39
            __M_writer(u'        : ')
            __M_writer(mako_websafe(thing.title))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'    </span>\n')
        # SOURCE LINE 42
        if hasattr(c.site, "idn"):
            # SOURCE LINE 43
            __M_writer(u'    <span class="help help-hoverable tooltip">\n      ')
            # SOURCE LINE 44
            __M_writer(mako_websafe(c.site.name))
            __M_writer(u'\n      <div id="idn-help" class="hover-bubble help-bubble anchor-top-left">\n        <div class="help-section help-idn">\n          <p>\n            ')
            # SOURCE LINE 48
            __M_writer(mako_websafe(_md("This is an [internationalized domain name](http://en.wikipedia.org/wiki/Internationalized_domain_name).  We've modified how it is displayed [for security reasons](http://en.wikipedia.org/wiki/IDN_homograph_attack).")))
            __M_writer(u'\n          </p>\n        </div>\n      </div>\n    </span>\n')
            pass
        # SOURCE LINE 54
        __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_help(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daac210')._populate(_import_ns, [u'plain_link', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 67
        __M_writer(u'\n  <span class="hover pagename redditname">\n    ')
        # SOURCE LINE 69
        __M_writer(mako_websafe(plain_link(thing.title, "/wiki", _sr_path=False)))
        __M_writer(u'\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nomenu(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daac210')._populate(_import_ns, [u'plain_link', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 63
        __M_writer(u'\n<span class="pagename selected">')
        # SOURCE LINE 64
        __M_writer(mako_websafe(thing.title))
        __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subreddits(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daac210')._populate(_import_ns, [u'plain_link', u'_md'])
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n  <span class="hover pagename redditname">\n    ')
        # SOURCE LINE 59
        __M_writer(mako_websafe(plain_link(_("subreddits"), "/subreddits/", _sr_path=False)))
        __M_writer(u'\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subreddit(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daac210')._populate(_import_ns, [u'plain_link', u'_md'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n  <span class="hover pagename redditname">\n    ')
        # SOURCE LINE 27
        __M_writer(mako_websafe(plain_link(c.site.name, c.site.path, _sr_path=False)))
        __M_writer(u'\n')
        # SOURCE LINE 28
        if hasattr(thing, "title"):
            # SOURCE LINE 29
            __M_writer(u'      : ')
            __M_writer(mako_websafe(thing.title))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 31
        __M_writer(u'  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_newpagelink(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daac210')._populate(_import_ns, [u'plain_link', u'_md'])
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(u'\n<span class="newpagelink">reddit all?&#32;')
        # SOURCE LINE 74
        __M_writer(mako_websafe(plain_link("click here to find new links.", "/new/", _sr_path=False)))
        __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


