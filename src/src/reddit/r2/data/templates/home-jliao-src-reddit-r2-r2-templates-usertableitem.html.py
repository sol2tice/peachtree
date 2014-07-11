# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402904141.50559
_template_filename='/home/jliao/src/reddit/r2/r2/templates/usertableitem.html'
_template_uri='/usertableitem.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['cell_type']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 24
    ns = runtime.TemplateNamespace('__anon_0x7f99b20d4e10', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f99b20d4e10')] = ns

    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f99b20d4850', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f99b20d4850')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f99b20d4e10')._populate(_import_ns, [u'plain_link', u'timestamp'])
        _mako_get_namespace(context, '__anon_0x7f99b20d4850')._populate(_import_ns, [u'ynbutton'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def cell_type():
            return render_cell_type(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n<tr>\n')
        # SOURCE LINE 27
        for cell in thing.cells:
            # SOURCE LINE 28
            __M_writer(u'    <td>\n      ')
            # SOURCE LINE 29

            thing.name = cell
                   
            
            # SOURCE LINE 31
            __M_writer(u'\n      ')
            # SOURCE LINE 32
            __M_writer(mako_websafe(cell_type()))
            __M_writer(u'\n    </td>\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'</tr>\n\n')
        # SOURCE LINE 83
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_cell_type(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f99b20d4e10')._populate(_import_ns, [u'plain_link', u'timestamp'])
        _mako_get_namespace(context, '__anon_0x7f99b20d4850')._populate(_import_ns, [u'ynbutton'])
        timestamp = _import_ns.get('timestamp', context.get('timestamp', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n')
        # SOURCE LINE 38
        if thing.name == "user":
            # SOURCE LINE 39
            __M_writer(u'      <span class="user">\n         ')
            # SOURCE LINE 40
            __M_writer(mako_websafe(plain_link(thing.user.name, "/user/%s/" % thing.user.name,
                      _sr_path=False)))
            # SOURCE LINE 41
            __M_writer(u'\n         &nbsp;(<b>')
            # SOURCE LINE 42
            __M_writer(mako_websafe(thing.user.safe_karma))
            __M_writer(u'</b>)\n      </span>\n      &nbsp;\n')
            # SOURCE LINE 45
        elif c.user_is_loggedin and thing.name == "sendmessage" and c.user != thing.user:
            # SOURCE LINE 46
            __M_writer(u'    ')
            __M_writer(mako_websafe(plain_link(_("send message"),
                 "/message/compose?to=%s" % (thing.user.name))))
            # SOURCE LINE 47
            __M_writer(u'\n      &nbsp;\n')
            # SOURCE LINE 49
        elif thing.name == "remove":
            # SOURCE LINE 50
            if thing.editable:
                # SOURCE LINE 51
                __M_writer(u'      ')
                __M_writer(mako_websafe(ynbutton(_("remove"), "removed", thing.remove_action,
                 callback="deleteRow",
                 hidden_data = dict(type = thing.type,
                                    id = thing.user._fullname,
                                    container = thing.container_name))))
                # SOURCE LINE 55
                __M_writer(u'\n')
                # SOURCE LINE 56
            else:
                # SOURCE LINE 57
                if c.user != thing.user:
                    # SOURCE LINE 58
                    __M_writer(u'        <span class="gray">')
                    __M_writer(mako_websafe(_("can't remove")))
                    __M_writer(u'</span>\n')
                    pass
                pass
            # SOURCE LINE 61
        elif thing.name == "note":
            # SOURCE LINE 62
            __M_writer(u'    <form action="/post/')
            __M_writer(mako_websafe(thing.type))
            __M_writer(u'note" id="')
            __M_writer(mako_websafe(thing.type))
            __M_writer(u'note-')
            __M_writer(mako_websafe(thing.rel._fullname))
            __M_writer(u'"\n          method="post" class="pretty-form medium-text rel-note ')
            # SOURCE LINE 63
            __M_writer(mako_websafe(thing.type))
            __M_writer(u'-note"\n          onsubmit="return post_form(this, \'')
            # SOURCE LINE 64
            __M_writer(mako_websafe(thing.type))
            __M_writer(u'note\');">\n      <input type="hidden" name="name" value="')
            # SOURCE LINE 65
            __M_writer(mako_websafe(thing.user.name))
            __M_writer(u'" />\n      <input type="text" maxlength="300" name="note" class="tiny"\n             onfocus="$(this).parent().addClass(\'edited\')"\n             value="')
            # SOURCE LINE 68
            __M_writer(mako_websafe(getattr(thing.rel, 'note', '')))
            __M_writer(u'" />\n      <button onclick="$(this).parent().removeClass(\'edited\')" type="submit">submit</button>\n      <span class="status"></span>\n    </form>\n')
            # SOURCE LINE 72
        elif thing.name == "age":
            # SOURCE LINE 73
            __M_writer(u'      ')
            __M_writer(mako_websafe(timestamp(thing.rel._date, include_tense=True)))
            __M_writer(u'\n')
            # SOURCE LINE 74
        elif thing.name == "permissions":
            # SOURCE LINE 75
            __M_writer(u'      ')
            __M_writer(mako_websafe(thing.permissions))
            __M_writer(u'\n')
            # SOURCE LINE 76
        elif thing.name == "permissionsctl":
            # SOURCE LINE 77
            if thing.editable:
                # SOURCE LINE 78
                __M_writer(u'      <span class="permissions-edit">\n        (<a href="javascript:void(0)">')
                # SOURCE LINE 79
                __M_writer(mako_websafe(_('change')))
                __M_writer(u'</a>)\n      </span>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


