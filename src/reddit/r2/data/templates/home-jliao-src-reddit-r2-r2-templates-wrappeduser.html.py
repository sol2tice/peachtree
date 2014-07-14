# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402247635.713875
_template_filename='/home/jliao/src/reddit/r2/r2/templates/wrappeduser.html'
_template_uri='/wrappeduser.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['flair']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f8c8d856310', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8d856310')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d856310')._populate(_import_ns, [u'plain_link'])
        target = _import_ns.get('target', context.get('target', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        context_deleted = _import_ns.get('context_deleted', context.get('context_deleted', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        def flair(user,enabled=None):
            return render_flair(context.locals_(__M_locals),user,enabled)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        if context_deleted and not c.user_is_admin:
            # SOURCE LINE 35
            __M_writer(u'  <span class="author">[deleted]</span>\n')
            # SOURCE LINE 36
        else:
            # SOURCE LINE 37
            if thing.user_deleted:
                # SOURCE LINE 38
                __M_writer(u'    <span class="author">[deleted]</span>\n')
                # SOURCE LINE 39
            elif thing.name == '[blocked]':
                # SOURCE LINE 40
                __M_writer(u'    <span class="author">')
                __M_writer(mako_websafe(_(thing.thing.original_author.name)))
                __M_writer(u'</span>\n')
                # SOURCE LINE 41
            else:
                # SOURCE LINE 42
                if thing.flair_position == 'left':
                    # SOURCE LINE 43
                    __M_writer(u'      ')
                    __M_writer(mako_websafe(flair(thing, enabled=thing.force_show_flair)))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 45
                __M_writer(u'    ')

                classes = [thing.author_cls, 'may-blank', 'id-%s' % thing.fullname]
                if thing.include_flair_selector:
                    classes.append('flairselectable')
                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['classes'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 49
                __M_writer(u'\n    ')
                # SOURCE LINE 50
                __M_writer(mako_websafe(plain_link(thing.name + thing.karma, "/user/%s" % thing.name,
                 _class = ' '.join(classes),
                 _sr_path = False, target=target, title=thing.author_title)))
                # SOURCE LINE 52
                __M_writer(u'\n')
                # SOURCE LINE 53
                if thing.flair_position == 'right':
                    # SOURCE LINE 54
                    __M_writer(u'      ')
                    __M_writer(mako_websafe(flair(thing, enabled=thing.force_show_flair)))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 56
                if thing.include_flair_selector:
                    # SOURCE LINE 57
                    __M_writer(u'      (<a class="flairselectbtn" data-name="')
                    __M_writer(mako_websafe(thing.name))
                    __M_writer(u'" href="javascript://void(0)">')
                    __M_writer(mako_websafe(_('edit')))
                    __M_writer(u'</a>)\n      <div class="flairselector drop-choices"></div>\n')
                    pass
                # SOURCE LINE 60
                __M_writer(u'    <span class="userattrs">\n')
                # SOURCE LINE 61
                if thing.attribs:
                    # SOURCE LINE 62
                    __M_writer(u'      [\n')
                    # SOURCE LINE 63
                    for priority, abbv, css_class, label, attr_link in thing.attribs:
                        # SOURCE LINE 64
                        if attr_link:
                            # SOURCE LINE 65
                            __M_writer(u'          <a class="')
                            __M_writer(mako_websafe(css_class))
                            __M_writer(u'" title="')
                            __M_writer(mako_websafe(label))
                            __M_writer(u'"\n')
                            # SOURCE LINE 66
                            if target:
                                # SOURCE LINE 67
                                __M_writer(u'             target="')
                                __M_writer(mako_websafe(target))
                                __M_writer(u'"\n')
                                pass
                            # SOURCE LINE 69
                            __M_writer(u'             href="')
                            __M_writer(mako_websafe(attr_link))
                            __M_writer(u'">\n            ')
                            # SOURCE LINE 70
                            __M_writer(mako_websafe(unsafe(abbv)))
                            __M_writer(u'\n          </a>\n')
                            # SOURCE LINE 72
                        else:
                            # SOURCE LINE 73
                            __M_writer(u'          <span class="')
                            __M_writer(mako_websafe(css_class))
                            __M_writer(u'" title="')
                            __M_writer(mako_websafe(label))
                            __M_writer(u'">')
                            __M_writer(mako_websafe(abbv))
                            __M_writer(u'</span>\n')
                            pass
                        # SOURCE LINE 76
                        if priority != thing.attribs[-1][0]:
                            # SOURCE LINE 77
                            __M_writer(u'          ,\n')
                            pass
                        pass
                    # SOURCE LINE 80
                    __M_writer(u'      ]\n')
                    pass
                # SOURCE LINE 82
                __M_writer(u'    </span>\n')
                pass
            pass
        # SOURCE LINE 85
        __M_writer(u'\n')
        # SOURCE LINE 86
        if thing.ip_span:
            # SOURCE LINE 87
            __M_writer(u'  ')
            __M_writer(mako_websafe(unsafe(thing.ip_span)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 89
        __M_writer(u'\n')
        # SOURCE LINE 90
        if c.user_is_admin and thing.context_thing:
            # SOURCE LINE 91
            __M_writer(u'  &#32;\n  <a class="adminbox" href="/details/')
            # SOURCE LINE 92
            __M_writer(mako_websafe(thing.context_thing._fullname))
            __M_writer(u'">i</a>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flair(context,user,enabled=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d856310')._populate(_import_ns, [u'plain_link'])
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        if enabled is None:
            # SOURCE LINE 27
            __M_writer(u'    ')
            enabled = user.flair_enabled 
            
            __M_writer(u'\n')
            pass
        # SOURCE LINE 29
        if user.has_flair and enabled:
            # SOURCE LINE 30
            __M_writer(u'    <span class="flair ')
            __M_writer(mako_websafe(user.flair_css_class))
            __M_writer(u'" title="')
            __M_writer(mako_websafe(user.flair_text))
            __M_writer(u'">')
            __M_writer(mako_websafe(user.flair_text))
            __M_writer(u'</span>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


