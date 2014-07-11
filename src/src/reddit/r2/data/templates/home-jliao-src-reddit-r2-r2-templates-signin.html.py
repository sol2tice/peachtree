# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405085705.351408
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/signin.html'
_template_uri=u'/signin.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['loader_spinner']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div id="signin_page" class="form_page">\n    <div id="form_header">\n        <div class="fh_title">\n            <span>\u767b\u5f55 \u8543\u6843\u6811</span>\n        </div>\n        <div class="fh_explain">\n            <div class="fh_header_link form_text_footer_bottom">\n                <span id="home-signin-forgot-password"><a href="#" target="">\u5fd8\u4e86\u5bc6\u7801?</a></span>\n            </div>\n        </div>\n        <div class="fh_bottom">\n            <div class="fh_message">\n                <span>\u6ce8\u518c\u8d26\u53f7?</span>\n            </div>\n            <div class="form_change" onclick="(function(e){PearltreesHomeSign.showPage(\'signup_page\');e.stopPropagation()})(event)">\n                <span>\u25b6 \u52a0\u5165</span>\n            </div>\n        </div>\n    </div>\n    <div id="form_body">\n        <form class="form_sign" id="signin_form" method="post" name="signin_form">\n            <input type="text" id="log_username" name="log_username" class="form_control beLowerCase form_control_focus" placeholder="\u7528\u6237\u540d" autofocus="" autocomplete="on">\n            <div class="form_error_container">\n                <div class="form_error"></div>\n            </div><input type="password" id="log_password" name="log_password" class="form_control" placeholder="\u5bc6\u7801">\n            <div class="form_error_container">\n                <div id="log_error" class="form_error"></div>\n            </div>\n            <div class="from_button_container">\n                <div id="cancel_button" class="form_button" onclick="PearltreesHomeSign.cancel(); return false;">\n                    \u53d6\u6d88\n                </div>\n                <div id="signin-button" class="form_button" onclick="PearltreesHomeSign.submitLogInForm(); return false;">\n                    \u767b\u5f55\n                </div>\n                <div id="signin-loader-button" class="form_button loader_button" style="display: none;">\n                    ')
        # SOURCE LINE 37
        __M_writer(mako_websafe(self.loader_spinner()))
        __M_writer(u'\n                </div>\n            </div>\n        </form>\n    </div>\n    ')
        # SOURCE LINE 54
        __M_writer(u'\n</div>\n\n')
        # SOURCE LINE 61
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_loader_spinner(context):
    context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n')
        # SOURCE LINE 58
        for i in range(1, 12):                         
            # SOURCE LINE 59
            __M_writer(u"        <div id='sl")
            __M_writer(mako_websafe(i))
            __M_writer(u"' class='load sprite-home-loader")
            __M_writer(mako_websafe(i))
            __M_writer(u"' style='display: none;'></div>  \n")
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


