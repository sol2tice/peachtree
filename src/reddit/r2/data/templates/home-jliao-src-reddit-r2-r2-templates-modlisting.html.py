# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402904141.470633
_template_filename='/home/jliao/src/reddit/r2/r2/templates/modlisting.html'
_template_uri='/modlisting.html'
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
    # SOURCE LINE 25
    ns = runtime.TemplateNamespace('__anon_0x7f99a8220950', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f99a8220950')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f99b1e856d0', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f99b1e856d0')] = ns

    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7f99b1e85d90', context._clean_inheritance_tokens(), templateuri=u'userlisting.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f99b1e85d90')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f99a8220950')._populate(_import_ns, [u'error_field'])
        _mako_get_namespace(context, '__anon_0x7f99b1e856d0')._populate(_import_ns, [u'ynbutton'])
        _mako_get_namespace(context, '__anon_0x7f99b1e85d90')._populate(_import_ns, [u'add_form', u'listing'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        add_form = _import_ns.get('add_form', context.get('add_form', UNDEFINED))
        listing = _import_ns.get('listing', context.get('listing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n<div class="')
        # SOURCE LINE 27
        __M_writer(mako_websafe(thing._class))
        __M_writer(u' usertable">\n')
        # SOURCE LINE 28
        if thing.can_remove_self:
            # SOURCE LINE 29
            __M_writer(u'      ')
            __M_writer(mako_websafe(ynbutton(op='unfriend',
                 title=_("leave"),
                 executed=_("you are no longer a moderator"),
                 question=_("stop being a moderator?"),
                 format=_('you are a moderator of this subreddit. %(action)s'),
                 format_arg='action',
                 _class=thing.type + ' remove-self',
                 hidden_data=dict(
                   id=c.user._fullname,
                   type=thing.type,
                   container=thing.container_name))))
            # SOURCE LINE 39
            __M_writer(u'\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'\n')
        # SOURCE LINE 42
        if thing.has_invite:
            # SOURCE LINE 43
            __M_writer(u'    ')
            __M_writer(mako_websafe(ynbutton(op='accept_moderator_invite',
               title=_("accept"),
               executed=_("you are now a moderator. welcome to the team!"),
               question=_("become a moderator of %s?" % ("/r/" + c.site.name)),
               format=_('you are invited to become a moderator. %(action)s'),
               format_arg='action',
               _class=thing.type + ' accept-invite')))
            # SOURCE LINE 49
            __M_writer(u'\n')
            pass
        # SOURCE LINE 51
        __M_writer(u'\n')
        # SOURCE LINE 52
        if thing.addable and thing.has_add_form:
            # SOURCE LINE 53
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                    __M_writer = context.writer()
                    __M_writer(u'\n      ')
                    # SOURCE LINE 54
                    __M_writer(mako_websafe(error_field("ALREADY_MODERATOR", "name")))
                    __M_writer(u'\n      ')
                    # SOURCE LINE 55
                    __M_writer(mako_websafe(error_field("BANNED_FROM_SUBREDDIT", "name")))
                    __M_writer(u'\n    ')
                    return ''
                return [body]
            __M_caller = context.caller_stack._get_caller()
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                # SOURCE LINE 53
                __M_writer(mako_websafe(add_form(thing.form_title, thing.destination, thing.type, thing.container_name, verb=_('add'))))
            finally:
                context.caller_stack.nextcaller = None
            # SOURCE LINE 56
            __M_writer(u'\n')
            pass
        # SOURCE LINE 58
        __M_writer(u'  ')
        __M_writer(mako_websafe(listing()))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


