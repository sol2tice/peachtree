# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402411028.548388
_template_filename='/home/jliao/src/reddit/r2/r2/templates/subscriptionbox.html'
_template_uri='/subscriptionbox.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7f30c4076250', context._clean_inheritance_tokens(), templateuri=u'subreddit.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f30c4076250')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f30c4076550', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f30c4076550')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f30c4076250')._populate(_import_ns, [u'permission_icons'])
        _mako_get_namespace(context, '__anon_0x7f30c4076550')._populate(_import_ns, [u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        permission_icons = _import_ns.get('permission_icons', context.get('permission_icons', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 26

        from r2.models import MultiReddit
        from r2.lib.pages import SubscribeButton
        is_multi = isinstance(c.site, MultiReddit)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['SubscribeButton','MultiReddit','is_multi'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 30
        __M_writer(u'\n\n<div class="subscription-box">\n')
        # SOURCE LINE 33
        if thing.prelink or thing.goldlink:
            # SOURCE LINE 34
            __M_writer(u'  <div class="box-top">\n')
            # SOURCE LINE 35
            if thing.prelink:
                # SOURCE LINE 36
                __M_writer(u'    <span class="column centered">\n      <a href="')
                # SOURCE LINE 37
                __M_writer(mako_websafe(thing.prelink[0]))
                __M_writer(u'">')
                __M_writer(mako_websafe(thing.prelink[1]))
                __M_writer(u'</a>\n    </span>\n')
                pass
            # SOURCE LINE 40
            if thing.goldlink:
                # SOURCE LINE 41
                __M_writer(u'    <span class="giftgold column">\n    <a href="')
                # SOURCE LINE 42
                __M_writer(mako_websafe(thing.goldlink))
                __M_writer(u'">\n      ')
                # SOURCE LINE 43
                __M_writer(mako_websafe(thing.goldmsg))
                __M_writer(u'\n    </a>\n    </span>\n')
                pass
            # SOURCE LINE 47
            __M_writer(u'  </div>\n')
            pass
        # SOURCE LINE 49
        __M_writer(u'  <div class="clear">\n')
        # SOURCE LINE 50
        if thing.prelink or thing.goldlink:
            # SOURCE LINE 51
            __M_writer(u'    <div class="box-separator"></div>\n')
            pass
        # SOURCE LINE 53
        __M_writer(u'    <ul>\n')
        # SOURCE LINE 54
        if thing.multi_path and thing.multi_text:
            # SOURCE LINE 55
            __M_writer(u'      ')
            __M_writer(mako_websafe(plain_link(thing.multi_text, thing.multi_path, _class="title")))
            __M_writer(u'\n      <div class="box-separator"></div>\n')
            pass
        # SOURCE LINE 58
        for sr in thing.reddits:
            # SOURCE LINE 59
            __M_writer(u'      ')
            is_spam = hasattr(sr, "_spam") and sr._spam 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_spam'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n      <li>\n')
            # SOURCE LINE 61
            if is_multi and is_spam:
                # SOURCE LINE 62
                __M_writer(u'          <span class="fancy-toggle-button">\n            <span class="active banned">')
                # SOURCE LINE 63
                __M_writer(mako_websafe(_("banned")))
                __M_writer(u'</span>\n          </span>\n          <span class="title banned">')
                # SOURCE LINE 65
                __M_writer(mako_websafe(sr.name))
                __M_writer(u'</span>\n')
                # SOURCE LINE 66
            elif is_spam:
                # SOURCE LINE 67
                __M_writer(u'          ')
                __M_writer(mako_websafe(SubscribeButton(sr)))
                __M_writer(u'\n          <span class="title banned">')
                # SOURCE LINE 68
                __M_writer(mako_websafe(sr.name))
                __M_writer(u'</span>\n')
                # SOURCE LINE 69
            else:
                # SOURCE LINE 70
                __M_writer(u'          ')
                __M_writer(mako_websafe(SubscribeButton(sr)))
                __M_writer(u'\n          ')
                # SOURCE LINE 71
                __M_writer(mako_websafe(plain_link(sr.name, sr.path, _class="title")))
                __M_writer(u'\n          ')
                # SOURCE LINE 72
                __M_writer(mako_websafe(permission_icons(sr)))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 74
            __M_writer(u'      </li>\n')
            pass
        # SOURCE LINE 76
        __M_writer(u'    </ul>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


