# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404039727.966482
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/invitation.html'
_template_uri=u'/invitation.html'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div id="special-home-invitation-page" class="form_page invitation_page" style="display: none">\n    <div id="special-home-invitation-header" class="invitation-page-header">\n        <div class="invitation-header-avatar">\n            <div id="signup-invitation-header-avatar-mask" class="invitation-header-avatar-mask sprite-home-masque_avatar_home"/>\n        </div>\n        <div class="invitation-header-title">\n\t\t\t\t    \t\t\t\t:</div>\n    </div>\n    <div id="special-home-invitation-body" class="invitation-page-body">\n        <div class="invitation-body-subscription-message invitation-teamup">\n\t\t\t\t    \t\t\t\tHi! I\'d like to team-up with you on Pearltrees. Create your account to get started!</div>\n        <div class="invitation-body-subscription-message invitation-default">\n\t\t\t\t    \t\t\t\tHi! I\'d like to connect with you on Pearltrees. Create your account to get started!</div>\n        <div class="form_button_invit invitation-body-subscription-button" onClick="PearltreesHomeSign.showPage(\'signup_page\')">\n\t\t\t\t    \t\t\t\tOK</div>\n        <div class="invitation-body-redirection-button form_text_footer" onClick="PearltreesHomeSign.showPage(\'signin_page\')">\n\t\t\t\t    \t\t\t\tAlready have an account?</div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


