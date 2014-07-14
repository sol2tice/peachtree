# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918235.310943
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/panestack.html'
_template_uri='/panestack.html'
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
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        for t in thing.stack:
            # SOURCE LINE 24
            if thing.div:
                # SOURCE LINE 25
                __M_writer(u'    <div ')
                __M_writer(mako_websafe(thing.div_id and ("id='%s'" % str(thing.div_id)) or ""))
                __M_writer(u'\n         ')
                # SOURCE LINE 26
                __M_writer(mako_websafe(thing.css_class and ("class='%s'" % str(thing.css_class)) or ""))
                __M_writer(u'>\n')
                pass
            # SOURCE LINE 28
            __M_writer(u'\n')
            # SOURCE LINE 29
            if thing.title:
                # SOURCE LINE 30
                __M_writer(u'    <div class="panestack-title">\n      <span class="title">')
                # SOURCE LINE 31
                __M_writer(mako_websafe(thing.title))
                __M_writer(u'</span>\n')
                # SOURCE LINE 32
                for link_text, link, link_class in thing.title_buttons:
                    # SOURCE LINE 33
                    __M_writer(u'         <a href="')
                    __M_writer(mako_websafe(link))
                    __M_writer(u'" class="title-button ')
                    __M_writer(mako_websafe(link_class))
                    __M_writer(u'">')
                    __M_writer(mako_websafe(link_text))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 35
                __M_writer(u'    </div>\n')
                pass
            # SOURCE LINE 37
            __M_writer(u'\n  ')
            # SOURCE LINE 38
            __M_writer(mako_websafe(t))
            __M_writer(u'\n\n')
            # SOURCE LINE 40
            if thing.div:
                # SOURCE LINE 41
                __M_writer(u'    </div>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


