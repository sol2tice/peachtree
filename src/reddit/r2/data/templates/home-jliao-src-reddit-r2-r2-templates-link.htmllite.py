# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402247704.426248
_template_filename='/home/jliao/src/reddit/r2/r2/templates/link.htmllite'
_template_uri='/link.htmllite'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['entry', 'hide_if_appropriate', 'flair']


# SOURCE LINE 25

from pylons.i18n import _, ungettext
from r2.lib.template_helpers import get_domain


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f8c8de279d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8de279d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'printable.htmllite', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8de279d0')._populate(_import_ns, [u'optionalstyle'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 123
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8de279d0')._populate(_import_ns, [u'optionalstyle'])
        def hide_if_appropriate(state):
            return render_hide_if_appropriate(context,state)
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        l = _import_ns.get('l', context.get('l', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def flair():
            return render_flair(context)
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n')
        # SOURCE LINE 47
 
        from r2.lib.strings import Score
        domain = get_domain(subreddit=False)
        permalink = "http://%s%s" % (domain, thing.permalink)
        expanded = request.GET.get("expanded")
        two_col = request.GET.has_key("twocolumn") if l else False
         
        
        # SOURCE LINE 53
        __M_writer(u'\n  ')
        # SOURCE LINE 54
        __M_writer(mako_websafe(self.arrows(thing)))
        __M_writer(u'\n  <div class="reddit-entry entry ')
        # SOURCE LINE 55
        __M_writer(mako_websafe(thing.like_cls))
        __M_writer(u'" \n')
        # SOURCE LINE 56
        if expanded:
            # SOURCE LINE 57
            __M_writer(u'         ')
            __M_writer(mako_websafe(optionalstyle("margin-left: 58px;")))
            __M_writer(u'\n')
            # SOURCE LINE 58
        else:
            # SOURCE LINE 59
            __M_writer(u'         ')
            __M_writer(mako_websafe(optionalstyle("margin-left: 28px; min-height:32px;")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 61
        __M_writer(u'       >\n')
        # SOURCE LINE 62
        if c.site.link_flair_position == 'left' and thing.flair_text:
            # SOURCE LINE 63
            __M_writer(u'      ')
            __M_writer(mako_websafe(flair()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 65
        __M_writer(u'    <a class="reddit-link-title may-blank"\n      ')
        # SOURCE LINE 66
        __M_writer(mako_websafe(optionalstyle("text-decoration:none;color:#336699;font-size:small;")))
        __M_writer(u'\n')
        # SOURCE LINE 67
        if thing.is_self:
            # SOURCE LINE 68
            __M_writer(u'         href="')
            __M_writer(mako_websafe(permalink))
            __M_writer(u'"\n')
            # SOURCE LINE 69
        else:
            # SOURCE LINE 70
            __M_writer(u'         href="')
            __M_writer(mako_websafe(thing.href_url))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 72
        if thing.nofollow:
            # SOURCE LINE 73
            __M_writer(u'         rel="nofollow"\n')
            pass
        # SOURCE LINE 75
        if c.link_target:
            # SOURCE LINE 76
            __M_writer(u'         target="')
            __M_writer(mako_websafe(c.link_target))
            __M_writer(u'"\n')
            # SOURCE LINE 77
        elif c.cname:
            # SOURCE LINE 78
            __M_writer(u'         target="_top"\n')
            pass
        # SOURCE LINE 80
        if thing.mousedown_url:
            # SOURCE LINE 81
            __M_writer(u'         onmousedown="save_href($(this));this.href=\'')
            __M_writer(mako_websafe(thing.mousedown_url))
            __M_writer(u'\'"\n')
            pass
        # SOURCE LINE 83
        __M_writer(u'       >\n      ')
        # SOURCE LINE 84
        __M_writer(mako_websafe(thing.title))
        __M_writer(u'\n    </a>\n')
        # SOURCE LINE 86
        if c.site.link_flair_position == 'right' and thing.flair_text:
            # SOURCE LINE 87
            __M_writer(u'      ')
            __M_writer(mako_websafe(flair()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 89
        if not expanded:
            # SOURCE LINE 90
            __M_writer(u'      <br />\n')
            pass
        # SOURCE LINE 92
        __M_writer(u'    <small \n')
        # SOURCE LINE 93
        if expanded:
            # SOURCE LINE 94
            __M_writer(u'         ')
            __M_writer(mako_websafe(optionalstyle("color:gray;margin-left:5px;")))
            __M_writer(u'\n')
            # SOURCE LINE 95
        else:
            # SOURCE LINE 96
            __M_writer(u'         ')
            __M_writer(mako_websafe(optionalstyle("color:gray;")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 98
        __M_writer(u'       >\n')
        # SOURCE LINE 99
        if not expanded:
            # SOURCE LINE 100
            __M_writer(u'      ')

            score_dislikes, score_unvoted, score_likes = thing.display_score
            
            
            # SOURCE LINE 102
            __M_writer(u'\n      <span class="score dislikes" ')
            # SOURCE LINE 103
            __M_writer(mako_websafe(hide_if_appropriate('dislikes')))
            __M_writer(u'>\n         ')
            # SOURCE LINE 104
            __M_writer(mako_websafe(score_dislikes))
            __M_writer(u'\n      </span>\n      <span class="score unvoted" ')
            # SOURCE LINE 106
            __M_writer(mako_websafe(hide_if_appropriate('unvoted')))
            __M_writer(u'>\n         ')
            # SOURCE LINE 107
            __M_writer(mako_websafe(score_unvoted))
            __M_writer(u'\n      </span>\n      <span class="score likes" ')
            # SOURCE LINE 109
            __M_writer(mako_websafe(hide_if_appropriate('likes')))
            __M_writer(u'>\n         ')
            # SOURCE LINE 110
            __M_writer(mako_websafe(score_likes))
            __M_writer(u'\n      </span>\n      &#32;|&#32;\n')
            pass
        # SOURCE LINE 114
        __M_writer(u'      <a class="reddit-comment-link may-blank"\n         ')
        # SOURCE LINE 115
        __M_writer(mako_websafe(optionalstyle("color:gray")))
        __M_writer(u'\n')
        # SOURCE LINE 116
        if c.link_target:
            # SOURCE LINE 117
            __M_writer(u'           target="')
            __M_writer(mako_websafe(c.link_target))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 119
        __M_writer(u'         href="')
        __M_writer(mako_websafe(permalink))
        __M_writer(u'">')
        __M_writer(mako_websafe(thing.comment_label))
        __M_writer(u'</a>\n    </small>\n  </div>\n  <div class="reddit-link-end" ')
        # SOURCE LINE 122
        __M_writer(mako_websafe(optionalstyle("clear:left; padding:3px;")))
        __M_writer(u'></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hide_if_appropriate(context,state):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8de279d0')._populate(_import_ns, [u'optionalstyle'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if thing.like_cls != state:
            # SOURCE LINE 42
            __M_writer(u'   ')
            __M_writer(mako_websafe(optionalstyle("display: none;")))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flair(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8de279d0')._populate(_import_ns, [u'optionalstyle'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 32
        if c.user.pref_show_link_flair:
            # SOURCE LINE 33
            __M_writer(u'    <span class="linkflairlabel"\n        ')
            # SOURCE LINE 34
            __M_writer(mako_websafe(optionalstyle("color: #545454; background-color: #f5f5f5; border: 1px solid #dedede; display: inline-block; font-size: x-small; margin-right: 0.5em; padding: 0 2px; max-width: 10em; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;")))
            __M_writer(u'>\n      ')
            # SOURCE LINE 35
            __M_writer(mako_websafe(thing.flair_text))
            __M_writer(u'\n    </span>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


