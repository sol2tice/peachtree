# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402411028.563868
_template_filename='/home/jliao/src/reddit/r2/r2/templates/searchbar.html'
_template_uri='/searchbar.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 25

from r2.lib.strings import strings
from r2.lib.pages import SearchForm
from r2.lib.template_helpers import static, search_url


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f30c4076150', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f30c4076150')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c4076150')._populate(_import_ns, [u'pretty_button'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        pretty_button = _import_ns.get('pretty_button', context.get('pretty_button', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        isize = 60 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['isize'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        if thing.prev_search and thing.elapsed_time > 0:
            # SOURCE LINE 34
            __M_writer(u'  <div class="search-summary">\n')
            # SOURCE LINE 35
            if thing.show_feedback:
                # SOURCE LINE 36
                __M_writer(u'    <div>\n      ')
                # SOURCE LINE 37
                __M_writer(mako_websafe(_("satisfied?")))
                __M_writer(u'\n      ')
                # SOURCE LINE 38
                __M_writer(mako_websafe(pretty_button("yes", "search_feedback", "'y'", "positive")))
                __M_writer(u'\n      ')
                # SOURCE LINE 39
                __M_writer(mako_websafe(pretty_button("no", "search_feedback", "'n'", "negative")))
                __M_writer(u'\n      <div class="thanks red" style="display: none">\n        ')
                # SOURCE LINE 41
                __M_writer(mako_websafe(_("thanks for your feedback!")))
                __M_writer(u'\n      </div>\n    </div>\n')
                pass
            # SOURCE LINE 45
            __M_writer(u'    <div>\n')
            # SOURCE LINE 46
            if thing.converted_data:
                # SOURCE LINE 47
                __M_writer(u'    <p class="debuginfo">\n      <span class="icon">&delta;</span>&nbsp;\n      <span class="content">')
                # SOURCE LINE 49
                __M_writer(mako_websafe(_('converted query to %(syntax)s syntax: %(converted)s') % thing.converted_data))
                __M_writer(u'</span>\n    </p>\n')
                pass
            # SOURCE LINE 52
            __M_writer(u'    </div>\n  </div>\n')
            pass
        # SOURCE LINE 55
        __M_writer(u'\n<div class="searchpane raisedbox">\n  <h4 style="color:gray">')
        # SOURCE LINE 57
        __M_writer(mako_websafe(thing.header))
        __M_writer(u'</h4>\n\n  <div id="previoussearch">\n    ')
        # SOURCE LINE 60
        __M_writer(mako_websafe(SearchForm(prev_search=thing.prev_search,
                 search_params=thing.search_params,
                 site=thing.site, subreddit_search=thing.subreddit_search,
                 simple=thing.simple, restrict_sr=thing.restrict_sr,
                 syntax=thing.syntax)))
        # SOURCE LINE 64
        __M_writer(u'\n  </div>\n</div>\n\n')
        # SOURCE LINE 68
        if thing.facets and len(thing.facets) > 1:
            # SOURCE LINE 69
            __M_writer(u'<div class="searchfacets">\n  <h4 class="title">')
            # SOURCE LINE 70
            __M_writer(mako_websafe(_("too many results? narrow it down to a subreddit!")))
            __M_writer(u'</h4>\n  <ol class="list">\n')
            # SOURCE LINE 72
            for subreddit, count in thing.facets:
                # SOURCE LINE 73
                __M_writer(u'    <li class="searchfacet reddit">\n      <a class="facet title word" href="')
                # SOURCE LINE 74
                __M_writer(mako_websafe(search_url(thing.prev_search, subreddit.name, restrict_sr='on', sort=thing.sort, recent=thing.recent)))
                __M_writer(u'">/r/')
                __M_writer(mako_websafe(subreddit.name))
                __M_writer(u'</a>&nbsp;\n      <span class="facet count number">(')
                # SOURCE LINE 75
                __M_writer(mako_websafe(count))
                __M_writer(u')</span>\n    </li>&nbsp;\n')
                pass
            # SOURCE LINE 78
            __M_writer(u'  </ol>\n</div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


