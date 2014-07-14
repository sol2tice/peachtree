# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402247720.606731
_template_filename='/home/jliao/src/reddit/r2/r2/templates/subreddit.html'
_template_uri='/subreddit.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['numcol', 'tagline', 'permission_icons', 'midcol', 'child', 'entry']


# SOURCE LINE 23

from r2.lib.template_helpers import static
from r2.lib.strings import strings
from r2.lib.utils import timesince
from r2.lib.pages import SubscribeButton


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f8c801affd0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c801affd0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'printable.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c801affd0')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n')
        # SOURCE LINE 60
        __M_writer(u'\n\n')
        # SOURCE LINE 90
        __M_writer(u'\n\n')
        # SOURCE LINE 97
        __M_writer(u'\n\n')
        # SOURCE LINE 100
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_numcol(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c801affd0')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c801affd0')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n  ')
        # SOURCE LINE 58
        __M_writer(mako_websafe(self.score(thing, thing.subscriber)))
        __M_writer(u',\n  ')
        # SOURCE LINE 59
        __M_writer(mako_websafe(_("a community for %(time)s") % dict(time=timesince(thing._date))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_permission_icons(context,sr):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c801affd0')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 63
        __M_writer(u'\n')
        # SOURCE LINE 64
        if sr.moderator:
            # SOURCE LINE 65
            __M_writer(u'    <img class="sr-type-img" title="')
            __M_writer(mako_websafe(_('moderator')))
            __M_writer(u'" alt="')
            __M_writer(mako_websafe(_('moderator')))
            __M_writer(u'" src="')
            __M_writer(mako_websafe(static('shield.png')))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 67
        __M_writer(u'\n')
        # SOURCE LINE 68
        if sr.type in ("restricted", "private") and not sr.moderator:
            # SOURCE LINE 69
            __M_writer(u'    <img class="sr-type-img"\n')
            # SOURCE LINE 70
            if sr.contributor:
                # SOURCE LINE 71
                __M_writer(u'         alt="')
                __M_writer(mako_websafe(_('approved submitter')))
                __M_writer(u'"\n         title="')
                # SOURCE LINE 72
                __M_writer(mako_websafe(_('approved submitter')))
                __M_writer(u'"\n         src="')
                # SOURCE LINE 73
                __M_writer(mako_websafe(static('pencil.png')))
                __M_writer(u'"\n')
                # SOURCE LINE 74
            else:
                # SOURCE LINE 75
                __M_writer(u'         alt="')
                __M_writer(mako_websafe(_('not approved')))
                __M_writer(u'"\n         title="')
                # SOURCE LINE 76
                __M_writer(mako_websafe(_('not approved')))
                __M_writer(u'"\n         src="')
                # SOURCE LINE 77
                __M_writer(mako_websafe(static('pencil-gray.png')))
                __M_writer(u'"\n')
                pass
            # SOURCE LINE 79
            __M_writer(u'    />\n')
            pass
        # SOURCE LINE 81
        __M_writer(u'\n')
        # SOURCE LINE 82
        if sr.type == "private":
            # SOURCE LINE 83
            __M_writer(u'    <img class="sr-type-img" title="')
            __M_writer(mako_websafe(_('private')))
            __M_writer(u'" alt="')
            __M_writer(mako_websafe(_('private')))
            __M_writer(u'" src="')
            __M_writer(mako_websafe(static('eye.png')))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 85
        __M_writer(u'\n')
        # SOURCE LINE 86
        if sr.over_18:
            # SOURCE LINE 87
            __M_writer(u'    <img class="sr-type-img" title="')
            __M_writer(mako_websafe(_('over18')))
            __M_writer(u'" alt="')
            __M_writer(mako_websafe(_('over18')))
            __M_writer(u'" src="')
            __M_writer(mako_websafe(static('over18_icon.png')))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 89
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,display=True,cls=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c801affd0')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def permission_icons(sr):
            return render_permission_icons(context,sr)
        __M_writer = context.writer()
        # SOURCE LINE 92
        __M_writer(u'\n  <div class="midcol">\n    ')
        # SOURCE LINE 94
        __M_writer(mako_websafe(SubscribeButton(thing)))
        __M_writer(u'\n    ')
        # SOURCE LINE 95
        __M_writer(mako_websafe(permission_icons(thing)))
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_child(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c801affd0')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 99
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c801affd0')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n')
        # SOURCE LINE 37
        fullname = thing._fullname 
        
        __M_writer(u'\n<p class="titlerow">\n  ')
        # SOURCE LINE 39
        __M_writer(mako_websafe(plain_link('%s: %s' % (thing.path.rstrip('/'), thing.title), thing.path, _class="title")))
        __M_writer(u'\n')
        # SOURCE LINE 40
        if c.user_is_admin:
            # SOURCE LINE 41
            __M_writer(u'  ')
            __M_writer(mako_websafe(self.admintagline()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 43
        __M_writer(u'</p>\n')
        # SOURCE LINE 44
        if thing.public_description_usertext:
            # SOURCE LINE 45
            __M_writer(u'  <div class="description">\n    ')
            # SOURCE LINE 46
            __M_writer(mako_websafe(thing.public_description_usertext))
            __M_writer(u'\n  </div>\n')
            pass
        # SOURCE LINE 49
        __M_writer(u'<p class="tagline">\n  ')
        # SOURCE LINE 50
        __M_writer(mako_websafe(self.tagline()))
        __M_writer(u'\n</p>\n<ul class="flat-list buttons">\n  ')
        # SOURCE LINE 53
        __M_writer(mako_websafe(self.buttons()))
        __M_writer(u'\n</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


