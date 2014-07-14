# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401923782.131673
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/prefotp.html'
_template_uri='/prefotp.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib import js
from r2.lib.strings import strings


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7f1dd6011990', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd6011990')] = ns

    # SOURCE LINE 29
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd6011990')._populate(_import_ns, [u'error_field', u'_md'])
        utils = _mako_get_namespace(context, 'utils')
        _md = _import_ns.get('_md', context.get('_md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 31
        __M_writer(mako_websafe(_("two-factor authentication")))
        __M_writer(u'</h1>\n\n')
        # SOURCE LINE 33
        if c.user.otp_secret:
            # SOURCE LINE 34
            __M_writer(u'<form action="/post/disable_otp" method="post" onsubmit="return post_form(this, \'disable_otp\')" id="pref-otp">\n\n')
            # SOURCE LINE 36
            __M_writer(mako_websafe(_md("two-factor authentication is currently **enabled**. fill out the form below if you would like to disable it.", wrap=True)))
            __M_writer(u'\n\n')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 38
                    __M_writer(u'\n  <input type="password" name="password" />\n  ')
                    # SOURCE LINE 40
                    __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "password")))
                    __M_writer(u'\n')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 38
                __M_writer(mako_websafe(utils.round_field(description=(_('(required)')),title=(_('password')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 41
            __M_writer(u'\n\n')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 43
                    __M_writer(u'\n  <input type="number" name="otp" maxlength="6" />\n  ')
                    # SOURCE LINE 45
                    __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "otp")))
                    __M_writer(u'\n  ')
                    # SOURCE LINE 46
                    __M_writer(mako_websafe(error_field("NO_OTP_SECRET", "otp")))
                    __M_writer(u'\n  ')
                    # SOURCE LINE 47
                    __M_writer(mako_websafe(error_field("RATELIMIT", "otp")))
                    __M_writer(u'\n')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 43
                __M_writer(mako_websafe(utils.round_field(description=(_('(required)')),title=(_('one-time password')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 48
            __M_writer(u'\n\n<input type="submit" value="')
            # SOURCE LINE 50
            __M_writer(mako_websafe(_("disable")))
            __M_writer(u'">\n</form>\n')
            # SOURCE LINE 52
        else:
            # SOURCE LINE 53
            __M_writer(u'<form action="/post/generate_otp_secret" method="post" onsubmit="return post_form(this, \'generate_otp_secret\')" id="pref-otp">\n\n')
            # SOURCE LINE 55
            __M_writer(mako_websafe(_md("enter your current password below to start the activation process for two-factor authentication.", wrap=True)))
            __M_writer(u'\n\n')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 57
                    __M_writer(u'\n  <input type="password" name="password" />\n  ')
                    # SOURCE LINE 59
                    __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "password")))
                    __M_writer(u'\n')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 57
                __M_writer(mako_websafe(utils.round_field(description=(_('(required)')),title=(_('password')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 60
            __M_writer(u'\n\n<input type="submit" value="')
            # SOURCE LINE 62
            __M_writer(mako_websafe(_("activate")))
            __M_writer(u'">\n\n</form>\n\n<form action="/post/enable_otp" method="post" onsubmit="return post_form(this, \'enable_otp\')" id="pref-otp-qr">\n\n<div id="otp-secret-info">\n    ')
            # SOURCE LINE 69
            __M_writer(mako_websafe(_md("below is your two-factor authentication secret. you can scan the QR code with Google Authenticator or enter the key below manually. you WILL NOT have another chance to see this secret.")))
            __M_writer(u'\n</div>\n\n')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 72
                    __M_writer(u'\n  <input type="number" name="otp" maxlength="6" />\n  ')
                    # SOURCE LINE 74
                    __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "otp")))
                    __M_writer(u'\n  ')
                    # SOURCE LINE 75
                    __M_writer(mako_websafe(error_field("EXPIRED", "otp")))
                    __M_writer(u'\n')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 72
                __M_writer(mako_websafe(utils.round_field(description=(_('(required)')),title=(_('one-time password')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 76
            __M_writer(u'\n\n<input type="submit" value="')
            # SOURCE LINE 78
            __M_writer(mako_websafe(_("enable")))
            __M_writer(u'">\n\n</form>\n')
            pass
        # SOURCE LINE 82
        __M_writer(u'\n')
        # SOURCE LINE 83
        __M_writer(mako_websafe(unsafe(js.use("qrcode"))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


