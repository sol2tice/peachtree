# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402178932.30777
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/redditheader.html'
_template_uri=u'/redditheader.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from pylons import request
from r2.lib.template_helpers import add_sr, header_url
from r2.models import Sub, FakeSubreddit
from r2.models.subreddit import DefaultSR
from r2.lib.pages import SearchForm
from r2.lib import authentication


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 31
    ns = runtime.TemplateNamespace('__anon_0x7f8c8d97e6d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8d97e6d0')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d97e6d0')._populate(_import_ns, [u'plain_link', u'img_link', u'text_with_links', u'separator', u'logout'])
        img_link = _import_ns.get('img_link', context.get('img_link', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        separator = _import_ns.get('separator', context.get('separator', UNDEFINED))
        logout = _import_ns.get('logout', context.get('logout', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n\n<div id="header" role="banner">\n  <a tabindex="1" href="#content" id="jumpToContent">')
        # SOURCE LINE 34
        __M_writer(mako_websafe(_('jump to content')))
        __M_writer(u'</a>\n  ')
        # SOURCE LINE 35
        __M_writer(mako_websafe(thing.srtopbar))
        __M_writer(u'\n  <div id="header-bottom-left">\n    ')
        # SOURCE LINE 37

        header_title = c.site.header_title
        d = DefaultSR()
        if c.site.header and c.can_apply_styles and c.allow_styles:
            header_img = c.site.header
            header_size = c.site.header_size
        else:
            header_img = d.header
            header_size = d.header_size
            header_title = d.header_title
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['header_title','d','header_size','header_img'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 47
        __M_writer(u'\n    \n')
        # SOURCE LINE 49
        if header_img != g.default_header_url:
            # SOURCE LINE 50
            __M_writer(u'        ')
            __M_writer(mako_websafe(img_link(c.site.name, header_url(header_img),
            '/', _id="header-img-a", img_id='header-img',
            title=header_title, size=header_size)))
            # SOURCE LINE 52
            __M_writer(u'\n')
            # SOURCE LINE 53
        else:
            # SOURCE LINE 54
            __M_writer(u'        <a href="/" id="header-img" class="default-header" title="')
            __M_writer(mako_websafe(header_title))
            __M_writer(u'">')
            __M_writer(mako_websafe(g.domain))
            __M_writer(u'</a>\n')
            pass
        # SOURCE LINE 56
        __M_writer(u'    \n')
        # SOURCE LINE 58
        __M_writer(u'    &nbsp;\n\n')
        # SOURCE LINE 60
        for toolbar in thing.toolbars:
            # SOURCE LINE 61
            __M_writer(u'      ')
            __M_writer(mako_websafe(toolbar))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 63
        __M_writer(u'  </div>\n\n  <div id="header-bottom-right">\n')
        # SOURCE LINE 66
        if not c.user_is_loggedin:
            # SOURCE LINE 67
            if thing.enable_login_cover and not g.read_only_mode:
                # SOURCE LINE 68
                __M_writer(u'      <span class="user">\n        ')
                # SOURCE LINE 69

                base = g.https_endpoint if not c.cname else ""
                login_url = add_sr(base + "/login", sr_path=False)
                        
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['base','login_url'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 72
                __M_writer(u'\n        ')
                # SOURCE LINE 73
                __M_writer(mako_websafe(text_with_links(_("want to join? %(login_or_register)s in seconds"),
            login_or_register = dict(link_text=_("login or register"), path=login_url, _class="login-required"))))
                # SOURCE LINE 74
                __M_writer(u'\n      </span>\n      ')
                # SOURCE LINE 76
                __M_writer(mako_websafe(separator("|")))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 78
        else:
            # SOURCE LINE 79
            __M_writer(u'      <span class="user">\n         ')
            # SOURCE LINE 80
            __M_writer(mako_websafe(plain_link(c.user.name, "/user/%s/" % c.user.name, _sr_path=False)))
            __M_writer(u'\n         &nbsp;(<span class="userkarma" title="')
            # SOURCE LINE 81
            __M_writer(mako_websafe(_("link karma")))
            __M_writer(u'">')
            __M_writer(mako_websafe(c.user.safe_karma))
            __M_writer(u'</span>)\n      </span>\n\n      ')
            # SOURCE LINE 84
            __M_writer(mako_websafe(separator("|")))
            __M_writer(u'\n\n      ')
            # SOURCE LINE 86

            if c.have_messages:
              mail_img_class = 'havemail'
              mail_img_title = "new mail!"
              mail_path = "/message/unread/"
            else:
              mail_img_class = 'nohavemail'
              mail_img_title = "no new mail"
              mail_path = "/message/inbox/"
                   
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mail_path','mail_img_title','mail_img_class'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 95
            __M_writer(u'\n      ')
            # SOURCE LINE 96
            __M_writer(mako_websafe(plain_link(_("messages"), path=mail_path,
                 title = mail_img_title, _sr_path = False,
                 _id = "mail", _class=mail_img_class)))
            # SOURCE LINE 98
            __M_writer(u'\n      ')
            # SOURCE LINE 99
            __M_writer(mako_websafe(separator("|")))
            __M_writer(u'\n')
            # SOURCE LINE 100
            if c.user_is_loggedin and c.user.is_moderator_somewhere:
                # SOURCE LINE 101
                __M_writer(u'         ')

                if c.have_mod_messages:
                  mail_img_class = 'havemail'
                  mail_img_title = "new mod mail!"
                  mail_path = "/message/moderator/"
                else:
                  mail_img_class = 'nohavemail'
                  mail_img_title = "no new mod mail"
                  mail_path = "/message/moderator/"
                          
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mail_path','mail_img_title','mail_img_class'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 110
                __M_writer(u'\n         ')
                # SOURCE LINE 111
                __M_writer(mako_websafe(plain_link(_("mod messages"), path=mail_path,
                    title = mail_img_title, _sr_path = False,
                    _id = "modmail", _class=mail_img_class)))
                # SOURCE LINE 113
                __M_writer(u'\n         ')
                # SOURCE LINE 114
                __M_writer(mako_websafe(separator("|")))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 117
        __M_writer(u'    ')
        __M_writer(mako_websafe(thing.corner_buttons()))
        __M_writer(u'\n')
        # SOURCE LINE 118
        if c.user_is_loggedin and authentication.user_can_log_out():
            # SOURCE LINE 119
            __M_writer(u'      ')
            __M_writer(mako_websafe(separator("|")))
            __M_writer(u'\n      ')
            # SOURCE LINE 120
            __M_writer(mako_websafe(logout(dest=request.fullpath)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 122
        __M_writer(u'  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


