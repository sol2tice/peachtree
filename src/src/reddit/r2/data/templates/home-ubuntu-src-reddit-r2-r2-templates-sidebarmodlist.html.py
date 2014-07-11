# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402128381.160393
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/sidebarmodlist.html'
_template_uri='/sidebarmodlist.html'
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
        __M_writer(u'\n<ul id="side-mod-list">\n')
        # SOURCE LINE 24
        for sr in thing.subreddits:
            # SOURCE LINE 25
            __M_writer(u'  <li><a href="')
            __M_writer(mako_websafe(sr.path))
            __M_writer(u'" title="/r/')
            __M_writer(mako_websafe(sr.name))
            __M_writer(u'">/r/')
            __M_writer(mako_websafe(sr.name))
            __M_writer(u'</a></li>\n')
            pass
        # SOURCE LINE 27
        __M_writer(u"</ul>\n\n<script>new r.ui.Summarize($('#side-mod-list'), 5)</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


