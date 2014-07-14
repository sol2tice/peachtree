# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402128316.954718
_template_filename=u'/home/ubuntu/src/reddit/r2/r2/templates/comment.html'
_template_uri=u'/comment.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['buttons', 'tagline', 'collapsed', 'arrows', 'ParentDiv', 'midcol', 'Child', 'thing_data_attributes', 'commentBody']


# SOURCE LINE 23

from r2.lib.filters import unsafe
from r2.lib.pages.things import CommentButtons
from r2.lib.pages import WrappedUser


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7fabd00527d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fabd00527d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'comment_skeleton.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n')
        # SOURCE LINE 76
        __M_writer(u'\n\n')
        # SOURCE LINE 80
        __M_writer(u'\n\n')
        # SOURCE LINE 143
        __M_writer(u'\n\n')
        # SOURCE LINE 157
        __M_writer(u'\n\n')
        # SOURCE LINE 161
        __M_writer(u'\n\n')
        # SOURCE LINE 165
        __M_writer(u'\n\n')
        # SOURCE LINE 170
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buttons(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 167
        __M_writer(u'\n  ')
        # SOURCE LINE 168
        __M_writer(mako_websafe(CommentButtons(thing)))
        __M_writer(u'\n  ')
        # SOURCE LINE 169
        __M_writer(mako_websafe(self.admintagline()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context,collapse=False,showexpandcollapse=True):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        edited = _import_ns.get('edited', context.get('edited', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 82
        __M_writer(u'\n  ')
        # SOURCE LINE 83

        if c.user_is_admin:
          show = True
        else:
          show = not thing.deleted
          
        
        # SOURCE LINE 88
        __M_writer(u'\n')
        # SOURCE LINE 89
        if showexpandcollapse:
            # SOURCE LINE 90
            __M_writer(u'    <a href="#" class="expand"\n')
            # SOURCE LINE 91
            if collapse:
                # SOURCE LINE 92
                __M_writer(u'         onclick="return showcomment(this)">\n')
                # SOURCE LINE 93
            else:
                # SOURCE LINE 94
                __M_writer(u'         onclick="return hidecomment(this)">\n')
                pass
            # SOURCE LINE 96
            __M_writer(u'       [')
            __M_writer(mako_websafe("+" if collapse else unsafe("&ndash;")))
            __M_writer(u']\n    </a>\n')
            pass
        # SOURCE LINE 99
        __M_writer(u'\n')
        # SOURCE LINE 100
        if show:
            # SOURCE LINE 101
            if thing.deleted:
                # SOURCE LINE 102
                __M_writer(u'       <em>')
                __M_writer(mako_websafe(_("deleted comment from")))
                __M_writer(u'</em>&#32;\n')
                pass
            # SOURCE LINE 104
            __M_writer(u'     ')
            __M_writer(mako_websafe(WrappedUser(thing.author, thing.attribs, thing,
                   gray = collapse).render()))
            # SOURCE LINE 105
            __M_writer(u'\n     &#32;\n')
            # SOURCE LINE 107
        else:
            # SOURCE LINE 108
            __M_writer(u'     <em>')
            __M_writer(mako_websafe(_("[deleted]")))
            __M_writer(u'</em>&#32;\n')
            pass
        # SOURCE LINE 110
        __M_writer(u'\n')
        # SOURCE LINE 111
        if collapse and thing.collapsed and show:
            # SOURCE LINE 112
            __M_writer(u'    ')
            __M_writer(mako_websafe(thing.collapsed_reason))
            __M_writer(u'\n')
            # SOURCE LINE 113
        else:
            # SOURCE LINE 114
            if show:
                # SOURCE LINE 115
                if thing.score_hidden:
                    # SOURCE LINE 116
                    __M_writer(u'        <span title="')
                    __M_writer(mako_websafe(_('this subreddit hides comment scores for %d minutes') % thing.subreddit.comment_score_hide_mins))
                    __M_writer(u'">\n          [')
                    # SOURCE LINE 117
                    __M_writer(mako_websafe(_("score hidden")))
                    __M_writer(u']\n        </span>&#32;\n')
                    # SOURCE LINE 119
                else:
                    # SOURCE LINE 120
                    __M_writer(u'        ')
                    __M_writer(mako_websafe(unsafe(self.score(thing, likes = thing.likes))))
                    __M_writer(u'&#32;\n')
                    pass
                pass
            # SOURCE LINE 123
            __M_writer(u'    ')
            __M_writer(mako_websafe(thing_timestamp(thing, thing.timesince, live=True, include_tense=True)))
            __M_writer(u'\n    ')
            # SOURCE LINE 124
            __M_writer(mako_websafe(edited(thing, thing.lastedited)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 126
        __M_writer(u'\n  ')
        # SOURCE LINE 127
        __M_writer(mako_websafe(self.gildings()))
        __M_writer(u'\n\n')
        # SOURCE LINE 129
        if collapse:
            # SOURCE LINE 130
            __M_writer(u'    &nbsp;<a href="#" class="expand"\n       onclick="return showcomment(this)">\n       (')
            # SOURCE LINE 132
            __M_writer(mako_websafe(thing.num_children))
            __M_writer(u' \n        ')
            # SOURCE LINE 133
            __M_writer(mako_websafe(ungettext("child", "children", thing.num_children)))
            __M_writer(u')\n    </a>\n')
            pass
        # SOURCE LINE 136
        __M_writer(u'  ')
        __M_writer(mako_websafe(self.approval_checkmark()))
        __M_writer(u'\n')
        # SOURCE LINE 137
        if getattr(thing, 'savedcategory', None) is not None:
            # SOURCE LINE 138
            __M_writer(u'    ')
            __M_writer(mako_websafe(plain_link(_('category: %s') % thing.savedcategory,
                 '/user/%s/saved/%s' % (c.user.name, thing.savedcategory),
                 _class='save-category' + ('' if thing.savedcategory else ' hidden')
                )))
            # SOURCE LINE 141
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_collapsed(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 78
        __M_writer(u'\n')
        # SOURCE LINE 79
        __M_writer(mako_websafe(parent.collapsed()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_arrows(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 163
        __M_writer(u'\n  ')
        # SOURCE LINE 164
        __M_writer(mako_websafe(parent.midcol()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ParentDiv(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(u'\n  ')
        # SOURCE LINE 49
        __M_writer(mako_websafe(parent.ParentDiv()))
        __M_writer(u'\n')
        # SOURCE LINE 50
        if not thing.deleted:
            # SOURCE LINE 51
            __M_writer(u'    <a name="')
            __M_writer(mako_websafe(thing._id36))
            __M_writer(u'"></a>\n')
            pass
        # SOURCE LINE 53
        if c.profilepage:
            # SOURCE LINE 54
            if thing.link: 
                # SOURCE LINE 55
                if thing.link.title:
                    # SOURCE LINE 56
                    __M_writer(u'        <a href="')
                    __M_writer(mako_websafe(thing.link.url))
                    __M_writer(u'" class="title"\n')
                    # SOURCE LINE 57
                    if thing.nofollow:
                        # SOURCE LINE 58
                        __M_writer(u'             rel="nofollow"\n')
                        pass
                    # SOURCE LINE 60
                    __M_writer(u'           >\n          ')
                    # SOURCE LINE 61
                    __M_writer(mako_websafe(thing.link.title))
                    __M_writer(u'\n        </a>\n')
                    # SOURCE LINE 63
                else:
                    # SOURCE LINE 64
                    __M_writer(u'          ')
                    __M_writer(mako_websafe(thing.link.url))
                    __M_writer(u'\n')
                    pass
                pass
            # SOURCE LINE 67
            __M_writer(u'    &#32;\n    ')
            # SOURCE LINE 68
            __M_writer(mako_websafe(_("by")))
            __M_writer(u'\n    &#32;\n    ')
            # SOURCE LINE 70
            __M_writer(mako_websafe(thing.link_author.render()))
            __M_writer(u'\n    ')
            # SOURCE LINE 71
            __M_writer(mako_websafe(_("in")))
            __M_writer(u'\n    &#32;\n    ')
            # SOURCE LINE 73
            __M_writer(mako_websafe(plain_link(thing.subreddit.name, thing.subreddit_path, sr_path = False,
                 cname = False, _class = "subreddit hover")))
            # SOURCE LINE 74
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,display=True,cls=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n')
        # SOURCE LINE 45
        __M_writer(mako_websafe(parent.midcol(not thing.collapsed, cls = cls)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Child(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 145
        __M_writer(u'\n')
        # SOURCE LINE 146
        if thing.link.contest_mode and hasattr(thing, "child") and not thing.parent_id:
            # SOURCE LINE 147
            __M_writer(u'  <a href="#" class="showreplies"\n     onclick="$(this).hide();$(this).parent().find(\'.noncollapsed\').show();return false;">\n    [')
            # SOURCE LINE 149
            __M_writer(mako_websafe(_("show replies")))
            __M_writer(u']\n  </a>\n  <div class="child noncollapsed" style="display:none">\n')
            # SOURCE LINE 152
        else:
            # SOURCE LINE 153
            __M_writer(u'  <div class="child" ')
            __M_writer(mako_websafe(thing.collapsed and "style='display:none'" or ""))
            __M_writer(u'>\n')
            pass
        # SOURCE LINE 155
        __M_writer(u'    ')
        __M_writer(mako_websafe(thing.childlisting))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_data_attributes(context,what):
    context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n')
        # SOURCE LINE 37
        if what.score_hidden:
            # SOURCE LINE 38
            __M_writer(u'    ')
            __M_writer(mako_websafe(parent.thing_data_attributes(what)))
            __M_writer(u' data-ups="0" data-downs="0"\n')
            # SOURCE LINE 39
        else:
            # SOURCE LINE 40
            __M_writer(u'    ')
            __M_writer(mako_websafe(parent.thing_data_attributes(what)))
            __M_writer(u' data-ups="')
            __M_writer(mako_websafe(what.upvotes))
            __M_writer(u'" data-downs="')
            __M_writer(mako_websafe(what.downvotes))
            __M_writer(u'"\n')
            pass
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_commentBody(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabd00527d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 159
        __M_writer(u'\n  ')
        # SOURCE LINE 160
        __M_writer(mako_websafe(parent.commentBody()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


