# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918615.810598
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/subredditselector.html'
_template_uri='/subredditselector.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x7f1dd60c7750', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd60c7750')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60c7750')._populate(_import_ns, [u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n\n<div id="sr-autocomplete-area">\n  <input id="sr-autocomplete" name="sr" type="text"\n         autocomplete="off"\n')
        # SOURCE LINE 11
        if thing.include_searches:
            # SOURCE LINE 12
            __M_writer(u'           onkeyup="sr_name_up(event)"\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'         onkeydown="return sr_name_down(event)"\n         onblur="hide_sr_name_list()"\n')
        # SOURCE LINE 16
        if thing.default_sr:
            # SOURCE LINE 17
            __M_writer(u'           value="')
            __M_writer(mako_websafe(thing.default_sr.name))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 19
        if thing.required:
            # SOURCE LINE 20
            __M_writer(u'         required\n')
            pass
        # SOURCE LINE 22
        __M_writer(u'         />\n  <ul id="sr-drop-down">\n    <li class="sr-name-row"\n        onmouseover="highlight_reddit(this)"\n        onmousedown="return sr_dropdown_mdown(this)"\n        onmouseup="sr_dropdown_mup(this)">nothin</li>\n  </ul>\n</div>\n<script type="text/javascript">\n  reddit.sr_cache = ')
        # SOURCE LINE 31
        __M_writer(mako_websafe(unsafe(thing.sr_searches)))
        __M_writer(u';\n</script>\n')
        # SOURCE LINE 33
        __M_writer(mako_websafe(error_field("SUBREDDIT_NOEXIST", "sr", "div")))
        __M_writer(u'\n')
        # SOURCE LINE 34
        __M_writer(mako_websafe(error_field("SUBREDDIT_NOTALLOWED", "sr", "div")))
        __M_writer(u'\n')
        # SOURCE LINE 35
        __M_writer(mako_websafe(error_field("SUBREDDIT_REQUIRED", "sr", "div")))
        __M_writer(u'\n\n<div id="suggested-reddits">\n')
        # SOURCE LINE 38
        for title, subreddits in thing.subreddit_names:
            # SOURCE LINE 39
            __M_writer(u'    <h3>')
            __M_writer(mako_websafe(title))
            __M_writer(u'</h3>\n    <ul>\n')
            # SOURCE LINE 41
            for name in subreddits:
                # SOURCE LINE 42
                __M_writer(u'      <li>\n        <a href="#" tabindex="100" onclick="set_sr_name(this); return false">')
                # SOURCE LINE 43
                __M_writer(mako_websafe(name))
                __M_writer(u'</a>&#32;\n      </li>\n')
                pass
            # SOURCE LINE 46
            __M_writer(u'    </ul>\n')
            pass
        # SOURCE LINE 48
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


