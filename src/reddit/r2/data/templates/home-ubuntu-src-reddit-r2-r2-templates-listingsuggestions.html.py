# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919915.945608
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/listingsuggestions.html'
_template_uri='/listingsuggestions.html'
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
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f1dc0164390', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dc0164390')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dc0164390')._populate(_import_ns, [u'text_with_links'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        if thing.suggestion_type:
            # SOURCE LINE 26
            __M_writer(u'\n<span class="next-suggestions">\n')
            # SOURCE LINE 28
            if thing.suggestion_type == 'explore':
                # SOURCE LINE 29
                __M_writer(u'  ')
                __M_writer(mako_websafe(_('or')))
                __M_writer(u'\n  <a href="/explore">')
                # SOURCE LINE 30
                __M_writer(mako_websafe(_('explore some new subreddits')))
                __M_writer(u'</a>\n')
                # SOURCE LINE 31
            elif thing.suggestion_type == 'multis':
                # SOURCE LINE 32
                __M_writer(u'  ')
                __M_writer(mako_websafe(_('or try a multi:')))
                __M_writer(u'\n')
                # SOURCE LINE 33
                for multi in thing.suggestions:
                    # SOURCE LINE 34
                    __M_writer(u'      <a href="')
                    __M_writer(mako_websafe(multi.path))
                    __M_writer(u'">/m/')
                    __M_writer(mako_websafe(multi.name))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 36
            elif thing.suggestion_type == 'random':
                # SOURCE LINE 37
                __M_writer(u'  ')
                __M_writer(mako_websafe(text_with_links(
    _('or try a %(random_subreddit)s'),
    random_subreddit=dict(link_text=_("random subreddit"), path="/r/random")
  )))
                # SOURCE LINE 40
                __M_writer(u'\n')
                pass
            # SOURCE LINE 42
            __M_writer(u'</span>\n\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


