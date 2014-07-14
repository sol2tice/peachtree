# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402178932.380954
_template_filename='/home/jliao/src/reddit/r2/r2/templates/navbutton.html'
_template_uri='/navbutton.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['plain', 'post', 'js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f8c8da01290', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8da01290')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da01290')._populate(_import_ns, [u'plain_link', u'post_link'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_plain(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da01290')._populate(_import_ns, [u'plain_link', u'post_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n  ')
        # SOURCE LINE 26
        __M_writer(mako_websafe(plain_link(thing.selected_title() if thing.selected else thing.title, 
               thing.path, _sr_path = thing.sr_path, nocname = thing.nocname,
               target = thing.target, 
               _class = thing.css_class, _id = thing._id)))
        # SOURCE LINE 29
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_post(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da01290')._populate(_import_ns, [u'plain_link', u'post_link'])
        post_link = _import_ns.get('post_link', context.get('post_link', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n  ')
        # SOURCE LINE 40
        __M_writer(mako_websafe(post_link(thing.selected_title() if thing.selected else thing.title,
              thing.base_path, thing.path, thing.action_params,
              _sr_path=thing.sr_path, nocname=thing.nocname,
              target=thing.target, _class=thing.css_class, _id=thing._id)))
        # SOURCE LINE 43
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da01290')._populate(_import_ns, [u'plain_link', u'post_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n  ')
        # SOURCE LINE 33
        __M_writer(mako_websafe(plain_link(thing.selected_title() if thing.selected else thing.title, 
               thing.path, _sr_path = False, nocname = True, 
               _class = thing.css_class, _id = thing._id, 
               onclick = thing.onclick)))
        # SOURCE LINE 36
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


