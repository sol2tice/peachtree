# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402128269.630056
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/linkcommentssettings.html'
_template_uri='/linkcommentssettings.html'
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
    ns = runtime.TemplateNamespace('__anon_0x7fabdc467110', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fabdc467110')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabdc467110')._populate(_import_ns, [u'ynbutton'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        if thing.is_author:
            # SOURCE LINE 26
            if thing.sendreplies:
                # SOURCE LINE 27
                __M_writer(u'    ')
                __M_writer(mako_websafe(ynbutton(_("disable inbox replies"), _("inbox replies disabled"), "sendreplies",
      hidden_data=dict(id=thing.link._fullname, state=False))))
                # SOURCE LINE 28
                __M_writer(u'\n')
                # SOURCE LINE 29
            else:
                # SOURCE LINE 30
                __M_writer(u'    ')
                __M_writer(mako_websafe(ynbutton(_("enable inbox replies"), _("inbox replies enabled"), "sendreplies",
      hidden_data=dict(id=thing.link._fullname, state=True))))
                # SOURCE LINE 31
                __M_writer(u'\n')
                pass
            # SOURCE LINE 33
            __M_writer(u'  &nbsp;<span class="help-hoverable" title="')
            __M_writer(mako_websafe(_('inbox replies will send you a message when this link receives a new top-level comment')))
            __M_writer(u'">(?)</span>\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'\n')
        # SOURCE LINE 36
        if thing.can_edit:
            # SOURCE LINE 37
            if thing.contest_mode:
                # SOURCE LINE 38
                __M_writer(u'    ')
                __M_writer(mako_websafe(ynbutton(_("disable contest mode"), _("contest mode disabled"), "set_contest_mode",
      hidden_data=dict(id=thing.link._fullname, state=False))))
                # SOURCE LINE 39
                __M_writer(u'\n')
                # SOURCE LINE 40
            else:
                # SOURCE LINE 41
                __M_writer(u'    ')
                __M_writer(mako_websafe(ynbutton(_("enable contest mode"), _("contest mode enabled"), "set_contest_mode",
      hidden_data=dict(id=thing.link._fullname, state=True))))
                # SOURCE LINE 42
                __M_writer(u'\n')
                pass
            # SOURCE LINE 44
        elif thing.contest_mode:
            # SOURCE LINE 45
            __M_writer(u'  <span>')
            __M_writer(mako_websafe(_("contest mode: scores hidden")))
            __M_writer(u'</span>\n')
            pass
        # SOURCE LINE 47
        __M_writer(u'\n')
        # SOURCE LINE 48
        if thing.can_edit or thing.contest_mode:
            # SOURCE LINE 49
            __M_writer(u'  &nbsp;<span class="help-hoverable" title="')
            __M_writer(mako_websafe(_('contest mode randomizes comment sorting, hides scores, and collapses replies by default.')))
            __M_writer(u'">(?)</span>\n')
            pass
        # SOURCE LINE 51
        __M_writer(u'\n')
        # SOURCE LINE 52
        if thing.can_edit and thing.link.is_self:
            # SOURCE LINE 53
            if thing.stickied:
                # SOURCE LINE 54
                __M_writer(u'    ')
                __M_writer(mako_websafe(ynbutton(_("unsticky this post"), _("unstickied"), "set_subreddit_sticky",
      hidden_data=dict(id=thing.link._fullname, state=False))))
                # SOURCE LINE 55
                __M_writer(u'\n')
                # SOURCE LINE 56
            else:
                # SOURCE LINE 57
                __M_writer(u'    ')
                __M_writer(mako_websafe(ynbutton(_("sticky this post"), _("stickied"), "set_subreddit_sticky",
      question=_("sticky this? (any existing sticky will be replaced)"),
      hidden_data=dict(id=thing.link._fullname, state=True))))
                # SOURCE LINE 59
                __M_writer(u'\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


