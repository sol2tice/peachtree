# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402247720.588322
_template_filename='/home/jliao/src/reddit/r2/r2/templates/subredditinfobar.html'
_template_uri='/subredditinfobar.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.strings import strings, Score
from r2.lib.pages import WrappedUser, SubscribeButton
from r2.models.listing import ModListing
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7f8c801b66d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c801b66d0')] = ns

    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f8c801b6790', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c801b6790')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c801b66d0')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'text_with_links'])
        _mako_get_namespace(context, '__anon_0x7f8c801b6790')._populate(_import_ns, [u'ynbutton', u'state_button'])
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        state_button = _import_ns.get('state_button', context.get('state_button', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n<div class="titlebox">\n  <h1 class="hover redditname">\n    ')
        # SOURCE LINE 34
        __M_writer(mako_websafe(plain_link(thing.sr.name, thing.sr.path, _sr_path=False, _class="hover")))
        __M_writer(u'\n  </h1>\n\n  ')
        # SOURCE LINE 37
        __M_writer(mako_websafe(SubscribeButton(thing.sr)))
        __M_writer(u'\n  <span class="subscribers">')
        # SOURCE LINE 38
        __M_writer(mako_websafe(unsafe(Score.readers(thing.subscribers))))
        __M_writer(u'</span>\n  <p class="users-online ')
        # SOURCE LINE 39
        __M_writer(mako_websafe('fuzzed' if thing.accounts_active_fuzzed else ''))
        __M_writer(u'" title="')
        __M_writer(mako_websafe(_('logged-in users viewing this subreddit in the past 15 minutes')))
        __M_writer(u'">\n      ')
        # SOURCE LINE 40
        __M_writer(mako_websafe(unsafe(Score.users_here_now(thing.accounts_active, prepend='~' if thing.accounts_active_fuzzed else ''))))
        __M_writer(u'\n  </p>\n\n')
        # SOURCE LINE 43
        if thing.sr.moderator:
            # SOURCE LINE 44
            __M_writer(u'    <div class="leavemoderator">\n      ')
            # SOURCE LINE 45
            __M_writer(mako_websafe(text_with_links(ModListing.remove_self_title % dict(action='(%(action)s)'),
          _sr_path=True,
          action=dict(
            ## TRANSLATORS: this label links to the edit moderators page.
            link_text=_('change'),
            path='about/moderators'))))
            # SOURCE LINE 50
            __M_writer(u'\n    </div>\n')
            pass
        # SOURCE LINE 53
        __M_writer(u'\n')
        # SOURCE LINE 54
        if thing.sr.contributor:
            # SOURCE LINE 55
            __M_writer(u'    ')
            __M_writer(mako_websafe(ynbutton(op='leavecontributor',
               title=_('leave'),
               executed=_('you are no longer an approved submitter'),
               question=_('stop being an approved submitter?'),
               format=_('you are an approved submitter on this subreddit. (%(leave)s)'),
               format_arg='leave',
               hidden_data=dict(
                 id=thing.sr._fullname))))
            # SOURCE LINE 62
            __M_writer(u'\n')
            pass
        # SOURCE LINE 64
        __M_writer(u'\n')
        # SOURCE LINE 65
        if thing.flair_prefs:
            # SOURCE LINE 66
            __M_writer(u'    ')
            __M_writer(mako_websafe(thing.flair_prefs))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 68
        __M_writer(u'\n')
        # SOURCE LINE 69
        if thing.sr.description:
            # SOURCE LINE 70
            __M_writer(u'    ')
            __M_writer(mako_websafe(thing.sr.description_usertext))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 72
        __M_writer(u'\n  <div class="bottom">\n')
        # SOURCE LINE 74
        if thing.sr.author:
            # SOURCE LINE 75
            __M_writer(u'      ')
            __M_writer(mako_websafe(unsafe(_("created by&#32;%(user)s") % dict(user = unsafe(thing.creator_text)))))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 77
        __M_writer(u'    \n    <span class="age">\n      ')
        # SOURCE LINE 79
        __M_writer(mako_websafe(_("a community for")))
        __M_writer(u'&#32;')
        __M_writer(mako_websafe(thing_timestamp(thing.sr)))
        __M_writer(u'\n    </span>  \n  </div>\n\n')
        # SOURCE LINE 83
        if c.user_is_admin:
            # SOURCE LINE 84
            if thing.sr._spam:
                # SOURCE LINE 85
                __M_writer(u'      ')
                __M_writer(mako_websafe(state_button("approve", _("approve this subreddit"),
        "return change_state(this, 'approve');", _("approved"),
        hidden_data = dict(id = thing.sr._fullname))))
                # SOURCE LINE 87
                __M_writer(u'\n')
                # SOURCE LINE 88
                if thing.sr._spam and hasattr(thing.sr, "banner"):
                    # SOURCE LINE 89
                    __M_writer(u'         &#32;(')
                    __M_writer(mako_websafe(strings.banned_by % thing.sr.banner))
                    __M_writer(u')\n')
                    pass
                # SOURCE LINE 91
                __M_writer(u'\n')
                # SOURCE LINE 92
            else:
                # SOURCE LINE 93
                __M_writer(u'      ')
                __M_writer(mako_websafe(state_button("remove", _("ban this subreddit"),
        "return change_state(this, 'remove');", _("banned"),
        hidden_data = dict(id = thing.sr._fullname))))
                # SOURCE LINE 95
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 98
        __M_writer(u'\n  <div class="clear"> </div>\n  \n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


