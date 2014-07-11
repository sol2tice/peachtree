# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405072833.734064
_template_filename='/home/jliao/src/reddit/r2/r2/templates/forum.html'
_template_uri='/forum.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['bodyContent', 'forum_stylesheets', 'stylesheet', 'javascript', 'sidebar']


# SOURCE LINE 1

from r2.lib.template_helpers import static
from r2.lib.strings import strings
from r2.lib.pages import Login, ListingChooser


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 8
    ns = runtime.TemplateNamespace('__anon_0x7fb77c65ff90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb77c65ff90')] = ns

    # SOURCE LINE 7
    ns = runtime.TemplateNamespace('__anon_0x7fb77c65f0d0', context._clean_inheritance_tokens(), templateuri=u'framebuster.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb77c65f0d0')] = ns

    # SOURCE LINE 6
    ns = runtime.TemplateNamespace('__anon_0x7fb78c1374d0', context._clean_inheritance_tokens(), templateuri=u'less.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fb78c1374d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'reddit.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb77c65ff90')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fb77c65f0d0')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7fb78c1374d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(u'\n\n')
        # SOURCE LINE 70
        __M_writer(u'\n\n')
        # SOURCE LINE 82
        __M_writer(u'\n\n')
        # SOURCE LINE 89
        __M_writer(u'\n\n')
        # SOURCE LINE 96
        __M_writer(u'\n\n')
        # SOURCE LINE 100
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyContent(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb77c65ff90')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fb77c65f0d0')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7fb78c1374d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        framebuster = _import_ns.get('framebuster', context.get('framebuster', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        tags = _import_ns.get('tags', context.get('tags', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        def sidebar(content=None):
            return render_sidebar(context,content)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n  <!--%include file="adminbar.html"/-->\n  ')
        # SOURCE LINE 13
        runtime._include_file(context, u'navbar.html', _template_uri)
        __M_writer(u'\n')
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16
        if thing.show_chooser:
            # SOURCE LINE 17
            __M_writer(u'    ')
            __M_writer(mako_websafe(ListingChooser()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 19
        __M_writer(u'\n  <div id="page-wrapper">\n    <div class="row">\n        <div class="col-lg-3">\n\t  ')
        # SOURCE LINE 23
        runtime._include_file(context, u'category.html', _template_uri)
        __M_writer(u'\n   \t</div>\n\t<div class="col-lg-9">\n  ')
        # SOURCE LINE 26
        content = getattr(self, "content", None) or thing.content 
        
        __M_writer(u'\n')
        # SOURCE LINE 27
        if content:
            # SOURCE LINE 28
            if thing.show_sidebar:
                # SOURCE LINE 29
                __M_writer(u'     <div class="side">\n       ')
                # SOURCE LINE 30
                __M_writer(mako_websafe(sidebar(content = thing.rightbox())))
                __M_writer(u'\n     </div>\n')
                pass
            # SOURCE LINE 33
            __M_writer(u'    <a name="content"></a>\n    <div ')
            # SOURCE LINE 34
            __M_writer(mako_websafe(tags(id=thing.content_id)))
            __M_writer(u' ')
            __M_writer(mako_websafe(classes("content", thing.css_class)))
            __M_writer(u' role="main">\n      ')
            # SOURCE LINE 35
            __M_writer(mako_websafe(content()))
            __M_writer(u'\n    </div>\n')
            pass
        # SOURCE LINE 38
        __M_writer(u'\t</div>\n  </div>\n')
        # SOURCE LINE 40
        if thing.footer:
            # SOURCE LINE 41
            __M_writer(u'\n    ')
            # SOURCE LINE 42
            __M_writer(mako_websafe(thing.footer))
            __M_writer(u'\n\n')
            # SOURCE LINE 44
            if not c.user_is_loggedin and not g.read_only_mode:
                # SOURCE LINE 45
                if thing.enable_login_cover:
                    # SOURCE LINE 46
                    __M_writer(u'      <div class="login-popup cover-overlay" style="display: none">\n        <div class="cover" onclick="return hidecover(this)"></div>\n        <div class="popup">\n          <a href="#" onclick="return hidecover(this)" class="hidecover">\n            ')
                    # SOURCE LINE 50
                    __M_writer(mako_websafe(_("close this window")))
                    __M_writer(u'\n          </a>\n          <h1 class="cover-msg">')
                    # SOURCE LINE 52
                    __M_writer(mako_websafe(strings.cover_msg))
                    __M_writer(u'</h1>\n          ')
                    # SOURCE LINE 53
                    __M_writer(mako_websafe(Login(is_popup=True)))
                    __M_writer(u'\n        </div>\n      </div>\n')
                    pass
                # SOURCE LINE 57
                __M_writer(u'      <div class="lang-popup cover-overlay" style="display: none">\n        <div class="cover" onclick="return hidecover(this)"></div>\n        <div class="popup">\n          <a href="#" onclick="return hidecover(this)" class="hidecover">\n            ')
                # SOURCE LINE 61
                __M_writer(mako_websafe(_("close this window")))
                __M_writer(u'\n          </a>\n          ')
                # SOURCE LINE 63
                runtime._include_file(context, u'prefoptions.html', _template_uri)
                __M_writer(u'\n        </div>\n      </div>\n')
                pass
            pass
        # SOURCE LINE 68
        __M_writer(u'  ')
        __M_writer(mako_websafe(framebuster()))
        __M_writer(u'\n  ')
        # SOURCE LINE 69
        __M_writer(mako_websafe(thing.debug_footer))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_forum_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb77c65ff90')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fb77c65f0d0')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7fb78c1374d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        __M_writer = context.writer()
        # SOURCE LINE 84
        __M_writer(u'\n   <link rel="stylesheet" href="')
        # SOURCE LINE 85
        __M_writer(mako_websafe(static('vendor/bootstrap.css')))
        __M_writer(u'" type="text/css" />\n   <link rel="stylesheet" href="')
        # SOURCE LINE 86
        __M_writer(mako_websafe(static('vendor/font-awesome/css/font-awesome.css')))
        __M_writer(u'" type="text/css" />\n   <link rel="stylesheet" href="')
        # SOURCE LINE 87
        __M_writer(mako_websafe(static('vendor/sb-admin.css')))
        __M_writer(u'"/>\n   <link rel="stylesheet" href="')
        # SOURCE LINE 88
        __M_writer(mako_websafe(static('homeSignFormsStyle.css')))
        __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheet(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb77c65ff90')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fb77c65f0d0')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7fb78c1374d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 91
        __M_writer(u'\n  ')
        # SOURCE LINE 92
        __M_writer(mako_websafe(self.forum_stylesheets()))
        __M_writer(u'\n  ')
        # SOURCE LINE 93
        __M_writer(mako_websafe(self.global_stylesheets()))
        __M_writer(u'\n  ')
        # SOURCE LINE 94
        __M_writer(mako_websafe(self.sr_stylesheets()))
        __M_writer(u'\n  ')
        # SOURCE LINE 95
        __M_writer(mako_websafe(self.extra_stylesheets()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb77c65ff90')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fb77c65f0d0')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7fb78c1374d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        less_js = _import_ns.get('less_js', context.get('less_js', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 72
        __M_writer(u'\n  ')
        # SOURCE LINE 73
        from r2.lib import js 
        
        __M_writer(u'\n  <!--[if gte IE 9]> <!-->\n    ')
        # SOURCE LINE 75
        __M_writer(mako_websafe(unsafe(js.use('jquery2x', 'navbar', 'reddit-init'))))
        __M_writer(u'\n  <!-- <![endif]-->\n\n  <!--[if lt IE 9]>\n    ')
        # SOURCE LINE 79
        __M_writer(mako_websafe(unsafe(js.use('html5shiv', 'jquery1x', 'navbar', 'reddit-init'))))
        __M_writer(u'\n  <![endif]-->\n  ')
        # SOURCE LINE 81
        __M_writer(mako_websafe(less_js()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar(context,content=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fb77c65ff90')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7fb77c65f0d0')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7fb78c1374d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        __M_writer = context.writer()
        # SOURCE LINE 98
        __M_writer(u'\n  ')
        # SOURCE LINE 99
        __M_writer(mako_websafe(content))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


