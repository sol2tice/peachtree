# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919973.898753
_template_filename=u'/home/ubuntu/src/reddit/r2/r2/templates/printable.htmllite'
_template_uri=u'/printable.htmllite'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['iframe_arrows', 'parent', 'real_arrows', 'arrows', 'Child', 'entry', 'static_arrows']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7f1dd60e9e10', context._clean_inheritance_tokens(), templateuri=u'printable.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd60e9e10')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f1dd60e9250', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd60e9250')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60e9e10')._populate(_import_ns, [u'arrow'])
        _mako_get_namespace(context, '__anon_0x7f1dd60e9250')._populate(_import_ns, [u'optionalstyle'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 26

        like_cls = "unvoted"
        if getattr(thing, "likes", None):
            like_cls = "likes"
        elif getattr(thing, "likes", None) is False:
            like_cls = "dislikes"
        thing.like_cls = like_cls
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['like_cls'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34
        __M_writer(mako_websafe(self.parent()))
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(mako_websafe(self.entry()))
        __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(mako_websafe(self.Child()))
        __M_writer(u'\n\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n\n\n')
        # SOURCE LINE 68
        __M_writer(u'\n\n')
        # SOURCE LINE 93
        __M_writer(u'\n\n')
        # SOURCE LINE 100
        __M_writer(u'\n\n\n')
        # SOURCE LINE 111
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_iframe_arrows(context,thing):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60e9e10')._populate(_import_ns, [u'arrow'])
        _mako_get_namespace(context, '__anon_0x7f1dd60e9250')._populate(_import_ns, [u'optionalstyle'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 70
        __M_writer(u'\n  ')
        # SOURCE LINE 71
 
        from r2.lib.template_helpers import get_domain
        
        
        # SOURCE LINE 73
        __M_writer(u'\n  <div class="reddit-voting-arrows" \n     ')
        # SOURCE LINE 75
        __M_writer(mako_websafe(optionalstyle("float:left; margin: 1px;")))
        __M_writer(u'>\n    <script type="text/javascript">\n      var reddit_bordercolor="FFFFFF";\n    </script>\n    ')
        # SOURCE LINE 79

        from r2.models import FakeSubreddit
        url = ("http://%s/static/button/button4.html?t=4&id=%s&sr=%s" % 
                (get_domain(cname = c.cname, subreddit = False), thing._fullname,
                c.site.name if not isinstance(c.site, FakeSubreddit) else ""))
        if c.bgcolor:
           url += "&bgcolor=%s&bordercolor=%s" % (c.bgcolor, c.bgcolor)
        else:
           url += "&bgcolor=FFFFFF&bordercolor=FFFFFF"
             
        
        # SOURCE LINE 88
        __M_writer(u'\n    <iframe src="')
        # SOURCE LINE 89
        __M_writer(mako_websafe(url))
        __M_writer(u'" height="55" width="51" scrolling="no" frameborder="0"\n            ')
        # SOURCE LINE 90
        __M_writer(mako_websafe(optionalstyle("margin:0px;")))
        __M_writer(u'>\n    </iframe>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_parent(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60e9e10')._populate(_import_ns, [u'arrow'])
        _mako_get_namespace(context, '__anon_0x7f1dd60e9250')._populate(_import_ns, [u'optionalstyle'])
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_real_arrows(context,thing):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60e9e10')._populate(_import_ns, [u'arrow'])
        _mako_get_namespace(context, '__anon_0x7f1dd60e9250')._populate(_import_ns, [u'optionalstyle'])
        arrow = _import_ns.get('arrow', context.get('arrow', UNDEFINED))
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 95
        __M_writer(u'\n  <div class="midcol ')
        # SOURCE LINE 96
        __M_writer(mako_websafe(thing.like_cls))
        __M_writer(u'" ')
        __M_writer(mako_websafe(optionalstyle("width: 15px")))
        __M_writer(u'>\n    ')
        # SOURCE LINE 97
        __M_writer(mako_websafe(arrow(thing, 1, thing.likes)))
        __M_writer(u'\n    ')
        # SOURCE LINE 98
        __M_writer(mako_websafe(arrow(thing, 0, thing.likes == False)))
        __M_writer(u'\n </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_arrows(context,thing):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60e9e10')._populate(_import_ns, [u'arrow'])
        _mako_get_namespace(context, '__anon_0x7f1dd60e9250')._populate(_import_ns, [u'optionalstyle'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 103
        __M_writer(u'\n')
        # SOURCE LINE 104
        if getattr(thing, 'embed_voting_style',None) == 'votable':
            # SOURCE LINE 105
            __M_writer(u'    ')
            __M_writer(mako_websafe(self.real_arrows(thing)))
            __M_writer(u'\n')
            # SOURCE LINE 106
        elif request.GET.get("expanded") or getattr(thing, 'embed_voting_style', None) == 'expanded':
            # SOURCE LINE 107
            __M_writer(u'    ')
            __M_writer(mako_websafe(self.iframe_arrows(thing)))
            __M_writer(u'\n')
            # SOURCE LINE 108
        else:
            # SOURCE LINE 109
            __M_writer(u'    ')
            __M_writer(mako_websafe(self.static_arrows(thing)))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Child(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60e9e10')._populate(_import_ns, [u'arrow'])
        _mako_get_namespace(context, '__anon_0x7f1dd60e9250')._populate(_import_ns, [u'optionalstyle'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\n  ')
        # SOURCE LINE 43
        __M_writer(mako_websafe(getattr(thing, "child", '')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60e9e10')._populate(_import_ns, [u'arrow'])
        _mako_get_namespace(context, '__anon_0x7f1dd60e9250')._populate(_import_ns, [u'optionalstyle'])
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_static_arrows(context,thing):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60e9e10')._populate(_import_ns, [u'arrow'])
        _mako_get_namespace(context, '__anon_0x7f1dd60e9250')._populate(_import_ns, [u'optionalstyle'])
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n  ')
        # SOURCE LINE 51

        from r2.lib.template_helpers import get_domain
        domain = get_domain(subreddit=False)
        permalink = "http://%s%s" % (domain, thing.permalink)
        if thing.likes == False:
           arrow = "http://%s/static/widget_arrows_down.gif"
        elif thing.likes:
           arrow = "http://%s/static/widget_arrows_up.gif"
        else:
           arrow = "http://%s/static/widget_arrows.gif"
        arrow = arrow % domain
        
        
        # SOURCE LINE 62
        __M_writer(u'\n  <a href="')
        # SOURCE LINE 63
        __M_writer(mako_websafe(permalink))
        __M_writer(u'" class="reddit-voting-arrows" target="_blank"\n     ')
        # SOURCE LINE 64
        __M_writer(mako_websafe(optionalstyle("float:left; display:block;")))
        __M_writer(u'>\n    <img src="')
        # SOURCE LINE 65
        __M_writer(mako_websafe(arrow))
        __M_writer(u'" alt="vote" \n         ')
        # SOURCE LINE 66
        __M_writer(mako_websafe(optionalstyle("border:none;margin-top:3px;")))
        __M_writer(u'/>\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


