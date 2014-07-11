# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405086132.961763
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/signup.html'
_template_uri=u'/signup.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7f7608235a90', context._clean_inheritance_tokens(), templateuri=u'signin.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f7608235a90')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f7608235a90')._populate(_import_ns, [u'loader_spinner'])
        loader_spinner = _import_ns.get('loader_spinner', context.get('loader_spinner', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n<div id="signup_page" class="form_page" style="display: none">\n    <div id="form_header">\n        <div class="fh_title">\n            <span>\u6ce8\u518c\u65b0\u8d26\u53f7</span>\n        </div>\n        <div class="fh_explain">\n            <span>\u6ce8\u518c\u7b80\u5355\u4e14\u65e0\u4efb\u4f55\u8d39\u7528</span>\n        </div>\n        <div class="fh_bottom">\n            <div class="fh_message">\n                <span>\u5df2\u7ecf\u5f00\u901a\u8d26\u53f7\uff1f</span>\n            </div>\n            <div class="form_change" onclick="(function(e){PearltreesHomeSign.showPage(\'signin_page\');e.stopPropagation()})(event)">\n                <span>\u25b6 \u767b\u5f55</span>\n            </div>\n        </div>\n    </div>\n    <div id="form_body">\n        <form class="form_sign" id="signup_form" autocomplete="off" name="signup_form">\n            <input type="text" id="username" name="username" class="form_control beLowerCase form_control_focus" placeholder="\u7528\u6237\u540d" autofocus="" autocomplete="off">\n            <div class="form_error_container">\n                <div id="username_error" class="form_error"></div>\n            </div><input type="text" id="email" name="email" class="form_control" placeholder="\u90ae\u7bb1" value="" autocomplete="off">\n            <div class="form_error_container">\n                <div id="email_error" class="form_error"></div>\n            </div><input type="password" id="password" name="password" class="form_control" placeholder="\u5bc6\u7801" autocomplete="off">\n            <div class="form_text_footer">\n                <span>\u6211\u5df2\u9605\u8bfb\u5e76\u540c\u610f&nbsp;<a href="http://www.pearltrees.com/info/terms" target="_blank">\u76f8\u5173\u670d\u52a1\u6761\u6b3e</a></span>\n            </div>\n            <div class="from_button_container">\n                <div id="cancel_button" class="form_button" onclick="PearltreesHomeSign.cancel(); return false;">\n                    \u53d6\u6d88\n                </div>\n                <div id="signup-button" class="form_button" onclick="$(\'#signup_form\').submit(); return false;">\n                    \u6ce8\u518c\n                </div>\n                <div id="signup-loader-button" class="form_button loader_button" style="display: none;">\n                    ')
        # SOURCE LINE 40
        __M_writer(mako_websafe(loader_spinner()))
        __M_writer(u'\n                </div>\n            </div>\n        </form>\n    </div>\n    ')
        # SOURCE LINE 57
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


