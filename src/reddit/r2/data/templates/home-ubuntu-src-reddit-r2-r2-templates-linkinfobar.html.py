# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402128269.579685
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/linkinfobar.html'
_template_uri='/linkinfobar.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.strings import strings
from r2.lib.template_helpers import format_number, html_datetime
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7fabdc46c350', context._clean_inheritance_tokens(), templateuri=u'printable.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fabdc46c350')] = ns

    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7fabdc46c190', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fabdc46c190')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabdc46c350')._populate(_import_ns, [u'thing_css_class'])
        _mako_get_namespace(context, '__anon_0x7fabdc46c190')._populate(_import_ns, [u'state_button'])
        int = _import_ns.get('int', context.get('int', UNDEFINED))
        max = _import_ns.get('max', context.get('max', UNDEFINED))
        float = _import_ns.get('float', context.get('float', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n\n\n<div class="linkinfo">\n  <div class="date">\n    <span>\n      ')
        # SOURCE LINE 37
        __M_writer(mako_websafe(_("this post was submitted on")))
        __M_writer(u'\n      &#32;\n    </span>\n    <time datetime="')
        # SOURCE LINE 40
        __M_writer(mako_websafe(html_datetime(thing.a._date)))
        __M_writer(u'">\n      ')
        # SOURCE LINE 41
        __M_writer(mako_websafe(thing.a._date.strftime(thing.datefmt)))
        __M_writer(u'\n    </time>\n  </div>\n\n  <div class="score">\n    ')
        # SOURCE LINE 46
        __M_writer(mako_websafe(unsafe(strings.person_label % dict(num = format_number(thing.a.score),
                                         persons = ungettext("point", "points", 
                                         thing.a.score)))))
        # SOURCE LINE 48
        __M_writer(u'\n    ')
        # SOURCE LINE 49
        percent = int(float(thing.a.upvotes) / max(thing.a.upvotes + thing.a.downvotes, 1) * 100) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['percent'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n    &#32;(')
        # SOURCE LINE 50
        __M_writer(mako_websafe(percent))
        __M_writer(u'% ')
        __M_writer(mako_websafe(_("like it")))
        __M_writer(u')\n  </div>\n\n  <span class="upvotes">\n    ')
        # SOURCE LINE 54
        __M_writer(mako_websafe(unsafe(strings.person_label % dict(num = format_number(thing.a.upvotes),
                                         persons = ungettext("upvote", "upvotes",
                                         thing.a.upvotes)))))
        # SOURCE LINE 56
        __M_writer(u'\n  </span>\n  &#32;\n  <span class="downvotes">\n    ')
        # SOURCE LINE 60
        __M_writer(mako_websafe(unsafe(strings.person_label % dict(num = format_number(thing.a.downvotes),
                                         persons = ungettext("downvote", "downvotes",
                                         thing.a.downvotes)))))
        # SOURCE LINE 62
        __M_writer(u'\n  </span>\n\n')
        # SOURCE LINE 65
        if getattr(thing.a, "shortlink", None):
            # SOURCE LINE 66
            __M_writer(u'  <div class="shortlink">\n    shortlink:\n    &#32;\n    <input type="text" value="http://')
            # SOURCE LINE 69
            __M_writer(mako_websafe(thing.a.shortlink))
            __M_writer(u'" readonly="readonly" id="shortlink-text" />\n  </div>\n')
            pass
        # SOURCE LINE 72
        __M_writer(u'\n  <table>\n')
        # SOURCE LINE 74
        if c.user_is_admin:
            # SOURCE LINE 75
            __M_writer(u'      ')
            runtime._include_file(context, u'adminlinkinfo.html', _template_uri)
            __M_writer(u'\n')
            pass
        # SOURCE LINE 77
        __M_writer(u'\n')
        # SOURCE LINE 78
        if c.user_is_sponsor:
            # SOURCE LINE 79
            __M_writer(u'      ')
            runtime._include_file(context, u'linkpromoteinfobar.html', _template_uri)
            __M_writer(u'\n')
            pass
        # SOURCE LINE 81
        __M_writer(u'  </table>\n</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


