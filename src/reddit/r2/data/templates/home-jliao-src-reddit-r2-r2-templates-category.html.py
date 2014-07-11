# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405040828.662053
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/category.html'
_template_uri=u'/category.html'
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
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

        items = [
            (u'College Admissions', '100 threads', '/forum', 'static/messages.png', 'Messages'),
            (u'College Essays', '100 threads', '/college_search', 'static/videocall.png', 'Video &amp; Voice Calls'),
            (u'What Are My Chances?', '100 threads', '/college_admission', 'static/channels_icon.png', 'Channels'),
            (u'College Search & Selection', '100 threads', '/college_life', 'static/photo.png', 'Photo Sharing'),
            (u'Financial Aid & Scholarships', '100 threads', '/summercamp', 'static/music.png', 'Music'),
            (u'College Life', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'International Students', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'SAT and ACT Tests & Test Prep', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Ivy League', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'College Majors', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Parents Forum', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Study Aboard', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Internships Careers', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Business School', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Graduate School', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Law School', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Dental School', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Pre-Med & Medical School', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'High School Life', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Prep School Admissions', '/consulting', '100 threads', 'static/games.png', 'Games'),
            (u'Summer Programs', '/consulting', '100 threads', 'static/games.png', 'Games'),
        ]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['items'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 25
        __M_writer(u'\n\n<div class="panel panel-default">\n    <div class="panel-heading">\n        <i class="fa fa-bell fa-fw"></i> Sort By\n    </div>\n    <div class="panel-body">\n')
        # SOURCE LINE 32
        for toolbar in thing.toolbars:
            # SOURCE LINE 33
            __M_writer(u'          ')
            __M_writer(mako_websafe(toolbar))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'    </div>\n</div>\n\n<div class="panel panel-default">\n    <div class="panel-heading">\n        <i class="fa fa-bell fa-fw"></i> Discussion Areas\n    </div>\n    <!-- /.panel-heading -->\n    <div class="panel-body">\n    \t<a href="#" class="btn btn-default btn-block">View More ... \n    \t\t<span class="fa fa-search pull-right"></span>\n    \t</a>\n\t')
        # SOURCE LINE 47
        __M_writer(mako_websafe(thing.srtopbar))
        __M_writer(u'\n\t')
        # SOURCE LINE 58
        __M_writer(u'\n        <!-- /.list-group -->                           \n    </div>\n    <!-- /.panel-body -->\n</div>\n<!-- /.panel -->\n')
        # SOURCE LINE 193
        __M_writer(u'\n<!-- /.panel .chat-panel -->     \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


