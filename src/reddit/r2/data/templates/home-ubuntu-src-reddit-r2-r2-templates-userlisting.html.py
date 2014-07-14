# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401922963.751033
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/userlisting.html'
_template_uri='/userlisting.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['add_form', 'listing']


# SOURCE LINE 23

from r2.models import Sub
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 26
    ns = runtime.TemplateNamespace('__anon_0x7f1dd5ff2a90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd5ff2a90')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5ff2a90')._populate(_import_ns, [u'error_field', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        def add_form(title,dest,add_type,container_name,verb=None,permissions_form=None):
            return render_add_form(context.locals_(__M_locals),title,dest,add_type,container_name,verb,permissions_form)
        def listing():
            return render_listing(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n')
        # SOURCE LINE 108
        __M_writer(u'\n\n<div class="')
        # SOURCE LINE 110
        __M_writer(mako_websafe(thing._class))
        __M_writer(u' usertable">\n')
        # SOURCE LINE 111
        if thing.addable and thing.has_add_form:
            # SOURCE LINE 112
            __M_writer(u'    ')
            __M_writer(mako_websafe(add_form(thing.form_title, thing.destination, thing.type, thing.container_name, permissions_form=thing.permissions_form)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 114
        __M_writer(u'\n')
        # SOURCE LINE 115
        if thing.show_jump_to:
            # SOURCE LINE 116
            __M_writer(u'    <h1>')
            __M_writer(mako_websafe(_('jump to')))
            __M_writer(u'</h1>\n    <form class="pretty-form medium-text">\n        <label for="user">')
            # SOURCE LINE 118
            __M_writer(mako_websafe(_('username')))
            __M_writer(u'&nbsp;</label>\n        <input type="text" id="user" name="user"\n')
            # SOURCE LINE 120
            if thing.jump_to_value:
                # SOURCE LINE 121
                __M_writer(u'            value="')
                __M_writer(mako_websafe(thing.jump_to_value))
                __M_writer(u'"\n')
                pass
            # SOURCE LINE 123
            __M_writer(u'        >\n        <button type="submit">')
            # SOURCE LINE 124
            __M_writer(mako_websafe(_('go')))
            __M_writer(u'</button>\n    </form>\n')
            pass
        # SOURCE LINE 127
        __M_writer(u'\n')
        # SOURCE LINE 128
        __M_writer(mako_websafe(listing()))
        __M_writer(u'\n\n')
        # SOURCE LINE 130
        if thing.jump_to_value:
            # SOURCE LINE 131
            __M_writer(u'    <p class="nextprev">\n        ')
            # SOURCE LINE 132
            __M_writer(mako_websafe(plain_link(_("show all"), request.path, rel="nofollow")))
            __M_writer(u'\n    </p>\n')
            pass
        # SOURCE LINE 135
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_add_form(context,title,dest,add_type,container_name,verb=None,permissions_form=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5ff2a90')._populate(_import_ns, [u'error_field', u'plain_link'])
        caller = _import_ns.get('caller', context.get('caller', UNDEFINED))
        error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n  <form action="/post/')
        # SOURCE LINE 29
        __M_writer(mako_websafe(dest))
        __M_writer(u'"\n        method="post" class="pretty-form medium-text friend-add"\n        onsubmit="return post_form(this, \'')
        # SOURCE LINE 31
        __M_writer(mako_websafe(dest))
        __M_writer(u'\')"\n        id="')
        # SOURCE LINE 32
        __M_writer(mako_websafe(add_type))
        __M_writer(u'">\n    <h1>')
        # SOURCE LINE 33
        __M_writer(mako_websafe(title))
        __M_writer(u'</h1>\n\n    <input type="hidden" name="action" value="add">\n    <input type="hidden" name="container" value="')
        # SOURCE LINE 36
        __M_writer(mako_websafe(container_name))
        __M_writer(u'">\n    <input type="hidden" name="type" value="')
        # SOURCE LINE 37
        __M_writer(mako_websafe(add_type))
        __M_writer(u'">\n')
        # SOURCE LINE 38
        if add_type in ("banned", "wikibanned"):
            # SOURCE LINE 39
            __M_writer(u'        <label for="name">')
            __M_writer(mako_websafe(_('who to ban?')))
            __M_writer(u' &nbsp;</label>\n        <input type="text" onfocus="$(this).parent(\'form\').addClass(\'edited\')" class="friend-name" name="name" id="name">\n        <span class="ban-reason">\n            <label for="note">')
            # SOURCE LINE 42
            __M_writer(mako_websafe(_('why the ban?')))
            __M_writer(u'</label>\n            <input type="text" maxlength="300" name="note" id="note">\n            <span>')
            # SOURCE LINE 44
            __M_writer(mako_websafe(_('(will not be visible to user)')))
            __M_writer(u'</span>\n        </span>\n')
            # SOURCE LINE 46
        else:
            # SOURCE LINE 47
            __M_writer(u'        <input type="text" name="name" id="name">\n')
            pass
        # SOURCE LINE 49
        if permissions_form:
            # SOURCE LINE 50
            __M_writer(u'      ')
            __M_writer(mako_websafe(permissions_form))
            __M_writer(u'\n      &#32;\n      <span class="permissions-edit">\n        (<a href="javascript:void(0)">')
            # SOURCE LINE 53
            __M_writer(mako_websafe(_('change')))
            __M_writer(u'</a>)\n      </span>\n')
            pass
        # SOURCE LINE 56
        __M_writer(u'    <button class="btn" type="submit">')
        __M_writer(mako_websafe(verb or _("add")))
        __M_writer(u'</button>\n    <span class="status"></span>\n    ')
        # SOURCE LINE 58
        __M_writer(mako_websafe(error_field("USER_DOESNT_EXIST", "name")))
        __M_writer(u'\n    ')
        # SOURCE LINE 59
        __M_writer(mako_websafe(error_field("ALREADY_MODERATOR", "name")))
        __M_writer(u'\n    ')
        # SOURCE LINE 60
        __M_writer(mako_websafe(error_field("BANNED_FROM_SUBREDDIT", "name")))
        __M_writer(u'\n')
        # SOURCE LINE 61
        if caller:
            # SOURCE LINE 62
            __M_writer(u'      ')
            __M_writer(mako_websafe(caller.body()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 64
        __M_writer(u'  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_listing(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5ff2a90')._populate(_import_ns, [u'error_field', u'plain_link'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 67
        __M_writer(u'\n  <div class="')
        # SOURCE LINE 68
        __M_writer(mako_websafe(thing.type))
        __M_writer(u'-table"\n    style="')
        # SOURCE LINE 69
        __M_writer(mako_websafe('display:none' if not thing.things and not thing.show_not_found else ''))
        __M_writer(u'">\n    <h1>\n      ')
        # SOURCE LINE 71
        __M_writer(mako_websafe(thing.title))
        __M_writer(u'\n    </h1>\n\n    <table>\n')
        # SOURCE LINE 75
        if thing.headers:
            # SOURCE LINE 76
            __M_writer(u'        <tr>\n')
            # SOURCE LINE 77
            for header in thing.headers:
                # SOURCE LINE 78
                __M_writer(u'            <th>')
                __M_writer(mako_websafe(header))
                __M_writer(u'</th>\n')
                pass
            # SOURCE LINE 80
            __M_writer(u'        </tr>\n')
            pass
        # SOURCE LINE 82
        if thing.things:
            # SOURCE LINE 83
            for item in thing.things:
                # SOURCE LINE 84
                __M_writer(u'                ')
                __M_writer(mako_websafe(item))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 86
        else:
            # SOURCE LINE 87
            __M_writer(u'        <tr class="notfound"><td>')
            __M_writer(mako_websafe(_('No items found') if thing.show_not_found else ''))
            __M_writer(u'</td></tr>\n')
            pass
        # SOURCE LINE 89
        __M_writer(u'    </table>\n  </div>\n\n')
        # SOURCE LINE 92
        if thing.nextprev and (thing.prev or thing.next):
            # SOURCE LINE 93
            __M_writer(u'  <p class="nextprev"> ')
            __M_writer(mako_websafe(_("view more:")))
            __M_writer(u'&#32;\n')
            # SOURCE LINE 94
            if thing.prev:
                # SOURCE LINE 95
                __M_writer(u'    ')
                __M_writer(mako_websafe(plain_link(_("first"), thing.first, _sr_path = (c.site != Sub), rel="nofollow first")))
                __M_writer(u' \n    <span class="separator"></span>\n    ')
                # SOURCE LINE 97
                __M_writer(mako_websafe(plain_link(unsafe("&lsaquo; " + _("prev")), thing.prev, _sr_path = (c.site != Sub), rel="nofollow prev")))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 99
            if thing.prev and thing.next:
                # SOURCE LINE 100
                __M_writer(u'    <span class="separator"></span>\n')
                pass
            # SOURCE LINE 102
            if thing.next:
                # SOURCE LINE 103
                __M_writer(u'  ')
                __M_writer(mako_websafe(plain_link(unsafe(_("next") + " &rsaquo;"), thing.next,  _sr_path = (c.site != Sub), rel="nofollow next")))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 105
            __M_writer(u'  </p>\n')
            pass
        # SOURCE LINE 107
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


