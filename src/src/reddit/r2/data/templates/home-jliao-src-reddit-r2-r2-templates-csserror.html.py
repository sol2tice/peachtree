# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402764509.803681
_template_filename='/home/jliao/src/reddit/r2/r2/templates/csserror.html'
_template_uri='/csserror.html'
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
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        error = thing.error 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['error'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<li>\n')
        # SOURCE LINE 25
        if hasattr(error,'line'):
            # SOURCE LINE 26
            __M_writer(u'    <a href="javascript:void(0)"\n       onclick="$(\'#stylesheet_contents\').select_line(')
            # SOURCE LINE 27
            __M_writer(mako_websafe(error.line))
            __M_writer(u'); return false;">\n      [line ')
            # SOURCE LINE 28
            __M_writer(mako_websafe(error.line))
            __M_writer(u']\n')
            pass
        # SOURCE LINE 30
        __M_writer(u'\n      ')
        # SOURCE LINE 31
        __M_writer(mako_websafe(thing.message))
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        if hasattr(error,'offending_line'):
            # SOURCE LINE 34
            __M_writer(u'    <div>\n      <tt>\n        <pre>')
            # SOURCE LINE 36
            __M_writer(mako_websafe(error.offending_line))
            __M_writer(u'</pre>\n      </tt>\n    </div>\n')
            pass
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if hasattr(error,'line'):
            # SOURCE LINE 42
            __M_writer(u'    </a>\n')
            pass
        # SOURCE LINE 44
        __M_writer(u'\n</li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


