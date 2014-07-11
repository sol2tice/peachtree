# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402178932.606599
_template_filename='/home/jliao/src/reddit/r2/r2/templates/login.html'
_template_uri='/login.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['login_form', 'login_panel']


# SOURCE LINE 23

from r2.lib.template_helpers import add_sr
from r2.lib.strings import strings
from r2.lib.utils import UrlParser
import random
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f8c8daf1c50', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8daf1c50')] = ns

    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7f8c8dbac490', context._clean_inheritance_tokens(), templateuri=u'captcha.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8dbac490')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daf1c50')._populate(_import_ns, [u'error_field', u'plain_link', u'img_link'])
        _mako_get_namespace(context, '__anon_0x7f8c8dbac490')._populate(_import_ns, [u'captchagen'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def login_form(register=False,user='',dest=''):
            return render_login_form(context.locals_(__M_locals),register,user,dest)
        def login_panel(lf,user_reg='',user_login='',dest='',registration_info=None):
            return render_login_panel(context.locals_(__M_locals),lf,user_reg,user_login,dest,registration_info)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        if c.user_is_loggedin:
            # SOURCE LINE 34
            __M_writer(u'  <p class="error">')
            __M_writer(mako_websafe(_("you are logged in. go use the site!")))
            __M_writer(u'</p>\n')
            # SOURCE LINE 35
        else:
            # SOURCE LINE 36
            __M_writer(u'  ')
            __M_writer(mako_websafe(login_panel(login_form, 
                user_reg = thing.user_reg, user_login = thing.user_login, 
                dest=thing.dest,
                registration_info=thing.registration_info)))
            # SOURCE LINE 39
            __M_writer(u'\n')
            # SOURCE LINE 40
            if not thing.is_popup and not g.disable_captcha:
                # SOURCE LINE 41
                __M_writer(u'  <script type="text/javascript">\n    $.request("new_captcha");\n  </script>\n')
                pass
            pass
        # SOURCE LINE 46
        __M_writer(u'\n')
        # SOURCE LINE 143
        __M_writer(u'\n\n\n')
        # SOURCE LINE 172
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_form(context,register=False,user='',dest=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daf1c50')._populate(_import_ns, [u'error_field', u'plain_link', u'img_link'])
        _mako_get_namespace(context, '__anon_0x7f8c8dbac490')._populate(_import_ns, [u'captchagen'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        captchagen = _import_ns.get('captchagen', context.get('captchagen', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n  ')
        # SOURCE LINE 48

        op = "reg" if register else "login"
        base = g.https_endpoint if not c.cname else ''
        tabindex = 3 if register else 2
          
        
        # SOURCE LINE 52
        __M_writer(u'\n  <form id="login_')
        # SOURCE LINE 53
        __M_writer(mako_websafe(op))
        __M_writer(u'" method="post" \n        action="')
        # SOURCE LINE 54
        __M_writer(mako_websafe(add_sr(base + '/post/' + op, nocname=not c.authorized_cname)))
        __M_writer(u'"\n        class="user-form ')
        # SOURCE LINE 55
        __M_writer(mako_websafe('register-form' if register else 'login-form'))
        __M_writer(u'">\n')
        # SOURCE LINE 56
        if c.cname:
            # SOURCE LINE 57
            __M_writer(u'       <input type="hidden" name="')
            __M_writer(mako_websafe(UrlParser.cname_get))
            __M_writer(u'" \n              value="')
            # SOURCE LINE 58
            __M_writer(mako_websafe(random.random()))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 60
        __M_writer(u'    <input type="hidden" name="op" value="')
        __M_writer(mako_websafe(op))
        __M_writer(u'" />\n')
        # SOURCE LINE 61
        if dest:
            # SOURCE LINE 62
            __M_writer(u'      <input type="hidden" name="dest" value="')
            __M_writer(mako_websafe(dest))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 64
        __M_writer(u'    <div>\n      <ul>\n        <li class="name-entry">\n          <label for="user_')
        # SOURCE LINE 67
        __M_writer(mako_websafe(op))
        __M_writer(u'">')
        __M_writer(mako_websafe(_('username')))
        __M_writer(u':</label>\n          <input value="')
        # SOURCE LINE 68
        __M_writer(mako_websafe(user))
        __M_writer(u'" name="user" id="user_')
        __M_writer(mako_websafe(op))
        __M_writer(u'" \n                 type="text" maxlength="20" tabindex="')
        # SOURCE LINE 69
        __M_writer(mako_websafe(tabindex))
        __M_writer(u'" autofocus />\n')
        # SOURCE LINE 70
        if register:
            # SOURCE LINE 71
            __M_writer(u'            <span class="throbber"></span>\n            <span class="notice-taken">')
            # SOURCE LINE 72
            __M_writer(mako_websafe(_('try another')))
            __M_writer(u'</span>\n            <span class="notice-available">')
            # SOURCE LINE 73
            __M_writer(mako_websafe(_('available!')))
            __M_writer(u'</span>\n            ')
            # SOURCE LINE 74
            __M_writer(mako_websafe(error_field("BAD_USERNAME", "user", kind="span")))
            __M_writer(u'\n            ')
            # SOURCE LINE 75
            __M_writer(mako_websafe(error_field("USERNAME_TAKEN", "user", kind="span")))
            __M_writer(u'\n            ')
            # SOURCE LINE 76
            __M_writer(mako_websafe(error_field("USERNAME_TAKEN_DEL", "user", kind="span")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 78
        __M_writer(u'        </li>\n')
        # SOURCE LINE 79
        if register:
            # SOURCE LINE 80
            __M_writer(u'        <li>\n          <label for="email_')
            # SOURCE LINE 81
            __M_writer(mako_websafe(op))
            __M_writer(u'">\n            ')
            # SOURCE LINE 82
            __M_writer(mako_websafe(_('account recovery email')))
            __M_writer(u': &nbsp;<i>(')
            __M_writer(mako_websafe(_('optional')))
            __M_writer(u')\n          </i></label>\n          <input value="" name="email" id="email_')
            # SOURCE LINE 84
            __M_writer(mako_websafe(op))
            __M_writer(u'" \n                 type="email" maxlength="50" tabindex="')
            # SOURCE LINE 85
            __M_writer(mako_websafe(tabindex))
            __M_writer(u'"/>\n          <label for="email_')
            # SOURCE LINE 86
            __M_writer(mako_websafe(op))
            __M_writer(u'" class="note">')
            __M_writer(mako_websafe(_('we only send email at your request')))
            __M_writer(u'</label>\n')
            # SOURCE LINE 87
            if register:
                # SOURCE LINE 88
                __M_writer(u'            ')
                __M_writer(mako_websafe(error_field("BAD_EMAILS", "email", kind="span")))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 90
            __M_writer(u'        </li>\n')
            pass
        # SOURCE LINE 92
        __M_writer(u'        <li>\n          <label for="passwd_')
        # SOURCE LINE 93
        __M_writer(mako_websafe(op))
        __M_writer(u'">')
        __M_writer(mako_websafe(_('password')))
        __M_writer(u':</label>\n          <input id="passwd_')
        # SOURCE LINE 94
        __M_writer(mako_websafe(op))
        __M_writer(u'" name="passwd" type="password" \n                 tabindex="')
        # SOURCE LINE 95
        __M_writer(mako_websafe(tabindex))
        __M_writer(u'"/>\n')
        # SOURCE LINE 96
        if register:
            # SOURCE LINE 97
            __M_writer(u'            ')
            __M_writer(mako_websafe(error_field("BAD_PASSWORD", "passwd", kind="span")))
            __M_writer(u'\n')
            # SOURCE LINE 98
        else:
            # SOURCE LINE 99
            __M_writer(u'            ')
            __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "passwd", kind="span")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 101
        __M_writer(u'        </li>\n')
        # SOURCE LINE 102
        if register:
            # SOURCE LINE 103
            __M_writer(u'        <li>\n          <label for="passwd2_')
            # SOURCE LINE 104
            __M_writer(mako_websafe(op))
            __M_writer(u'">')
            __M_writer(mako_websafe(_('verify password')))
            __M_writer(u':</label>\n          <input name="passwd2" id="passwd2_')
            # SOURCE LINE 105
            __M_writer(mako_websafe(op))
            __M_writer(u'" \n                 type="password" tabindex="')
            # SOURCE LINE 106
            __M_writer(mako_websafe(tabindex))
            __M_writer(u'"/>\n          ')
            # SOURCE LINE 107
            __M_writer(mako_websafe(error_field("BAD_PASSWORD_MATCH", "passwd2", kind="span")))
            __M_writer(u'\n        </li>\n        <li>\n')
            # SOURCE LINE 110
            if not g.disable_captcha:
                # SOURCE LINE 111
                __M_writer(u'          ')
                iden = hasattr(thing, "captcha") and thing.captcha.iden or '' 
                
                __M_writer(u'\n          ')
                # SOURCE LINE 112
                __M_writer(mako_websafe(captchagen(iden, tabulate=True, label=False, size=30, tabindex=tabindex)))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 114
            __M_writer(u'        </li>\n')
            pass
        # SOURCE LINE 116
        __M_writer(u'      <li>\n        <input type="checkbox" name="rem" id="rem_')
        # SOURCE LINE 117
        __M_writer(mako_websafe(op))
        __M_writer(u'" tabindex="')
        __M_writer(mako_websafe(tabindex))
        __M_writer(u'" />\n        <label for="rem_')
        # SOURCE LINE 118
        __M_writer(mako_websafe(op))
        __M_writer(u'" class="remember">\n          ')
        # SOURCE LINE 119
        __M_writer(mako_websafe(_('remember me')))
        __M_writer(u'\n        </label>\n      </li>\n')
        # SOURCE LINE 122
        if not register:
            # SOURCE LINE 123
            __M_writer(u'      <li>\n        <a class="recover-password" href="/password">\n          ')
            # SOURCE LINE 125
            __M_writer(mako_websafe(_("recover password")))
            __M_writer(u'\n        </a>\n      </li>\n')
            pass
        # SOURCE LINE 129
        __M_writer(u'    </ul>\n      <p class="submit">\n        <button type="submit" class="button" tabindex="')
        # SOURCE LINE 131
        __M_writer(mako_websafe(tabindex))
        __M_writer(u'">\n          ')
        # SOURCE LINE 132
        __M_writer(mako_websafe(register and _("create account") or _("login")))
        __M_writer(u'\n        </button>\n        <span class="throbber"></span>\n        <span class="status"></span>\n')
        # SOURCE LINE 136
        if register:
            # SOURCE LINE 137
            __M_writer(u'          ')
            __M_writer(mako_websafe(error_field("RATELIMIT", "ratelimit")))
            __M_writer(u'\n          ')
            # SOURCE LINE 138
            __M_writer(mako_websafe(error_field("RATELIMIT", "vdelay")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 140
        __M_writer(u'      </p>\n    </div>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_panel(context,lf,user_reg='',user_login='',dest='',registration_info=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daf1c50')._populate(_import_ns, [u'error_field', u'plain_link', u'img_link'])
        _mako_get_namespace(context, '__anon_0x7f8c8dbac490')._populate(_import_ns, [u'captchagen'])
        __M_writer = context.writer()
        # SOURCE LINE 146
        __M_writer(u'\n  <div class="login-form-section divide register">\n    <h3>')
        # SOURCE LINE 148
        __M_writer(mako_websafe(_("create a new account")))
        __M_writer(u'</h3>\n    <p class="tagline">\n      ')
        # SOURCE LINE 150
        __M_writer(mako_websafe(_("all it takes is a username and password")))
        __M_writer(u'\n    </p>\n')
        # SOURCE LINE 152
        if registration_info:
            # SOURCE LINE 153
            __M_writer(u'      <div class="registration-info">\n        ')
            # SOURCE LINE 154
            __M_writer(mako_websafe(registration_info))
            __M_writer(u'\n      </div>\n')
            pass
        # SOURCE LINE 157
        __M_writer(u'    ')
        __M_writer(mako_websafe(lf(register=True, user=user_reg, dest=dest)))
        __M_writer(u'\n    <p>\n      <span class="orangered">\n        ')
        # SOURCE LINE 160
        __M_writer(mako_websafe(_("is it really that easy? only one way to find out...")))
        __M_writer(u'\n      </span>\n    </p>\n  </div>\n  <div class="login-form-section login">\n    <h3>')
        # SOURCE LINE 165
        __M_writer(mako_websafe(_("login")))
        __M_writer(u'</h3>\n    <p class="tagline">\n      ')
        # SOURCE LINE 167
        __M_writer(mako_websafe(_("already have an account and just want to login?")))
        __M_writer(u'\n    </p>\n    ')
        # SOURCE LINE 169
        __M_writer(mako_websafe(lf(user = user_login, dest = dest)))
        __M_writer(u'\n  </div>\n  <div class="clear"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


