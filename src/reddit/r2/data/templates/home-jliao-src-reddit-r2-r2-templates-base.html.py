# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402178932.266418
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/base.html'
_template_uri=u'/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['head', 'javascript_bottom', 'Title', 'javascript', 'robots', 'keywords', 'stylesheet', 'javascript_run', 'bodyContent', 'pagemeta', 'viewport']


# SOURCE LINE 24

from r2.lib.template_helpers import static
from r2.models import Link, Comment, Subreddit
from r2.lib import tracking


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7f8c8d97eb10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8d97eb10')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        js_setup = _import_ns.get('js_setup', context.get('js_setup', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<!doctype html>\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n<html xmlns="http://www.w3.org/1999/xhtml" lang="')
        # SOURCE LINE 30
        __M_writer(mako_websafe(c.lang))
        __M_writer(u'" \n      xml:lang="')
        # SOURCE LINE 31
        __M_writer(mako_websafe(c.lang))
        __M_writer(u'">\n  <head>\n    <title>')
        # SOURCE LINE 33
        __M_writer(mako_websafe(self.Title()))
        __M_writer(u'</title>\n    <meta name="keywords" content="')
        # SOURCE LINE 34
        __M_writer(mako_websafe(self.keywords()))
        __M_writer(u'" />\n    <meta name="description" content="')
        # SOURCE LINE 35
        __M_writer(mako_websafe(getattr(thing, 'short_description', None) or g.short_description))
        __M_writer(u'" />\n')
        # SOURCE LINE 36
        if getattr(thing, 'meta_thumbnail', None):
            # SOURCE LINE 37
            __M_writer(u'      <meta name="og:image" content="')
            __M_writer(mako_websafe(thing.meta_thumbnail))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 39
        __M_writer(u'    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n    ')
        # SOURCE LINE 40
        __M_writer(mako_websafe(self.viewport()))
        __M_writer(u'\n    ')
        # SOURCE LINE 41
        __M_writer(mako_websafe(self.robots()))
        __M_writer(u'\n    ')
        # SOURCE LINE 42
        __M_writer(mako_websafe(self.pagemeta()))
        __M_writer(u'\n    ')
        # SOURCE LINE 43
        __M_writer(mako_websafe(self.stylesheet()))
        __M_writer(u'\n    ')
        # SOURCE LINE 44
        __M_writer(mako_websafe(self.javascript()))
        __M_writer(u'\n    ')
        # SOURCE LINE 45
        __M_writer(mako_websafe(js_setup(getattr(thing, "extra_js_config", None))))
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'    <script type="text/javascript">\n      ')
        # SOURCE LINE 49
        __M_writer(mako_websafe(self.javascript_run()))
        __M_writer(u'\n    </script>\n    <style type="text/css">\n      ')
        # SOURCE LINE 52
        __M_writer(mako_websafe(unsafe(_("/* Custom css: use this block to insert special translation-dependent css in the page header */"))))
        __M_writer(u'\n    </style>\n\n    ')
        # SOURCE LINE 55
        __M_writer(mako_websafe(self.head()))
        __M_writer(u'\n  </head>\n\n  <body ')
        # SOURCE LINE 58
        __M_writer(mako_websafe(classes(*thing.page_classes())))
        __M_writer(u'>\n    ')
        # SOURCE LINE 59
        __M_writer(mako_websafe(self.bodyContent()))
        __M_writer(u'\n    ')
        # SOURCE LINE 60
        __M_writer(mako_websafe(self.javascript_bottom()))
        __M_writer(u'\n  </body>\n</html>\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 73
        __M_writer(u'\n\n')
        # SOURCE LINE 77
        __M_writer(u'\n\n')
        # SOURCE LINE 83
        __M_writer(u'\n\n')
        # SOURCE LINE 86
        __M_writer(u'\n\n')
        # SOURCE LINE 102
        __M_writer(u'\n\n')
        # SOURCE LINE 105
        __M_writer(u'\n\n')
        # SOURCE LINE 108
        __M_writer(u'\n\n')
        # SOURCE LINE 111
        __M_writer(u'\n\n')
        # SOURCE LINE 114
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        googleanalytics = _import_ns.get('googleanalytics', context.get('googleanalytics', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 88
        __M_writer(u'\n')
        # SOURCE LINE 89
        if g.tracker_url and thing.site_tracking:
            # SOURCE LINE 90
            __M_writer(u'<script type="text/javascript">\n    (function() {\n        var url = \'')
            # SOURCE LINE 92
            __M_writer(mako_websafe(tracking.get_pageview_pixel_url()))
            __M_writer(u'\';\n        var cachebuster = Math.round(Math.random() * 2147483647);\n        var cachebusted_url = url + "&r=" + cachebuster;\n        var img = new Image();\n        img.src = cachebusted_url;\n    })();\n</script>\n')
            pass
        # SOURCE LINE 100
        __M_writer(u'\n')
        # SOURCE LINE 101
        __M_writer(mako_websafe(googleanalytics('web')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_bottom(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 113
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 67
        __M_writer(u'\n')
        # SOURCE LINE 68
        __M_writer(mako_websafe(c.site.title))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 110
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_robots(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer(u'\n')
        # SOURCE LINE 80
        if hasattr(thing, 'robots') and thing.robots:
            # SOURCE LINE 81
            __M_writer(u'     <meta name="robots" content="')
            __M_writer(mako_websafe(thing.robots))
            __M_writer(u'" />\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_keywords(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 71
        __M_writer(u'\nreddit, reddit.com, vote, comment, submit\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheet(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 107
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_run(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 85
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyContent(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 64
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagemeta(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 104
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_viewport(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97eb10')._populate(_import_ns, [u'js_setup', u'googleanalytics', u'classes'])
        __M_writer = context.writer()
        # SOURCE LINE 75
        __M_writer(u'\n<meta name="viewport" content="width=1024">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


