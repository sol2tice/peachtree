# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402179425.876884
_template_filename='/home/jliao/src/reddit/r2/r2/templates/passwordverificationform.html'
_template_uri='/passwordverificationform.html'
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
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7f8c8da9a350', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8da9a350')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da9a350')._populate(_import_ns, [u'error_field'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23

        from r2.lib.template_helpers import static
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n<div class="content over18" style="text-align: center">\n  <img src="')
        # SOURCE LINE 31
        __M_writer(mako_websafe(static('over18.png')))
        __M_writer(u'" alt="" height="254" width="180" />\n\n  <h1>let me see your papers</h1>\n\n  <form action="/post/adminon" method="post"\n      onsubmit="return post_form(this, \'adminon\')" id="adminon">\n    <div class="spacer">\n      ')
        def ccall(caller):
            def body():
                thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
                error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 38
                __M_writer(u'\n')
                # SOURCE LINE 39
                if thing.dest:
                    # SOURCE LINE 40
                    __M_writer(u'          <input type="hidden" name="dest" value="')
                    __M_writer(mako_websafe(thing.dest))
                    __M_writer(u'" />\n')
                    pass
                # SOURCE LINE 42
                __M_writer(u'      <input type="password" name="password" tabindex="1" autofocus />\n      ')
                # SOURCE LINE 43
                __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "password")))
                __M_writer(u'\n      ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 38
            __M_writer(mako_websafe(utils.round_field(css_class=u'adminpasswordform',description=(_('(required)')),title=(_('password')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        if not g.disable_require_admin_otp or c.user.otp_secret:
            # SOURCE LINE 47
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    __M_writer(u'\n      <input type="text" name="otp" maxlength="6" tabindex="1" required pattern="[0-9]{6}" autocomplete="off"\n')
                    # SOURCE LINE 49
                    if c.otp_cached:
                        # SOURCE LINE 50
                        __M_writer(u'      disabled\n')
                        pass
                    # SOURCE LINE 52
                    __M_writer(u'      />\n      ')
                    # SOURCE LINE 53
                    __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "otp")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 54
                    __M_writer(mako_websafe(error_field("NO_OTP_SECRET", "otp")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 55
                    __M_writer(mako_websafe(error_field("RATELIMIT", "otp")))
                    __M_writer(u'\n\n      <label>\n          <input type="checkbox" name="remember" tabindex="1"\n')
                    # SOURCE LINE 59
                    if c.otp_cached:
                        # SOURCE LINE 60
                        __M_writer(u'            disabled\n            checked\n')
                        pass
                    # SOURCE LINE 63
                    __M_writer(u'          > ')
                    __M_writer(mako_websafe(_("remember this computer")))
                    __M_writer(u'</label>\n      ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 47
                __M_writer(mako_websafe(utils.round_field(css_class=u'adminpasswordform',description=(_('(required)')),title=(_('one-time password')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 64
            __M_writer(u'\n')
            pass
        # SOURCE LINE 66
        __M_writer(u'\n      <p><button type="submit" class="btn" tabindex="1">')
        # SOURCE LINE 67
        __M_writer(mako_websafe(_('turn admin on')))
        __M_writer(u'</button></p>\n      <p class="status error"></p>\n    </div>\n  </form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


