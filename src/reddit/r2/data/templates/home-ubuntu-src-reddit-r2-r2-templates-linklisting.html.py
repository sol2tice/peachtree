# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918235.599154
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/linklisting.html'
_template_uri='/linklisting.html'
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
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'<style>\n  body > .content .link .rank, .rank-spacer {\n    width: ')
        # SOURCE LINE 27
        __M_writer(mako_websafe(thing.rank_width))
        __M_writer(u'ex\n  }\n  body > .content .link .midcol, .midcol-spacer {\n    width: ')
        # SOURCE LINE 30
        __M_writer(mako_websafe(thing.midcol_width))
        __M_writer(u'ex\n  }\n</style>\n')
        # SOURCE LINE 33
        runtime._include_file(context, u'listing.html', _template_uri)
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


