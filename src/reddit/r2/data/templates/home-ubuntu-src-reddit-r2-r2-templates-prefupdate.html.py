# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401922943.677895
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/prefupdate.html'
_template_uri='/prefupdate.html'
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
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f1db4360050', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1db4360050')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1db4360050')._populate(_import_ns, [u'error_field'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n\n')
        # SOURCE LINE 27
        if thing.email:
            # SOURCE LINE 28
            __M_writer(u'<form action="/post/update_email" method="post" \n      onsubmit="return post_form(this, \'update_email\')" id="pref-update-email">\n\n  <h1>\n')
            # SOURCE LINE 32
            if thing.verify:
                # SOURCE LINE 33
                __M_writer(u'    ')
                __M_writer(mako_websafe(_("verify your email")))
                __M_writer(u'\n')
                # SOURCE LINE 34
            else:
                # SOURCE LINE 35
                __M_writer(u'    ')
                __M_writer(mako_websafe(_("update your email")))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 37
            __M_writer(u'  </h1>\n\n  <div class="spacer">\n    ')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 40
                    __M_writer(u'\n      <input type="password" name="curpass">\n      ')
                    # SOURCE LINE 42
                    __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "curpass")))
                    __M_writer(u'\n    ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 40
                __M_writer(mako_websafe(utils.round_field(description=(_('(required)')),title=(_('current password')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 43
            __M_writer(u'\n  </div>\n\n  ')
            # SOURCE LINE 46

            if not c.user.email:
              description = _("not set")
              v_link = None
            elif c.user.email_verified:
              description = _("verified")
              v_link = None
            elif c.user.email_verified is False:
              description = _("verification pending")
              v_link = _("click to resend")
            else:
              description = _("unverified")
              v_link = _("click to verify")
            
            if v_link and not thing.verify:
              description = "(%s;&#32;<a href='/verify'>%s</a>)" % (description, v_link)
              description = unsafe(description)
            else:
              description = "(%s)" % description
              
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['description','v_link'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 65
            __M_writer(u'\n\n  <div class="spacer">\n    ')
            def ccall(caller):
                def body():
                    getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 68
                    __M_writer(u'\n      <input type="text" name="email" value="')
                    # SOURCE LINE 69
                    __M_writer(mako_websafe(getattr(c.user, 'email', '')))
                    __M_writer(u'">\n      ')
                    # SOURCE LINE 70
                    __M_writer(mako_websafe(error_field("BAD_EMAILS", "email")))
                    __M_writer(u'\n    ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 68
                __M_writer(mako_websafe(utils.round_field(description=(description),title=(_('email')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 71
            __M_writer(u'\n  </div>\n\n')
            # SOURCE LINE 74
            if thing.verify and not c.user.email_verified:
                # SOURCE LINE 75
                __M_writer(u'     <input type="hidden" name="verify" value="1"/>\n     <input type="hidden" name="dest" value="')
                # SOURCE LINE 76
                __M_writer(mako_websafe(thing.dest))
                __M_writer(u'">\n     <button type="submit" class="btn">')
                # SOURCE LINE 77
                __M_writer(mako_websafe(_('send verification email')))
                __M_writer(u'</button>\n')
                # SOURCE LINE 78
            else:
                # SOURCE LINE 79
                __M_writer(u'     <button type="submit" class="btn">')
                __M_writer(mako_websafe(_('save')))
                __M_writer(u'</button>\n')
                pass
            # SOURCE LINE 81
            __M_writer(u'  <span class="status error"></span>\n</form>\n')
            pass
        # SOURCE LINE 84
        __M_writer(u'\n')
        # SOURCE LINE 85
        if thing.email and thing.password:
            # SOURCE LINE 86
            __M_writer(u'<br>\n')
            pass
        # SOURCE LINE 88
        __M_writer(u'\n')
        # SOURCE LINE 89
        if thing.password:
            # SOURCE LINE 90
            __M_writer(u'<form action="/post/update_password" method="post" \n      onsubmit="return post_form(this, \'update_password\')" id="pref-update-password">\n\n  <h1>')
            # SOURCE LINE 93
            __M_writer(mako_websafe(_("update your password")))
            __M_writer(u'</h1>\n\n  <div class="spacer">\n    ')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 96
                    __M_writer(u'\n      <input type="password" name="curpass">\n      ')
                    # SOURCE LINE 98
                    __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "curpass")))
                    __M_writer(u'\n    ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 96
                __M_writer(mako_websafe(utils.round_field(description=(_('(required)')),title=(_('current password')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 99
            __M_writer(u'\n  </div>\n\n  <div class="spacer">\n    ')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 103
                    __M_writer(u'\n      <input type="password" name="newpass">\n      ')
                    # SOURCE LINE 105
                    __M_writer(mako_websafe(error_field("BAD_PASSWORD", "newpass")))
                    __M_writer(u'\n    ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 103
                __M_writer(mako_websafe(utils.round_field(title=(_('new password')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 106
            __M_writer(u'\n  </div>\n\n  <div class="spacer">\n    ')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 110
                    __M_writer(u'\n      <input type="password" name="verpass">\n      ')
                    # SOURCE LINE 112
                    __M_writer(mako_websafe(error_field("BAD_PASSWORD_MATCH", "verpass")))
                    __M_writer(u'\n    ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 110
                __M_writer(mako_websafe(utils.round_field(title=(_('verify password')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 113
            __M_writer(u'\n  </div>\n\n  <button type="submit" class="btn">')
            # SOURCE LINE 116
            __M_writer(mako_websafe(_('save')))
            __M_writer(u'</button>\n  <span class="status error"></span>\n</form>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


