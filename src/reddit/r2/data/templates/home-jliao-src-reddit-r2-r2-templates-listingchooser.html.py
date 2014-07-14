# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402179366.450094
_template_filename='/home/jliao/src/reddit/r2/r2/templates/listingchooser.html'
_template_uri='/listingchooser.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['section_items']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f8c8daa3d90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8daa3d90')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daa3d90')._populate(_import_ns, [u'classes'])
        def section_items(itemlist):
            return render_section_items(context.locals_(__M_locals),itemlist)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n<div class="listing-chooser">\n  <div class="grippy"></div>\n  <div class="contents">\n    <ul class="global">\n      ')
        # SOURCE LINE 42
        __M_writer(mako_websafe(section_items(thing.sections['global'])))
        __M_writer(u'\n    </ul>\n\n    <h3>')
        # SOURCE LINE 45
        __M_writer(mako_websafe(_('multireddits')))
        __M_writer(u'</h3>\n')
        # SOURCE LINE 46
        if thing.show_samples:
            # SOURCE LINE 47
            __M_writer(u'      <div class="intro">\n        <p>')
            # SOURCE LINE 48
            __M_writer(mako_websafe(_('new! create sets of subreddits to view together.')))
            __M_writer(u'</p>\n        <p>')
            # SOURCE LINE 49
            __M_writer(mako_websafe(_('for starters, try one of these:')))
            __M_writer(u'</p>\n        <ul class="multis">\n          ')
            # SOURCE LINE 51
            __M_writer(mako_websafe(section_items(thing.sections['sample'])))
            __M_writer(u'\n        </ul>\n        <p>')
            # SOURCE LINE 53
            __M_writer(mako_websafe(_('to hide these samples, create a multi of your own:')))
            __M_writer(u'</p>\n      </div>\n')
            pass
        # SOURCE LINE 56
        __M_writer(u'    <ul class="multis">\n      ')
        # SOURCE LINE 57
        __M_writer(mako_websafe(section_items(thing.sections['multi'])))
        __M_writer(u'\n      <li class="create">\n        <form>\n          <input type="text" class="multi-name" placeholder="')
        # SOURCE LINE 60
        __M_writer(mako_websafe(_('name')))
        __M_writer(u'"></input>\n          <div class="error"></div>\n          <button>')
        # SOURCE LINE 62
        __M_writer(mako_websafe(_('create')))
        __M_writer(u'</button><div class="throbber"></div>\n        </form>\n      </li>\n    </ul>\n\n    <ul class="other">\n      ')
        # SOURCE LINE 68
        __M_writer(mako_websafe(section_items(thing.sections['other'])))
        __M_writer(u'\n    </ul>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_section_items(context,itemlist):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8daa3d90')._populate(_import_ns, [u'classes'])
        classes = _import_ns.get('classes', context.get('classes', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        for item in itemlist:
            # SOURCE LINE 27
            __M_writer(u'    <li ')
            __M_writer(mako_websafe(classes(item['extra_class'], 'selected' if item['selected'] else None)))
            __M_writer(u'>\n      <a href="')
            # SOURCE LINE 28
            __M_writer(mako_websafe(item['path']))
            __M_writer(u'">\n        ')
            # SOURCE LINE 29
            __M_writer(mako_websafe(item['name']))
            __M_writer(u'\n')
            # SOURCE LINE 30
            if 'description' in item:
                # SOURCE LINE 31
                __M_writer(u'          <br><span class="description">')
                __M_writer(mako_websafe(item['description']))
                __M_writer(u'</span>\n')
                pass
            # SOURCE LINE 33
            __M_writer(u'      </a>\n    </li>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


