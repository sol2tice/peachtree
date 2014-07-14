# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919418.808522
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/menuarea.html'
_template_uri='/menuarea.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<div class="menuarea">\n')
        # SOURCE LINE 24
        for menu in thing.menus:
            # SOURCE LINE 25
            __M_writer(u'    <div class="spacer">\n      ')
            # SOURCE LINE 26
            __M_writer(mako_websafe(menu))
            __M_writer(u'\n    </div>\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


