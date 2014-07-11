# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918615.771676
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/usertext.html'
_template_uri='/usertext.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['action_button', 'markhelp']


# SOURCE LINE 23

from r2.lib.filters import unsafe, safemarkdown, keep_space
from r2.lib.strings import strings
from r2.lib.utils import randstr


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7f1dd60a6490', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd60a6490')] = ns

    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7f1dd60a6910', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd60a6910')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60a6490')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dd60a6910')._populate(_import_ns, [u'error_field', u'md'])
        def action_button(name,btn_type,onclick,display):
            return render_action_button(context.locals_(__M_locals),name,btn_type,onclick,display)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        def markhelp():
            return render_markhelp(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 99
        __M_writer(u'\n\n')
        # SOURCE LINE 106
        __M_writer(u'\n\n')
        # SOURCE LINE 108
        if thing.have_form:
            # SOURCE LINE 109
            __M_writer(u'  <form action="#" class="')
            __M_writer(mako_websafe(thing.css_class))
            __M_writer(u'"\n')
            # SOURCE LINE 110
            if thing.post_form:
                # SOURCE LINE 111
                __M_writer(u'        onsubmit="return post_form(this, \'')
                __M_writer(mako_websafe(thing.post_form))
                __M_writer(u'\')"\n')
                pass
            # SOURCE LINE 113
            __M_writer(u'        ')
            __M_writer(mako_websafe("style='display:none'" if not thing.display else ""))
            __M_writer(u'\n        id="form-')
            # SOURCE LINE 114
            __M_writer(mako_websafe(thing.fullname + randstr(3)))
            __M_writer(u'">\n')
            # SOURCE LINE 115
        else:
            # SOURCE LINE 116
            __M_writer(u'  <div class="')
            __M_writer(mako_websafe(thing.css_class))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 118
        __M_writer(u'\n')
        # SOURCE LINE 120
        __M_writer(u'  <input type="hidden" name="thing_id" value="')
        __M_writer(mako_websafe(thing.fullname))
        __M_writer(u'"/>\n\n')
        # SOURCE LINE 122
        if not thing.creating:
            # SOURCE LINE 123
            __M_writer(u'    <div class="usertext-body may-blank-within">\n')
            # SOURCE LINE 124
            if not thing.expunged:
                # SOURCE LINE 125
                __M_writer(u'      ')
                __M_writer(mako_websafe(unsafe(safemarkdown(thing.text, nofollow = thing.nofollow,
                                        target = thing.target))))
                # SOURCE LINE 126
                __M_writer(u'\n')
                # SOURCE LINE 127
            else:
                # SOURCE LINE 128
                __M_writer(u'      <em>')
                __M_writer(mako_websafe(_("[removed]")))
                __M_writer(u'</em>&#32;\n')
                pass
            # SOURCE LINE 130
            __M_writer(u'    </div>\n')
            pass
        # SOURCE LINE 132
        __M_writer(u'\n')
        # SOURCE LINE 133
        if thing.editable or thing.creating:
            # SOURCE LINE 135
            __M_writer(u'    <div class="usertext-edit"\n         style="')
            # SOURCE LINE 136
            __M_writer(mako_websafe("" if thing.creating else 'display: none'))
            __M_writer(u'">\n')
            # SOURCE LINE 138
            __M_writer(u'      <div>\n        <textarea rows="1" cols="1"\n                  name="')
            # SOURCE LINE 140
            __M_writer(mako_websafe(thing.name))
            __M_writer(u'"\n                  class="')
            # SOURCE LINE 141
            __M_writer(mako_websafe(thing.textarea_class))
            __M_writer(u'"\n                  >')
            # SOURCE LINE 142
            __M_writer(mako_websafe(keep_space(thing.text)))
            __M_writer(u'</textarea>\n      </div>\n\n      <div class="bottom-area">\n        ')
            # SOURCE LINE 146
            __M_writer(mako_websafe(toggle_button("help-toggle", _("formatting help"), _("hide help"),
                        "helpon", "helpoff",
                         style = "" if thing.creating else "display: none")))
            # SOURCE LINE 148
            __M_writer(u'\n\n        <a href="/wiki/reddiquette" class="reddiquette" target="_blank" tabindex="100">')
            # SOURCE LINE 150
            __M_writer(mako_websafe(_('reddiquette')))
            __M_writer(u'</a>\n\n')
            # SOURCE LINE 152
            if thing.include_errors:
                # SOURCE LINE 153
                __M_writer(u'          ')
                __M_writer(mako_websafe(error_field("TOO_LONG", thing.name, "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 154
                __M_writer(mako_websafe(error_field("RATELIMIT", "ratelimit", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 155
                __M_writer(mako_websafe(error_field("NO_TEXT", thing.name, "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 156
                __M_writer(mako_websafe(error_field("TOO_OLD", "parent", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 157
                __M_writer(mako_websafe(error_field("DELETED_COMMENT", "parent", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 158
                __M_writer(mako_websafe(error_field("DELETED_LINK", "parent", "span")))
                __M_writer(u'\n          ')
                # SOURCE LINE 159
                __M_writer(mako_websafe(error_field("USER_BLOCKED", "parent", "span")))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 161
            __M_writer(u'        <div class="usertext-buttons">\n          ')
            # SOURCE LINE 162
            __M_writer(mako_websafe(action_button("save", "submit", "",
                          thing.creating and thing.have_form)))
            # SOURCE LINE 163
            __M_writer(u'\n          ')
            # SOURCE LINE 164
            __M_writer(mako_websafe(action_button("cancel", "button", "cancel_usertext(this)", False)))
            __M_writer(u'\n')
            # SOURCE LINE 165
            if thing.have_form:
                # SOURCE LINE 166
                __M_writer(u'            <span class="status"></span>\n')
                pass
            # SOURCE LINE 168
            __M_writer(u'        </div>\n      </div>\n\n      ')
            # SOURCE LINE 171
            __M_writer(mako_websafe(markhelp()))
            __M_writer(u'\n    </div>\n')
            pass
        # SOURCE LINE 174
        __M_writer(u'\n')
        # SOURCE LINE 175
        if thing.have_form:
            # SOURCE LINE 176
            __M_writer(u'  </form>\n')
            # SOURCE LINE 177
        else:
            # SOURCE LINE 178
            __M_writer(u'  </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_action_button(context,name,btn_type,onclick,display):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60a6490')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dd60a6910')._populate(_import_ns, [u'error_field', u'md'])
        __M_writer = context.writer()
        # SOURCE LINE 101
        __M_writer(u'\n  <button type="')
        # SOURCE LINE 102
        __M_writer(mako_websafe(btn_type))
        __M_writer(u'" onclick="')
        __M_writer(mako_websafe(onclick))
        __M_writer(u'" class="')
        __M_writer(mako_websafe(name))
        __M_writer(u'"\n          ')
        # SOURCE LINE 103
        __M_writer(mako_websafe("style='display:none'" if not display else ""))
        __M_writer(u'>\n    ')
        # SOURCE LINE 104
        __M_writer(mako_websafe(name))
        __M_writer(u'\n  </button>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_markhelp(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd60a6490')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dd60a6910')._populate(_import_ns, [u'error_field', u'md'])
        md = _import_ns.get('md', context.get('md', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n  <div class="markhelp" style="display:none">\n    <p>')
        # SOURCE LINE 34
        __M_writer(mako_websafe(md(strings.formatting_help_info)))
        __M_writer(u'</p>\n    <table class="md">\n      <tr style="background-color: #ffff99; text-align: center">\n        <td><em>')
        # SOURCE LINE 37
        __M_writer(mako_websafe(_( "you type:")))
        __M_writer(u'</em></td>\n        <td><em>')
        # SOURCE LINE 38
        __M_writer(mako_websafe(_( "you see:")))
        __M_writer(u'</em></td>\n      </tr>\n      <tr>\n        <td>*')
        # SOURCE LINE 41
        __M_writer(mako_websafe(_( "italics")))
        __M_writer(u'*</td>\n        <td><em>')
        # SOURCE LINE 42
        __M_writer(mako_websafe(_( "italics")))
        __M_writer(u'</em></td>\n      </tr>\n      <tr>\n        <td>**')
        # SOURCE LINE 45
        __M_writer(mako_websafe(_( "bold")))
        __M_writer(u'**</td>\n        <td><b>')
        # SOURCE LINE 46
        __M_writer(mako_websafe(_( "bold")))
        __M_writer(u'</b></td>\n      </tr>\n      <tr>\n        <td>[reddit!](http://reddit.com)</td>\n        <td><a href="http://reddit.com">reddit!</a></td>\n      </tr>\n      <tr>\n        <td>\n          * ')
        # SOURCE LINE 54
        __M_writer(mako_websafe(_( "item")))
        __M_writer(u' 1<br/>\n          * ')
        # SOURCE LINE 55
        __M_writer(mako_websafe(_( "item")))
        __M_writer(u' 2<br/>\n          * ')
        # SOURCE LINE 56
        __M_writer(mako_websafe(_( "item")))
        __M_writer(u' 3\n        </td>\n        <td>\n          <ul>\n            <li>')
        # SOURCE LINE 60
        __M_writer(mako_websafe(_( "item")))
        __M_writer(u' 1</li>\n            <li>')
        # SOURCE LINE 61
        __M_writer(mako_websafe(_( "item")))
        __M_writer(u' 2</li>\n            <li>')
        # SOURCE LINE 62
        __M_writer(mako_websafe(_( "item")))
        __M_writer(u' 3</li>\n          </ul>\n        </td>\n      </tr>\n      <tr>\n        <td>&gt; ')
        # SOURCE LINE 67
        __M_writer(mako_websafe(_( "quoted text")))
        __M_writer(u'</td>\n        <td><blockquote>')
        # SOURCE LINE 68
        __M_writer(mako_websafe(_( "quoted text" )))
        __M_writer(u'</blockquote></td>\n      </tr>\n      <tr>\n          <td>\n              Lines starting with four spaces <br/>\n              are treated like code:<br/><br/>\n              <span class="spaces">\n                  &nbsp;&nbsp;&nbsp;&nbsp;\n              </span>\n              if 1 * 2 &lt; 3:<br/>\n              <span class="spaces">\n                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n              </span>\n              print "hello, world!"<br/>\n          </td>\n          <td>Lines starting with four spaces <br/>\n              are treated like code:<br/>\n              <pre>if 1 * 2 &lt; 3:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print "hello,\n              world!"</pre>\n          </td>\n      </tr>\n      <tr>\n          <td>~~strikethrough~~</td>\n          <td><strike>strikethrough</strike></td>\n      </tr>\n      <tr>\n          <td>super^script</td>\n          <td>super<sup>script</sup></td>\n      </tr>\n    </table>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


