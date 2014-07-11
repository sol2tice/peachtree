# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918235.818128
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/debugfooter.html'
_template_uri='/debugfooter.html'
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
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n<p class="bottommenu debuginfo"><span class="icon">&pi;</span>&nbsp;<span class="content">Rendered by PID ')
        # SOURCE LINE 23
        __M_writer(mako_websafe(g.reddit_pid))
        __M_writer(u' on ')
        __M_writer(mako_websafe(g.reddit_host))
        __M_writer(u' at ')
        __M_writer(mako_websafe(c.start_time))
        __M_writer(u' running ')
        __M_writer(mako_websafe(g.short_version))
        __M_writer(u'.</span></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


