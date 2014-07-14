# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402127456.084387
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/createsubreddit.html'
_template_uri='/createsubreddit.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.filters import keep_space
from r2.lib.pages import UserText
from r2.lib.strings import strings


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 32
    ns = runtime.TemplateNamespace(u'utils', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'utils')] = ns

    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7fabf17bec90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fabf17bec90')] = ns

    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7fabf17bea10', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fabf17bea10')] = ns

    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7fabf17b61d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fabf17b61d0')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabf17bec90')._populate(_import_ns, [u'image_upload'])
        _mako_get_namespace(context, '__anon_0x7fabf17bea10')._populate(_import_ns, [u'toggle_button', u'simple_button'])
        _mako_get_namespace(context, '__anon_0x7fabf17b61d0')._populate(_import_ns, [u'error_field', u'language_tool', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        utils = _mako_get_namespace(context, 'utils')
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n \n<div class="create-reddit fancy-settings thing"\n')
        # SOURCE LINE 35
        if thing.site:
            # SOURCE LINE 36
            __M_writer(u'       id="')
            __M_writer(mako_websafe(thing.site._fullname))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 38
        __M_writer(u'     >\n\n<div class="pretty-form" id="sr-form">\n\n')
        # SOURCE LINE 42
        if not thing.site:
            # SOURCE LINE 43
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    # SOURCE LINE 44
                    __M_writer(u'\n     <input type="text" name="name" id="name" class="text"\n            value="')
                    # SOURCE LINE 46
                    __M_writer(mako_websafe(thing.name))
                    __M_writer(u'"/>\n')
                    # SOURCE LINE 47
                    if not thing.site:
                        # SOURCE LINE 48
                        __M_writer(u'        ')
                        __M_writer(mako_websafe(error_field("SUBREDDIT_EXISTS", "name")))
                        __M_writer(u'\n        ')
                        # SOURCE LINE 49
                        __M_writer(mako_websafe(error_field("BAD_SR_NAME", "name")))
                        __M_writer(u'\n')
                        pass
                    # SOURCE LINE 51
                    __M_writer(u'    ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 43
                __M_writer(mako_websafe(utils.line_field(description=(_("no spaces, e.g., slashdot")),title=(_('name')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 51
            __M_writer(u'\n')
            # SOURCE LINE 52
        else:
            # SOURCE LINE 53
            __M_writer(u'  <input type="hidden" name="sr" id="name" value="')
            __M_writer(mako_websafe(thing.site._fullname))
            __M_writer(u'"/>\n')
            pass
        # SOURCE LINE 55
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 57
                __M_writer(u'\n')
                # SOURCE LINE 58
                if thing.site:
                    # SOURCE LINE 59
                    __M_writer(u'      <input id="title" type="text" name="title" class="text"\n             value="')
                    # SOURCE LINE 60
                    __M_writer(mako_websafe(thing.site.title))
                    __M_writer(u'"/>\n')
                    # SOURCE LINE 61
                else:
                    # SOURCE LINE 62
                    __M_writer(u'      <input id="title" type="text" name="title" class="text" />\n')
                    pass
                # SOURCE LINE 64
                __M_writer(u'    ')
                __M_writer(mako_websafe(error_field("NO_TEXT", "title")))
                __M_writer(u'\n    ')
                # SOURCE LINE 65
                __M_writer(mako_websafe(error_field("TOO_LONG", "title")))
                __M_writer(u'\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 56
            __M_writer(mako_websafe(utils.line_field(description=(_("e.g., slashdot: news for nerds, stuff that matters")),title=(_('title')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 66
        __M_writer(u'\n\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 69
                __M_writer(u'\n')
                # SOURCE LINE 70
                if thing.site and thing.site.public_description:
                    # SOURCE LINE 71
                    __M_writer(u'     ')
                    __M_writer(mako_websafe(UserText(None, text=thing.site.public_description or "", editable=True, creating=True, name="public_description", have_form=False)))
                    __M_writer(u'\n')
                    # SOURCE LINE 72
                else:
                    # SOURCE LINE 73
                    __M_writer(u'     ')
                    __M_writer(mako_websafe(UserText(None, text="", creating=True, name="public_description", have_form=False)))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 75
                __M_writer(u'  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 68
            __M_writer(mako_websafe(utils.line_field(css_class=u'usertext',description=(_('publicly describe your subreddit for all to see. 500 characters max.')),title=(_('description')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 75
        __M_writer(u'\n\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 78
                __M_writer(u'\n')
                # SOURCE LINE 79
                if thing.site and thing.site.description:
                    # SOURCE LINE 80
                    __M_writer(u'     ')
                    __M_writer(mako_websafe(UserText(None, text=thing.site.description or "", editable=True, creating=True, name="description", have_form=False)))
                    __M_writer(u'\n')
                    # SOURCE LINE 81
                else:
                    # SOURCE LINE 82
                    __M_writer(u'     ')
                    __M_writer(mako_websafe(UserText(None, text="", creating=True, name="description", have_form=False)))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 84
                __M_writer(u'  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 77
            __M_writer(mako_websafe(utils.line_field(css_class=u'usertext',description=(_('shown in the sidebar of your subreddit. 5120 characters max.')),title=(_('sidebar')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 84
        __M_writer(u'\n\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 87
                __M_writer(u'\n')
                # SOURCE LINE 88
                if thing.site and thing.site.submit_text:
                    # SOURCE LINE 89
                    __M_writer(u'     ')
                    __M_writer(mako_websafe(UserText(None, text=thing.site.submit_text or "", editable=True, creating=True, name="submit_text", have_form=False)))
                    __M_writer(u'\n')
                    # SOURCE LINE 90
                else:
                    # SOURCE LINE 91
                    __M_writer(u'     ')
                    __M_writer(mako_websafe(UserText(None, text="", creating=True, name="submit_text", have_form=False)))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 93
                __M_writer(u'  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 86
            __M_writer(mako_websafe(utils.line_field(css_class=u'usertext',description=(_('text to show on submission page. 1024 characters max.')),title=(_('submission text')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 93
        __M_writer(u'\n\n  ')
        def ccall(caller):
            def body():
                language_tool = _import_ns.get('language_tool', context.get('language_tool', UNDEFINED))
                len = _import_ns.get('len', context.get('len', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 95
                __M_writer(u'\n    <div class="delete-field">\n      ')
                # SOURCE LINE 97

                default_lang = thing.site and thing.site.lang or c.lang or ''
                default_lang = default_lang.split('-')[0]
                default_lang = g.lang if len(default_lang) != 2 else default_lang
                       
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['default_lang'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 101
                __M_writer(u'\n      ')
                # SOURCE LINE 102
                __M_writer(mako_websafe(language_tool(all_langs = True, default_lang = default_lang)))
                __M_writer(u'\n    </div>\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 95
            __M_writer(mako_websafe(utils.line_field(title=(_('language')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 104
        __M_writer(u'\n\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 106
                __M_writer(u'\n    <div class="delete-field">\n      <table>\n      ')
                # SOURCE LINE 109
                __M_writer(mako_websafe(utils.radio_type('type', "public", _("public"),
                         _("anyone can view and submit"),
                         (not thing.site or thing.site.type=='public'))))
                # SOURCE LINE 111
                __M_writer(u'\n      ')
                # SOURCE LINE 112
                __M_writer(mako_websafe(utils.radio_type('type', "restricted", _("restricted"),
                         _("anyone can view, but only some are approved to submit links"),
                         (thing.site and thing.site.type=='restricted'))))
                # SOURCE LINE 114
                __M_writer(u'\n      ')
                # SOURCE LINE 115
                __M_writer(mako_websafe(utils.radio_type('type', "private", _("private"),
                         _("only approved members can view and submit"),
                         (thing.site and thing.site.type=='private'))))
                # SOURCE LINE 117
                __M_writer(u'\n\n      ')
                # SOURCE LINE 119
                is_archived = thing.site and thing.site.type == 'archived' 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_archived'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                # SOURCE LINE 120
                if c.user_is_admin or is_archived:
                    # SOURCE LINE 121
                    __M_writer(u'        ')
                    __M_writer(mako_websafe(utils.radio_type('type', "archived", _("archived"),
                           _("anyone can view, but submissions are no longer accepted"),
                           is_archived)))
                    # SOURCE LINE 123
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 125
                __M_writer(u'\n      ')
                # SOURCE LINE 126
                is_gold_restricted = thing.site and thing.site.type == 'gold_restricted' 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_gold_restricted'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                # SOURCE LINE 127
                if c.user_is_admin or is_gold_restricted:
                    # SOURCE LINE 128
                    __M_writer(u'        ')
                    __M_writer(mako_websafe(utils.radio_type('type', "gold_restricted", _("gold restricted"),
                           _("anyone can view, but only reddit gold members can submit or comment"),
                           is_gold_restricted)))
                    # SOURCE LINE 130
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 132
                __M_writer(u'      </table>\n      ')
                # SOURCE LINE 133
                __M_writer(mako_websafe(error_field("INVALID_OPTION", "type")))
                __M_writer(u'\n    </div>\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 106
            __M_writer(mako_websafe(utils.line_field(title=(_('type')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 135
        __M_writer(u'\n\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 137
                __M_writer(u'\n    <div class="delete-field">\n      <table>\n        ')
                # SOURCE LINE 140
                __M_writer(mako_websafe(utils.radio_type('link_type', "any", _("any"),
                           _("any link type is allowed"),
                           (not thing.site or thing.site.link_type=='any'))))
                # SOURCE LINE 142
                __M_writer(u'\n        ')
                # SOURCE LINE 143
                __M_writer(mako_websafe(utils.radio_type('link_type', "link", _("links only"),
                           _("only links to external sites are allowed"),
                           (thing.site and thing.site.link_type=='link'))))
                # SOURCE LINE 145
                __M_writer(u'\n        ')
                # SOURCE LINE 146
                __M_writer(mako_websafe(utils.radio_type('link_type', "self", _("text posts only"),
                           _("only text/self posts are allowed"),
                           (thing.site and thing.site.link_type=='self'))))
                # SOURCE LINE 148
                __M_writer(u'\n      </table>\n      ')
                # SOURCE LINE 150
                __M_writer(mako_websafe(error_field("INVALID_OPTION", "link_type")))
                __M_writer(u'\n    </div>\n    <div class="usertext-edit">\n      <div class="delete-field">\n        <label for="submit_link_label">')
                # SOURCE LINE 154
                __M_writer(mako_websafe(_('Custom label for submit link button (blank for default):')))
                __M_writer(u'</label>\n        <input id="submit_link_label" type="text" name="submit_link_label" maxlength="60" placeholder="')
                # SOURCE LINE 155
                __M_writer(mako_websafe(strings.submit_link_label))
                __M_writer(u'"\n')
                # SOURCE LINE 156
                if thing.site:
                    # SOURCE LINE 157
                    __M_writer(u'                value="')
                    __M_writer(mako_websafe(thing.site.submit_link_label))
                    __M_writer(u'"\n')
                    pass
                # SOURCE LINE 159
                __M_writer(u'        >\n      </div>\n      <div class="delete-field">\n        <label for="submit_text_label">')
                # SOURCE LINE 162
                __M_writer(mako_websafe(_('Custom label for submit text post button (blank for default):')))
                __M_writer(u'</label>\n        <input id="submit_text_label" type="text" name="submit_text_label" maxlength="60" placeholder="')
                # SOURCE LINE 163
                __M_writer(mako_websafe(strings.submit_text_label))
                __M_writer(u'"\n')
                # SOURCE LINE 164
                if thing.site:
                    # SOURCE LINE 165
                    __M_writer(u'                value="')
                    __M_writer(mako_websafe(thing.site.submit_text_label))
                    __M_writer(u'"\n')
                    pass
                # SOURCE LINE 167
                __M_writer(u'        >\n      </div>\n    </div>\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 137
            __M_writer(mako_websafe(utils.line_field(title=(_('content options')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 170
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 171
                __M_writer(u'\n    <div class="delete-field">\n      <table>\n        ')
                # SOURCE LINE 174
                __M_writer(mako_websafe(utils.radio_type('wikimode', "disabled", _("disabled"),
                           _("Wiki is disabled for all users except mods"),
                           (not thing.site or thing.site.wikimode == 'disabled'))))
                # SOURCE LINE 176
                __M_writer(u'\n        ')
                # SOURCE LINE 177
                __M_writer(mako_websafe(utils.radio_type('wikimode', "modonly", _("mod editing"),
                           _("Only mods, approved wiki contributors, or those on a page's edit list may edit"),
                           (thing.site and thing.site.wikimode == 'modonly'))))
                # SOURCE LINE 179
                __M_writer(u'\n        ')
                # SOURCE LINE 180
                __M_writer(mako_websafe(utils.radio_type('wikimode', "anyone", _("anyone"),
                           _("Anyone who can submit to the subreddit may edit"),
                           (thing.site and thing.site.wikimode == 'anyone'))))
                # SOURCE LINE 182
                __M_writer(u'\n      </table>\n      ')
                # SOURCE LINE 184
                __M_writer(mako_websafe(error_field("INVALID_OPTION", "wikimode")))
                __M_writer(u'\n    </div>\n    <div class="usertext-edit">\n    <div class="delete-field">\n    <label for="wiki_edit_karma">')
                # SOURCE LINE 188
                __M_writer(mako_websafe(_('Subreddit karma required to edit and create wiki pages:')))
                __M_writer(u'</label>\n')
                # SOURCE LINE 189
                if thing.site:
                    # SOURCE LINE 190
                    __M_writer(u'            <input id="wiki_edit_karma" type="text" name="wiki_edit_karma" \n                   value = "')
                    # SOURCE LINE 191
                    __M_writer(mako_websafe(thing.site.wiki_edit_karma))
                    __M_writer(u'"/>\n')
                    # SOURCE LINE 192
                else:
                    # SOURCE LINE 193
                    __M_writer(u'            <input id="wiki_edit_karma" type="text" name="wiki_edit_karma" value="100" />\n')
                    pass
                # SOURCE LINE 195
                __M_writer(u'        ')
                __M_writer(mako_websafe(error_field("BAD_NUMBER", "wiki_edit_karma")))
                __M_writer(u'\n    </div>\n    <div class="delete-field">\n    <label for="wiki_edit_age">')
                # SOURCE LINE 198
                __M_writer(mako_websafe(_('Account age (days) required to edit and create wiki pages:')))
                __M_writer(u'</label>\n')
                # SOURCE LINE 199
                if thing.site:
                    # SOURCE LINE 200
                    __M_writer(u'            <input id="wiki_edit_age" type="text" name="wiki_edit_age" \n                   value = "')
                    # SOURCE LINE 201
                    __M_writer(mako_websafe(thing.site.wiki_edit_age))
                    __M_writer(u'"/>\n')
                    # SOURCE LINE 202
                else:
                    # SOURCE LINE 203
                    __M_writer(u'            <input id="wiki_edit_age" type="text" name="wiki_edit_age" value="0" />\n')
                    pass
                # SOURCE LINE 205
                __M_writer(u'        ')
                __M_writer(mako_websafe(error_field("BAD_NUMBER", "wiki_edit_age")))
                __M_writer(u'\n    </div>\n    </div>\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 171
            __M_writer(mako_websafe(utils.line_field(title=(_('wiki')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 208
        __M_writer(u'\n  \n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 210
                __M_writer(u'\n  \t<div class="delete-field">\n        <p class="little gray">')
                # SOURCE LINE 212
                __M_writer(mako_websafe(_("high is the standard filter, low disables most filtering, all will filter every post initially and they will need to be approved manually to be visible.")))
                __M_writer(u'</p>\n  \t\t<table>\n  \t\t\t<tr>\n  \t\t\t\t<td>')
                # SOURCE LINE 215
                __M_writer(mako_websafe(_("links")))
                __M_writer(u':</td>\n  \t\t\t\t<td>\n  \t\t\t\t\t')
                # SOURCE LINE 217
                __M_writer(mako_websafe(utils.inline_radio_type('spam_links', 'low', _("low"),
  						checked=thing.site and thing.site.spam_links == 'low')))
                # SOURCE LINE 218
                __M_writer(u'\n  \t\t\t\t\t')
                # SOURCE LINE 219
                __M_writer(mako_websafe(utils.inline_radio_type('spam_links', 'high', _("high"),
  						checked=not thing.site or thing.site.spam_links == 'high')))
                # SOURCE LINE 220
                __M_writer(u'\n  \t\t\t\t\t')
                # SOURCE LINE 221
                __M_writer(mako_websafe(utils.inline_radio_type('spam_links', 'all', _("all"),
  						checked=thing.site and thing.site.spam_links == 'all')))
                # SOURCE LINE 222
                __M_writer(u'\n\t  \t\t\t</td>\n\t  \t\t</tr>\n\t  \t\t<tr>\n\t  \t\t\t<td>')
                # SOURCE LINE 226
                __M_writer(mako_websafe(_("self posts")))
                __M_writer(u':</td>\n\t  \t\t\t<td>\n\t  \t\t\t\t')
                # SOURCE LINE 228
                __M_writer(mako_websafe(utils.inline_radio_type('spam_selfposts', 'low', _("low"),
  						checked=thing.site and thing.site.spam_selfposts == 'low')))
                # SOURCE LINE 229
                __M_writer(u'\n  \t\t\t\t\t')
                # SOURCE LINE 230
                __M_writer(mako_websafe(utils.inline_radio_type('spam_selfposts', 'high', _("high"),
  						checked=not thing.site or thing.site.spam_selfposts == 'high')))
                # SOURCE LINE 231
                __M_writer(u'\n  \t\t\t\t\t')
                # SOURCE LINE 232
                __M_writer(mako_websafe(utils.inline_radio_type('spam_selfposts', 'all', _("all"),
  						checked=thing.site and thing.site.spam_selfposts == 'all')))
                # SOURCE LINE 233
                __M_writer(u'\n\t  \t\t\t</td>\n\t  \t\t</tr>\n\t  \t\t<tr>\n\t  \t\t\t<td>')
                # SOURCE LINE 237
                __M_writer(mako_websafe(_("comments")))
                __M_writer(u':</td>\n\t  \t\t\t<td>\n\t  \t\t\t\t')
                # SOURCE LINE 239
                __M_writer(mako_websafe(utils.inline_radio_type('spam_comments', 'low', _("low"),
  						checked=not thing.site or thing.site.spam_comments == 'low')))
                # SOURCE LINE 240
                __M_writer(u'\n  \t\t\t\t\t')
                # SOURCE LINE 241
                __M_writer(mako_websafe(utils.inline_radio_type('spam_comments', 'high', _("high"),
  						checked=thing.site and thing.site.spam_comments == 'high')))
                # SOURCE LINE 242
                __M_writer(u'\n  \t\t\t\t\t')
                # SOURCE LINE 243
                __M_writer(mako_websafe(utils.inline_radio_type('spam_comments', 'all', _("all"),
  						checked=thing.site and thing.site.spam_comments == 'all')))
                # SOURCE LINE 244
                __M_writer(u'\n\t  \t\t\t</td>\n\t  \t\t</tr>\n\t\t</table>\n  \t</div>\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 210
            __M_writer(mako_websafe(utils.line_field(title=(_('spam filter strength')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 249
        __M_writer(u'\n  \n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 251
                __M_writer(u'\n    <div class="delete-field">\n      <ul>\n        <li>\n          <input class="nomargin" type="checkbox"\n                 name="over_18" id="over_18"\n')
                # SOURCE LINE 257
                if thing.site and thing.site.over_18:
                    # SOURCE LINE 258
                    __M_writer(u'                   checked="checked"\n')
                    pass
                # SOURCE LINE 260
                __M_writer(u'          >\n          <label for="over_18">\n            ')
                # SOURCE LINE 262
                __M_writer(mako_websafe(_("viewers must be over eighteen years old")))
                __M_writer(u'\n          </label>\n        </li>\n        <li>\n          <input class="nomargin" type="checkbox"\n                 name="allow_top" id="allow_top"\n')
                # SOURCE LINE 268
                if not thing.site or thing.site.allow_top:
                    # SOURCE LINE 269
                    __M_writer(u'                   checked="checked"\n')
                    pass
                # SOURCE LINE 271
                __M_writer(u'          >\n          <label for="allow_top">\n            ')
                # SOURCE LINE 273
                __M_writer(mako_websafe(_("allow this subreddit to be included in the default and trending lists")))
                __M_writer(u'\n          </label>\n        </li>\n        <li>\n          <input class="nomargin" type="checkbox"\n                 name="show_media" id="show_media"\n')
                # SOURCE LINE 279
                if thing.site and thing.site.show_media:
                    # SOURCE LINE 280
                    __M_writer(u'                   checked="checked"\n')
                    pass
                # SOURCE LINE 282
                __M_writer(u'          >\n          <label for="show_media">\n            ')
                # SOURCE LINE 284
                __M_writer(mako_websafe(_("show thumbnail images of content")))
                __M_writer(u'\n          </label>\n        </li>\n        <li>\n          <input class="nomargin" type="checkbox"\n                 name="exclude_banned_modqueue" id="exclude_banned_modqueue"\n')
                # SOURCE LINE 290
                if thing.site and thing.site.exclude_banned_modqueue:
                    # SOURCE LINE 291
                    __M_writer(u'                   checked="checked"\n')
                    pass
                # SOURCE LINE 293
                __M_writer(u'          >\n          <label for="exclude_banned_modqueue">\n            ')
                # SOURCE LINE 295
                __M_writer(mako_websafe(_("exclude posts by site-wide banned users from modqueue/unmoderated")))
                __M_writer(u'\n          </label>\n        </li>\n        <li>\n          <input class="nomargin" type="checkbox"\n                 name="public_traffic" id="public_traffic"\n                 ')
                # SOURCE LINE 301
                __M_writer(mako_websafe(thing.site and thing.site.public_traffic and "checked='checked'" or ""))
                __M_writer(u'>\n          <label for="public_traffic">\n            ')
                # SOURCE LINE 303
                __M_writer(mako_websafe(_("make the traffic stats page available to everyone")))
                __M_writer(u'\n          </label>\n        </li>\n      </ul>\n    </div>\n    <div class="usertext-edit">\n      <div class="delete-field">\n        <label for="comment_score_hide_mins">')
                # SOURCE LINE 310
                __M_writer(mako_websafe(_('Minutes to hide comment scores:')))
                __M_writer(u'</label>\n')
                # SOURCE LINE 311
                if thing.site:
                    # SOURCE LINE 312
                    __M_writer(u'                <input id="comment_score_hide_mins" type="text" name="comment_score_hide_mins" placeholder="0" \n                       value = "')
                    # SOURCE LINE 313
                    __M_writer(mako_websafe(thing.site.comment_score_hide_mins))
                    __M_writer(u'" />\n')
                    # SOURCE LINE 314
                else:
                    # SOURCE LINE 315
                    __M_writer(u'                <input id="comment_score_hide_mins" type="text" name="comment_score_hide_mins" value="0" placeholder="0" />\n')
                    pass
                # SOURCE LINE 317
                __M_writer(u'            ')
                __M_writer(mako_websafe(error_field("BAD_NUMBER", "comment_score_hide_mins")))
                __M_writer(u'\n      </div>\n    </div>\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 251
            __M_writer(mako_websafe(utils.line_field(title=(_('other options')))))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 320
        __M_writer(u'\n\n')
        # SOURCE LINE 322
        if thing.site and thing.site.domain != thing.site._defaults['domain']:
            # SOURCE LINE 323
            __M_writer(u'  ')
            def ccall(caller):
                def body():
                    getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
                    toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
                    __M_writer = context.writer()
                    __M_writer(u'\n    <div class="delete-field">\n')
                    # SOURCE LINE 325
                    if thing.site and c.site.domain:
                        # SOURCE LINE 326
                        __M_writer(u'          <input class="nomargin" type="checkbox" \n                 name="css_on_cname" id="css_on_cname"\n')
                        # SOURCE LINE 328
                        if thing.site.css_on_cname:
                            # SOURCE LINE 329
                            __M_writer(u'                   checked="checked"\n')
                            pass
                        # SOURCE LINE 331
                        __M_writer(u'          >\n          <label for="css_on_cname">\n            ')
                        # SOURCE LINE 333
                        __M_writer(mako_websafe(_("make custom CSS styles apply only when accessed from the cname.")))
                        __M_writer(u'\n          </label>\n          <br/>\n          <input class="nomargin" type="checkbox"\n                 name="show_cname_sidebar" id="show_cname_sidebar"\n')
                        # SOURCE LINE 338
                        if thing.site.show_cname_sidebar:
                            # SOURCE LINE 339
                            __M_writer(u'                   checked="checked"\n')
                            pass
                        # SOURCE LINE 341
                        __M_writer(u'          >\n          <label for="show_cname_sidebar">\n            ')
                        # SOURCE LINE 343
                        __M_writer(mako_websafe(_("show sidebar when accessed from the cname.")))
                        __M_writer(u'\n          </label>\n')
                        pass
                    # SOURCE LINE 346
                    __M_writer(u'    </div>\n    <div class="usertext-edit">\n')
                    # SOURCE LINE 348
                    if thing.site:
                        # SOURCE LINE 349
                        __M_writer(u'        <input id="domain" type="text" name="domain" class="text"\n               value="')
                        # SOURCE LINE 350
                        __M_writer(mako_websafe(getattr(thing.site, 'domain', None) or ""))
                        __M_writer(u'"/>\n')
                        # SOURCE LINE 351
                    else:
                        # SOURCE LINE 352
                        __M_writer(u'        <input id="domain" type="text" name="domain" class="text" />\n')
                        pass
                    # SOURCE LINE 354
                    __M_writer(u'      <div class="bottom-area">\n        ')
                    # SOURCE LINE 355
                    __M_writer(mako_websafe(toggle_button("help-toggle", _("what's this?"), _("hide help"),
            "helpon", "helpoff")))
                    # SOURCE LINE 356
                    __M_writer(u'\n      </div>\n      <div class="infobar markhelp md" style="display: none">\n        ')
                    # SOURCE LINE 359
                    __M_writer(mako_websafe(_("Own a domain?  Enter it here and then go to your DNS provider and add a CNAME record aliasing your domain to rhs.reddit.com. You will be able to access your reddit through your domain.")))
                    __M_writer(u'\n      </div>\n    </div>\n  ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 323
                __M_writer(mako_websafe(utils.line_field(css_class=u'usertext',title=(_('domain')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 362
            __M_writer(u'\n')
            pass
        # SOURCE LINE 364
        __M_writer(u'\n')
        # SOURCE LINE 365
        if thing.site:
            # SOURCE LINE 366
            __M_writer(u'  <input type="hidden" name="sr" value="')
            __M_writer(mako_websafe(thing.site._fullname))
            __M_writer(u'"/> \n    ')
            def ccall(caller):
                def body():
                    plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
                    __M_writer = context.writer()
                    # SOURCE LINE 367
                    __M_writer(u'\n      <ul class="upload">\n        <li>\n        ')
                    # SOURCE LINE 370
                    __M_writer(mako_websafe(plain_link(_("edit the stylesheet"),
                      "/about/stylesheet",
                      _sr_path = True)))
                    # SOURCE LINE 372
                    __M_writer(u'\n        &#32;\n        <span class="gray">(')
                    # SOURCE LINE 374
                    __M_writer(mako_websafe(_("leaves this page")))
                    __M_writer(u')</span>\n        </li>\n        <li>\n          <label for="header-title">header mouseover text:</label>\n          <input type="text" name="header-title" id="header-title"\n                 value="')
                    # SOURCE LINE 379
                    __M_writer(mako_websafe(thing.site.header_title))
                    __M_writer(u'"\n                 />\n        </li>\n        <li>\n          ')
                    def ccall(caller):
                        def body():
                            __M_writer = context.writer()
                            # SOURCE LINE 386
                            __M_writer(u'\n            <br/>\n            <button id="delete-img" class="delete-img"\n')
                            # SOURCE LINE 389
                            if not thing.site.header:
                                # SOURCE LINE 390
                                __M_writer(u'                       style="display: none;"\n')
                                pass
                            # SOURCE LINE 392
                            __M_writer(u'                    onclick="return post_form(this.form, \'delete_sr_header\');">\n              ')
                            # SOURCE LINE 393
                            __M_writer(mako_websafe(_('restore default header')))
                            __M_writer(u'\n            </button>\n            <div class="clearleft"></div>\n            <input type="hidden" name="uh" value="')
                            # SOURCE LINE 396
                            __M_writer(mako_websafe(c.modhash))
                            __M_writer(u'" />\n            <input type="hidden" name="r"  value="')
                            # SOURCE LINE 397
                            __M_writer(mako_websafe(c.site.name))
                            __M_writer(u'" />\n            <input type="hidden" name="header" value="1" />\n  \n            <script type="text/javascript">\n              function on_image_success(img) {\n                 $("#header-img").log().attr("src", img.attr("src"));\n              }\n            </script>\n          ')
                            return ''
                        return [body]
                    __M_caller = context.caller_stack._get_caller()
                    context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                    try:
                        # SOURCE LINE 383
                        __M_writer(mako_websafe(utils.image_upload(current_image=(thing.site.header),post_target=u'/api/upload_sr_img',ask_type=(True),label=(_('upload header image')))))
                    finally:
                        context.caller_stack.nextcaller = None
                    # SOURCE LINE 405
                    __M_writer(u'\n        </li>\n      </ul>\n    ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 367
                __M_writer(mako_websafe(utils.line_field(title=(_('look and feel')))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 408
            __M_writer(u'\n')
            pass
        # SOURCE LINE 410
        __M_writer(u'\n\n  <div class="save-button">\n  ')
        # SOURCE LINE 413

        if thing.site:
            name = "edit"
            text = _("save options")
        else:
            name = "create"
            text = _("create")
          
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['text','name'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 420
        __M_writer(u'\n  <button name="')
        # SOURCE LINE 421
        __M_writer(mako_websafe(name))
        __M_writer(u'" class="btn" type="button"\n          onclick="return post_pseudo_form(\'#sr-form\', \'site_admin\')">\n    ')
        # SOURCE LINE 423
        __M_writer(mako_websafe(text))
        __M_writer(u'\n  </button>\n  &#32;\n  <span class="status error"></span>\n  ')
        # SOURCE LINE 427
        __M_writer(mako_websafe(error_field("RATELIMIT", "ratelimit")))
        __M_writer(u'\n  </div>\n</div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


