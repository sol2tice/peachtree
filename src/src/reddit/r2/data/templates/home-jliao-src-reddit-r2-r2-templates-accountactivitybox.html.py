# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402179366.441744
_template_filename='/home/jliao/src/reddit/r2/r2/templates/accountactivitybox.html'
_template_uri='/accountactivitybox.html'
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
        __M_writer(u'\n<div class="account-activity-box">\n    <p><a href="/account-activity">')
        # SOURCE LINE 24
        __M_writer(mako_websafe(_("account activity")))
        __M_writer(u'</a></p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


