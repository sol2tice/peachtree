# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919915.812847
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/link.html'
_template_uri='/link.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['domain', 'numcol', 'tagline', 'thumbnail', 'subreddit', 'buttons', 'thing_data_attributes', 'midcol', 'child', 'make_link', 'entry', 'bottom_buttons', 'thing_css_class', 'flair']


# SOURCE LINE 23

from r2.lib.template_helpers import get_domain
from r2.lib.template_helpers import media_https_if_secure
from r2.lib.pages.things import LinkButtons
from r2.lib.pages import WrappedUser
from r2.lib.strings import Score, strings


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 33
    ns = runtime.TemplateNamespace('__anon_0x7f1dbc37d690', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dbc37d690')] = ns

    # SOURCE LINE 32
    ns = runtime.TemplateNamespace('__anon_0x7f1dbc37d910', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dbc37d910')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'printable.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n \n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(u'\n \n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'\n\n')
        # SOURCE LINE 85
        __M_writer(u'\n\n')
        # SOURCE LINE 158
        __M_writer(u'\n\n')
        # SOURCE LINE 166
        __M_writer(u'\n\n')
        # SOURCE LINE 170
        __M_writer(u'\n\n')
        # SOURCE LINE 175
        __M_writer(u'\n\n')
        # SOURCE LINE 193
        __M_writer(u'\n\n\n')
        # SOURCE LINE 204
        __M_writer(u'\n\n')
        # SOURCE LINE 229
        __M_writer(u'\n\n')
        # SOURCE LINE 232
        __M_writer(u'\n\n')
        # SOURCE LINE 238
        __M_writer(u'\n\n')
        # SOURCE LINE 254
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_domain(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 196
        __M_writer(u'\n  <span class="domain">\n    (<a href="')
        # SOURCE LINE 198
        __M_writer(mako_websafe(thing.domain_path))
        __M_writer(u'">')
        __M_writer(mako_websafe(thing.domain_str))
        __M_writer(u'</a>)\n')
        # SOURCE LINE 199
        if c.user_is_admin:
            # SOURCE LINE 200
            __M_writer(u'      &#32;\n      <a class="adminbox" href="/admin/domain/')
            # SOURCE LINE 201
            __M_writer(mako_websafe(thing.domain))
            __M_writer(u'">d</a>\n')
            pass
        # SOURCE LINE 203
        __M_writer(u'  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_numcol(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n  ')
        # SOURCE LINE 36
        num = thing.num 
        
        __M_writer(u'\n  <span class="rank">\n')
        # SOURCE LINE 38
        if thing.num > 0:
            # SOURCE LINE 39
            __M_writer(u'      ')
            __M_writer(mako_websafe(thing.num))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tagline(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        edited = _import_ns.get('edited', context.get('edited', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 206
        __M_writer(u'\n  ')
        # SOURCE LINE 207

        taglinetext = thing.taglinetext.replace(" ", "&#32;")
          
        
        # SOURCE LINE 209
        __M_writer(u'\n  ')
        # SOURCE LINE 210
        __M_writer(mako_websafe(unsafe(taglinetext % dict(reddit=self.subreddit(),
                              score=capture(self.score, thing, thing.likes, tag='span'),
                              when=capture(thing_timestamp, thing, thing.timesince, live=True, include_tense=True),
                              author=WrappedUser(thing.author, thing.attribs, thing).render(),
                              lastedited=capture(edited, thing, thing.lastedited)
                              ))))
        # SOURCE LINE 215
        __M_writer(u'\n')
        # SOURCE LINE 216
        if c.permalink_page or c.profilepage:
            # SOURCE LINE 217
            __M_writer(u'    ')
            __M_writer(mako_websafe(self.gildings()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 219
        if thing.stickied:
            # SOURCE LINE 220
            __M_writer(u'    &#32;-&#32;<span class="stickied-tagline" title="selected by this subreddit\'s moderators">stickied post</span>\n')
            pass
        # SOURCE LINE 222
        __M_writer(u'\n')
        # SOURCE LINE 223
        if getattr(thing, 'savedcategory', None) is not None:
            # SOURCE LINE 224
            __M_writer(u'    ')
            __M_writer(mako_websafe(plain_link(_('category: %s') % thing.savedcategory,
                 '/user/%s/saved/%s' % (c.user.name, thing.savedcategory),
                 _class='save-category' + ('' if thing.savedcategory else ' hidden')
                )))
            # SOURCE LINE 227
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thumbnail(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        def make_link(name,css_class,tabindex=0):
            return render_make_link(context,name,css_class,tabindex)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 240
        __M_writer(u'\n')
        # SOURCE LINE 241
        if thing.thumbnail:
            # SOURCE LINE 242
            __M_writer(u'  ')
            def ccall(caller):
                def body():
                    hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
                    __M_writer = context.writer()
                    __M_writer(u'\n')
                    # SOURCE LINE 243
                    if not thing.thumbnail_sprited:
                        # SOURCE LINE 244
                        __M_writer(u'        ')

                        if hasattr(thing, 'thumbnail_size'):
                            size_str = "width='%d' height='%d'" % (thing.thumbnail_size[0], thing.thumbnail_size[1])
                        else:
                            size_str = ""
                                
                        
                        # SOURCE LINE 249
                        __M_writer(u'\n        <img src="')
                        # SOURCE LINE 250
                        __M_writer(mako_websafe(media_https_if_secure(thing.thumbnail)))
                        __M_writer(u'" ')
                        __M_writer(mako_websafe(size_str))
                        __M_writer(u' alt=""/>\n')
                        pass
                    # SOURCE LINE 252
                    __M_writer(u'  ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 242
                __M_writer(mako_websafe(make_link('thumbnail', 'thumbnail ' + (thing.thumbnail if thing.thumbnail_sprited else ''))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 252
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subreddit(context):
    context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 172
        __M_writer(u'\n  ')
        # SOURCE LINE 173
        __M_writer(mako_websafe(plain_link('/r/' + thing.subreddit.name, thing.subreddit_path, sr_path = False,
               cname = False, _class = "subreddit hover may-blank")))
        # SOURCE LINE 174
        __M_writer(u'\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_buttons(context,comments=True,delete=True,report=True,additional=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 234
        __M_writer(u'\n  ')
        # SOURCE LINE 235
        __M_writer(mako_websafe(LinkButtons(thing, comments = comments, delete = delete,
                report = report,
               )))
        # SOURCE LINE 237
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_data_attributes(context,what):
    context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 168
        __M_writer(u'\n')
        # SOURCE LINE 169
        __M_writer(mako_websafe(parent.thing_data_attributes(what)))
        __M_writer(u' data-ups="')
        __M_writer(mako_websafe(what.upvotes))
        __M_writer(u'" data-downs="')
        __M_writer(mako_websafe(what.downvotes))
        __M_writer(u'"\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_midcol(context,display=True,cls=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 177
        __M_writer(u'\n    <div class="midcol ')
        # SOURCE LINE 178
        __M_writer(mako_websafe(cls))
        __M_writer(u'"\n       ')
        # SOURCE LINE 179
        __M_writer(mako_websafe(not display and "style='display:none'" or ''))
        __M_writer(u'>\n    ')
        # SOURCE LINE 180
        __M_writer(mako_websafe(self.arrow(thing, 1, thing.likes)))
        __M_writer(u'\n')
        # SOURCE LINE 181
        if thing.pref_compress:
            # SOURCE LINE 182
            __M_writer(u'      <div class="score-placeholder"></div>\n')
            # SOURCE LINE 183
        elif thing.hide_score:
            # SOURCE LINE 184
            __M_writer(u'      <div class="score likes">&bull;</div> \n      <div class="score unvoted">&bull;</div> \n      <div class="score dislikes">&bull;</div> \n')
            # SOURCE LINE 187
        else:
            # SOURCE LINE 188
            __M_writer(u'      ')
            __M_writer(mako_websafe(self.score(thing, thing.likes, tag='div')))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 190
        __M_writer(u'    ')
        __M_writer(mako_websafe(self.arrow(thing, 0, thing.likes == False)))
        __M_writer(u'\n  </div>\n ')
        # SOURCE LINE 192
        __M_writer(mako_websafe(self.thumbnail()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_child(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        __M_writer = context.writer()
        # SOURCE LINE 231
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_make_link(context,name,css_class,tabindex=0):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        caller = _import_ns.get('caller', context.get('caller', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n  <a class="')
        # SOURCE LINE 45
        __M_writer(mako_websafe(css_class))
        __M_writer(u' may-blank ')
        __M_writer(mako_websafe( c.user_is_loggedin and 'loggedin' or ''))
        __M_writer(u'"\n     href="')
        # SOURCE LINE 46
        __M_writer(mako_websafe(thing.href_url))
        __M_writer(u'"\n')
        # SOURCE LINE 47
        if tabindex:
            # SOURCE LINE 48
            __M_writer(u'       tabindex="')
            __M_writer(mako_websafe(tabindex))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 50
        if thing.nofollow:
            # SOURCE LINE 51
            __M_writer(u'       rel="nofollow"\n')
            pass
        # SOURCE LINE 53
        if c.cname:
            # SOURCE LINE 54
            __M_writer(u'       target="_top"\n')
            pass
        # SOURCE LINE 56
        if thing.mousedown_url:
            # SOURCE LINE 57
            __M_writer(u'       onmousedown="save_href($(this));this.href=\'')
            __M_writer(mako_websafe(thing.mousedown_url))
            __M_writer(u'\'"\n')
            pass
        # SOURCE LINE 59
        if thing.link_child and getattr(thing, "media_override", False):
            # SOURCE LINE 60
            __M_writer(u'       onclick="return expando_child(this)"\n')
            pass
        # SOURCE LINE 62
        __M_writer(u'     >\n     ')
        # SOURCE LINE 63
        __M_writer(mako_websafe(caller.body()))
        __M_writer(u'\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_entry(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        def make_link(name,css_class,tabindex=0):
            return render_make_link(context,name,css_class,tabindex)
        def bottom_buttons():
            return render_bottom_buttons(context)
        def flair():
            return render_flair(context)
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\n  <p class="title">\n')
        # SOURCE LINE 89
        if c.site.link_flair_position == 'left':
            # SOURCE LINE 90
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(mako_websafe(flair()))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
            pass
        # SOURCE LINE 92
        __M_writer(u'    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n      ')
                # SOURCE LINE 93
                __M_writer(mako_websafe(thing.title))
                __M_writer(u'\n    ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 92
            __M_writer(mako_websafe(make_link('title', 'title', tabindex=1)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 94
        __M_writer(u'\n')
        # SOURCE LINE 95
        if c.site.link_flair_position == 'right':
            # SOURCE LINE 96
            __M_writer(u'      ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(mako_websafe(flair()))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
            pass
        # SOURCE LINE 98
        __M_writer(u'    ')
        __M_writer(mako_websafe(self.approval_checkmark()))
        __M_writer(u'\n    &#32;\n\n    ')
        # SOURCE LINE 101
        __M_writer(mako_websafe(self.domain()))
        __M_writer(u'\n\n')
        # SOURCE LINE 103
        if c.user_is_admin:
            # SOURCE LINE 104
            for link_note in thing.link_notes:
                # SOURCE LINE 105
                __M_writer(u'           &#32;<span class="link-note">[')
                __M_writer(mako_websafe(link_note))
                __M_writer(u']</span>\n')
                pass
            pass
        # SOURCE LINE 108
        __M_writer(u'  </p>\n\n')
        # SOURCE LINE 111
        __M_writer(u'  ')
        selftext_hide = thing.is_self and not thing.selftext 
        
        __M_writer(u'\n')
        # SOURCE LINE 112
        if thing.link_child and not thing.link_child.expand and not selftext_hide:
            # SOURCE LINE 113
            __M_writer(u'    <div class="expando-button collapsed\n                ')
            # SOURCE LINE 114
            __M_writer(mako_websafe(thing.link_child.css_style))
            __M_writer(u'"\n         onclick="expando_child(this)"></div>\n')
            pass
        # SOURCE LINE 117
        __M_writer(u'\n  <p class="tagline">\n    ')
        # SOURCE LINE 119
        __M_writer(mako_websafe(self.tagline()))
        __M_writer(u'\n  </p>\n\n  ')
        # SOURCE LINE 122
 
        child_content = ""
        if thing.link_child and thing.link_child.load:
          child_content = unsafe(thing.link_child.content())
        expand = thing.link_child and thing.link_child.expand
          
        
        # SOURCE LINE 127
        __M_writer(u'\n\n')
        # SOURCE LINE 130
        if not expand:
            # SOURCE LINE 131
            __M_writer(u'    ')
            __M_writer(mako_websafe(bottom_buttons()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 133
        __M_writer(u'\n')
        # SOURCE LINE 134
        if not getattr(thing, "votable", True):
            # SOURCE LINE 135
            __M_writer(u'  <div class="unvotable-message">')
            __M_writer(mako_websafe(strings.unvotable_message))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 137
        __M_writer(u'\n  <div class="expando" ')
        # SOURCE LINE 138
        __M_writer(mako_websafe("style='display: none'" if not expand else ""))
        __M_writer(u'>\n')
        # SOURCE LINE 139
        if expand:
            # SOURCE LINE 140
            __M_writer(u'      ')
            __M_writer(mako_websafe(child_content))
            __M_writer(u'\n')
            # SOURCE LINE 141
        else:
            # SOURCE LINE 142
            __M_writer(u'      <span class="error">loading...</span>\n')
            pass
        # SOURCE LINE 144
        __M_writer(u'  </div>\n\n')
        # SOURCE LINE 147
        if expand:
            # SOURCE LINE 148
            __M_writer(u'    ')
            __M_writer(mako_websafe(bottom_buttons()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 150
        __M_writer(u'\n')
        # SOURCE LINE 152
        if not expand and child_content:
            # SOURCE LINE 153
            __M_writer(u'    <script type="text/javascript">\n      var cache = expando_cache();\n      cache["')
            # SOURCE LINE 155
            __M_writer(mako_websafe(thing._fullname))
            __M_writer(u'_cache"] = "')
            __M_writer(mako_websafe(websafe(child_content)))
            __M_writer(u'";\n    </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottom_buttons(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 67
        __M_writer(u'\n  <ul class="flat-list buttons">\n')
        # SOURCE LINE 69
        if thing.nsfw:
            # SOURCE LINE 70
            __M_writer(u'     <li class="rounded nsfw-stamp stamp">\n       <acronym title="')
            # SOURCE LINE 71
            __M_writer(mako_websafe(_('Adult content: Not Safe For Work')))
            __M_writer(u'">\n         ')
            # SOURCE LINE 72
            __M_writer(mako_websafe(_("NSFW")))
            __M_writer(u'\n       </acronym>\n     </li>\n')
            pass
        # SOURCE LINE 76
        __M_writer(u'    ')
        __M_writer(mako_websafe(self.buttons()))
        __M_writer(u'\n    ')
        # SOURCE LINE 77
        __M_writer(mako_websafe(self.admintagline()))
        __M_writer(u'\n  </ul>\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_css_class(context,what):
    context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 160
        __M_writer(u'\n')
        # SOURCE LINE 161
        __M_writer(mako_websafe(parent.thing_css_class(what)))
        __M_writer(u' ')
        __M_writer(mako_websafe("over18" if thing.over_18 else ""))
        __M_writer(u' ')
        __M_writer(mako_websafe(thing.visited and 'visited' or ''))
        __M_writer(u'\n')
        # SOURCE LINE 162
        if c.user.pref_show_link_flair and (thing.flair_text or thing.flair_css_class):
            # SOURCE LINE 163
            __M_writer(u'  ')
            css = thing.flair_css_class or '' 
            
            __M_writer(u'\n  linkflair ')
            # SOURCE LINE 164
            __M_writer(mako_websafe(' '.join('linkflair-' + c for c in css.split())))
            __M_writer(u'\n')
            pass
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_flair(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dbc37d690')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x7f1dbc37d910')._populate(_import_ns, [u'plain_link', u'thing_timestamp', u'edited'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 81
        __M_writer(u'\n')
        # SOURCE LINE 82
        if c.user.pref_show_link_flair and thing.flair_text:
            # SOURCE LINE 83
            __M_writer(u'    <span class="linkflairlabel" title="')
            __M_writer(mako_websafe(thing.flair_text))
            __M_writer(u'">')
            __M_writer(mako_websafe(thing.flair_text))
            __M_writer(u'</span>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


