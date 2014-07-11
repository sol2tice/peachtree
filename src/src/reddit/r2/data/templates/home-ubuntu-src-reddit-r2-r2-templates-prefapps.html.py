# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401922994.271049
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/prefapps.html'
_template_uri='/prefapps.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['authorized_app', 'sr_list', 'developed_app', 'editable_developer', 'scope_details', 'app_type_selector', 'developers', 'icon']


# SOURCE LINE 23

from r2.lib.template_helpers import static, media_https_if_secure
from r2.lib.utils import timeuntil


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7f1dc0158ed0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dc0158ed0')] = ns

    # SOURCE LINE 28
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f1dc0158850', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dc0158850')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0158ed0')._populate(_import_ns, [u'error_field', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f1dc0158850')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        def app_type_selector(selection='web'):
            return render_app_type_selector(context.locals_(__M_locals),selection)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        def developed_app(app,collapsed=True):
            return render_developed_app(context.locals_(__M_locals),app,collapsed)
        def authorized_app(app_data):
            return render_authorized_app(context.locals_(__M_locals),app_data)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 57
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 80
        __M_writer(u'\n\n')
        # SOURCE LINE 208
        __M_writer(u'\n\n')
        # SOURCE LINE 217
        __M_writer(u'\n\n')
        # SOURCE LINE 264
        __M_writer(u'\n\n')
        # SOURCE LINE 291
        __M_writer(u'\n\n')
        # SOURCE LINE 293
        if thing.my_apps:
            # SOURCE LINE 294
            __M_writer(u'  <h1>')
            __M_writer(mako_websafe(_("authorized applications")))
            __M_writer(u'</h1>\n\n')
            # SOURCE LINE 296
            for app_data in thing.my_apps.values():
                # SOURCE LINE 297
                __M_writer(u'    ')
                __M_writer(mako_websafe(authorized_app(app_data)))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 300
        __M_writer(u'\n<div id="developed-apps">\n  <h1 style="')
        # SOURCE LINE 302
        __M_writer(mako_websafe('' if thing.developed_apps else 'display:none'))
        __M_writer(u'">\n    ')
        # SOURCE LINE 303
        __M_writer(mako_websafe(_("developed applications")))
        __M_writer(u'\n  </h1>\n  <ul>\n')
        # SOURCE LINE 306
        for app in thing.developed_apps:
            # SOURCE LINE 307
            __M_writer(u'      ')
            __M_writer(mako_websafe(developed_app(app)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 309
        __M_writer(u'  </ul>\n</div>\n\n<div class="edit-app-form">\n  <button id="create-app-button" class="submit-img">\n')
        # SOURCE LINE 314
        if thing.developed_apps:
            # SOURCE LINE 315
            __M_writer(u'      ')
            __M_writer(mako_websafe(_('create another app...')))
            __M_writer(u'\n')
            # SOURCE LINE 316
        else:
            # SOURCE LINE 317
            __M_writer(u'      ')
            __M_writer(mako_websafe(_('are you a developer? create an app...')))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 319
        __M_writer(u'  </button>\n  <form method="post" action="/api/updateapp" class="pretty-form" id="create-app"\n   onsubmit="')
        # SOURCE LINE 321
        __M_writer(mako_websafe("return post_form(this, 'updateapp', function(x) {return '%s'})" % _("creating...")))
        __M_writer(u'">\n    <h1>')
        # SOURCE LINE 322
        __M_writer(mako_websafe(_("create application")))
        __M_writer(u'</h1>\n    <input type="hidden" name="uh" value="')
        # SOURCE LINE 323
        __M_writer(mako_websafe(c.modhash))
        __M_writer(u'" />\n    <table class="content preftable">\n      <tr>\n        <th>')
        # SOURCE LINE 326
        __M_writer(mako_websafe(_("name")))
        __M_writer(u'</th>\n        <td class="prefright">\n          <input class="text" name="name">\n          ')
        # SOURCE LINE 329
        __M_writer(mako_websafe(error_field("NO_TEXT", "name")))
        __M_writer(u'\n        </td>\n      </tr>\n      ')
        # SOURCE LINE 332
        __M_writer(mako_websafe(app_type_selector()))
        __M_writer(u'\n      <tr>\n        <th>')
        # SOURCE LINE 334
        __M_writer(mako_websafe(_("description")))
        __M_writer(u'</th>\n        <td class="prefright">\n          <textarea name="description"></textarea>\n        </td>\n      </tr>\n      <tr>\n        <th>')
        # SOURCE LINE 340
        __M_writer(mako_websafe(_("about url")))
        __M_writer(u'</th>\n        <td class="prefright">\n          <input class="text" name="about_url">\n          ')
        # SOURCE LINE 343
        __M_writer(mako_websafe(error_field("BAD_URL", "about_url")))
        __M_writer(u'\n        </td>\n      </tr>\n      <tr>\n        <th>')
        # SOURCE LINE 347
        __M_writer(mako_websafe(_("redirect uri")))
        __M_writer(u'</th>\n        <td class="prefright">\n          <input class="text" name="redirect_uri">\n          ')
        # SOURCE LINE 350
        __M_writer(mako_websafe(error_field("NO_URL", "redirect_uri")))
        __M_writer(u'\n          ')
        # SOURCE LINE 351
        __M_writer(mako_websafe(error_field("BAD_URL", "redirect_uri")))
        __M_writer(u'\n          ')
        # SOURCE LINE 352
        __M_writer(mako_websafe(error_field("INVALID_SCHEME", "redirect_uri")))
        __M_writer(u'\n        </td>\n      </tr>\n    </table>\n    <button type="submit">')
        # SOURCE LINE 356
        __M_writer(mako_websafe(_('create app')))
        __M_writer(u'</button>\n    <span class="status"></span>\n  </form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_authorized_app(context,app_data):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0158ed0')._populate(_import_ns, [u'error_field', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f1dc0158850')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        def scope_details(scope,compact=False,expiration=None):
            return render_scope_details(context,scope,compact,expiration)
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        def developers(app):
            return render_developers(context,app)
        def icon(app):
            return render_icon(context,app)
        __M_writer = context.writer()
        # SOURCE LINE 266
        __M_writer(u'\n  <div id="authorized-app-')
        # SOURCE LINE 267
        __M_writer(mako_websafe(app_data['client']._id))
        __M_writer(u'" class="authorized-app rounded">\n    ')
        # SOURCE LINE 268
        __M_writer(mako_websafe(icon(app_data['client'])))
        __M_writer(u'\n    <div class="app-details">\n      <h2>\n')
        # SOURCE LINE 271
        if app_data['client'].about_url:
            # SOURCE LINE 272
            __M_writer(u'        <a href="')
            __M_writer(mako_websafe(app_data['client'].about_url))
            __M_writer(u'">')
            __M_writer(mako_websafe(app_data['client'].name))
            __M_writer(u'</a>\n')
            # SOURCE LINE 273
        else:
            # SOURCE LINE 274
            __M_writer(u'        ')
            __M_writer(mako_websafe(app_data['client'].name))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 276
        __M_writer(u'      </h2>\n')
        # SOURCE LINE 278
        for sr in sorted(app_data['scopes']):
            # SOURCE LINE 279
            __M_writer(u'        ')
            __M_writer(mako_websafe(scope_details(app_data['scopes'][sr], compact=True)))
            __M_writer(u'<br>\n')
            pass
        # SOURCE LINE 281
        __M_writer(u'    </div>\n    <div class="app-description">')
        # SOURCE LINE 282
        __M_writer(mako_websafe(app_data['client'].description))
        __M_writer(u'</div>\n    ')
        # SOURCE LINE 283
        __M_writer(mako_websafe(developers(app_data['client'])))
        __M_writer(u'\n    ')
        # SOURCE LINE 284
        __M_writer(mako_websafe(ynbutton(_("revoke access"),
               _("revoked"),
               "revokeapp",
               callback="r.apps.revoked",
               hidden_data=dict(client_id=app_data['client']._id),
               _class="revoke-app-button")))
        # SOURCE LINE 289
        __M_writer(u'\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sr_list(context,srs):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0158ed0')._populate(_import_ns, [u'error_field', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f1dc0158850')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 210
        __M_writer(u'\n')
        # SOURCE LINE 211
        for i, name in enumerate(sorted(srs)):
            # SOURCE LINE 212
            if i:
                # SOURCE LINE 213
                __M_writer(u'      ,&#32;\n')
                pass
            # SOURCE LINE 215
            __M_writer(u'    <a href="/r/')
            __M_writer(mako_websafe(name))
            __M_writer(u'">/r/')
            __M_writer(mako_websafe(name))
            __M_writer(u'</a>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_developed_app(context,app,collapsed=True):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0158ed0')._populate(_import_ns, [u'error_field', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f1dc0158850')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        def editable_developer(app,dev):
            return render_editable_developer(context,app,dev)
        utils = _mako_get_namespace(context, 'utils')
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        def developers(app):
            return render_developers(context,app)
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        def icon(app):
            return render_icon(context,app)
        __M_writer = context.writer()
        # SOURCE LINE 82
        __M_writer(u'\n  <li id="developed-app-')
        # SOURCE LINE 83
        __M_writer(mako_websafe(app._id))
        __M_writer(u'"\n      class="developed-app rounded ')
        # SOURCE LINE 84
        __M_writer(mako_websafe('collapsed' if collapsed else ''))
        __M_writer(u'">\n    ')
        # SOURCE LINE 85
        __M_writer(mako_websafe(icon(app)))
        __M_writer(u'\n    <a class="edit-app-button ')
        # SOURCE LINE 86
        __M_writer(mako_websafe('' if collapsed else 'collapsed'))
        __M_writer(u'"\n       href="javascript:void(0)">\n       ')
        # SOURCE LINE 88
        __M_writer(mako_websafe(_("edit")))
        __M_writer(u'\n    </a>\n    <div class="app-details">\n      <h2>\n')
        # SOURCE LINE 92
        if app.about_url:
            # SOURCE LINE 93
            __M_writer(u'        <a href="')
            __M_writer(mako_websafe(app.about_url))
            __M_writer(u'">')
            __M_writer(mako_websafe(app.name))
            __M_writer(u'</a>\n')
            # SOURCE LINE 94
        else:
            # SOURCE LINE 95
            __M_writer(u'        ')
            __M_writer(mako_websafe(app.name))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 97
        __M_writer(u'      </h2>\n      <h3>\n')
        # SOURCE LINE 99
        if app.app_type == 'web':
            # SOURCE LINE 100
            __M_writer(u'          ')
            __M_writer(mako_websafe(_("web app")))
            __M_writer(u'\n')
            # SOURCE LINE 101
        elif app.app_type == 'installed':
            # SOURCE LINE 102
            __M_writer(u'          ')
            __M_writer(mako_websafe(_("installed app")))
            __M_writer(u'\n')
            # SOURCE LINE 103
        elif app.app_type == 'script':
            # SOURCE LINE 104
            __M_writer(u'          ')
            __M_writer(mako_websafe(_("personal use script")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 106
        __M_writer(u'      </h3>\n      <h3>')
        # SOURCE LINE 107
        __M_writer(mako_websafe(app._id))
        __M_writer(u'</h3>\n    </div>\n    <div class="app-description">')
        # SOURCE LINE 109
        __M_writer(mako_websafe(app.description))
        __M_writer(u'</div>\n')
        # SOURCE LINE 110
        if collapsed:
            # SOURCE LINE 111
            __M_writer(u'      ')
            __M_writer(mako_websafe(developers(app)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 113
        __M_writer(u'    <div class="edit-app ')
        __M_writer(mako_websafe('collapsed' if collapsed else ''))
        __M_writer(u'">\n      <a class="edit-app-icon-button" href="javascript:void(0)">\n        change icon\n      </a>\n      ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 118
                __M_writer(u'\n        <input type="hidden" name="client_id" value="')
                # SOURCE LINE 119
                __M_writer(mako_websafe(app._id))
                __M_writer(u'" />\n        ')
                # SOURCE LINE 120
                __M_writer(mako_websafe(error_field('TOO_LONG', 'file')))
                __M_writer(u'\n        ')
                # SOURCE LINE 121
                __M_writer(mako_websafe(error_field('BAD_IMAGE', 'file')))
                __M_writer(u'\n      ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 117
            __M_writer(mako_websafe(utils.ajax_upload(target=u'/api/setappicon',form_id=u'app-icon-upload-' + (app._id))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 122
        __M_writer(u'\n      <div class="edit-app-form">\n        <form method="post" action="/api/updateapp" class="pretty-form"\n         id="update-app-')
        # SOURCE LINE 125
        __M_writer(mako_websafe(app._id))
        __M_writer(u'"\n         onsubmit="')
        # SOURCE LINE 126
        __M_writer(mako_websafe("return post_form(this, 'updateapp', function(x) {return '%s'})" % _("updating...")))
        __M_writer(u'">\n          <input type="hidden" name="uh" value="')
        # SOURCE LINE 127
        __M_writer(mako_websafe(c.modhash))
        __M_writer(u'" />\n          <input type="hidden" name="client_id" value="')
        # SOURCE LINE 128
        __M_writer(mako_websafe(app._id))
        __M_writer(u'" />\n          <input type="hidden" name="app_type" value="')
        # SOURCE LINE 129
        __M_writer(mako_websafe(app.app_type))
        __M_writer(u'" />\n          <table class="preftable">\n            <tr>\n              <th>')
        # SOURCE LINE 132
        __M_writer(mako_websafe(_("secret")))
        __M_writer(u'</th>\n              <td class="prefright">')
        # SOURCE LINE 133
        __M_writer(mako_websafe(app.secret))
        __M_writer(u'</td>\n            </tr>\n            <tr>\n              <th>')
        # SOURCE LINE 136
        __M_writer(mako_websafe(_("name")))
        __M_writer(u'</th>\n              <td class="prefright">\n                <input class="text" name="name" value="')
        # SOURCE LINE 138
        __M_writer(mako_websafe(app.name))
        __M_writer(u'">\n                ')
        # SOURCE LINE 139
        __M_writer(mako_websafe(error_field("NO_TEXT", "name")))
        __M_writer(u'\n              </td>\n            </tr>\n            <tr>\n              <th>')
        # SOURCE LINE 143
        __M_writer(mako_websafe(_("description")))
        __M_writer(u'</th>\n              <td class="prefright">\n                <textarea name="description">')
        # SOURCE LINE 145
        __M_writer(mako_websafe(app.description))
        __M_writer(u'</textarea>\n              </td>\n            </tr>\n            <tr>\n              <th>')
        # SOURCE LINE 149
        __M_writer(mako_websafe(_("about url")))
        __M_writer(u'</th>\n              <td class="prefright">\n                <input class="text" name="about_url" value="')
        # SOURCE LINE 151
        __M_writer(mako_websafe(app.about_url))
        __M_writer(u'">\n                ')
        # SOURCE LINE 152
        __M_writer(mako_websafe(error_field("BAD_URL", "about_url")))
        __M_writer(u'\n              </td>\n            </tr>\n            <tr>\n              <th>')
        # SOURCE LINE 156
        __M_writer(mako_websafe(_("redirect uri")))
        __M_writer(u'</th>\n              <td class="prefright">\n                <input class="text" name="redirect_uri"\n                 value="')
        # SOURCE LINE 159
        __M_writer(mako_websafe(app.redirect_uri if app.redirect_uri else ''))
        __M_writer(u'">\n                ')
        # SOURCE LINE 160
        __M_writer(mako_websafe(error_field("NO_URL", "redirect_uri")))
        __M_writer(u'\n                ')
        # SOURCE LINE 161
        __M_writer(mako_websafe(error_field("BAD_URL", "redirect_uri")))
        __M_writer(u'\n                ')
        # SOURCE LINE 162
        __M_writer(mako_websafe(error_field("INVALID_SCHEME", "redirect_uri")))
        __M_writer(u'\n              </td>\n            </tr>\n          </table>\n          <button type="submit">')
        # SOURCE LINE 166
        __M_writer(mako_websafe(_('update app')))
        __M_writer(u'</button>\n          <span class="status"></span>\n        </form>\n      </div>\n      <div class="edit-app-form pretty-form">\n        <table class="preftable">\n          <tr>\n            <th>')
        # SOURCE LINE 173
        __M_writer(mako_websafe(_("developers")))
        __M_writer(u'</th>\n            <td class="prefright">\n              <ul>\n')
        # SOURCE LINE 176
        for dev in sorted(app._developers, key=lambda d: d.name):
            # SOURCE LINE 177
            __M_writer(u'                  ')
            __M_writer(mako_websafe(editable_developer(app, dev)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 179
        __M_writer(u'              </ul>\n              <br>\n              <form method="post" action="/api/adddeveloper"\n               class="pretty-form" id="app-developer-')
        # SOURCE LINE 182
        __M_writer(mako_websafe(app._id))
        __M_writer(u'"\n               onsubmit="')
        # SOURCE LINE 183
        __M_writer(mako_websafe("return post_form(this, 'adddeveloper', function(x) {return '%s'})" % _("adding...")))
        __M_writer(u'">\n                <input type="hidden" name="uh" value="')
        # SOURCE LINE 184
        __M_writer(mako_websafe(c.modhash))
        __M_writer(u'" />\n                <input type="hidden" name="client_id" value="')
        # SOURCE LINE 185
        __M_writer(mako_websafe(app._id))
        __M_writer(u'" />\n                ')
        # SOURCE LINE 186
        __M_writer(mako_websafe(_('add developer')))
        __M_writer(u': <input class="text" name="name">\n                <br>\n                ')
        # SOURCE LINE 188
        __M_writer(mako_websafe(error_field('TOO_MANY_DEVELOPERS', '')))
        __M_writer(u'\n                ')
        # SOURCE LINE 189
        __M_writer(mako_websafe(error_field('OAUTH2_INVALID_CLIENT', 'client_id')))
        __M_writer(u'\n                ')
        # SOURCE LINE 190
        __M_writer(mako_websafe(error_field('DEVELOPER_ALREADY_ADDED', 'name')))
        __M_writer(u'\n                ')
        # SOURCE LINE 191
        __M_writer(mako_websafe(error_field('USER_DOESNT_EXIST', 'name')))
        __M_writer(u'\n                ')
        # SOURCE LINE 192
        __M_writer(mako_websafe(error_field('NO_USER', 'name')))
        __M_writer(u'\n                <span class="status"></span>\n              </form>\n            </td>\n          </tr>\n        </table>\n      </div>\n      <div class="delete-app-button">\n        ')
        # SOURCE LINE 200
        __M_writer(mako_websafe(ynbutton(_("delete app"),
                   "deleted",
                   "deleteapp",
                   callback="r.apps.deleted",
                   hidden_data=dict(client_id=app._id))))
        # SOURCE LINE 204
        __M_writer(u'\n      </div>\n    </div>\n  </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_editable_developer(context,app,dev):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0158ed0')._populate(_import_ns, [u'error_field', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f1dc0158850')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ajax_ynbutton = _import_ns.get('ajax_ynbutton', context.get('ajax_ynbutton', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 71
        __M_writer(u'\n  <li id="app-dev-')
        # SOURCE LINE 72
        __M_writer(mako_websafe(app._id))
        __M_writer(u'-')
        __M_writer(mako_websafe(dev._id))
        __M_writer(u'">\n    ')
        # SOURCE LINE 73
        __M_writer(mako_websafe(dev.name))
        __M_writer(u'&#32;\n')
        # SOURCE LINE 74
        if c.user == dev:
            # SOURCE LINE 75
            __M_writer(u'      <span class="gray">')
            __M_writer(mako_websafe(_("(that's you!)")))
            __M_writer(u'</span>&#32;\n')
            pass
        # SOURCE LINE 77
        __M_writer(u'    ')
        __M_writer(mako_websafe(ajax_ynbutton(_("remove"), "removedeveloper",
                    hidden_data=dict(client_id=app._id, name=dev.name))))
        # SOURCE LINE 78
        __M_writer(u'\n  </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scope_details(context,scope,compact=False,expiration=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0158ed0')._populate(_import_ns, [u'error_field', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f1dc0158850')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        def sr_list(srs):
            return render_sr_list(context,srs)
        __M_writer = context.writer()
        # SOURCE LINE 219
        __M_writer(u'\n  <div class="app-permissions">\n    <ul>\n')
        # SOURCE LINE 222
        if scope.subreddit_only:
            # SOURCE LINE 223
            if compact:
                # SOURCE LINE 224
                __M_writer(u'\t  ')
                __M_writer(mako_websafe(_("Only in:")))
                __M_writer(u'&#32;\n\t  ')
                # SOURCE LINE 225
                __M_writer(mako_websafe(sr_list(scope.subreddits)))
                __M_writer(u'\n\t  <br>\n')
                # SOURCE LINE 227
            else:
                # SOURCE LINE 228
                __M_writer(u'          <li>\n            ')
                # SOURCE LINE 229
                __M_writer(mako_websafe(_("Only in the subreddits:")))
                __M_writer(u'&#32;\n            ')
                # SOURCE LINE 230
                __M_writer(mako_websafe(sr_list(scope.subreddits)))
                __M_writer(u'.\n          </li>\n')
                pass
            pass
        # SOURCE LINE 234
        for name, scope_info in scope.details():
            # SOURCE LINE 235
            __M_writer(u'        <li>\n')
            # SOURCE LINE 236
            if compact:
                # SOURCE LINE 237
                __M_writer(u'            ')
                __M_writer(mako_websafe(scope_info['name']))
                __M_writer(u'\n            <span class="app-scope">')
                # SOURCE LINE 238
                __M_writer(mako_websafe(scope_info['description']))
                __M_writer(u'</span>\n')
                # SOURCE LINE 239
            else:
                # SOURCE LINE 240
                __M_writer(u'            ')
                __M_writer(mako_websafe(scope_info['description']))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 242
            __M_writer(u'        </li>\n')
            pass
        # SOURCE LINE 244
        if not compact:
            # SOURCE LINE 245
            __M_writer(u'        <li>\n')
            # SOURCE LINE 246
            if expiration:
                # SOURCE LINE 247
                __M_writer(u'            ')
                __M_writer(mako_websafe(_("Expires in:")))
                __M_writer(u'&#32;\n            ')
                # SOURCE LINE 248
                __M_writer(mako_websafe(timeuntil(expiration)))
                __M_writer(u'\n')
                # SOURCE LINE 249
            else:
                # SOURCE LINE 250
                __M_writer(u'            ')
                __M_writer(mako_websafe(_("Maintain this access indefinitely"
                " (or until manually revoked).")))
                # SOURCE LINE 251
                __M_writer(u'\n')
                pass
            # SOURCE LINE 253
            __M_writer(u'        </li>\n')
            pass
        # SOURCE LINE 255
        __M_writer(u'    </ul>\n')
        # SOURCE LINE 256
        if compact and expiration:
            # SOURCE LINE 257
            __M_writer(u'      <div class="app-permissions-details">\n        ')
            # SOURCE LINE 258
            __M_writer(mako_websafe(_("Expires in:")))
            __M_writer(u'&#32;\n        ')
            # SOURCE LINE 259
            __M_writer(mako_websafe(timeuntil(expiration)))
            __M_writer(u'\n        <br>\n      </div>\n')
            pass
        # SOURCE LINE 263
        __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_app_type_selector(context,selection='web'):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0158ed0')._populate(_import_ns, [u'error_field', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f1dc0158850')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        utils = _mako_get_namespace(context, 'utils')
        __M_writer = context.writer()
        # SOURCE LINE 59
        __M_writer(u'\n')
        # SOURCE LINE 60
        __M_writer(mako_websafe(utils.radio_type('app_type', "web", _("web app"),
                   _("A web based application"),
                   selection == "web")))
        # SOURCE LINE 62
        __M_writer(u'\n')
        # SOURCE LINE 63
        __M_writer(mako_websafe(utils.radio_type('app_type', "installed", _("installed app"),
                   _("An app intended for installation, such as on a mobile phone"),
                   selection == "installed")))
        # SOURCE LINE 65
        __M_writer(u'\n')
        # SOURCE LINE 66
        __M_writer(mako_websafe(utils.radio_type('app_type', "script", _("script"),
                   _("Script for personal use. Will only have access to the developers accounts"),
                   selection == "script")))
        # SOURCE LINE 68
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_developers(context,app):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0158ed0')._populate(_import_ns, [u'error_field', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f1dc0158850')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n  ')
        # SOURCE LINE 41
        devs = app._developers 
        
        __M_writer(u'\n')
        # SOURCE LINE 42
        if devs:
            # SOURCE LINE 43
            __M_writer(u'    <div class="app-developers">\n      Developers:&#32;\n')
            # SOURCE LINE 45
            for i, dev in enumerate(sorted(devs, key=lambda d: d.name)):
                # SOURCE LINE 46
                if i:
                    # SOURCE LINE 47
                    if i == len(devs) - 1:
                        # SOURCE LINE 48
                        __M_writer(u'            &#32;and&#32;\n')
                        # SOURCE LINE 49
                    else:
                        # SOURCE LINE 50
                        __M_writer(u'            ,&#32;\n')
                        pass
                    pass
                # SOURCE LINE 53
                __M_writer(u'        ')
                __M_writer(mako_websafe(plain_link(dev.name, "/u/" + dev.name)))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 55
            __M_writer(u'    </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_icon(context,app):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0158ed0')._populate(_import_ns, [u'error_field', u'plain_link'])
        _mako_get_namespace(context, '__anon_0x7f1dc0158850')._populate(_import_ns, [u'ajax_ynbutton', u'ynbutton'])
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n  <div class="app-icon">\n    &nbsp;\n    <img src="')
        # SOURCE LINE 35
        __M_writer(mako_websafe(media_https_if_secure(app.icon_url) or static('defaultapp.png')))
        __M_writer(u'">\n    &nbsp;\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


