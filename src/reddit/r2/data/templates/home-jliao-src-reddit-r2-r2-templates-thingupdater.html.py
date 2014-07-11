# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402247720.525459
_template_filename='/home/jliao/src/reddit/r2/r2/templates/thingupdater.html'
_template_uri='/thingupdater.html'
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
        list = context.get('list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23

        import simplejson
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['simplejson'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 25
        __M_writer(u'\n<script type="text/javascript">\n  (function() {\n    var likes = ')
        # SOURCE LINE 28
        __M_writer(mako_websafe(unsafe(simplejson.dumps(thing.likes))))
        __M_writer(u';\n    var dislikes = ')
        # SOURCE LINE 29
        __M_writer(mako_websafe(unsafe(simplejson.dumps(thing.dislikes))))
        __M_writer(u';\n    var friends = ')
        # SOURCE LINE 30
        __M_writer(mako_websafe(unsafe(simplejson.dumps(list(thing.is_friend)))))
        __M_writer(u';\n    $.map(likes, function(l) {\n              $(".id-" + l + " > .midcol").find(".arrow.up").vote("", null, null, true);\n          });\n    $.map(dislikes, function(l) {\n              $(".id-" + l + " > .midcol").find(".arrow.down").vote("", null, null, true);\n          });\n    $.map(friends, show_friend);\n\n    var gildings = ')
        # SOURCE LINE 39
        __M_writer(mako_websafe(unsafe(simplejson.dumps(thing.gildings))))
        __M_writer(u';\n    for (var gilded_thing in gildings) {\n      var gilding_data = gildings[gilded_thing];\n      r.gold.gildThing(gilded_thing, gilding_data[0], gilding_data[1]);\n    }\n\n    var saves = ')
        # SOURCE LINE 45
        __M_writer(mako_websafe(unsafe(simplejson.dumps(list(thing.saves)))))
        __M_writer(u';\n    $.map(saves, r.ui.setSavedFullname);\n  })()\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


