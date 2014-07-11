# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919973.396532
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/listing.htmllite'
_template_uri='/listing.htmllite'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x48ea450', context._clean_inheritance_tokens(), templateuri=u'printable.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x48ea450')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x48ea350', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x48ea350')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x48ea450')._populate(_import_ns, [u'thing_css_class'])
        _mako_get_namespace(context, '__anon_0x48ea350')._populate(_import_ns, [u'optionalstyle'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        optionalstyle = _import_ns.get('optionalstyle', context.get('optionalstyle', UNDEFINED))
        thing_css_class = _import_ns.get('thing_css_class', context.get('thing_css_class', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n<div ')
        # SOURCE LINE 25
        __M_writer(mako_websafe(optionalstyle("margin-left:5px;margin-top:7px;")))
        __M_writer(u'>\n  ')
        # SOURCE LINE 26
 
        t = thing.things
        l = len(t)
        two_col = request.GET.has_key("twocolumn") if l else False
           
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['two_col','t','l'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        for i, a in enumerate(t):
            # SOURCE LINE 32
            __M_writer(u'   ')
 
            cls = "reddit-link "
            cls += "odd " if i % 2 else "even "
            cls += "first-half" if i < (l+1)/2 else "second-half"
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['cls'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 36
            __M_writer(u'\n')
            # SOURCE LINE 37
            if two_col:
                # SOURCE LINE 38
                if i == 0:
                    # SOURCE LINE 39
                    __M_writer(u'       <div class="reddit-listing-left" \n            ')
                    # SOURCE LINE 40
                    __M_writer(mako_websafe(optionalstyle("float:left;width:47%")))
                    __M_writer(u'>\n')
                    # SOURCE LINE 41
                elif i - 1 < (l+1)/2 and i >= (l+1)/2:
                    # SOURCE LINE 42
                    __M_writer(u'       </div>\n       <div class="reddit-listing-right" \n            ')
                    # SOURCE LINE 44
                    __M_writer(mako_websafe(optionalstyle("float:right; width:49%;")))
                    __M_writer(u'>\n')
                    pass
                pass
            # SOURCE LINE 47
            __M_writer(u'\n     <div class="')
            # SOURCE LINE 48
            __M_writer(mako_websafe(cls))
            __M_writer(u' ')
            __M_writer(mako_websafe(thing_css_class(a)))
            __M_writer(u'">\n       ')
            # SOURCE LINE 49
            __M_writer(mako_websafe(a))
            __M_writer(u'\n     </div>\n')
            # SOURCE LINE 51
            if two_col and i == l - 1:
                # SOURCE LINE 52
                __M_writer(u'   </div>\n')
                pass
            pass
        # SOURCE LINE 55
        if two_col:
            # SOURCE LINE 56
            __M_writer(u'    <div ')
            __M_writer(mako_websafe(optionalstyle("clear:both")))
            __M_writer(u'></div>\n')
            pass
        # SOURCE LINE 58
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


