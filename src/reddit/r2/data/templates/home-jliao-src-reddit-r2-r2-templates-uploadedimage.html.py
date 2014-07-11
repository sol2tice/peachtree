# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402764053.540607
_template_filename='/home/jliao/src/reddit/r2/r2/templates/uploadedimage.html'
_template_uri='/uploadedimage.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23
 
import simplejson
 

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n<html>\n  <head>\n    <script type="text/javascript">\n      ')
        # SOURCE LINE 29

        errors = simplejson.dumps(thing.errors)
               
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['errors'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 31
        __M_writer(u"\n      parent.completedUploadImage('")
        # SOURCE LINE 32
        __M_writer(mako_websafe(thing.status))
        __M_writer(u"','")
        __M_writer(mako_websafe(thing.img_src or ""))
        __M_writer(u"',\n                                  '")
        # SOURCE LINE 33
        __M_writer(mako_websafe(thing.name or ""))
        __M_writer(u"', ")
        __M_writer(mako_websafe(unsafe(errors)))
        __M_writer(u",'")
        __M_writer(mako_websafe(thing.form_id))
        __M_writer(u"');    \n    </script>\n  </head>\n  <body>\n    you shouldn't be here\n  </body>\n</html>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


