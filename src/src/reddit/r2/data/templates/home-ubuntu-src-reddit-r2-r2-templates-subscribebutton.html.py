# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919501.115305
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/subscribebutton.html'
_template_uri='/subscribebutton.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7f1dd60ae190', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd60ae190')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60ae190')._populate(_import_ns, [u'toggle_button'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(mako_websafe(toggle_button(
    class_name="subscribe-button fancy-toggle-button",
    title=_("subscribe"),
    alt_title=_("unsubscribe"),
    callback="subscribe('%s')" % thing.sr._fullname,
    cancelback="unsubscribe('%s')" % thing.sr._fullname,
    css_class="add",
    alt_css_class="remove",
    reverse=thing.sr.subscriber,
    login_required=True,
    data_attrs=thing.data_attrs,
)))
        # SOURCE LINE 36
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


