# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401923687.212272
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/prefdelete.html'
_template_uri='/prefdelete.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.filters import safemarkdown


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

    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7f1dd6011290', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd6011290')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd6011290')._populate(_import_ns, [u'error_field'])
        utils = _mako_get_namespace(context, 'utils')
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 29
        __M_writer(mako_websafe(_("delete your reddit account")))
        __M_writer(u'</h1>\n\n<form action="/post/delete" method="post"\n  onsubmit="')
        # SOURCE LINE 32
        __M_writer(mako_websafe("return post_form(this, 'delete_user', function(x) {return '%s'})" % _("deleting...")))
        __M_writer(u'" id="pref-delete">\n\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 35
                __M_writer(u'\n    <div class="rounded white-field">\n      ')
                # SOURCE LINE 37
                __M_writer(mako_websafe(unsafe(safemarkdown(_(
        " * if you're having a problem on reddit, please consider [contacting us](/feedback) about it before deleting your account.\n"
        " * deleting your account will not delete the content of posts and comments you've made on reddit. to do so, please delete them individually."
      )))))
                # SOURCE LINE 40
                __M_writer(u'\n    </div>\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 35
            __M_writer(mako_websafe(utils.round_field(title=(_('sorry to see you go!')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 42
        __M_writer(u'\n</div>\n\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 46
                __M_writer(u'\n    <textarea name="delete_message" id="delete-message"></textarea>\n    ')
                # SOURCE LINE 48
                __M_writer(mako_websafe(error_field("TOO_LONG", "delete_message")))
                __M_writer(u'\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 46
            __M_writer(mako_websafe(utils.round_field(description=u'(' + (_('optional')) + u')',title=(_('why are you deleting this account?')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 49
        __M_writer(u'\n</div>\n\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 53
                __M_writer(u'\n    <label for="delete-password">')
                # SOURCE LINE 54
                __M_writer(mako_websafe(_("username")))
                __M_writer(u'</label>\n    ')
                # SOURCE LINE 55
                __M_writer(mako_websafe(error_field("NOT_USER", "user")))
                __M_writer(u'\n    <input name="user" id="delete_user" type="text" />\n    <label for="delete-password">')
                # SOURCE LINE 57
                __M_writer(mako_websafe(_("password")))
                __M_writer(u'</label>\n    ')
                # SOURCE LINE 58
                __M_writer(mako_websafe(error_field("WRONG_PASSWORD", "passwd")))
                __M_writer(u'\n    <input name="passwd" id="delete_password" type="password" />\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 53
            __M_writer(mako_websafe(utils.round_field(css_class=u'credentials',description=u'(' + (_('for security purposes')) + u')',title=(_('account credentials')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 60
        __M_writer(u'\n</div>  \n\n<div class="spacer">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 64
                __M_writer(u'\n    <div class="rounded white-field">\n      <input name="confirm" id="confirm-delete" type="checkbox"/>\n      <label for="confirm-delete">')
                # SOURCE LINE 67
                __M_writer(mako_websafe(_("I understand that deleted accounts are not recoverable.")))
                __M_writer(u'</label>\n    </div>\n    ')
                # SOURCE LINE 69
                __M_writer(mako_websafe(error_field("CONFIRM", "confirm")))
                __M_writer(u'\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 64
            __M_writer(mako_websafe(utils.round_field(title=(_('confirmation')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 70
        __M_writer(u'\n</div>\n\n<div class="spacer">\n  <button type="submit" class="btn">')
        # SOURCE LINE 74
        __M_writer(mako_websafe(_("delete account")))
        __M_writer(u'</button>\n  <span class="status"></span>\n  ')
        # SOURCE LINE 76
        __M_writer(mako_websafe(error_field("RATELIMIT", "vdelay")))
        __M_writer(u'\n</div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


