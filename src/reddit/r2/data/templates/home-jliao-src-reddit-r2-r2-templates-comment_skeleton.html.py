# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402247767.881191
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/comment_skeleton.html'
_template_uri=u'/comment_skeleton.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['tagline', 'collapsed', 'commentBody', 'midcol', 'entry']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7f8c780d0550', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c780d0550')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'printable.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c780d0550')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context,collapse=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c780d0550')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_collapsed(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c780d0550')._populate(_import_ns, [u'plain_link'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(mako_websafe(self.tagline(True)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_commentBody(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c780d0550')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n  ')
        # SOURCE LINE 40
        __M_writer(mako_websafe(thing.usertext))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_midcol(context,display=True,cls=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c780d0550')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        if c.profilepage or (not thing._deleted and  (not thing._spam or thing.is_author or c.user_is_admin)):
            # SOURCE LINE 28
            __M_writer(u'    ')
            __M_writer(mako_websafe(parent.midcol(display=display, cls = cls)))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c780d0550')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n')
        # SOURCE LINE 45

        from r2.lib.strings import strings
        collapse = thing.collapsed
        
        
        # SOURCE LINE 48
        __M_writer(u'\n\n<div class="collapsed" ')
        # SOURCE LINE 50
        __M_writer(mako_websafe((not collapse and "style='display:none'" or "")))
        __M_writer(u'>\n  ')
        # SOURCE LINE 51
        __M_writer(mako_websafe(self.collapsed()))
        __M_writer(u'\n</div>\n<div class="noncollapsed" ')
        # SOURCE LINE 53
        __M_writer(mako_websafe((collapse and "style='display:none'" or "")))
        __M_writer(u'>\n  <p class="tagline">\n    ')
        # SOURCE LINE 55
        __M_writer(mako_websafe(self.tagline()))
        __M_writer(u'\n')
        # SOURCE LINE 56
        if not getattr(thing, "votable", True):
            # SOURCE LINE 57
            __M_writer(u'    <div class="unvotable-message">')
            __M_writer(mako_websafe(strings.unvotable_message))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 59
        __M_writer(u'  </p>\n  ')
        # SOURCE LINE 60
        __M_writer(mako_websafe(self.commentBody()))
        __M_writer(u'\n  <ul class="flat-list buttons">\n    ')
        # SOURCE LINE 62
        __M_writer(mako_websafe(self.buttons()))
        __M_writer(u'\n  </ul>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


