# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918232.262904
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/reddit.html'
_template_uri='/reddit.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['global_stylesheets', 'javascript_bottom', 'Title', 'javascript', 'sr_stylesheets', 'stylesheet', 'javascript_run', 'bodyContent', 'pagemeta', 'sidebar', 'extra_stylesheets']


# SOURCE LINE 23
 
from r2.lib.template_helpers import add_sr, static, join_urls, class_dict, get_domain
from r2.lib.filters import unsafe
from r2.lib.pages import SearchForm, ClickGadget, SideContentBox, Login, ListingChooser
from r2.lib import tracking
from pylons import request
from r2.lib.strings import strings
from r2.models import make_feedurl, Sub


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 35
    ns = runtime.TemplateNamespace('__anon_0x7f1dd5a44350', context._clean_inheritance_tokens(), templateuri=u'adminbar.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd5a44350')] = ns

    # SOURCE LINE 34
    ns = runtime.TemplateNamespace('__anon_0x7f1dd5a44290', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd5a44290')] = ns

    # SOURCE LINE 32
    ns = runtime.TemplateNamespace('__anon_0x7f1dd5a44110', context._clean_inheritance_tokens(), templateuri=u'framebuster.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd5a44110')] = ns

    # SOURCE LINE 33
    ns = runtime.TemplateNamespace('__anon_0x7f1dd5a441d0', context._clean_inheritance_tokens(), templateuri=u'less.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd5a441d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 61
        __M_writer(u'\n\n')
        # SOURCE LINE 72
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n\n')
        # SOURCE LINE 104
        __M_writer(u'\n\n')
        # SOURCE LINE 116
        __M_writer(u'\n\n')
        # SOURCE LINE 122
        __M_writer(u'\n\n')
        # SOURCE LINE 126
        __M_writer(u'\n\n')
        # SOURCE LINE 182
        __M_writer(u'\n\n')
        # SOURCE LINE 186
        __M_writer(u'\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_global_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        less_stylesheet = _import_ns.get('less_stylesheet', context.get('less_stylesheet', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n  ')
        # SOURCE LINE 47
        __M_writer(mako_websafe(less_stylesheet("reddit.less")))
        __M_writer(u'\n')
        # SOURCE LINE 48
        if c.site.stylesheet:
            # SOURCE LINE 49
            __M_writer(u'    <link rel="stylesheet" href="')
            __M_writer(mako_websafe(static(c.site.stylesheet)))
            __M_writer(u'" type="text/css" >\n')
            pass
        # SOURCE LINE 51
        __M_writer(u'\n  <!--[if lt IE 7]>\n    <link rel="stylesheet" href="')
        # SOURCE LINE 53
        __M_writer(mako_websafe(static('reddit-ie6-hax.css')))
        __M_writer(u'"\n          type="text/css" />\n  <![endif]-->\n\n  <!--[if lt IE 8]>\n    <link rel="stylesheet" href="')
        # SOURCE LINE 58
        __M_writer(mako_websafe(static('reddit-ie7-hax.css')))
        __M_writer(u'"\n          type="text/css" />\n  <![endif]-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_bottom(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        __M_writer = context.writer()
        # SOURCE LINE 118
        __M_writer(u'\n  ')
        # SOURCE LINE 119
        from r2.lib import js 
        
        __M_writer(u'\n  ')
        # SOURCE LINE 120
        __M_writer(mako_websafe(unsafe(js.use('reddit'))))
        __M_writer(u'\n  ')
        # SOURCE LINE 121
        __M_writer(mako_websafe(unsafe(c.js_preload.use())))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 38
        __M_writer(u'\n')
        # SOURCE LINE 39
        if thing.title:
            # SOURCE LINE 40
            __M_writer(u'    ')
            __M_writer(mako_websafe(thing.title))
            __M_writer(u'\n')
            # SOURCE LINE 41
        else:
            # SOURCE LINE 42
            __M_writer(u'    ')
            __M_writer(mako_websafe(parent.Title()))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        less_js = _import_ns.get('less_js', context.get('less_js', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 106
        __M_writer(u'\n  ')
        # SOURCE LINE 107
        from r2.lib import js 
        
        __M_writer(u'\n  <!--[if gte IE 9]> <!-->\n    ')
        # SOURCE LINE 109
        __M_writer(mako_websafe(unsafe(js.use('jquery2x', 'reddit-init'))))
        __M_writer(u'\n  <!-- <![endif]-->\n\n  <!--[if lt IE 9]>\n    ')
        # SOURCE LINE 113
        __M_writer(mako_websafe(unsafe(js.use('html5shiv', 'jquery1x', 'reddit-init'))))
        __M_writer(u'\n  <![endif]-->\n  ')
        # SOURCE LINE 115
        __M_writer(mako_websafe(less_js()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sr_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 63
        __M_writer(u'\n')
        # SOURCE LINE 64
        if thing.subreddit_stylesheet_url:
            # SOURCE LINE 65
            __M_writer(u'    <!--[if gte IE 8]> <!-->\n    <link rel="stylesheet"\n          href="')
            # SOURCE LINE 67
            __M_writer(mako_websafe(thing.subreddit_stylesheet_url))
            __M_writer(u'"\n          title="applied_subreddit_stylesheet"\n          type="text/css">\n    <!-- <![endif]-->\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheet(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 100
        __M_writer(u'\n  ')
        # SOURCE LINE 101
        __M_writer(mako_websafe(self.global_stylesheets()))
        __M_writer(u'\n  ')
        # SOURCE LINE 102
        __M_writer(mako_websafe(self.sr_stylesheets()))
        __M_writer(u'\n  ')
        # SOURCE LINE 103
        __M_writer(mako_websafe(self.extra_stylesheets()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_run(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 124
        __M_writer(u'\n   reddit.cur_site = "')
        # SOURCE LINE 125
        __M_writer(mako_websafe(c.site._fullname if hasattr(c.site, '_fullname') else ''))
        __M_writer(u'";\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyContent(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        framebuster = _import_ns.get('framebuster', context.get('framebuster', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        tags = _import_ns.get('tags', context.get('tags', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        def sidebar(content=None):
            return render_sidebar(context,content)
        __M_writer = context.writer()
        # SOURCE LINE 128
        __M_writer(u'\n  ')
        # SOURCE LINE 129
        runtime._include_file(context, u'adminbar.html', _template_uri)
        __M_writer(u'\n  ')
        # SOURCE LINE 130
        runtime._include_file(context, u'redditheader.html', _template_uri)
        __M_writer(u'\n\n')
        # SOURCE LINE 132
        if thing.show_sidebar:
            # SOURCE LINE 133
            __M_writer(u'    <div class="side">\n      ')
            # SOURCE LINE 134
            __M_writer(mako_websafe(sidebar(content = thing.rightbox())))
            __M_writer(u'\n    </div>\n')
            pass
        # SOURCE LINE 137
        __M_writer(u'\n')
        # SOURCE LINE 138
        if thing.show_chooser:
            # SOURCE LINE 139
            __M_writer(u'    ')
            __M_writer(mako_websafe(ListingChooser()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 141
        __M_writer(u'\n  ')
        # SOURCE LINE 142
        content = getattr(self, "content", None) or thing.content 
        
        __M_writer(u'\n')
        # SOURCE LINE 143
        if content:
            # SOURCE LINE 146
            __M_writer(u'    <a name="content"></a>\n    <div ')
            # SOURCE LINE 147
            __M_writer(mako_websafe(tags(id=thing.content_id)))
            __M_writer(u' ')
            __M_writer(mako_websafe(classes("content", thing.css_class)))
            __M_writer(u' role="main">\n      ')
            # SOURCE LINE 148
            __M_writer(mako_websafe(content()))
            __M_writer(u'\n    </div>\n')
            pass
        # SOURCE LINE 151
        __M_writer(u'\n')
        # SOURCE LINE 152
        if thing.footer:
            # SOURCE LINE 153
            __M_writer(u'\n    ')
            # SOURCE LINE 154
            __M_writer(mako_websafe(thing.footer))
            __M_writer(u'\n\n')
            # SOURCE LINE 156
            if not c.user_is_loggedin and not g.read_only_mode:
                # SOURCE LINE 157
                if thing.enable_login_cover:
                    # SOURCE LINE 158
                    __M_writer(u'      <div class="login-popup cover-overlay" style="display: none">\n        <div class="cover" onclick="return hidecover(this)"></div>\n        <div class="popup">\n          <a href="#" onclick="return hidecover(this)" class="hidecover">\n            ')
                    # SOURCE LINE 162
                    __M_writer(mako_websafe(_("close this window")))
                    __M_writer(u'\n          </a>\n          <h1 class="cover-msg">')
                    # SOURCE LINE 164
                    __M_writer(mako_websafe(strings.cover_msg))
                    __M_writer(u'</h1>\n          ')
                    # SOURCE LINE 165
                    __M_writer(mako_websafe(Login(is_popup=True)))
                    __M_writer(u'\n        </div>\n      </div>\n')
                    pass
                # SOURCE LINE 169
                __M_writer(u'      <div class="lang-popup cover-overlay" style="display: none">\n        <div class="cover" onclick="return hidecover(this)"></div>\n        <div class="popup">\n          <a href="#" onclick="return hidecover(this)" class="hidecover">\n            ')
                # SOURCE LINE 173
                __M_writer(mako_websafe(_("close this window")))
                __M_writer(u'\n          </a>\n          ')
                # SOURCE LINE 175
                runtime._include_file(context, u'prefoptions.html', _template_uri)
                __M_writer(u'\n        </div>\n      </div>\n')
                pass
            pass
        # SOURCE LINE 180
        __M_writer(u'  ')
        __M_writer(mako_websafe(framebuster()))
        __M_writer(u'\n  ')
        # SOURCE LINE 181
        __M_writer(mako_websafe(thing.debug_footer))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagemeta(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 81
        __M_writer(u'\n')
        # SOURCE LINE 82
        if hasattr(thing, "shortlink"):
            # SOURCE LINE 83
            __M_writer(u'    <link rel="shorturl" href="http://')
            __M_writer(mako_websafe(thing.shortlink))
            __M_writer(u'"/>\n')
            pass
        # SOURCE LINE 85
        __M_writer(u'\n  <link rel=\'icon\' href="')
        # SOURCE LINE 86
        __M_writer(mako_websafe(static('icon.png')))
        __M_writer(u'" sizes="256x256" type="image/png" />\n  <link rel=\'shortcut icon\' href="')
        # SOURCE LINE 87
        __M_writer(mako_websafe(static('favicon.ico')))
        __M_writer(u'" type="image/x-icon" />\n  <link rel=\'apple-touch-icon-precomposed\' href="')
        # SOURCE LINE 88
        __M_writer(mako_websafe(static('icon-touch.png')))
        __M_writer(u'" />\n')
        # SOURCE LINE 89
        if thing.extension_handling:
            # SOURCE LINE 90
            __M_writer(u'    ')

            rss = add_sr(join_urls(request.path,'.rss'))
            if thing.extension_handling == "private":
               rss = make_feedurl(c.user, rss)
                 
            
            # SOURCE LINE 94
            __M_writer(u'\n    <link rel="alternate" type="application/rss+xml" title="RSS"\n          href="')
            # SOURCE LINE 96
            __M_writer(mako_websafe(rss))
            __M_writer(u'" />\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar(context,content=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        __M_writer = context.writer()
        # SOURCE LINE 184
        __M_writer(u'\n  ')
        # SOURCE LINE 185
        __M_writer(mako_websafe(content))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5a44350')._populate(_import_ns, [u'adminbar_stylesheet'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44290')._populate(_import_ns, [u'tags', u'classes'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a44110')._populate(_import_ns, [u'framebuster'])
        _mako_get_namespace(context, '__anon_0x7f1dd5a441d0')._populate(_import_ns, [u'less_js', u'less_stylesheet'])
        adminbar_stylesheet = _import_ns.get('adminbar_stylesheet', context.get('adminbar_stylesheet', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        less_stylesheet = _import_ns.get('less_stylesheet', context.get('less_stylesheet', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 74
        __M_writer(u'\n  ')
        # SOURCE LINE 75
        __M_writer(mako_websafe(adminbar_stylesheet()))
        __M_writer(u'\n')
        # SOURCE LINE 76
        for extra_stylesheet in getattr(thing, 'extra_stylesheets', ()):
            # SOURCE LINE 77
            __M_writer(u'    ')
            __M_writer(mako_websafe(less_stylesheet(extra_stylesheet)))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


