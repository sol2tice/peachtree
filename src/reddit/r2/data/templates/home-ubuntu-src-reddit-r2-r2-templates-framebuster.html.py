# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918232.599309
_template_filename=u'/home/ubuntu/src/reddit/r2/r2/templates/framebuster.html'
_template_uri=u'/framebuster.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['framebuster']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7f1dd5af93d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd5af93d0')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f1dd5af9310', context._clean_inheritance_tokens(), templateuri=u'reddit.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd5af9310')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5af93d0')._populate(_import_ns, [u'js_setup'])
        _mako_get_namespace(context, '__anon_0x7f1dd5af9310')._populate(_import_ns, [u'javascript'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        js_setup = _import_ns.get('js_setup', context.get('js_setup', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n<html>\n  <head>\n    <title>escappit</title>\n    ')
        # SOURCE LINE 29
        from r2.lib import js 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['js'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n\n    <!--[if gte IE 9]> <!-->\n      ')
        # SOURCE LINE 33
        __M_writer(mako_websafe(unsafe(js.use('jquery2x', 'reddit'))))
        __M_writer(u'\n    <!-- <![endif]-->\n\n    <!--[if lt IE 9]>\n      ')
        # SOURCE LINE 37
        __M_writer(mako_websafe(unsafe(js.use('jquery1x', 'reddit'))))
        __M_writer(u'\n    <![endif]-->\n    ')
        # SOURCE LINE 39
        __M_writer(mako_websafe(js_setup()))
        __M_writer(u'\n  </head>\n  <body>\n    <script type="text/javascript">\n')
        # SOURCE LINE 43
        if thing.login:
            # SOURCE LINE 44
            __M_writer(u'        $.cookie_write({name: "redditSession", data: "cname",\n                        domain: "')
            # SOURCE LINE 45
            __M_writer(mako_websafe(c.site.domain))
            __M_writer(u'" });\n        if(parent.$ && parent.$.framebuster) \n           parent.$.framebuster();\n')
            # SOURCE LINE 48
        else:
            # SOURCE LINE 49
            __M_writer(u'        $.cookie_write({name: "redditSession", data: "",\n                        domain: "')
            # SOURCE LINE 50
            __M_writer(mako_websafe(c.site.domain))
            __M_writer(u'"});\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'    </script>\n  </body>\n</html>\n\n\n')
        # SOURCE LINE 83
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_framebuster(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5af93d0')._populate(_import_ns, [u'js_setup'])
        _mako_get_namespace(context, '__anon_0x7f1dd5af9310')._populate(_import_ns, [u'javascript'])
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n')
        # SOURCE LINE 58
        if c.cname and (c.frameless_cname or not c.user_is_loggedin) and not c.authorized_cname:
            # SOURCE LINE 59
            __M_writer(u'    ')
 
            import random 
            from r2.lib.template_helpers import get_domain
            
            
            # SOURCE LINE 62
            __M_writer(u'\n    <script type="text/javascript">\n      (function($) {\n         $.framebuster = function() {\n            $(function() {\n                if($.browser.mozilla) {\n                   var url = window.location.href;\n                   $.redirect(url + ((url.indexOf(\'?\') == -1)?\'?\':\'&\') +\n                         \'v=\' + Math.random());\n                }\n                else\n                   $.refresh();\n             });\n         }\n      })(jQuery);\n      document.write(\'<iframe name="reddit-window" id="reddit-window"\' +\n       \'src="http://')
            # SOURCE LINE 78
            __M_writer(mako_websafe(get_domain(cname=False, subreddit=True)))
            __M_writer(u'/framebuster/\'\n       + Math.random() + \n       \'" width="1" height="1" style="visibility: hidden"></iframe>\');\n    </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


