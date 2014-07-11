# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402247635.679461
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/printable.html'
_template_uri=u'/printable.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['ParentDiv', 'midcol', 'numcol', 'Child', 'RenderPrintable', 'gildings', 'buttons', 'thing_css_rowclass', 'score', 'approval_checkmark', 'arrow', 'entry', 'thing_data_attributes', 'admintagline', 'thing_css_class']


# SOURCE LINE 23
 
from r2.lib.template_helpers import add_sr, static
from r2.lib.strings import strings
from r2.lib.pages.things import BanButtons


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7f8c78129450', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c78129450')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(mako_websafe(self.RenderPrintable()))
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n\n')
        # SOURCE LINE 76
        __M_writer(u'\n\n')
        # SOURCE LINE 102
        __M_writer(u'\n\n')
        # SOURCE LINE 119
        __M_writer(u'\n\n')
        # SOURCE LINE 160
        __M_writer(u'\n\n')
        # SOURCE LINE 164
        __M_writer(u'\n\n')
        # SOURCE LINE 167
        __M_writer(u'\n\n')
        # SOURCE LINE 170
        __M_writer(u'\n\n')
        # SOURCE LINE 173
        __M_writer(u'\n\n')
        # SOURCE LINE 179
        __M_writer(u'\n\n')
        # SOURCE LINE 202
        __M_writer(u'\n\n')
        # SOURCE LINE 214
        __M_writer(u'\n\n\n')
        # SOURCE LINE 223
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ParentDiv(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 166
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,display=True,cls=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 217
        __M_writer(u'\n  <div class="midcol ')
        # SOURCE LINE 218
        __M_writer(mako_websafe(cls))
        __M_writer(u'" \n       ')
        # SOURCE LINE 219
        __M_writer(mako_websafe(not display and "style='display:none'" or ''))
        __M_writer(u'>\n    ')
        # SOURCE LINE 220
        __M_writer(mako_websafe(self.arrow(thing, 1, thing.likes)))
        __M_writer(u'\n    ')
        # SOURCE LINE 221
        __M_writer(mako_websafe(self.arrow(thing, 0, thing.likes == False)))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_numcol(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 169
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Child(context,display=True):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 175
        __M_writer(u'\n<div class="child" ')
        # SOURCE LINE 176
        __M_writer(mako_websafe((not display and "style='display:none'" or "")))
        __M_writer(u'>\n  ')
        # SOURCE LINE 177
        __M_writer(mako_websafe(thing.childlisting))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_RenderPrintable(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 121
        __M_writer(u'\n')
        # SOURCE LINE 122
        cls = thing.lookups[0].__class__.__name__.lower() 
        
        __M_writer(u'\n')
        # SOURCE LINE 123

        if hasattr(thing, 'render_css_class'):
           cls = thing.render_css_class
        elif hasattr(thing, 'render_class'):
           cls = thing.render_class.__name__.lower()
        else:
           cls = thing.lookups[0].__class__.__name__.lower()
        
        cls += ' ' + getattr(thing, 'extra_css_class', '')
        
        if getattr(thing, "is_self", False):
           selflink = "self"
        else:
           selflink = ""
         
        
        # SOURCE LINE 137
        __M_writer(u'\n<div class="')
        # SOURCE LINE 138
        __M_writer(mako_websafe(self.thing_css_class(thing)))
        __M_writer(u' ')
        __M_writer(mako_websafe(self.thing_css_rowclass(thing)))
        __M_writer(u' ')
        __M_writer(mako_websafe(unsafe(cls)))
        __M_writer(u' ')
        __M_writer(mako_websafe(selflink))
        __M_writer(u'"\n    ')
        # SOURCE LINE 139
        __M_writer(mako_websafe(thing.display))
        __M_writer(u' onclick="click_thing(this)"\n    ')
        # SOURCE LINE 140
        __M_writer(mako_websafe(unsafe(self.thing_data_attributes(thing))))
        __M_writer(u'>\n  <p class="parent">\n    ')
        # SOURCE LINE 142
        __M_writer(mako_websafe(self.ParentDiv()))
        __M_writer(u'\n  </p>\n  ')
        # SOURCE LINE 144
        __M_writer(mako_websafe(self.numcol()))
        __M_writer(u'\n  ')
        # SOURCE LINE 145

        like_cls = "unvoted"
        if getattr(thing, "likes", None):
            like_cls = "likes"
        elif getattr(thing, "likes", None) is False:
            like_cls = "dislikes"
           
        
        # SOURCE LINE 151
        __M_writer(u'\n  ')
        # SOURCE LINE 152
        __M_writer(mako_websafe(self.midcol(cls = like_cls)))
        __M_writer(u'\n  <div class="entry ')
        # SOURCE LINE 153
        __M_writer(mako_websafe(like_cls))
        __M_writer(u'">\n    ')
        # SOURCE LINE 154
        __M_writer(mako_websafe(self.entry()))
        __M_writer(u'\n  </div>\n  ')
        # SOURCE LINE 156
        __M_writer(mako_websafe(self.Child()))
        __M_writer(u'\n  <div class="clearleft"></div>\n</div>\n<div class="clearleft"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_gildings(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n')
        # SOURCE LINE 58
        if thing.gilded_message:
            # SOURCE LINE 59
            __M_writer(u'  <a href="')
            __M_writer(mako_websafe(thing.subreddit_path))
            __M_writer(u'gilded">\n    <span class="gilded-icon" title="')
            # SOURCE LINE 60
            __M_writer(mako_websafe(thing.gilded_message))
            __M_writer(u'" data-count="')
            __M_writer(mako_websafe(thing.gildings))
            __M_writer(u'">\n')
            # SOURCE LINE 61
            if thing.gildings > 1:
                # SOURCE LINE 62
                __M_writer(u'        x')
                __M_writer(mako_websafe(thing.gildings))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 64
            __M_writer(u'    </span>\n  </a>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buttons(context,ban=True):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 162
        __M_writer(u'\n  ')
        # SOURCE LINE 163
        __M_writer(mako_websafe(BanButtons(thing)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_rowclass(context,what):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 78
        __M_writer(u'\n  ')
        # SOURCE LINE 79

        if what.show_spam:
          rowclass = what.rowstyle + " spam"
          if what.show_spam == "author":
            rowclass += " banned-user"
        elif what.show_reports:
          rowclass = what.rowstyle + " reported"
        else:
          rowclass = what.rowstyle
        if getattr(what, "deleted", False):
          rowclass += " deleted"
        if hasattr(what, "saved") and what.saved:
          rowclass += " saved"
        if hasattr(what, "hidden") and what.hidden:
          rowclass += " hidden"
        if hasattr(what, "gildings") and what.gildings > 0:
          rowclass += " gilded"
        if hasattr(what, "user_gilded") and what.user_gilded:
          rowclass += " user-gilded"
        if getattr(what, "stickied", False):
          rowclass += " stickied"
          
        
        # SOURCE LINE 100
        __M_writer(u'\n  ')
        # SOURCE LINE 101
        __M_writer(mako_websafe(rowclass))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_score(context,this,likes=None,scores=None,tag='span'):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        zip = _import_ns.get('zip', context.get('zip', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 204
        __M_writer(u'\n  ')
        # SOURCE LINE 205

        if scores is None:
           scores = this.display_score
           
        
        # SOURCE LINE 208
        __M_writer(u'\n')
        # SOURCE LINE 209
        for cls, score in zip(["dislikes", "unvoted", "likes"], scores):
            # SOURCE LINE 210
            __M_writer(u'    <')
            __M_writer(mako_websafe(tag))
            __M_writer(u' class="score ')
            __M_writer(mako_websafe(cls))
            __M_writer(u'">\n      ')
            # SOURCE LINE 211
            __M_writer(mako_websafe(score))
            __M_writer(u'\n    </')
            # SOURCE LINE 212
            __M_writer(mako_websafe(tag))
            __M_writer(u'>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_approval_checkmark(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(u'\n')
        # SOURCE LINE 49
        if getattr(thing, "approval_checkmark", None):
            # SOURCE LINE 50
            __M_writer(u'      <img class="approval-checkmark" title="')
            __M_writer(mako_websafe(thing.approval_checkmark))
            __M_writer(u'"\n           src="')
            # SOURCE LINE 51
            __M_writer(mako_websafe(static('green-check.png')))
            __M_writer(u'"\n           onclick="alert(\'')
            # SOURCE LINE 52
            __M_writer(mako_websafe(thing.approval_checkmark))
            __M_writer(u'\\n\\n')
            __M_writer(mako_websafe(_("(no need to click for this info; just hover over the checkmark next time)")))
            __M_writer(u'\')"\n         >\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_arrow(context,this,dir,mod):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 181
        __M_writer(u'\n')
        # SOURCE LINE 182
 
        _type = "up" if dir > 0 else "down"
        _class = _type + ("mod" if mod else "")
        fullname = this._fullname
        
        
        # SOURCE LINE 186
        __M_writer(u'\n  <div class="arrow ')
        # SOURCE LINE 187
        __M_writer(mako_websafe(_class))
        __M_writer(u' login-required"\n')
        # SOURCE LINE 188
        if getattr(thing, "votable", True):
            # SOURCE LINE 189
            __M_writer(u'         onclick="$(this).vote(r.config.vote_hash, null, event)"\n')
            # SOURCE LINE 190
        else:
            # SOURCE LINE 191
            __M_writer(u'         onclick="$(this).show_unvotable_message()"\n')
            pass
        # SOURCE LINE 193
        __M_writer(u'       role="button"\n')
        # SOURCE LINE 194
        if dir > 0:
            # SOURCE LINE 195
            __M_writer(u'       aria-label="')
            __M_writer(mako_websafe(_("upvote")))
            __M_writer(u'"\n')
            # SOURCE LINE 196
        else:
            # SOURCE LINE 197
            __M_writer(u'       aria-label="')
            __M_writer(mako_websafe(_("downvote")))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 199
        __M_writer(u'       tabindex="0"\n       >\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 172
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_data_attributes(context,what):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 104
        __M_writer(u'\n')
        # SOURCE LINE 105
        if not getattr(what, 'deleted', False):
            # SOURCE LINE 106
            __M_writer(u'      data-fullname="')
            __M_writer(mako_websafe(what._fullname))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 108
        if hasattr(what, 'campaign'):
            # SOURCE LINE 109
            __M_writer(u'      data-cid="')
            __M_writer(mako_websafe(what.campaign))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 111
        __M_writer(u'\n')
        # SOURCE LINE 112
        if hasattr(what, 'adserver_imp_pixel'):
            # SOURCE LINE 113
            __M_writer(u'      data-adserver-imp-pixel="')
            __M_writer(mako_websafe(what.adserver_imp_pixel))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 115
        __M_writer(u'\n')
        # SOURCE LINE 116
        if hasattr(what, 'adserver_click_url'):
            # SOURCE LINE 117
            __M_writer(u'      data-adserver-click-url="')
            __M_writer(mako_websafe(what.adserver_click_url))
            __M_writer(u'"\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admintagline(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34
        if thing.show_spam:
            # SOURCE LINE 35
            __M_writer(u'      <li><b>[\n')
            # SOURCE LINE 36
            if c.user_is_admin:
                # SOURCE LINE 37
                __M_writer(u'          ')
                __M_writer(mako_websafe("auto" if thing.autobanned else ""))
                __M_writer(mako_websafe(strings.banned))
                __M_writer(u' \n          ')
                # SOURCE LINE 38
                __M_writer(mako_websafe(("by %s" % thing.banner) if thing.banner else ""))
                __M_writer(u'\n')
                # SOURCE LINE 39
            elif thing.moderator_banned and thing.banner:
                # SOURCE LINE 40
                __M_writer(u'          ')
                __M_writer(mako_websafe(strings.banned_by % thing.banner))
                __M_writer(u'\n')
                # SOURCE LINE 41
            else:
                # SOURCE LINE 42
                __M_writer(u'          ')
                __M_writer(mako_websafe(strings.banned))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 44
            __M_writer(u'      ]</li></b>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_class(context,what):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c78129450')._populate(_import_ns, [u'plain_link'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 69
        __M_writer(u'\n  ')
        # SOURCE LINE 70

        cssclass = "thing"
        if not getattr(what, 'deleted', False) or getattr(what, 'can_ban', False):
          cssclass += " id-" + what._fullname
          
        
        # SOURCE LINE 74
        __M_writer(u'\n  ')
        # SOURCE LINE 75
        __M_writer(mako_websafe(cssclass))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


