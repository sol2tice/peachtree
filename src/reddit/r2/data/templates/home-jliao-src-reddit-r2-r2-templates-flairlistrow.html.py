# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402865717.967423
_template_filename='/home/jliao/src/reddit/r2/r2/templates/flairlistrow.html'
_template_uri='/flairlistrow.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 25

from r2.lib.pages import WrappedUser


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<div id="flairrow_')
        # SOURCE LINE 29
        __M_writer(mako_websafe(thing.user._id36))
        __M_writer(u'" class="flairrow">\n  <span class="tagline flaircell">\n    ')
        # SOURCE LINE 31
        __M_writer(mako_websafe(unsafe(WrappedUser(thing.user, force_show_flair=True,
                         include_flair_selector=True).render())))
        # SOURCE LINE 32
        __M_writer(u'\n  </span>\n  <form action="/post/flair" id="flair-')
        # SOURCE LINE 34
        __M_writer(mako_websafe(thing.user._id36))
        __M_writer(u'" method="post"\n        class="medium-text flair-entry">\n    <input type="hidden" name="name" value="')
        # SOURCE LINE 36
        __M_writer(mako_websafe(thing.user.name))
        __M_writer(u'" />\n    <span class="flaircell">\n      <input type="text" size="32" maxlength="64" name="text"\n             value="')
        # SOURCE LINE 39
        __M_writer(mako_websafe(thing.flair_text))
        __M_writer(u'" />\n    </span>\n    <span class="flaircell">\n      <input type="text" size="32" maxlength="1000" name="css_class"\n             value="')
        # SOURCE LINE 43
        __M_writer(mako_websafe(thing.flair_css_class))
        __M_writer(u'" />\n    </span>\n    <button type="submit">')
        # SOURCE LINE 45
        __M_writer(mako_websafe(_('save')))
        __M_writer(u'</button>\n    <button class="flairdeletebtn">delete</button>\n    <span class="status"></span>\n    ')
        # SOURCE LINE 48
        __M_writer(mako_websafe(utils.error_field('BAD_CSS_NAME', 'css_class')))
        __M_writer(u'\n    ')
        # SOURCE LINE 49
        __M_writer(mako_websafe(utils.error_field('TOO_MUCH_FLAIR_CSS', 'css_class')))
        __M_writer(u'\n  </form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


