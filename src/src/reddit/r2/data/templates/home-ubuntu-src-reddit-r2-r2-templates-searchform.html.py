# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918235.32854
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/searchform.html'
_template_uri='/searchform.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['search_faq']


# SOURCE LINE 23

from r2.models.subreddit import DefaultSR
from r2.lib.template_helpers import add_sr, static


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        thing = context.get('thing', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        def search_faq():
            return render_search_faq(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 54
        __M_writer(u'\n\n<form action="')
        # SOURCE LINE 56
        __M_writer(mako_websafe(add_sr('/search')))
        __M_writer(u'" id="search" role="search">\n  <input type="text" \n')
        # SOURCE LINE 58
        if thing.prev_search:
            # SOURCE LINE 59
            __M_writer(u'           value="')
            __M_writer(mako_websafe(thing.prev_search))
            __M_writer(u'" style="color:black"\n')
            pass
        # SOURCE LINE 61
        __M_writer(u'         name="q" placeholder="')
        __M_writer(mako_websafe(_('search reddit')))
        __M_writer(u'" />\n')
        # SOURCE LINE 62
        if thing.subreddit_search:
            # SOURCE LINE 63
            __M_writer(u'    \n')
            # SOURCE LINE 64
        elif thing.simple:
            # SOURCE LINE 65
            __M_writer(u'  <div id="searchexpando" class="infobar">\n')
            # SOURCE LINE 66
            if not isinstance(c.site, DefaultSR):
                # SOURCE LINE 67
                __M_writer(u'      <label><input type="checkbox" name="restrict_sr" />')
                __M_writer(mako_websafe(_('limit my search to %(path)s') % dict(path=c.site.path.rstrip('/'))))
                __M_writer(u'</label>\n')
                pass
            # SOURCE LINE 69
            __M_writer(u'\n      ')
            # SOURCE LINE 70
            __M_writer(mako_websafe(search_faq()))
            __M_writer(u'\n  </div>\n')
            # SOURCE LINE 72
        else:
            # SOURCE LINE 73
            if not thing.site or isinstance(thing.site, DefaultSR):
                # SOURCE LINE 74
                __M_writer(u'      <input type="hidden" name="restrict_sr" value="off" />\n')
                # SOURCE LINE 75
            else:
                # SOURCE LINE 76
                __M_writer(u'      <br /><br />\n      <label><input type="checkbox" ')
                # SOURCE LINE 77
                __M_writer(mako_websafe('checked="checked"' if thing.restrict_sr else ''))
                __M_writer(u' name="restrict_sr" />\n      ')
                # SOURCE LINE 78
                __M_writer(mako_websafe(_('limit my search to %(path)s') % dict(path=thing.site.path.rstrip('/'))))
                __M_writer(u'</label>\n')
                pass
            # SOURCE LINE 80
            __M_writer(u'    ')
            __M_writer(mako_websafe(search_faq()))
            __M_writer(u'\n    <input type="submit" value="')
            # SOURCE LINE 81
            __M_writer(mako_websafe(_('search reddit')))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 83
        __M_writer(u'\n')
        # SOURCE LINE 84
        for k, v in thing.search_params.iteritems():
            # SOURCE LINE 85
            __M_writer(u'    <input type="hidden" name="')
            __M_writer(mako_websafe(k))
            __M_writer(u'" value="')
            __M_writer(mako_websafe(v))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 87
        __M_writer(u'</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search_faq(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n  <div id="moresearchinfo">\n  <p>use the following search parameters to narrow your results:</p>\n\n  <dl>\n      <dt>subreddit:<i>subreddit</i></dt>\n      <dd>')
        # SOURCE LINE 34
        __M_writer(mako_websafe(_('find submissions in "subreddit"')))
        __M_writer(u'</dd>\n      <dt>author:<i>username</i></dt>\n      <dd>')
        # SOURCE LINE 36
        __M_writer(mako_websafe(_('find submissions by "username"')))
        __M_writer(u'</dd>\n      <dt>site:<i>example.com</i></dt>\n      <dd>')
        # SOURCE LINE 38
        __M_writer(mako_websafe(_('find submissions from "example.com"')))
        __M_writer(u'</dd>\n      <dt>url:<i>text</i></dt>\n      <dd>')
        # SOURCE LINE 40
        __M_writer(mako_websafe(_('search for "text" in url')))
        __M_writer(u'</dd>\n      <dt>selftext:<i>text</i></dt>\n      <dd>')
        # SOURCE LINE 42
        __M_writer(mako_websafe(_('search for "text" in self post contents')))
        __M_writer(u'</dd>\n      <dt>self:yes (or self:no)</dt>\n      <dd>')
        # SOURCE LINE 44
        __M_writer(mako_websafe(_('include (or exclude) self posts')))
        __M_writer(u'</dd>\n      <dt>nsfw:yes (or nsfw:no)</dt>\n      <dd>')
        # SOURCE LINE 46
        __M_writer(mako_websafe(_('include (or exclude) results marked as NSFW')))
        __M_writer(u'</dd>\n  </dl>\n\n  <p>e.g.&#32;<code>subreddit:aww site:imgur.com dog</code></p>\n  <p><a href="http://www.reddit.com/wiki/search">')
        # SOURCE LINE 50
        __M_writer(mako_websafe(_('see the search faq for details.')))
        __M_writer(u'</a></p>\n  </div>\n\n  <p><a href="http://www.reddit.com/wiki/search" id="search_showmore">')
        # SOURCE LINE 53
        __M_writer(mako_websafe(_('advanced search: by author, subreddit...')))
        __M_writer(u'</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


