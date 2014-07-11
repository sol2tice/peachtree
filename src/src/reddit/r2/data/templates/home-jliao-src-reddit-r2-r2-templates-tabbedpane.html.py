# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402865367.412373
_template_filename='/home/jliao/src/reddit/r2/r2/templates/tabbedpane.html'
_template_uri='/tabbedpane.html'
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
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(mako_websafe(thing.tabmenu))
        __M_writer(u'\n<div class="tabpane-content">\n')
        # SOURCE LINE 25
        for i, (name, title, pane) in enumerate(thing.tabs):
            # SOURCE LINE 26
            __M_writer(u'    <div id="tabbedpane-')
            __M_writer(mako_websafe(name))
            __M_writer(u'" class="tabbedpane"\n         ')
            # SOURCE LINE 27
            __M_writer(mako_websafe("style='display:none'" if i > 0 else ""))
            __M_writer(u'>\n      ')
            # SOURCE LINE 28
            __M_writer(mako_websafe(pane))
            __M_writer(u'\n    </div>\n')
            pass
        # SOURCE LINE 31
        __M_writer(u'</div>\n')
        # SOURCE LINE 32
        if thing.linkable:
            # SOURCE LINE 33
            __M_writer(u'  <script>\n    $(function() {\n        var target = "tab-" + $(window.location).attr("hash").substr(1);\n        $(".tabmenu li").each(function() {\n            if (this.id == target) {\n                $(this).find("a").click();\n            }\n        });\n    });\n  </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


