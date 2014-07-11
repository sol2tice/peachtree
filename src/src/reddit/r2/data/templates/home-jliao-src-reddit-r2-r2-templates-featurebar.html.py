# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405007078.733686
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/featurebar.html'
_template_uri=u'/featurebar.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['navigation_links']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

        items = [
            (u'留学在线问答', '/forum', 'static/messages.png', 'Messages'),
            (u'美国大学搜索', '/college_search', 'static/videocall.png', 'Video &amp; Voice Calls'),
            (u'留美录取申请', '/college_admission', 'static/channels_icon.png', 'Channels'),
            (u'留学校园生活', '/college_life', 'static/photo.png', 'Photo Sharing'),
            (u'美国高中生夏令营', '/summercamp', 'static/music.png', 'Music'),
            (u'专家升学指导', '/consulting', 'static/games.png', 'Games')
        ]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['items'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 10
        __M_writer(u'\n<div class="features-bar">\n    <div class="container">\n        <div style="margin-left: 2em">\n            ')
        # SOURCE LINE 14
        __M_writer(mako_websafe(self.navigation_links(items)))
        __M_writer(u'\n        </div>\n    </div>\n</div>\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation_links(context,links):
    context.caller_stack._push_frame()
    try:
        def link(idx,label,url,image,alt):
            context.caller_stack._push_frame()
            try:
                __M_writer = context.writer()
                # SOURCE LINE 20
                __M_writer(u'\n          <a href="')
                # SOURCE LINE 21
                __M_writer(mako_websafe(url))
                __M_writer(u'" class="feature-href desktop">\n              <div class="icon-feature loop-')
                # SOURCE LINE 22
                __M_writer(mako_websafe(idx +1))
                __M_writer(u'">\n                  <img src="')
                # SOURCE LINE 23
                __M_writer(mako_websafe(image))
                __M_writer(u'" alt="')
                __M_writer(mako_websafe(alt))
                __M_writer(u'" />\n              </div>\n              <div class="name-feature">')
                # SOURCE LINE 25
                __M_writer(mako_websafe(label))
                __M_writer(u'</div>\n          </a>\n          <a href="')
                # SOURCE LINE 27
                __M_writer(mako_websafe(url))
                __M_writer(u'" class="feature-href mobile">\n              <div class="icon-feature loop-')
                # SOURCE LINE 28
                __M_writer(mako_websafe(idx))
                __M_writer(u'"">\n                  <img src="')
                # SOURCE LINE 29
                __M_writer(mako_websafe(image))
                __M_writer(u'" alt="')
                __M_writer(mako_websafe(alt))
                __M_writer(u'" />\n              </div>\n              <div class="name-feature">')
                # SOURCE LINE 31
                __M_writer(mako_websafe(label))
                __M_writer(u'</div>\n          </a>\n    ')
                return ''
            finally:
                context.caller_stack._pop_frame()
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n    ')
        # SOURCE LINE 33
        __M_writer(u'\n\n    <ul>\n')
        # SOURCE LINE 36
        for i, item in enumerate(links):
            # SOURCE LINE 37
            __M_writer(u'        <li>')
            # SOURCE LINE 38
            __M_writer(u'        ')
            __M_writer(mako_websafe(link(i, item[0], item[1], item[2], item[3])))
            # SOURCE LINE 39
            __M_writer(u'        </li>\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


