# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919973.488342
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/clickgadget.html'
_template_uri='/clickgadget.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f1dd60e9890', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd60e9890')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60e9890')._populate(_import_ns, [u'simple_button'])
        simple_button = _import_ns.get('simple_button', context.get('simple_button', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n<div class="gadget">\n  <div class="click-gadget">\n    ')
        # SOURCE LINE 27
        __M_writer(mako_websafe(unsafe(thing.content)))
        __M_writer(u'\n  </div>\n\n  <div class="right">\n    ')
        # SOURCE LINE 31
        __M_writer(mako_websafe(simple_button(_("clear"), "clear_clicked_items")))
        __M_writer(u'\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


