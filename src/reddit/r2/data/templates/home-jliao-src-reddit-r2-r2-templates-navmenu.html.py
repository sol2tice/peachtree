# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405040828.729107
_template_filename='/home/jliao/src/reddit/r2/r2/templates/navmenu.html'
_template_uri='/navmenu.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['tabmenu', 'flatlist', 'multicolumn', 'dropdown']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f537dfaf2d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f537dfaf2d0')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f537dfaf2d0')._populate(_import_ns, [u'plain_link', u'post_link', u'img_link', u'separator'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 60
        __M_writer(u'\n\n\n')
        # SOURCE LINE 109
        __M_writer(u'\n\n')
        # SOURCE LINE 132
        __M_writer(u'\n\n')
        # SOURCE LINE 164
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabmenu(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f537dfaf2d0')._populate(_import_ns, [u'plain_link', u'post_link', u'img_link', u'separator'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 134
        __M_writer(u'\n')
        # SOURCE LINE 135
        if thing:
            # SOURCE LINE 136
            __M_writer(u'    <div class="list-group">\n')
            # SOURCE LINE 137
            for i, option in enumerate(thing):
                # SOURCE LINE 138
                __M_writer(u'            <a href="')
                __M_writer(mako_websafe(option.sr_path))
                __M_writer(u'" class="list-group-item">\n')
                # SOURCE LINE 139
                if option == thing.selected:
                    # SOURCE LINE 140
                    __M_writer(u'                <i class="fa fa-check">\n')
                    # SOURCE LINE 141
                else:
                    # SOURCE LINE 142
                    __M_writer(u'                <i class="fa ">\n')
                    pass
                # SOURCE LINE 144
                __M_writer(u'                ')
                __M_writer(mako_websafe(option.title))
                __M_writer(u'</i>\n            </a>\n')
                pass
            # SOURCE LINE 147
            __M_writer(u'    </div>\n')
            # SOURCE LINE 148
        else:
            # SOURCE LINE 149
            __M_writer(u'    ')
            css_class = str(thing.css_class) if thing.css_class else "" 
            
            __M_writer(u'\n    <ul class="tabmenu ')
            # SOURCE LINE 150
            __M_writer(mako_websafe(css_class))
            __M_writer(u'"\n        ')
            # SOURCE LINE 151
            __M_writer(mako_websafe("id='%s'" % thing._id if thing._id else ""))
            __M_writer(u'>\n')
            # SOURCE LINE 152
            for i, option in enumerate(thing):
                # SOURCE LINE 153
                __M_writer(u'        ')

                tab_name = getattr(option, 'tab_name', None)
                li_id = "id='tab-%s'" % tab_name if tab_name else ""
                li_class = "class='selected'" if option == thing.selected else ""
                        
                
                # SOURCE LINE 157
                __M_writer(u'\n        <li ')
                # SOURCE LINE 158
                __M_writer(mako_websafe(li_id))
                __M_writer(u' ')
                __M_writer(mako_websafe(li_class))
                __M_writer(u'>\n          ')
                # SOURCE LINE 159
                __M_writer(mako_websafe(option))
                __M_writer(u'\n        </li>\n')
                pass
            # SOURCE LINE 162
            __M_writer(u'    </ul>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flatlist(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f537dfaf2d0')._populate(_import_ns, [u'plain_link', u'post_link', u'img_link', u'separator'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        separator = _import_ns.get('separator', context.get('separator', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 63
        __M_writer(u'\n')
        # SOURCE LINE 64
        if str(thing.css_class) == "flat-list sr-bar":
            # SOURCE LINE 65
            __M_writer(u'  <div class="list-group">\n')
            # SOURCE LINE 66
            for i, option in enumerate(thing):
                # SOURCE LINE 67
                __M_writer(u'            <a href="')
                __M_writer(mako_websafe(option.sr_path))
                __M_writer(u'" class="list-group-item">\n')
                # SOURCE LINE 68
                if option == thing.selected:
                    # SOURCE LINE 69
                    __M_writer(u'\t\t<i class="fa fa-check">\n')
                    # SOURCE LINE 70
                else:
                    # SOURCE LINE 71
                    __M_writer(u'\t\t<i class="fa ">\n')
                    pass
                # SOURCE LINE 73
                __M_writer(u'\t\t')
                __M_writer(mako_websafe(option.title))
                __M_writer(u'</i>\n\t\t<span class="pull-right text-muted small"><em>100 threads</em></span>\n\t    </a>\n')
                pass
            # SOURCE LINE 77
            __M_writer(u'  </div>\n')
            # SOURCE LINE 78
        elif str(thing.css_class) == 'separator':
            # SOURCE LINE 79
            __M_writer(u'  pass \n')
            # SOURCE LINE 80
        else:
            # SOURCE LINE 81
            __M_writer(u'  ')
            css_class = str(thing.css_class) if thing.css_class else "" 
            
            __M_writer(u'\n')
            # SOURCE LINE 82
            if thing:
                # SOURCE LINE 83
                __M_writer(u'    <ul class="')
                __M_writer(mako_websafe(css_class))
                __M_writer(u' hover"\n        ')
                # SOURCE LINE 84
                __M_writer(mako_websafe("id='%s'" % thing._id if thing._id else ""))
                __M_writer(u'>\n\n')
                # SOURCE LINE 86
                if thing.title:
                    # SOURCE LINE 87
                    __M_writer(u'        <li class="')
                    __M_writer(mako_websafe(css_class))
                    __M_writer(u' title">')
                    __M_writer(mako_websafe(thing.title))
                    __M_writer(u'</li>\n')
                    pass
                # SOURCE LINE 89
                __M_writer(u'\n')
                # SOURCE LINE 90
                for i, option in enumerate(thing):
                    # SOURCE LINE 91
                    __M_writer(u'        ')

           ##option.title isn't the title, option.render() is the entire link
                    if option == thing.selected:
                      class_name = "class='selected'"
                      option.selected = True                                           
                    else:
                      class_name = ""
                            
                    
                    # SOURCE LINE 98
                    __M_writer(u'\n        <li ')
                    # SOURCE LINE 99
                    __M_writer(mako_websafe(class_name))
                    __M_writer(u'>\n')
                    # SOURCE LINE 100
                    if i > 0:
                        # SOURCE LINE 101
                        __M_writer(u'            ')
                        __M_writer(mako_websafe(separator(thing.separator)))
                        __M_writer(u'\n')
                        pass
                    # SOURCE LINE 103
                    __M_writer(u'          ')
                    __M_writer(mako_websafe(option))
                    __M_writer(u'\n        </li>\n')
                    pass
                # SOURCE LINE 106
                __M_writer(u'    </ul>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_multicolumn(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f537dfaf2d0')._populate(_import_ns, [u'plain_link', u'post_link', u'img_link', u'separator'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        max = _import_ns.get('max', context.get('max', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 111
        __M_writer(u'\n  ')
        # SOURCE LINE 112
 
        buttons = thing.options
        l = len(buttons)/2
        l = max(l, len(buttons) - l)
        buttons = (buttons[:l], buttons[l:])
           
        
        # SOURCE LINE 117
        __M_writer(u'\n')
        # SOURCE LINE 118
        for b in buttons:
            # SOURCE LINE 119
            __M_writer(u'    <ul class="hover">\n')
            # SOURCE LINE 120
            for i, option in enumerate(b):
                # SOURCE LINE 121
                __M_writer(u'        ')

                cls = "first" if i == 0 else ""
                         
                
                # SOURCE LINE 123
                __M_writer(u'\n')
                # SOURCE LINE 124
                if option == thing.selected:
                    # SOURCE LINE 125
                    __M_writer(u'          <li class="selected ')
                    __M_writer(mako_websafe(cls))
                    __M_writer(u'">')
                    __M_writer(mako_websafe(option.selected_title()))
                    __M_writer(u'</li>\n')
                    # SOURCE LINE 126
                else:
                    # SOURCE LINE 127
                    __M_writer(u'          <li class="')
                    __M_writer(mako_websafe(cls))
                    __M_writer(u'">')
                    __M_writer(mako_websafe(option))
                    __M_writer(u'</li>\n')
                    pass
                pass
            # SOURCE LINE 130
            __M_writer(u'    </ul>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_dropdown(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f537dfaf2d0')._populate(_import_ns, [u'plain_link', u'post_link', u'img_link', u'separator'])
        post_link = _import_ns.get('post_link', context.get('post_link', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'  ')
        css_class = str(thing.css_class) if thing.css_class else "" 
        
        __M_writer(u'\n')
        # SOURCE LINE 30
        if thing:
            # SOURCE LINE 31
            if thing.title and thing.selected:
                # SOURCE LINE 32
                __M_writer(u'      <span class="dropdown-title ')
                __M_writer(mako_websafe(css_class))
                __M_writer(u'">')
                __M_writer(mako_websafe(thing.title))
                __M_writer(u':&#32;</span>\n')
                pass
            # SOURCE LINE 34
            __M_writer(u'\n    <div class="dropdown ')
            # SOURCE LINE 35
            __M_writer(mako_websafe(css_class))
            __M_writer(u'"\n         ')
            # SOURCE LINE 36
            __M_writer(mako_websafe("id='%s'" % thing._id if thing._id else ""))
            __M_writer(u'\n         onclick="open_menu(this)"\n         onmouseover="hover_open_menu(this)">\n \n')
            # SOURCE LINE 40
            if thing.selected:
                # SOURCE LINE 41
                __M_writer(u'          <span class="selected">')
                __M_writer(mako_websafe(thing.selected.selected_title()))
                __M_writer(u'</span>\n')
                # SOURCE LINE 42
            elif thing.title:
                # SOURCE LINE 43
                __M_writer(u'          <span class="selected title">')
                __M_writer(mako_websafe(thing.title))
                __M_writer(u'</span>\n')
                pass
            # SOURCE LINE 45
            __M_writer(u'    </div>\n\n    <div class="drop-choices ')
            # SOURCE LINE 47
            __M_writer(mako_websafe(css_class))
            __M_writer(u'">\n')
            # SOURCE LINE 48
            for option in thing:
                # SOURCE LINE 49
                __M_writer(u'        ')
                _class = "choice " + option.css_class + (" selected" if option == thing.selected else "") 
                
                __M_writer(u'\n')
                # SOURCE LINE 50
                if thing.use_post:
                    # SOURCE LINE 51
                    __M_writer(u'          ')
                    __M_writer(mako_websafe(post_link(option.title, option.base_path, option.path,
                      option.action_params, _sr_path=option.sr_path, _class=_class)))
                    # SOURCE LINE 52
                    __M_writer(u'\n')
                    # SOURCE LINE 53
                else:
                    # SOURCE LINE 54
                    __M_writer(u'          ')
                    __M_writer(mako_websafe(plain_link(option.title, option.path, _sr_path = option.sr_path, _class=_class)))
                    __M_writer(u'\n')
                    pass
                pass
            # SOURCE LINE 57
            __M_writer(u'    </div>\n\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


