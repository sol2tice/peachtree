# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402179366.487054
_template_filename='/home/jliao/src/reddit/r2/r2/templates/goldpayment.html'
_template_uri='/goldpayment.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['stripe_button', 'creddits_button', 'stripe_form', 'paypal_button', 'base_stripe_form', 'coinbase_button']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f8c8da9a350', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8da9a350')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da9a350')._populate(_import_ns, [u'error_field', u'success_field', u'radio_type'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 25

        from r2.lib.filters import unsafe, safemarkdown
        from r2.lib.template_helpers import static
        
        clone_class = ''
        if thing.clone_template:
          if thing.thing_type == 'comment':
            clone_class = 'cloneable-comment'
          else:
            clone_class = 'cloneable-link'
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['safemarkdown','static','unsafe','clone_class'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 35
        __M_writer(u'\n\n<div class="gold-form gold-payment ')
        # SOURCE LINE 37
        __M_writer(mako_websafe(clone_class))
        __M_writer(u'">\n  <div class="roundfield">\n')
        # SOURCE LINE 39
        if thing.clone_template:
            # SOURCE LINE 40
            __M_writer(u'      <button class="close-button">')
            __M_writer(mako_websafe(_('close')))
            __M_writer(u'</button>\n')
            pass
        # SOURCE LINE 42
        __M_writer(u'    <img src="')
        __M_writer(mako_websafe(static('reddit_gold-70.png')))
        __M_writer(u'" class="gold-logo">\n    <div class="roundfield-content">\n      ')
        # SOURCE LINE 44
        __M_writer(mako_websafe(unsafe(safemarkdown(thing.summary, wrap=False))))
        __M_writer(u'\n')
        # SOURCE LINE 45
        if thing.thing and not thing.clone_template:
            # SOURCE LINE 46
            __M_writer(u'        <div class="giftmessage">\n          ')
            # SOURCE LINE 47
            __M_writer(mako_websafe(unsafe(safemarkdown(thing.description))))
            __M_writer(u'\n        </div>\n')
            pass
        # SOURCE LINE 50
        __M_writer(u'\n')
        # SOURCE LINE 51
        if thing.giftmessage:
            # SOURCE LINE 52
            __M_writer(u'      <p>')
            __M_writer(mako_websafe(_("The following gift note will be attached:")))
            __M_writer(u'</p>\n      <div class="giftmessage">\n        ')
            # SOURCE LINE 54
            __M_writer(mako_websafe(unsafe(safemarkdown(thing.giftmessage))))
            __M_writer(u'\n      </div>\n')
            pass
        # SOURCE LINE 57
        __M_writer(u'\n')
        # SOURCE LINE 58
        if thing.pay_from_creddits:
            # SOURCE LINE 59
            __M_writer(u'      ')
            __M_writer(mako_websafe(self.creddits_button()))
            __M_writer(u'\n')
            # SOURCE LINE 60
        else:
            # SOURCE LINE 61
            __M_writer(u'      <p>')
            __M_writer(mako_websafe(_("Please select a payment method.")))
            __M_writer(u'</p>\n\n')
            # SOURCE LINE 63
            if thing.paypal_buttonid:
                # SOURCE LINE 64
                __M_writer(u'        ')
                __M_writer(mako_websafe(self.paypal_button()))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 66
            __M_writer(u'\n')
            # SOURCE LINE 67
            if thing.coinbase_button_id:
                # SOURCE LINE 68
                __M_writer(u'        ')
                __M_writer(mako_websafe(self.coinbase_button()))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 70
            __M_writer(u'\n')
            # SOURCE LINE 71
            if thing.stripe_key:
                # SOURCE LINE 72
                __M_writer(u'        ')
                __M_writer(mako_websafe(self.stripe_button()))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 74
            __M_writer(u'\n')
            # SOURCE LINE 75
            if thing.stripe_key and not thing.clone_template:
                # SOURCE LINE 76
                __M_writer(u'        ')
                __M_writer(mako_websafe(self.stripe_form()))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 78
            __M_writer(u'\n')
            # SOURCE LINE 79
            if thing.clone_template:
                # SOURCE LINE 80
                __M_writer(u'        <div class="note">')
                __M_writer(mako_websafe(unsafe(safemarkdown(_("Give gold often? Consider [buying creddits to use](/gold?goldtype=creddits), they're 40% cheaper if purchased in a set of 12."), wrap=False))))
                __M_writer(u'</div>\n')
                pass
            # SOURCE LINE 82
            __M_writer(u'      <div class="throbber"></div>\n')
            pass
        # SOURCE LINE 84
        __M_writer(u'    </div>\n  </div>\n</div>\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n\n')
        # SOURCE LINE 112
        __M_writer(u'\n\n')
        # SOURCE LINE 116
        __M_writer(u'\n\n')
        # SOURCE LINE 192
        __M_writer(u'\n\n')
        # SOURCE LINE 220
        __M_writer(u'\n\n')
        # SOURCE LINE 230
        __M_writer(u'\n\n')
        # SOURCE LINE 232
        if not thing.clone_template:
            # SOURCE LINE 233
            __M_writer(u'<script src="//checkout.google.com/files/digital/ga_post.js"\n  type="text/javascript"></script>\n')
            pass
        # SOURCE LINE 236
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stripe_button(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da9a350')._populate(_import_ns, [u'error_field', u'success_field', u'radio_type'])
        __M_writer = context.writer()
        # SOURCE LINE 114
        __M_writer(u'\n  <button class="btn stripe-gold gold-button">')
        # SOURCE LINE 115
        __M_writer(mako_websafe(_('Credit Card')))
        __M_writer(u'</button>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_creddits_button(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da9a350')._populate(_import_ns, [u'error_field', u'success_field', u'radio_type'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 88
        __M_writer(u'\n  <form id="giftgold" action="/api/spendcreddits" method="post"\n        class="content"\n        onsubmit="return post_form(this, \'spendcreddits\');">\n    <input type="hidden" name="months" value="')
        # SOURCE LINE 92
        __M_writer(mako_websafe(thing.months))
        __M_writer(u'">\n    <input type="hidden" name="passthrough" value="')
        # SOURCE LINE 93
        __M_writer(mako_websafe(thing.passthrough))
        __M_writer(u'" class="passthrough">\n    <button class="btn gold-button">')
        # SOURCE LINE 94
        __M_writer(mako_websafe(_("use creddit")))
        __M_writer(u'</button>\n    <span class="status"></span>\n    <div class="throbber"></div>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stripe_form(context,display=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da9a350')._populate(_import_ns, [u'error_field', u'success_field', u'radio_type'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def base_stripe_form():
            return render_base_stripe_form(context)
        __M_writer = context.writer()
        # SOURCE LINE 194
        __M_writer(u'\n<div id="stripe-payment"\n     class="charge"\n     ')
        # SOURCE LINE 197
        __M_writer(mako_websafe(not display and "style='display:none'" or ''))
        __M_writer(u'>\n  <hr>\n  <table class="credit-card-input">\n    <tr> \n      <th><label>')
        # SOURCE LINE 201
        __M_writer(mako_websafe(_('amount')))
        __M_writer(u'</label></th>\n      <th class="credit-card-amount">')
        # SOURCE LINE 202
        __M_writer(mako_websafe(thing.price))
        __M_writer(u'</th>\n    </tr>\n')
        # SOURCE LINE 204
        if thing.period:
            # SOURCE LINE 205
            __M_writer(u'    <tr>\n      <th><label>')
            # SOURCE LINE 206
            __M_writer(mako_websafe(_('renewal interval')))
            __M_writer(u'</label></th>\n      <th class="credit-card-interval">')
            # SOURCE LINE 207
            __M_writer(mako_websafe(_(thing.period)))
            __M_writer(u'</th>\n    </tr>\n')
            pass
        # SOURCE LINE 210
        __M_writer(u'  </table>\n\n  <input type="hidden" name="pennies" value="')
        # SOURCE LINE 212
        __M_writer(mako_websafe(thing.price.pennies))
        __M_writer(u'">\n  <input type="hidden" name="months" value="')
        # SOURCE LINE 213
        __M_writer(mako_websafe(thing.months))
        __M_writer(u'">\n  <input type="hidden" name="period" value="')
        # SOURCE LINE 214
        __M_writer(mako_websafe(thing.period))
        __M_writer(u'">\n  <input type="hidden" name="passthrough" value="')
        # SOURCE LINE 215
        __M_writer(mako_websafe(thing.passthrough))
        __M_writer(u'">\n\n  <hr>\n  ')
        # SOURCE LINE 218
        __M_writer(mako_websafe(base_stripe_form()))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_paypal_button(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da9a350')._populate(_import_ns, [u'error_field', u'success_field', u'radio_type'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 100
        __M_writer(u'\n  <form action="https://www.paypal.com/cgi-bin/webscr" method="post"\n        class="gold-checkout"\n        data-vendor="paypal" target="')
        # SOURCE LINE 103
        __M_writer(mako_websafe('_blank' if thing.clone_template else '_top'))
        __M_writer(u'">\n    <input type="hidden" name="cmd" value="_s-xclick">\n    <input type="hidden" name="custom" value="')
        # SOURCE LINE 105
        __M_writer(mako_websafe(thing.passthrough))
        __M_writer(u'" class="passthrough">\n')
        # SOURCE LINE 106
        if thing.quantity:
            # SOURCE LINE 107
            __M_writer(u'      <input type="hidden" name="quantity" value="')
            __M_writer(mako_websafe(thing.quantity))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 109
        __M_writer(u'    <input type="hidden" name="hosted_button_id" value="')
        __M_writer(mako_websafe(thing.paypal_buttonid))
        __M_writer(u'">\n    <button type="submit" class="btn gold-button">')
        # SOURCE LINE 110
        __M_writer(mako_websafe(_("PayPal")))
        __M_writer(u'</button>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_base_stripe_form(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da9a350')._populate(_import_ns, [u'error_field', u'success_field', u'radio_type'])
        xrange = _import_ns.get('xrange', context.get('xrange', UNDEFINED))
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 118
        __M_writer(u'\n  <script type="text/javascript" src="https://js.stripe.com/v1/"></script>\n\n  <div id="base-stripe-form"\n        class="gold-checkout"\n        data-vendor="stripe">\n    <div class="stripe-note">\n      <a class="icon" href="https://stripe.com/help/security">powered by stripe</a>\n      <div>')
        # SOURCE LINE 126
        __M_writer(mako_websafe(_('Stripe is PCI compliant and your credit card information is sent directly to them.')))
        __M_writer(u'</div>\n    </div>\n    <table class="credit-card-input">\n      <tr>\n        <th><label>')
        # SOURCE LINE 130
        __M_writer(mako_websafe(_('name')))
        __M_writer(u'</label></th>\n        <td><input type="text" autocomplete="off" class="card-name"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 134
        __M_writer(mako_websafe(_('card number')))
        __M_writer(u'</label></th>\n        <td><input type="text" autocomplete="off" class="card-number"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 138
        __M_writer(mako_websafe(_('cvc')))
        __M_writer(u'</label></th>\n        <td><input type="text" autocomplete="off" class="card-cvc"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 142
        __M_writer(mako_websafe(_('expiration date')))
        __M_writer(u'</label></th>\n        <td>\n          ')
        # SOURCE LINE 144
 
        import datetime
        months = ['%02d' % m for m in xrange(1, 13)]
        years = ['%04d' % y for y in xrange(datetime.datetime.now().year,
                                            datetime.datetime.now().year + 25)]
                   
        
        # SOURCE LINE 149
        __M_writer(u'\n          <select class="card-expiry-month" title=')
        # SOURCE LINE 150
        __M_writer(mako_websafe(_('month')))
        __M_writer(u'>\n')
        # SOURCE LINE 151
        for m in months:
            # SOURCE LINE 152
            __M_writer(u'              <option value="')
            __M_writer(mako_websafe(m))
            __M_writer(u'">')
            __M_writer(mako_websafe(m))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 154
        __M_writer(u'          </select>\n          <select class="card-expiry-year" title=')
        # SOURCE LINE 155
        __M_writer(mako_websafe(_('year')))
        __M_writer(u'>\n')
        # SOURCE LINE 156
        for y in years:
            # SOURCE LINE 157
            __M_writer(u'              <option value="')
            __M_writer(mako_websafe(y))
            __M_writer(u'">')
            __M_writer(mako_websafe(y))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 159
        __M_writer(u'          </select>\n        </td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 163
        __M_writer(mako_websafe(_('address line 1')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_line1"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 167
        __M_writer(mako_websafe(_('address line 2')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_line2"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 171
        __M_writer(mako_websafe(_('city')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_city"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 175
        __M_writer(mako_websafe(_('state/province')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_state"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 179
        __M_writer(mako_websafe(_('country')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_country"></td>\n      </tr>\n      <tr>\n        <th><label>')
        # SOURCE LINE 183
        __M_writer(mako_websafe(_('zip')))
        __M_writer(u'</label></th>\n        <td><input type="text" class="card-address_zip"></td>\n      </tr>\n    </table>\n    <input type="hidden" name="stripePublicKey" value="')
        # SOURCE LINE 187
        __M_writer(mako_websafe(thing.stripe_key))
        __M_writer(u'">\n    <input type="hidden" name="stripeToken" value="">\n    <button class="btn gold-button stripe-submit">')
        # SOURCE LINE 189
        __M_writer(mako_websafe(_('Submit')))
        __M_writer(u'</button>\n    <span class="status"></span>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_coinbase_button(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8da9a350')._populate(_import_ns, [u'error_field', u'success_field', u'radio_type'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 222
        __M_writer(u'\n  <button class="btn coinbase-gold gold-button gold-checkout"\n          data-vendor="coinbase"\n')
        # SOURCE LINE 225
        if not thing.clone_template:
            # SOURCE LINE 226
            __M_writer(u'            onclick="window.open(\'https://coinbase.com/checkouts/')
            __M_writer(mako_websafe(thing.coinbase_button_id))
            __M_writer(u'?c=')
            __M_writer(mako_websafe(thing.passthrough))
            __M_writer(u'\')"\n')
            pass
        # SOURCE LINE 228
        __M_writer(u'          >')
        __M_writer(mako_websafe(_('Bitcoin')))
        __M_writer(u'</button>\n  <input type="hidden" name="cbbaseurl" value="https://coinbase.com/checkouts/')
        # SOURCE LINE 229
        __M_writer(mako_websafe(thing.coinbase_button_id))
        __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


