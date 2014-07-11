# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402909948.743283
_template_filename='/home/jliao/src/reddit/r2/r2/templates/mediaembed.html'
_template_uri='/mediaembed.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.utils import randstr


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n<iframe src="//')
        # SOURCE LINE 26
        __M_writer(mako_websafe(thing.media_domain))
        __M_writer(u'/mediaembed/')
        __M_writer(mako_websafe(thing.id36))
        __M_writer(mako_websafe(thing.credentials))
        __M_writer(u'"\n        id="media-embed-')
        # SOURCE LINE 27
        __M_writer(mako_websafe(thing.id36))
        __M_writer(u'-')
        __M_writer(mako_websafe(randstr(3)))
        __M_writer(u'" class="media-embed"\n        width="')
        # SOURCE LINE 28
        __M_writer(mako_websafe(thing.width))
        __M_writer(u'" height="')
        __M_writer(mako_websafe(thing.height))
        __M_writer(u'" border="0"\n        frameBorder="0" scrolling="')
        # SOURCE LINE 29
        __M_writer(mako_websafe('auto' if thing.scrolling else 'no'))
        __M_writer(u'"\n        allowfullscreen></iframe>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


