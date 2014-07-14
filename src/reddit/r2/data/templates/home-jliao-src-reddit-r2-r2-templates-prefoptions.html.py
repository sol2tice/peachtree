# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402178932.652156
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/prefoptions.html'
_template_uri=u'/prefoptions.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['num_input', 'link_options', 'checkbox', 'media_radio']


# SOURCE LINE 23

from r2.lib.template_helpers import add_sr
from r2.lib.utils import UrlParser
import random


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x7f8c8dba74d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8dba74d0')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8dba74d0')._populate(_import_ns, [u'language_tool', u'language_checkboxes', u'plain_link'])
        language_checkboxes = _import_ns.get('language_checkboxes', context.get('language_checkboxes', UNDEFINED))
        def checkbox(text,name,disabled=False,disabled_text='',prefix='pref_'):
            return render_checkbox(context.locals_(__M_locals),text,name,disabled,disabled_text,prefix)
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        language_tool = _import_ns.get('language_tool', context.get('language_tool', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def link_options():
            return render_link_options(context.locals_(__M_locals))
        def media_radio(val,label):
            return render_media_radio(context.locals_(__M_locals),val,label)
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        def num_input(s,name):
            return render_num_input(context.locals_(__M_locals),s,name)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 45
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n')
        # SOURCE LINE 63
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 71
        if c.user_is_loggedin and thing.done:
            # SOURCE LINE 72
            __M_writer(u'  <p class="error">')
            __M_writer(mako_websafe(_("your preferences have been updated")))
            __M_writer(u'</p>\n')
            pass
        # SOURCE LINE 74
        __M_writer(u'\n')
        # SOURCE LINE 75

        if c.user_is_loggedin:
            action = "/post/options" 
        else:
            action = "/post/unlogged_options" 
        if not c.frameless_cname:
            action = add_sr(action, sr_path = False, nocname=True)
         
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['action'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 82
        __M_writer(u'\n<form action="')
        # SOURCE LINE 83
        __M_writer(mako_websafe(action))
        __M_writer(u'" method="post" class="pretty-form short-text">\n  <input type="hidden" name="uh" value="')
        # SOURCE LINE 84
        __M_writer(mako_websafe(c.modhash))
        __M_writer(u'" />\n')
        # SOURCE LINE 85
        if c.cname:
            # SOURCE LINE 86
            __M_writer(u'    <input type="hidden" name="')
            __M_writer(mako_websafe(UrlParser.cname_get))
            __M_writer(u'" value="')
            __M_writer(mako_websafe(random.random()))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 88
        __M_writer(u'<table class="content preftable">\n  <tr>\n    <th>')
        # SOURCE LINE 90
        __M_writer(mako_websafe(_("interface language")))
        __M_writer(u'</th>\n    <td class="prefright">\n      ')
        # SOURCE LINE 92
        __M_writer(mako_websafe(language_tool(allow_blank = False, show_regions = True,
                      default_lang = c.user.pref_lang)))
        # SOURCE LINE 93
        __M_writer(u'\n      &#32;<span class="little gray hover">(*) ')
        # SOURCE LINE 94
        __M_writer(mako_websafe(_("incomplete")))
        __M_writer(u'\n      &#32;<a href="http://www.reddit.com/r/i18n/wiki/getting_started">')
        # SOURCE LINE 95
        __M_writer(mako_websafe(_("volunteer to translate")))
        __M_writer(u'</a></span>\n    </td>\n  </tr>\n  <tr>\n    <th>')
        # SOURCE LINE 99
        __M_writer(mako_websafe(_("content language")))
        __M_writer(u'</th>\n    <td class="prefright">\n      ')
        # SOURCE LINE 101
        __M_writer(mako_websafe(language_checkboxes(default = c.user.pref_content_langs)))
        __M_writer(u'\n    </td>\n  </tr>\n')
        # SOURCE LINE 104
        if c.user_is_loggedin:
            # SOURCE LINE 105
            __M_writer(u'  <tr>\n    <th>')
            # SOURCE LINE 106
            __M_writer(mako_websafe(_("clicking options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 108
            __M_writer(mako_websafe(checkbox(_("display links with a reddit toolbar"), "frame")))
            __M_writer(u'\n      <br/>\n      ')
            # SOURCE LINE 110
            __M_writer(mako_websafe(checkbox(_("open links in a new window"), "newwindow")))
            __M_writer(u'\n    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 114
            __M_writer(mako_websafe(_("media")))
            __M_writer(u'</th>\n    <td class="prefright">\n')
            # SOURCE LINE 116
            if not c.user.pref_compress:
                # SOURCE LINE 117
                __M_writer(u'      ')
                __M_writer(mako_websafe(media_radio("on", _("show thumbnails next to links"))))
                __M_writer(u'\n      ')
                # SOURCE LINE 118
                __M_writer(mako_websafe(media_radio("off", _("don't show thumbnails next to links"))))
                __M_writer(u'\n      ')
                # SOURCE LINE 119
                __M_writer(mako_websafe(media_radio("subreddit", _("show thumbnails based on that subreddit's media preferences"))))
                __M_writer(u'\n     ')
                # SOURCE LINE 120
                __M_writer(mako_websafe(checkbox(_("make safe(r) for work "), "no_profanity", disabled = not c.user.pref_over_18, disabled_text = "(requires over 18)")))
                __M_writer(u'\n      &#32;\n      <span class="little gray">\n        ')
                # SOURCE LINE 123
                __M_writer(mako_websafe(_("(Don't show thumbnails next to anything labeled NSFW)")))
                __M_writer(u'\n      </span>\n')
                # SOURCE LINE 125
            else:
                # SOURCE LINE 126
                __M_writer(u'      <p class="error">')
                __M_writer(mako_websafe(_("to enable thumbnails, disable compressed link display")))
                __M_writer(u'</p>\n      <input type="hidden" name="media" value="')
                # SOURCE LINE 127
                __M_writer(mako_websafe(c.user.pref_media))
                __M_writer(u'"/>\n')
                pass
            # SOURCE LINE 129
            __M_writer(u'     <br/>\n    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 133
            __M_writer(mako_websafe(_("link options")))
            __M_writer(u'</th>\n    <td class="prefright">\n')
            # SOURCE LINE 135
            if c.user_is_loggedin:
                # SOURCE LINE 136
                __M_writer(u'      <p>\n        ')
                # SOURCE LINE 137
                __M_writer(mako_websafe(checkbox(_("show the spotlight box on the front page"), "organic")))
                __M_writer(u'\n        &#32;\n        <span class="little gray">\n          ')
                # SOURCE LINE 140
                __M_writer(mako_websafe(_("(it shows new and promoted links, and gives you a say in what's spam and what isn't.)")))
                __M_writer(u'\n        </span>\n      </p>\n')
                # SOURCE LINE 143
            else:
                # SOURCE LINE 144
                __M_writer(u'      <p>')
                __M_writer(mako_websafe(checkbox(_("show me new links on the front page"), "organic")))
                __M_writer(u'</p>\n')
                pass
            # SOURCE LINE 146
            __M_writer(u'\n      <p>\n        ')
            # SOURCE LINE 148
            __M_writer(mako_websafe(checkbox(_("show trending subreddits on the front page"), "show_trending")))
            __M_writer(u'\n        &#32;\n        <span class="little gray">\n          ')
            # SOURCE LINE 151
            __M_writer(mako_websafe(_("(a list of popular and notable subreddits to check out)")))
            __M_writer(u'\n        </span>\n      </p>\n\n      <p>')
            # SOURCE LINE 155
            __M_writer(mako_websafe(checkbox(_("show me links I've recently viewed"), "clickgadget")))
            __M_writer(u'</p>\n      <p>')
            # SOURCE LINE 156
            __M_writer(mako_websafe(checkbox(_("compress the link display"), "compress")))
            __M_writer(u'</p>\n      <p>')
            # SOURCE LINE 157
            __M_writer(mako_websafe(checkbox(_("show additional details in the domain text when available"), "domain_details")))
            __M_writer(u'\n        &#32;\n        <span class="little gray">\n          ')
            # SOURCE LINE 160
            __M_writer(mako_websafe(_("(such as the source subreddit or the content author's url/name)")))
            __M_writer(u'\n        </span>\n      </p>\n      <p>')
            # SOURCE LINE 163
            __M_writer(mako_websafe(checkbox(_("don't show links after I've liked them"), "hide_ups")))
            __M_writer(u'\n         &#32;\n         <span class="little gray">')
            # SOURCE LINE 165
            __M_writer(mako_websafe(_("(except my own)")))
            __M_writer(u'</span>\n      </p>\n      <p>')
            # SOURCE LINE 167
            __M_writer(mako_websafe(checkbox(_("don't show links after I've disliked them"), "hide_downs")))
            __M_writer(u'\n         &#32;\n         <span class="little gray">')
            # SOURCE LINE 169
            __M_writer(mako_websafe(_("(except my own)")))
            __M_writer(u'</span>\n      </p>\n      ')
            # SOURCE LINE 171

         # stuff I can soon delete:
            _("display")
            _("links at once")
            _("don't show me sites with a score less than")
            _("don't show me comments with a score less than")
            _("comments by default")
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 178
            __M_writer(u'\n      <p>\n        ')
            # SOURCE LINE 180
            __M_writer(mako_websafe(unsafe(_("display %(num)s links at once") % \
        dict(num=capture(link_options)))))
            # SOURCE LINE 181
            __M_writer(u'\n      </p>\n      ')
            # SOURCE LINE 183

            input = capture(num_input, c.user.pref_min_link_score,
            'min_link_score')
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['input'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 186
            __M_writer(u'\n      <p>\n      ')
            # SOURCE LINE 188
            __M_writer(mako_websafe(unsafe(_("don't show me sites with a score less than %(num)s") % dict(num = input))))
            __M_writer(u'\n      &#32;<span class="little gray">')
            # SOURCE LINE 189
            __M_writer(mako_websafe(_("(blank for none)")))
            __M_writer(u'</span>\n      </p>\n    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 194
            __M_writer(mako_websafe(_("comment options")))
            __M_writer(u'</th>\n    <td class="prefright">\n    ')
            # SOURCE LINE 196
 
            input = capture(num_input, c.user.pref_min_comment_score,
                            'min_comment_score')
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['input'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 199
            __M_writer(u'\n    <p>\n      ')
            # SOURCE LINE 201
            __M_writer(mako_websafe(unsafe(_("don't show me comments with a score less than %(num)s") % dict(num = input))))
            __M_writer(u'\n      &#32;<span class="little gray">')
            # SOURCE LINE 202
            __M_writer(mako_websafe(_("(blank for none)")))
            __M_writer(u'</span>\n    </p>\n    <p>\n      ')
            # SOURCE LINE 205
 
            input = capture(num_input, c.user.pref_num_comments,
            'num_comments')
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['input'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 208
            __M_writer(u'\n    ')
            # SOURCE LINE 209
            s = c.user.pref_num_comments 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['s'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n    ')
            # SOURCE LINE 210
            __M_writer(mako_websafe(unsafe(_("display %(num)s comments by default") % \
    dict(num = input))))
            # SOURCE LINE 211
            __M_writer(u'\n    &#32;\n    <span class="little gray">\n      (1 - ')
            # SOURCE LINE 214
            __M_writer(mako_websafe(g.max_comments))
            __M_writer(u');\n      &#32;\n      ')
            # SOURCE LINE 216
            __M_writer(mako_websafe(_("the smaller the number, the faster your comments pages will load")))
            __M_writer(u'\n    </span>\n    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 221
            __M_writer(mako_websafe(_("messaging options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 223
            __M_writer(mako_websafe(checkbox(_("show message conversations in the inbox"), \
         "threaded_messages")))
            # SOURCE LINE 224
            __M_writer(u'\n      &#32;<span class="little gray">\n        ')
            # SOURCE LINE 226
            __M_writer(mako_websafe(_("(only applies when you go to the 'messages' panel)")))
            __M_writer(u'\n      </span>\n      <br/>\n')
            # SOURCE LINE 229
            if c.user.pref_threaded_messages:
                # SOURCE LINE 230
                __M_writer(u'        ')
                __M_writer(mako_websafe(checkbox(_("collapse messages after I've read them"), \
           "collapse_read_messages")))
                # SOURCE LINE 231
                __M_writer(u'\n        &#32;<span class="little gray">\n          ')
                # SOURCE LINE 233
                __M_writer(mako_websafe(_("(otherwise, you'll have to collapse them yourself)")))
                __M_writer(u'\n        </span>\n        <br/>\n')
                pass
            # SOURCE LINE 237
            __M_writer(u'      ')
            __M_writer(mako_websafe(checkbox(_("mark messages as read when I open my inbox"), \
         "mark_messages_read")))
            # SOURCE LINE 238
            __M_writer(u'\n      &#32;<span class="little gray">\n        ')
            # SOURCE LINE 240
            __M_writer(mako_websafe(_("(otherwise, they will be marked as read when you click them)")))
            __M_writer(u'\n      </span>\n    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 245
            __M_writer(mako_websafe(_("display options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 247
            __M_writer(mako_websafe(checkbox(_("allow subreddits to show me custom styles"), "show_stylesheets")))
            __M_writer(u'\n      <br/>\n      ')
            # SOURCE LINE 249
            __M_writer(mako_websafe(checkbox(_("show user flair"), "show_flair")))
            __M_writer(u'\n      <br/>\n      ')
            # SOURCE LINE 251
            __M_writer(mako_websafe(checkbox(_("show link flair"), "show_link_flair")))
            __M_writer(u'\n')
            # SOURCE LINE 252
            if c.user.pref_show_promote is not None:
                # SOURCE LINE 253
                __M_writer(u'        <br/>\n        ')
                # SOURCE LINE 254
                __M_writer(mako_websafe(checkbox(_("show self-serve advertising tab on front page"), 
          "show_promote")))
                # SOURCE LINE 255
                __M_writer(u'\n')
                pass
            # SOURCE LINE 257
            __M_writer(u'    </td>\n  </tr>\n  <tr>\n    <th>')
            # SOURCE LINE 260
            __M_writer(mako_websafe(_("content options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 262
            __M_writer(mako_websafe(checkbox(_("I am over eighteen years old and willing to view adult content"), "over_18")))
            __M_writer(u'\n      &#32;<span class="little gray">(')
            # SOURCE LINE 263
            __M_writer(mako_websafe(_("required to view some subreddits")))
            __M_writer(u')</span>\n      <br/>\n        ')
            # SOURCE LINE 265
            __M_writer(mako_websafe(checkbox(_("label posts that are not safe for work (NSFW)"), "label_nsfw", disabled = c.user.pref_no_profanity, disabled_text = "(requires not 'safer for work' mode)")))
            __M_writer(u'\n      <br/>\n        ')
            # SOURCE LINE 267
            __M_writer(mako_websafe(checkbox(_("enable private RSS feeds"), "private_feeds")))
            __M_writer(u' \n       &#32;<span class="little gray">\n        ')
            # SOURCE LINE 269
            __M_writer(mako_websafe(_("(available from the 'RSS feed' tab in prefs)")))
            __M_writer(u'</span>\n    </td>\n  <tr>\n    <th>')
            # SOURCE LINE 272
            __M_writer(mako_websafe(_("privacy options")))
            __M_writer(u'</th>\n    <td class="prefright">\n      ')
            # SOURCE LINE 274
            __M_writer(mako_websafe(checkbox(_("make my votes public"), "public_votes")))
            __M_writer(u'\n      &#32;\n      <span class="little gray">\n        ')
            # SOURCE LINE 277

            link1 = "&#32;<a href='/user/%s/liked'>/user/%s/liked</a>&#32;" % (c.user.name, c.user.name)
            link2 = "&#32;<a href='/user/%s/disliked'>/user/%s/disliked</a>" % (c.user.name, c.user.name)
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['link1','link2'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 280
            __M_writer(u'\n        (')
            # SOURCE LINE 281
            __M_writer(mako_websafe(unsafe(_("let everyone see %(link1)s and %(link2)s") % dict(link1=link1, link2=link2))))
            __M_writer(u')\n      </span>\n      <br/>\n      ')
            # SOURCE LINE 284
            __M_writer(mako_websafe(checkbox(_("allow my data to be used for research purposes"), "research")))
            __M_writer(u'\n      &#32;\n      <span class="little gray">\n       (\n         <a href="http://www.reddit.com/r/redditdev/comments/dtg4j/want_to_help_reddit_build_a_recommender_a_public/">\n           ')
            # SOURCE LINE 289
            __M_writer(mako_websafe(_("details")))
            __M_writer(u'\n         </a>\n       )\n      </span>\n      <br />\n      ')
            # SOURCE LINE 294
            __M_writer(mako_websafe(checkbox(_("don't allow search engines to index my user profile"), "hide_from_robots")))
            __M_writer(u'\n      &#32;\n      <span class="little gray">\n        (\n        <a href="http://www.reddit.com/wiki/noindex">')
            # SOURCE LINE 298
            __M_writer(mako_websafe(_("details")))
            __M_writer(u'</a>\n        )\n      </span>\n      <br />\n      ')
            # SOURCE LINE 302
            __M_writer(mako_websafe(checkbox(_("load core JS libraries from reddit servers"), "local_js")))
            __M_writer(u'\n      &#32;\n      <span class="little gray">\n       (\n         <a href="http://www.reddit.com/wiki/localjs">\n           ')
            # SOURCE LINE 307
            __M_writer(mako_websafe(_("details")))
            __M_writer(u'\n         </a>\n       )\n      </span>\n    </td>\n  </tr>\n')
            pass
        # SOURCE LINE 314
        if c.user.gold:
            # SOURCE LINE 315
            __M_writer(u'  <tr class="gold-accent">\n    <th>')
            # SOURCE LINE 316
            __M_writer(mako_websafe(_("gold options")))
            __M_writer(u'</th>\n    <td class="prefright">\n        ')
            # SOURCE LINE 318
            __M_writer(mako_websafe(checkbox(_("show the right sidebar ad box"), "show_adbox")))
            __M_writer(u'\n        &#32;<span class="little gray">(')
            # SOURCE LINE 319
            __M_writer(mako_websafe(_("the attractive 300x250 one that usually only has reddit t-shirts in it")))
            __M_writer(u')</span>\n        <br/>\n        ')
            # SOURCE LINE 321
            __M_writer(mako_websafe(checkbox(_("show sponsored links"), "show_sponsors")))
            __M_writer(u'\n        &#32;<span class="little gray">(')
            # SOURCE LINE 322
            __M_writer(mako_websafe(_("the blue advertisements that sometimes appear on the top of the page")))
            __M_writer(u')</span>\n        <br/>\n        ')
            # SOURCE LINE 324
            __M_writer(mako_websafe(checkbox(_("show sponsorships"), "show_sponsorships")))
            __M_writer(u'\n        &#32;<span class="little gray">(')
            # SOURCE LINE 325
            __M_writer(mako_websafe(_("the 300x100 'sponsored by...' images that sometimes appear in sidebars")))
            __M_writer(u')</span>\n        <br/>\n        ')
            # SOURCE LINE 327
            __M_writer(mako_websafe(checkbox(_("remember what links I've visited"), "store_visits")))
            __M_writer(u'\n        &#32;<span class="little gray">(')
            # SOURCE LINE 328
            __M_writer(mako_websafe(_("we'll remember and mark what links you've already read, even between computers")))
            __M_writer(u')</span>\n        <br/>\n        <br/>\n        ')
            # SOURCE LINE 331
            __M_writer(mako_websafe(checkbox(_("highlight new comments"), "highlight_new_comments")))
            __M_writer(u'\n        &#32;<span class="little gray">\n          (')
            # SOURCE LINE 333
            __M_writer(mako_websafe(_("we'll remember your visits for 48 hours and show you which comments you haven't seen yet")))
            __M_writer(u')\n        </span>\n        <br/>\n        ')
            # SOURCE LINE 336
            __M_writer(mako_websafe(checkbox(_("notify me when people say my username"), "monitor_mentions")))
            __M_writer(u'\n    </td>\n  </tr>\n')
            pass
        # SOURCE LINE 340
        __M_writer(u'  <tr>\n    <td>\n      <input type="submit" class="btn" value="')
        # SOURCE LINE 342
        __M_writer(mako_websafe(_('save options')))
        __M_writer(u'"/>\n    </td>\n  </tr>\n</table>\n\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_num_input(context,s,name):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8dba74d0')._populate(_import_ns, [u'language_tool', u'language_checkboxes', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 65
        __M_writer(u'\n  <input type="text" size="4" maxlength="4" \n         name="')
        # SOURCE LINE 67
        __M_writer(mako_websafe(name))
        __M_writer(u'" style="margin:  0 .5em 0 .5em"\n         value="')
        # SOURCE LINE 68
        __M_writer(mako_websafe(s if s is not None else ''))
        __M_writer(u'" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_link_options(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8dba74d0')._populate(_import_ns, [u'language_tool', u'language_checkboxes', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n  <select name="numsites" style="margin: 0 .5em 0 .5em">\n')
        # SOURCE LINE 49
        for x in [10, 25, 50, 100]:
            # SOURCE LINE 50
            __M_writer(u'        <option ')
            __M_writer(mako_websafe(x == c.user.pref_numsites and "selected='selected'" or ""))
            __M_writer(u'>\n          ')
            # SOURCE LINE 51
            __M_writer(mako_websafe(x))
            __M_writer(u'\n        </option>\n')
            pass
        # SOURCE LINE 54
        __M_writer(u'  </select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_checkbox(context,text,name,disabled=False,disabled_text='',prefix='pref_'):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8dba74d0')._populate(_import_ns, [u'language_tool', u'language_checkboxes', u'plain_link'])
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n    <input name="')
        # SOURCE LINE 31
        __M_writer(mako_websafe(name))
        __M_writer(u'" id="')
        __M_writer(mako_websafe(name))
        __M_writer(u'" type="checkbox"\n')
        # SOURCE LINE 32
        if getattr(c.user, prefix + name):
            # SOURCE LINE 33
            __M_writer(u'                 checked="checked"\n')
            pass
        # SOURCE LINE 35
        if disabled:
            # SOURCE LINE 36
            __M_writer(u'                 disabled="disabled"\n')
            pass
        # SOURCE LINE 38
        __M_writer(u'               />\n    <label class="')
        # SOURCE LINE 39
        __M_writer(mako_websafe('disabled' if disabled else ''))
        __M_writer(u'" for="')
        __M_writer(mako_websafe(name))
        __M_writer(u'">\n      ')
        # SOURCE LINE 40
        __M_writer(mako_websafe(text))
        __M_writer(u'\n    </label>\n')
        # SOURCE LINE 42
        if disabled and disabled_text:
            # SOURCE LINE 43
            __M_writer(u'      &#32;<span class="little gray">')
            __M_writer(mako_websafe(disabled_text))
            __M_writer(u'</span>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_media_radio(context,val,label):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8dba74d0')._populate(_import_ns, [u'language_tool', u'language_checkboxes', u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n  <input id="media_')
        # SOURCE LINE 58
        __M_writer(mako_websafe(val))
        __M_writer(u'" class="nomargin" \n         type="radio"  value="')
        # SOURCE LINE 59
        __M_writer(mako_websafe(val))
        __M_writer(u'" name="media"\n         ')
        # SOURCE LINE 60
        __M_writer(mako_websafe("checked='checked'" if c.user.pref_media == val else ''))
        __M_writer(u' /> \n  <label for="media_')
        # SOURCE LINE 61
        __M_writer(mako_websafe(val))
        __M_writer(u'">')
        __M_writer(mako_websafe(label))
        __M_writer(u'</label>\n  <br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


