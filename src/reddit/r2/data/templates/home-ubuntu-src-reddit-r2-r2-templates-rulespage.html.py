# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919392.913152
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/rulespage.html'
_template_uri='/rulespage.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['expando_end', 'good_example', 'bad_example', 'expando_start']


# SOURCE LINE 23

from r2.lib.template_helpers import static


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def expando_end():
            return render_expando_end(context.locals_(__M_locals))
        def good_example(phrase,leadin='OK:'):
            return render_good_example(context.locals_(__M_locals),phrase,leadin)
        def bad_example(phrase,leadin='NOT OK:'):
            return render_bad_example(context.locals_(__M_locals),phrase,leadin)
        def expando_start(phrase):
            return render_expando_start(context.locals_(__M_locals),phrase)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n<script type="text/javascript">\nfunction toggle_expando(elem){\n  var examples = $(elem).siblings(".rule-examples");\n  var toggle = $(elem).find(".toggle");\n  if (examples.is(":visible")){\n    toggle.text("[+]");\n    examples.slideUp();\n  } else {\n    toggle.text("[\\u2013]");\n    examples.slideDown();\n  }\n}\n</script>\n\n<div class="rulespage">\n  <h1>rules of reddit</h1>\n  <div>\n    <p class="info">reddit is a pretty open platform and free speech place, but there are a few rules:</p>\n    <ol class="rule-list">\n      <li id="spam" class="first-rule">\n        <p>Don\'t&#32;<a href="http://www.reddit.com/wiki/faq#wiki_what_constitutes_spam.3F">spam</a>.</p>\n        ')
        # SOURCE LINE 69
        __M_writer(mako_websafe(expando_start("What is spam?")))
        __M_writer(u'\n          ')
        # SOURCE LINE 70
        __M_writer(mako_websafe(bad_example('Submitting only links to your blog or personal website.')))
        __M_writer(u'\n          ')
        # SOURCE LINE 71
        __M_writer(mako_websafe(good_example('Submitting links from a variety of sites and sources.')))
        __M_writer(u'\n          ')
        # SOURCE LINE 72
        __M_writer(mako_websafe(good_example('Submitting links from your own site, talking with redditors in the comments, and also submitting cool stuff from other sites.')))
        __M_writer(u'\n          ')
        # SOURCE LINE 73
        __M_writer(mako_websafe(bad_example('Posting the same comment repeatedly in multiple subreddits.')))
        __M_writer(u'\n        ')
        # SOURCE LINE 74
        __M_writer(mako_websafe(expando_end()))
        __M_writer(u'\n      </li>\n      <li id="votecheating">\n        <p>Don\'t ask for votes or engage in&#32;<a href="http://www.reddit.com/wiki/faq#wiki_what_constitutes_vote_cheating_and_vote_manipulation.3F">vote manipulation</a>.</p>\n        ')
        # SOURCE LINE 78
        __M_writer(mako_websafe(expando_start("What does vote manipulation look like?")))
        __M_writer(u'\n          ')
        # SOURCE LINE 79
        __M_writer(mako_websafe(bad_example('Buying votes or using services to vote.')))
        __M_writer(u'\n          ')
        # SOURCE LINE 80
        __M_writer(mako_websafe(good_example('Sharing reddit links with your friends.')))
        __M_writer(u'\n          ')
        # SOURCE LINE 81
        __M_writer(mako_websafe(bad_example('Sharing links with your friends or coworkers and asking them to vote.')))
        __M_writer(u'\n          ')
        # SOURCE LINE 82
        __M_writer(mako_websafe(bad_example('Creating submissions such as "For every upvote I will ..." or "... please upvote this!", regardless of the cause.')))
        __M_writer(u'\n        ')
        # SOURCE LINE 83
        __M_writer(mako_websafe(expando_end()))
        __M_writer(u'\n      </li>\n      <li id="personalinfo">\n        <p>Don\'t post&#32;<a href="http://www.reddit.com/wiki/faq#wiki_is_posting_personal_information_ok.3F">personal information</a>.</p>\n        ')
        # SOURCE LINE 87
        __M_writer(mako_websafe(expando_start("What might be personal information?")))
        __M_writer(u'\n          ')
        # SOURCE LINE 88
        __M_writer(mako_websafe(bad_example("Posting a link to your friend's facebook profile.")))
        __M_writer(u'\n          ')
        # SOURCE LINE 89
        __M_writer(mako_websafe(good_example("Posting your senator's publicly available contact information")))
        __M_writer(u'\n          ')
        # SOURCE LINE 90
        __M_writer(mako_websafe(bad_example("Posting the full name, employer, or other real-life details of another redditor")))
        __M_writer(u'\n          ')
        # SOURCE LINE 91
        __M_writer(mako_websafe(good_example("Posting a link to a public page maintained by a celebrity.")))
        __M_writer(u'\n        ')
        # SOURCE LINE 92
        __M_writer(mako_websafe(expando_end()))
        __M_writer(u'\n      </li>\n      <li id="minors">\n        <p>No&#32;<a href="http://www.missingkids.com/Exploitation/FAQ" rel="nofollow">child pornography</a>&#32;or&#32;<a href="http://www.reddit.com/r/blog/comments/pmj7f/a_necessary_change_in_policy/" rel="nofollow">sexually suggestive content featuring minors</a>.</p>\n      </li>\n      <li id="breakthesite">\n        <p>Don\'t break the site or do anything that interferes with normal use of the site.</p>\n        ')
        # SOURCE LINE 99
        __M_writer(mako_websafe(expando_start("Tell me more.")))
        __M_writer(u'\n          ')
        # SOURCE LINE 100
        __M_writer(mako_websafe(bad_example('Creating programs that request information more than once every 2 seconds or violate any of our other <a href="https://github.com/reddit/reddit/wiki/API">&nbsp;API rules</a>.')))
        __M_writer(u'\n          ')
        # SOURCE LINE 101
        __M_writer(mako_websafe(good_example('Responsibly <a href="/wiki/whitehat">&nbsp;reporting security&nbsp;</a> issues to us.', leadin="AWESOME:")))
        __M_writer(u'\n        ')
        # SOURCE LINE 102
        __M_writer(mako_websafe(expando_end()))
        __M_writer(u'\n      </li>\n      <!--  Also, \'reddit\' is STRICTLY lowercase -->\n    </ol>\n  </div>\n  <div id="followreddiquette" class="info">\n    <p>You should also be mindful of <a href="/wiki/reddiquette">&nbsp;reddiquette</a>, an&nbsp;<em>informal</em>&nbsp;expression of reddit\'s community values as written by the community itself. Please abide by it the best you can.</p>\n  </div>\n  <div class="info">\n  <img id="brick" class="bottom" title="')
        # SOURCE LINE 111
        __M_writer(mako_websafe(_("here at reddit, we inscribe our rules on a brick. screw tablets.")))
        __M_writer(u'" alt="')
        __M_writer(mako_websafe(_('this brick has no semantic value')))
        __M_writer(u'" src="')
        __M_writer(mako_websafe(static('brick.png')))
        __M_writer(u'">\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_expando_end(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n      </ul>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_good_example(context,phrase,leadin='OK:'):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n<li class="example good-example"><em>')
        # SOURCE LINE 41
        __M_writer(mako_websafe(leadin))
        __M_writer(u'</em>&nbsp;')
        __M_writer(mako_websafe(unsafe(phrase)))
        __M_writer(u'</li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bad_example(context,phrase,leadin='NOT OK:'):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n<li class="example bad-example"><em>')
        # SOURCE LINE 45
        __M_writer(mako_websafe(leadin))
        __M_writer(u'</em>&nbsp;')
        __M_writer(mako_websafe(unsafe(phrase)))
        __M_writer(u'</li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_expando_start(context,phrase):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n  <div class="examples">\n    <p class="expander" onClick="return toggle_expando(this);"><em class="toggle">[+]</em>&nbsp;')
        # SOURCE LINE 29
        __M_writer(mako_websafe(phrase))
        __M_writer(u'</p>\n    <div class="rule-examples" style="display:none;">\n      <ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


