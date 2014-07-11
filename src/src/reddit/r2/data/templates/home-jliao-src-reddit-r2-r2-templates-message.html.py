# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402411213.191441
_template_filename='/home/jliao/src/reddit/r2/r2/templates/message.html'
_template_uri='/message.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['buttons', 'tagline', 'ParentDiv', 'midcol', 'entry', 'commentBody', 'thing_css_class', 'subject']


# SOURCE LINE 23

from r2.lib.filters import safemarkdown
from r2.lib.pages.things import MessageButtons
from r2.lib.pages import WrappedUser
from r2.lib.template_helpers import static


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f30c016be50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f30c016be50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'comment_skeleton.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c016be50')._populate(_import_ns, [u'thing_timestamp'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        __M_writer(u'\n\n')
        # SOURCE LINE 76
        __M_writer(u'\n\n')
        # SOURCE LINE 109
        __M_writer(u'\n\n')
        # SOURCE LINE 116
        __M_writer(u'\n\n')
        # SOURCE LINE 128
        __M_writer(u'\n\n')
        # SOURCE LINE 132
        __M_writer(u'\n\n')
        # SOURCE LINE 136
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buttons(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c016be50')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 130
        __M_writer(u'\n  ')
        # SOURCE LINE 131
        __M_writer(mako_websafe(MessageButtons(thing)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context,collapse=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c016be50')._populate(_import_ns, [u'thing_timestamp'])
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\n     <a href="#" class="expand"\n')
        # SOURCE LINE 47
        if collapse:
            # SOURCE LINE 48
            __M_writer(u'           onclick="return showcomment(this)">\n')
            # SOURCE LINE 49
        else:
            # SOURCE LINE 50
            __M_writer(u'           onclick="return hidecomment(this)">\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'         [')
        __M_writer(mako_websafe("+" if collapse else unsafe("&ndash;")))
        __M_writer(u']&nbsp;\n     </a>\n  <span class="head">\n  ')
        # SOURCE LINE 55

        author = WrappedUser(thing.author, thing.attribs, thing).render()
        if thing.sr_id:
          subreddit = '<a href="%s">%s</a>' % (thing.subreddit.path,
                                               thing.subreddit.path)
          if not thing.dest:
            thing.dest = subreddit
          author = thing.updated_author.replace(' ', '&#32;') % dict(
            author=author,
            subreddit=subreddit)
        
        taglinetext = thing.taglinetext.replace(' ', '&#32;') % dict(
          when=capture(thing_timestamp, thing, thing.timesince, include_tense=True),
          author=u"<b>%s</b>" % author,
          dest=u"<b>%s</b>" % thing.dest)
          
        
        # SOURCE LINE 70
        __M_writer(u'\n  ')
        # SOURCE LINE 71
        __M_writer(mako_websafe(unsafe(taglinetext)))
        __M_writer(u'\n  </span>\n')
        # SOURCE LINE 73
        if c.user_is_admin:
            # SOURCE LINE 74
            __M_writer(u'    ')
            __M_writer(mako_websafe(self.admintagline()))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ParentDiv(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c016be50')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 111
        __M_writer(u'\n')
        # SOURCE LINE 112
        if getattr(thing, 'distinguished', '') == 'gold':
            # SOURCE LINE 113
            __M_writer(u'    <div class="insignia"><img src="')
            __M_writer(mako_websafe(static('gold/gold-insignia-big.png')))
            __M_writer(u'"></div>\n')
            pass
        # SOURCE LINE 115
        __M_writer(mako_websafe(self.subject()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,cls=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c016be50')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34
        if thing.was_comment and not thing._spam:
            # SOURCE LINE 35
            __M_writer(u'    ')
            __M_writer(mako_websafe(parent.midcol(display=True, cls = cls)))
            __M_writer(u'\n')
            # SOURCE LINE 36
        else:
            # SOURCE LINE 37
            __M_writer(u'    <div class="midcol" style=\'display:none\'></div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c016be50')._populate(_import_ns, [u'thing_timestamp'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 134
        __M_writer(u'\n  ')
        # SOURCE LINE 135
        __M_writer(mako_websafe(parent.entry()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_commentBody(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c016be50')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 118
        __M_writer(u'\n')
        # SOURCE LINE 119
        if thing.was_comment and hasattr(thing, "parent"):
            # SOURCE LINE 120
            __M_writer(u'    <p>\n      <a href="#" class="parent-link"\n         onclick="return fetch_parent(this, \'')
            # SOURCE LINE 122
            __M_writer(mako_websafe(thing.parent_permalink))
            __M_writer(u"/.json', '")
            __M_writer(mako_websafe(thing.parent))
            __M_writer(u'\')">\n        ')
            # SOURCE LINE 123
            __M_writer(mako_websafe(_("show parent")))
            __M_writer(u'\n      </a>\n    </p>\n')
            pass
        # SOURCE LINE 127
        __M_writer(mako_websafe(unsafe(safemarkdown(thing.body))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_class(context,what):
    context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c016be50')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n')
        # SOURCE LINE 42
        __M_writer(mako_websafe(parent.thing_css_class(what)))
        __M_writer(u' ')
        __M_writer(mako_websafe("new" if thing.new else ""))
        __M_writer(u' ')
        __M_writer(mako_websafe("was-comment" if thing.was_comment else ""))
        __M_writer(u' ')
        __M_writer(mako_websafe("recipient" if thing.recipient else ""))
        __M_writer(u' ')
        __M_writer(mako_websafe("message-reply" if getattr(thing, "is_child", False) else ""))
        __M_writer(u' ')
        __M_writer(mako_websafe("message-parent" if getattr(thing, "is_parent", False) else ""))
        __M_writer(u' ')
        __M_writer(mako_websafe("focal" if getattr(thing, "focal", False) else ""))
        __M_writer(u' ')
        __M_writer(mako_websafe("gold" if getattr(thing, "distinguished", "") == "gold" else ""))
        __M_writer(u' ')
        __M_writer(mako_websafe("gold-auto" if getattr(thing, "distinguished", "") == "gold-auto" else ""))
        __M_writer(u'\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_subject(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c016be50')._populate(_import_ns, [u'thing_timestamp'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 78
        __M_writer(u'\n  <p class="subject">\n')
        # SOURCE LINE 80
        if getattr(thing, "is_parent", False):
            # SOURCE LINE 81
            if thing.sr_id:
                # SOURCE LINE 82
                __M_writer(u'         <span class="correspondent reddit rounded">\n           <a href="')
                # SOURCE LINE 83
                __M_writer(mako_websafe(thing.subreddit.path))
                __M_writer(u'message/moderator/inbox">\n             /r/')
                # SOURCE LINE 84
                __M_writer(mako_websafe(thing.subreddit.name))
                __M_writer(u'\n           </a>\n         </span>\n')
                # SOURCE LINE 87
            else:
                # SOURCE LINE 88
                __M_writer(u'         <span class="correspondent rounded">\n           ')
                # SOURCE LINE 89

                corr = thing.author if thing.recipient else thing.to
                            
                
                # SOURCE LINE 91
                __M_writer(u'\n           ')
                # SOURCE LINE 92
                __M_writer(mako_websafe(WrappedUser(corr)))
                __M_writer(u'\n         </span>\n')
                pass
            pass
        # SOURCE LINE 96
        __M_writer(u'    ')
        __M_writer(mako_websafe(thing.subject))
        __M_writer(u'\n')
        # SOURCE LINE 97
        if thing.was_comment:
            # SOURCE LINE 98
            __M_writer(u'    <a href="')
            __M_writer(mako_websafe(thing.link_permalink))
            __M_writer(u'" class="title">')
            __M_writer(mako_websafe(thing.link_title))
            __M_writer(u'</a>\n')
            # SOURCE LINE 99
        elif getattr(thing, "is_parent", False):
            # SOURCE LINE 100
            __M_writer(u'    <br/>\n      <a class="expand-btn" href="#" onclick="return show_all_messages(this)">\n        ')
            # SOURCE LINE 102
            __M_writer(mako_websafe(_("expand all")))
            __M_writer(u'\n      </a>\n      <a class="expand-btn" href="#"  onclick="return hide_all_messages(this)">\n        ')
            # SOURCE LINE 105
            __M_writer(mako_websafe(_("collapse all")))
            __M_writer(u'\n      </a>\n')
            pass
        # SOURCE LINE 108
        __M_writer(u' </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


