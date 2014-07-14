# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918232.605764
_template_filename=u'/home/ubuntu/src/reddit/r2/r2/templates/less.html'
_template_uri=u'/less.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['less_stylesheet', 'less_js']


# SOURCE LINE 23

from r2.lib.template_helpers import static
from r2.lib import js


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_less_stylesheet(context,*names):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        for name in names:
            # SOURCE LINE 30
            __M_writer(u'    ')
            name = name[:name.rfind('.less')] 
            
            __M_writer(u'\n')
            # SOURCE LINE 31
            if g.uncompressedJS:
                # SOURCE LINE 32
                __M_writer(u'      <link rel="stylesheet/less" type="text/css" href="')
                __M_writer(mako_websafe(static(name+'.less')))
                __M_writer(u'" media="all">\n')
                # SOURCE LINE 33
            else:
                # SOURCE LINE 34
                __M_writer(u'      <link rel="stylesheet" type="text/css" href="')
                __M_writer(mako_websafe(static(name+'.css')))
                __M_writer(u'" media="all">\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_less_js(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n')
        # SOURCE LINE 40
        if g.uncompressedJS:
            # SOURCE LINE 41
            __M_writer(u'    <script type="text/javascript">\n      less = {env: \'development\'};\n    </script>\n    ')
            # SOURCE LINE 44
            __M_writer(mako_websafe(unsafe(js.use('less'))))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


