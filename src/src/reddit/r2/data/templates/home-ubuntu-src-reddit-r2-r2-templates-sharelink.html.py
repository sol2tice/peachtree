# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918569.563311
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/sharelink.html'
_template_uri='/sharelink.html'
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
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f1dd60c7190', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd60c7190')] = ns

    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7f1dd60c75d0', context._clean_inheritance_tokens(), templateuri=u'captcha.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd60c75d0')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60c7190')._populate(_import_ns, [u'error_field'])
        _mako_get_namespace(context, '__anon_0x7f1dd60c75d0')._populate(_import_ns, [u'captchagen'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        captchagen = _import_ns.get('captchagen', context.get('captchagen', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n<form onsubmit="return post_form(this, \'share\')" method="post"\n      id="sharelink_')
        # SOURCE LINE 27
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'"\n      class="pretty-form sharelink" action="/post/share"\n     ')
        # SOURCE LINE 29
        __M_writer(mako_websafe("" if thing.link_name else "style='display:none'"))
        __M_writer(u'>\n  <div class="clearleft"></div>\n    ')
        # SOURCE LINE 31
        __M_writer(mako_websafe(error_field("RATELIMIT", "ratelimit")))
        __M_writer(u'\n    <input type="hidden" name="parent" value="')
        # SOURCE LINE 32
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'"/>\n    <table class="sharetable preftable">\n      <tr class="">\n        <th>\n          <label for="share_to_')
        # SOURCE LINE 36
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'">\n            ')
        # SOURCE LINE 37
        __M_writer(mako_websafe(_("send this link to")))
        __M_writer(u'\n          </label>&nbsp;\n          <span class="little gray">\n            ')
        # SOURCE LINE 40
        __M_writer(mako_websafe(_("(list of emails or usernames)")))
        __M_writer(u'\n          </span>\n        </th>\n        <td>\n          <textarea id="share_to_')
        # SOURCE LINE 44
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'" \n                    name="share_to" rows="4" cols="40"\n                    placeholder="')
        # SOURCE LINE 46
        __M_writer(mako_websafe(unsafe('email@example.com, /u/%s, &hellip;' % g.system_user)))
        __M_writer(u'">\n            ')
        # SOURCE LINE 47
        __M_writer(mako_websafe(unsafe('&#x0D;&#x0A;'.join(websafe(e) for e in thing.emails))))
        __M_writer(u'\n          </textarea>\n        </td>\n        <td class="share-to-errors">\n          ')
        # SOURCE LINE 51
        __M_writer(mako_websafe(error_field("BAD_EMAILS", "share_to")))
        __M_writer(u'\n          ')
        # SOURCE LINE 52
        __M_writer(mako_websafe(error_field("TOO_MANY_EMAILS", "share_to")))
        __M_writer(u'\n          ')
        # SOURCE LINE 53
        __M_writer(mako_websafe(error_field("NO_EMAILS", "share_to")))
        __M_writer(u'\n        </td>\n      </tr>\n      <tr>\n        <th>\n          <label for="share_from_')
        # SOURCE LINE 58
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'">\n            ')
        # SOURCE LINE 59
        __M_writer(mako_websafe(_("your name")))
        __M_writer(u'\n          </label>&nbsp;\n          <span class="little gray">\n            ')
        # SOURCE LINE 62
        __M_writer(mako_websafe(_("(optional)")))
        __M_writer(u'\n          </span>\n        </th>\n        <td>\n          <input class="real-name" value="')
        # SOURCE LINE 66
        __M_writer(mako_websafe(thing.username))
        __M_writer(u'"\n                 type="text" id="share_from_')
        # SOURCE LINE 67
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'" \n                 name="share_from" />\n        </td>\n        <td class="share-from-errors">\n          ')
        # SOURCE LINE 71
        __M_writer(mako_websafe(error_field("TOO_LONG", "share_from" )))
        __M_writer(u'\n        </td>\n      </tr>\n      <tr>\n        <th>\n          <label for="replyto_')
        # SOURCE LINE 76
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'">\n            ')
        # SOURCE LINE 77
        __M_writer(mako_websafe(_("your email")))
        __M_writer(u'\n          </label>&nbsp;\n          <span class="little gray">\n            ')
        # SOURCE LINE 80
        __M_writer(mako_websafe(_("(optional)")))
        __M_writer(u'\n          </span>\n        </th>\n        <td>\n          <input name="replyto" type="text" size="30"\n                 id="replyto_')
        # SOURCE LINE 85
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'"/>\n        </td>\n        <td class="reply-to-errors">\n          ')
        # SOURCE LINE 88
        __M_writer(mako_websafe(error_field("BAD_EMAILS", "replyto")))
        __M_writer(u'\n          ')
        # SOURCE LINE 89
        __M_writer(mako_websafe(error_field("TOO_MANY_EMAILS", "replyto")))
        __M_writer(u'\n        </td>\n      </tr>\n      <tr>\n        <th>\n          <label for="message_')
        # SOURCE LINE 94
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'">\n            ')
        # SOURCE LINE 95
        __M_writer(mako_websafe(_("message {share form}")))
        __M_writer(u'\n          </label>&nbsp;\n          <span class="little gray">\n            ')
        # SOURCE LINE 98
        __M_writer(mako_websafe(_("(optional)")))
        __M_writer(u'\n          </span>\n        </th>\n        <td>\n          <textarea id="message_')
        # SOURCE LINE 102
        __M_writer(mako_websafe(thing.link_name))
        __M_writer(u'" \n                    name="message" rows="4" cols="40">\n          </textarea>\n        </td>\n        <td class="message-errors">\n          ')
        # SOURCE LINE 107
        __M_writer(mako_websafe(error_field("TOO_LONG", "message")))
        __M_writer(u'\n        </td>\n      </tr>\n')
        # SOURCE LINE 110
        if thing.captcha:
            # SOURCE LINE 111
            __M_writer(u'        ')
            __M_writer(mako_websafe(captchagen('', tabulate = False, size = 30)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 113
        __M_writer(u'      <tr>\n        <td>\n        </td>\n        <td>\n          <button type="submit" class="btn">\n            ')
        # SOURCE LINE 118
        __M_writer(mako_websafe(_("share")))
        __M_writer(u'\n          </button>\n          <button class="btn" \n                  onclick="return cancelShare(this);">\n            ')
        # SOURCE LINE 122
        __M_writer(mako_websafe(_("cancel")))
        __M_writer(u'\n          </button>\n          <span class="status error"></span>\n        </td>\n        <td>\n        </td>\n      </tr>\n    </table>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


