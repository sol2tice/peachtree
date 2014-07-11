# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919370.320162
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/errorpage.html'
_template_uri='/errorpage.html'
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
        # SOURCE LINE 23

        from r2.lib.template_helpers import static
        from r2.lib.filters import unsafe, safemarkdown
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['safemarkdown','unsafe','static'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 26
        __M_writer(u'\n\n<div id="classy-error" class="content">\n  <img src="')
        # SOURCE LINE 29
        __M_writer(mako_websafe(static(thing.image_url)))
        __M_writer(u'" alt="" />\n\n  <h1>')
        # SOURCE LINE 31
        __M_writer(mako_websafe(thing.title))
        __M_writer(u'</h1>\n  <div class="errorpage-message">\n  ')
        # SOURCE LINE 33
        __M_writer(mako_websafe(unsafe(safemarkdown(thing.message, wrap=False))))
        __M_writer(u'\n')
        # SOURCE LINE 34
        if thing.explanation:
            # SOURCE LINE 35
            __M_writer(u'    &mdash; ')
            __M_writer(mako_websafe(thing.explanation))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 37
        __M_writer(u'  </div>\n\n')
        # SOURCE LINE 39
        if thing.sr_description:
            # SOURCE LINE 40
            __M_writer(u'  <div class="errorpage-message sr-description">\n      <h2>')
            # SOURCE LINE 41
            __M_writer(mako_websafe(_("a message from the moderators of /r/%s") % c.site.name))
            __M_writer(u'</h2>\n      ')
            # SOURCE LINE 42
            __M_writer(mako_websafe(unsafe(safemarkdown(thing.sr_description, wrap=False))))
            __M_writer(u'\n  </div>\n')
            pass
        # SOURCE LINE 45
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


