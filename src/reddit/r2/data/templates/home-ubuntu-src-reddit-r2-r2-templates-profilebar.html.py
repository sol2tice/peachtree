# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401919418.721501
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/profilebar.html'
_template_uri='/profilebar.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23
 
from r2.lib.filters import unsafe, safemarkdown
from r2.lib.template_helpers import static, format_number
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 28
    ns = runtime.TemplateNamespace('__anon_0x4794a50', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x4794a50')] = ns

    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x4794110', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x4794110')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x4794a50')._populate(_import_ns, [u'toggle_button'])
        _mako_get_namespace(context, '__anon_0x4794110')._populate(_import_ns, [u'submit_form', u'plain_link', u'thing_timestamp'])
        toggle_button = _import_ns.get('toggle_button', context.get('toggle_button', UNDEFINED))
        thing_timestamp = _import_ns.get('thing_timestamp', context.get('thing_timestamp', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n<div class="titlebox">\n  <h1>\n    ')
        # SOURCE LINE 32
        __M_writer(mako_websafe(thing.user.name))
        __M_writer(u'\n\n')
        # SOURCE LINE 34
        if c.user_is_admin:
            # SOURCE LINE 35
            __M_writer(u'      <span class="account-notes">\n        #')
            # SOURCE LINE 36
            __M_writer(mako_websafe(thing.user._id))
            __M_writer(u'\n\n')
            # SOURCE LINE 38
            if thing.user._deleted:
                # SOURCE LINE 39
                __M_writer(u'          <span class="unusual">(deleted)</span>\n')
                pass
            # SOURCE LINE 41
            __M_writer(u'\n')
            # SOURCE LINE 42
            if thing.user._spam:
                # SOURCE LINE 43
                __M_writer(u'          <span class="unusual">(banned)</span>\n')
                pass
            # SOURCE LINE 45
            __M_writer(u'      </span>\n')
            pass
        # SOURCE LINE 47
        __M_writer(u'\n  </h1>\n\n')
        # SOURCE LINE 50
        if c.user != thing.user:
            # SOURCE LINE 51
            __M_writer(u'    <div>\n    ')
            # SOURCE LINE 52
            __M_writer(mako_websafe(toggle_button("fancy-toggle-button", _("+ friends"), _("- friends"),
         "friend('%s', '%s', 'friend')" % (thing.user.name, thing.my_fullname),
         "unfriend('%s', '%s', 'friend')" % (thing.user.name, thing.my_fullname),
         css_class = "add", alt_css_class = "remove",
         reverse = thing.is_friend, login_required=True)))
            # SOURCE LINE 56
            __M_writer(u'\n    </div>\n')
            pass
        # SOURCE LINE 59
        __M_writer(u'\n  <span class="karma">')
        # SOURCE LINE 60
        __M_writer(mako_websafe(format_number(thing.user.safe_karma)))
        __M_writer(u'</span>\n  &#32;\n  ')
        # SOURCE LINE 62
        __M_writer(mako_websafe(_("link karma")))
        __M_writer(u'\n\n  <br/>\n  <span class="karma comment-karma">')
        # SOURCE LINE 65
        __M_writer(mako_websafe(format_number(thing.user.comment_karma)))
        __M_writer(u'</span>\n  &#32;\n  ')
        # SOURCE LINE 67
        __M_writer(mako_websafe(_("comment karma")))
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        if c.user_is_admin or c.user == thing.user:
            # SOURCE LINE 70
            __M_writer(u'    <table id="per-sr-karma"\n')
            # SOURCE LINE 71
            if not c.user_is_admin:
                # SOURCE LINE 72
                __M_writer(u'      class="more-karmas"\n')
                pass
            # SOURCE LINE 74
            __M_writer(u'      >\n     <thead>\n        <tr>\n          <th id="sr-karma-header">subreddit</th>\n          <th>link</th>\n          <th>comment</th>\n        </tr>\n     </thead>\n     ')
            # SOURCE LINE 82

            karmas = thing.user.all_karmas()
                 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['karmas'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 84
            __M_writer(u'\n     <tbody>\n')
            # SOURCE LINE 86
            for i, (label, title, lc, cc) in enumerate(karmas):
                # SOURCE LINE 87
                __M_writer(u'        <tr\n')
                # SOURCE LINE 88
                if c.user_is_admin and i >= 5:
                    # SOURCE LINE 89
                    __M_writer(u'          class="more-karmas"\n')
                    pass
                # SOURCE LINE 91
                __M_writer(u'        >\n')
                # SOURCE LINE 92
                if title:
                    # SOURCE LINE 93
                    __M_writer(u'          <th class="helpful" title="')
                    __M_writer(mako_websafe(title))
                    __M_writer(u'"><span>')
                    __M_writer(mako_websafe(label))
                    __M_writer(u'</span></th>\n')
                    # SOURCE LINE 94
                else:
                    # SOURCE LINE 95
                    __M_writer(u'          <th>')
                    __M_writer(mako_websafe(label))
                    __M_writer(u'</th>\n')
                    pass
                # SOURCE LINE 97
                __M_writer(u'          <td>')
                __M_writer(mako_websafe(lc))
                __M_writer(u'</td>\n          <td>')
                # SOURCE LINE 98
                __M_writer(mako_websafe(cc))
                __M_writer(u'</td>\n        </tr>\n')
                pass
            # SOURCE LINE 101
            __M_writer(u'      </tbody>\n    </table>\n')
            # SOURCE LINE 103
            if not c.user_is_admin or len(karmas) > 5:
                # SOURCE LINE 104
                __M_writer(u'    <div class="karma-breakdown">\n      <a href="javascript:void(0)"\n         onclick="$(\'.more-karmas\').show();$(this).hide();return false">\n         show karma breakdown by subreddit\n      </a>\n    </div>\n')
                pass
            pass
        # SOURCE LINE 112
        __M_writer(u'\n')
        # SOURCE LINE 113
        if thing.gold_remaining or thing.gold_creddit_message:
            # SOURCE LINE 114
            __M_writer(u'    <div class="rounded gold-accent gold-expiration-info">\n')
            # SOURCE LINE 115
            if thing.gold_remaining:
                # SOURCE LINE 116
                __M_writer(u'        <div class="gold-remaining"\n')
                # SOURCE LINE 117
                if thing.gold_expiration:
                    # SOURCE LINE 118
                    __M_writer(u'               title="')
                    __M_writer(mako_websafe(thing.gold_expiration.strftime('%Y-%m-%d')))
                    __M_writer(u'"\n')
                    pass
                # SOURCE LINE 120
                __M_writer(u'             >\n          <span class="karma">\n            ')
                # SOURCE LINE 122
                __M_writer(mako_websafe(thing.gold_remaining))
                __M_writer(u'\n          </span>\n          <br>\n          ')
                # SOURCE LINE 125
                __M_writer(mako_websafe(_("of reddit gold remaining")))
                __M_writer(u'\n        </div>\n')
                # SOURCE LINE 127
                if getattr(thing, "paypal_subscr_id", None):
                    # SOURCE LINE 128
                    __M_writer(u'          ')
  
                    paypal_link = ("https://www.paypal.com/cgi-bin/webscr?cmd=_subscr-find&alias=%s" % g.goldthanks_email)
                               
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['paypal_link'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 130
                    __M_writer(u'\n           <div>\n            <a href=')
                    # SOURCE LINE 132
                    __M_writer(mako_websafe(paypal_link))
                    __M_writer(u'>\n              ')
                    # SOURCE LINE 133
                    __M_writer(mako_websafe(_("Recurring Paypal subscription")))
                    __M_writer(u'\n            </a>\n            &#32;\n            ')
                    # SOURCE LINE 136
                    __M_writer(mako_websafe(thing.paypal_subscr_id))
                    __M_writer(u'\n          </div>\n')
                    pass
                # SOURCE LINE 139
                __M_writer(u'\n')
                # SOURCE LINE 140
                if getattr(thing, "stripe_customer_id", None):
                    # SOURCE LINE 141
                    __M_writer(u'           <div>\n            <a href="/gold/subscription">\n              ')
                    # SOURCE LINE 143
                    __M_writer(mako_websafe(_("manage recurring subscription")))
                    __M_writer(u'\n            </a>\n          </div>\n')
                    pass
                pass
            # SOURCE LINE 148
            if thing.gold_creddit_message:
                # SOURCE LINE 149
                __M_writer(u'        <div class="gold-creddits-remaining">\n          ')
                # SOURCE LINE 150
                __M_writer(mako_websafe(plain_link(thing.gold_creddit_message, "/gold?goldtype=gift")))
                __M_writer(u'\n        </div>\n')
                pass
            # SOURCE LINE 153
            __M_writer(u'    </div>\n')
            pass
        # SOURCE LINE 155
        __M_writer(u'\n')
        # SOURCE LINE 156
        if getattr(thing, "goldlink", None):
            # SOURCE LINE 157
            __M_writer(u'  <div class="giftgold">\n    <a href="')
            # SOURCE LINE 158
            __M_writer(mako_websafe(thing.goldlink))
            __M_writer(u'">\n      ')
            # SOURCE LINE 159
            __M_writer(mako_websafe(thing.giftmsg))
            __M_writer(u'\n    </a>\n  </div>\n')
            pass
        # SOURCE LINE 163
        __M_writer(u'\n  <div class="bottom">\n')
        # SOURCE LINE 165
        if thing.user != c.user:
            # SOURCE LINE 166
            __M_writer(u'      <img src="')
            __M_writer(mako_websafe(static('mailgray.png')))
            __M_writer(u'"/>\n      &#32;\n      ')
            # SOURCE LINE 168
            __M_writer(mako_websafe(plain_link(_("send message"), "/message/compose/?to=%s" % thing.user.name)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 170
        __M_writer(u'\n    <span class="age">\n      ')
        # SOURCE LINE 172
        __M_writer(mako_websafe(_("redditor for")))
        __M_writer(u'&#32;')
        __M_writer(mako_websafe(thing_timestamp(thing.user)))
        __M_writer(u'\n    </span>\n  </div>\n\n  <div class="clear"> </div>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


