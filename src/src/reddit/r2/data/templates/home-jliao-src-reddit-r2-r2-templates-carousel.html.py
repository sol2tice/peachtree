# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404254409.816379
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/carousel.html'
_template_uri=u'/carousel.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['indicators', 'inner_links']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

        items = [
            ('static/homeAsset1.png', 'Find the discussion community related to college admissions'),
            ('', 'Help you narrow down your school choices. Search more than 3,000 colleges and universities by name, location, or area of study!'),
            ('', 'Helpful resources and expert advice to assist you throughout the college admissions process'),
            ('', 'Submit your questions about the college admissions process, financial aid, and college search to College Confidential\'s resident expert'),
            ('', 'You\'ll find hundreds of pages of articles about choosing a college, getting into the college you want')
        ]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['items'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 9
        __M_writer(u'\n\n<div id="carousel-container">\n\t<div id="myCarousel" class="carousel slide" data-ride="carousel" data-wrap="true" data-interval="5000" data-pause="hover">\n        ')
        # SOURCE LINE 13
        __M_writer(mako_websafe(self.indicators(items)))
        __M_writer(u'\n        <div class="carousel-inner" onClick="nextSlide()">\n            ')
        # SOURCE LINE 15
        __M_writer(mako_websafe(self.inner_links(items)))
        __M_writer(u'\n        </div>\n    </div>\n</div>\n\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_indicators(context,links):
    context.caller_stack._push_frame()
    try:
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n    <ol class="carousel-indicators">\n')
        # SOURCE LINE 38
        for i, item in enumerate(links):
            # SOURCE LINE 39
            __M_writer(u'        <li id="carousel-indicator-')
            __M_writer(mako_websafe(i))
            __M_writer(u'" class="')
            __M_writer(mako_websafe('sprite-home-slide_on active' if (i==0) else 'sprite-home-slide_off'))
            __M_writer(u'" data-target="#myCarousel" data-slide-to="')
            __M_writer(mako_websafe(i))
            __M_writer(u'" ></li>\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'    </ol>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inner_links(context,links):
    context.caller_stack._push_frame()
    try:
        def link(idx,img,msg):
            context.caller_stack._push_frame()
            try:
                __M_writer = context.writer()
                # SOURCE LINE 21
                __M_writer(u'\n          <div class="')
                # SOURCE LINE 22
                __M_writer(mako_websafe('item active' if(i==0) else 'item'))
                __M_writer(u'">\n  \t\t  <img id=\'homeAsset')
                # SOURCE LINE 23
                __M_writer(mako_websafe(idx + 1))
                __M_writer(u'\' src="')
                __M_writer(mako_websafe(img))
                __M_writer(u'" if img} width=\'560px\' height=\'360px\'> \n            <div class="container">\n              <div class="carousel-caption">\n                <p>')
                # SOURCE LINE 26
                __M_writer(mako_websafe(msg))
                __M_writer(u'</p>\n              </div>\n            </div>\n          </div>\n    ')
                return ''
            finally:
                context.caller_stack._pop_frame()
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n    ')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        for i, item in enumerate(links):
            # SOURCE LINE 32
            __M_writer(u'        ')
            __M_writer(mako_websafe(link(i, item[0], item[1])))
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


