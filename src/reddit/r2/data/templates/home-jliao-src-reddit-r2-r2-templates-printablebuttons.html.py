# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402178932.523726
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/printablebuttons.html'
_template_uri=u'/printablebuttons.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['toggle_button', 'toggleable_label', 'distinguish_setter', 'state_button', 'give_gold', 'messagebuttons', 'bylink_button', 'banbuttons', 'ynbutton', 'commentbuttons', 'big_modbuttons', 'ignore_reports_toggle', 'simple_button', 'comment_button', 'distinguish', 'linkbuttons', 'ajax_ynbutton']


# SOURCE LINE 25

from r2.lib.strings import strings
from r2.models.promo import PROMOTE_STATUS
 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 23
    ns = runtime.TemplateNamespace('__anon_0x7f8c8d9de1d0', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f8c8d9de1d0')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 74
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'\n\n')
        # SOURCE LINE 123
        __M_writer(u'\n\n')
        # SOURCE LINE 134
        __M_writer(u'\n\n')
        # SOURCE LINE 143
        __M_writer(u'\n\n')
        # SOURCE LINE 175
        __M_writer(u'\n\n')
        # SOURCE LINE 265
        __M_writer(u'\n\n')
        # SOURCE LINE 326
        __M_writer(u'\n\n\n')
        # SOURCE LINE 357
        __M_writer(u'\n\n')
        # SOURCE LINE 391
        __M_writer(u'\n\n\n')
        # SOURCE LINE 412
        __M_writer(u'\n\n')
        # SOURCE LINE 447
        __M_writer(u'\n\n')
        # SOURCE LINE 452
        __M_writer(u'\n\n')
        # SOURCE LINE 487
        __M_writer(u'\n\n')
        # SOURCE LINE 495
        __M_writer(u'\n\n')
        # SOURCE LINE 499
        __M_writer(u'\n\n')
        # SOURCE LINE 521
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toggle_button(context,class_name,title,alt_title,callback,cancelback,css_class='',alt_css_class='',reverse=False,login_required=False,style='',data_attrs=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        data = _import_ns.get('data', context.get('data', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 459
        __M_writer(u'\n')
        # SOURCE LINE 460

        if reverse:
            callback, cancelback = cancelback, callback
            title, alt_title = alt_title, title
            css_class, alt_css_class = alt_css_class, css_class
        extra_class = "login-required" if login_required else ""
         
        
        # SOURCE LINE 466
        __M_writer(u'\n<span class="')
        # SOURCE LINE 467
        __M_writer(mako_websafe(class_name))
        __M_writer(u' toggle" style="')
        __M_writer(mako_websafe(style))
        __M_writer(u'" ')
        __M_writer(mako_websafe(data(**data_attrs or dict())))
        __M_writer(u'>\n <a class="option active ')
        # SOURCE LINE 468
        __M_writer(mako_websafe(css_class))
        __M_writer(u' ')
        __M_writer(mako_websafe(extra_class))
        __M_writer(u'" href="#" tabindex="100"\n')
        # SOURCE LINE 469
        if not login_required or c.user_is_loggedin:
            # SOURCE LINE 470
            __M_writer(u'      onclick="return toggle(this, ')
            __M_writer(mako_websafe(callback))
            __M_writer(u', ')
            __M_writer(mako_websafe(cancelback))
            __M_writer(u')"\n')
            pass
        # SOURCE LINE 472
        __M_writer(u'    >\n')
        # SOURCE LINE 473
        if title:
            # SOURCE LINE 474
            __M_writer(u'     ')
            __M_writer(mako_websafe(title))
            __M_writer(u'\n')
            # SOURCE LINE 475
        else:
            # SOURCE LINE 476
            __M_writer(u'     &nbsp;\n')
            pass
        # SOURCE LINE 478
        __M_writer(u' </a>\n <a class="option ')
        # SOURCE LINE 479
        __M_writer(mako_websafe(alt_css_class))
        __M_writer(u'" href="#">\n')
        # SOURCE LINE 480
        if alt_title:
            # SOURCE LINE 481
            __M_writer(u'     ')
            __M_writer(mako_websafe(alt_title))
            __M_writer(u'\n')
            # SOURCE LINE 482
        else:
            # SOURCE LINE 483
            __M_writer(u'     &nbsp;\n')
            pass
        # SOURCE LINE 485
        __M_writer(u' </a>\n</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toggleable_label(context,class_name,title,alt_title,callback,cancelback,reverse=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        __M_writer = context.writer()
        # SOURCE LINE 504
        __M_writer(u'\n ')
        # SOURCE LINE 505

        if reverse:
            callback, cancelback = cancelback, callback
            title, alt_title = alt_title, title
         
        
        # SOURCE LINE 509
        __M_writer(u'\n<span class="')
        # SOURCE LINE 510
        __M_writer(mako_websafe(class_name))
        __M_writer(u' toggle">\n  <span class="toggle option active">')
        # SOURCE LINE 511
        __M_writer(mako_websafe(title))
        __M_writer(u'</span>\n  <span class="toggle option">')
        # SOURCE LINE 512
        __M_writer(mako_websafe(alt_title))
        __M_writer(u'</span>\n  &#32;(\n  <a href="#"\n     onclick="return toggle_label(this, ')
        # SOURCE LINE 515
        __M_writer(mako_websafe(callback))
        __M_writer(u', ')
        __M_writer(mako_websafe(cancelback))
        __M_writer(u')"\n     >\n    ')
        # SOURCE LINE 517
        __M_writer(mako_websafe(_("toggle")))
        __M_writer(u'\n  </a>\n  )\n</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_distinguish_setter(context,name,value=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        __M_writer = context.writer()
        # SOURCE LINE 76
        __M_writer(u'\n  <a href="javascript:void(0)"\n     onclick="return set_distinguish(this, \'')
        # SOURCE LINE 78
        __M_writer(mako_websafe(value or name))
        __M_writer(u'\')">')
        __M_writer(mako_websafe(_(name)))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_state_button(context,name,title,onclick,executed,clicked=False,a_class='',fmt=None,fmt_param='',hidden_data={}):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        def _link():
            context.caller_stack._push_frame()
            try:
                context._push_buffer()
                __M_writer = context.writer()
                # SOURCE LINE 362
                __M_writer(u'\n    <a href="javascript:void(0)"\n')
                # SOURCE LINE 364
                if a_class:
                    # SOURCE LINE 365
                    __M_writer(u'         class="')
                    __M_writer(mako_websafe(a_class))
                    __M_writer(u'" \n')
                    pass
                # SOURCE LINE 367
                __M_writer(u'       onclick="')
                __M_writer(mako_websafe(onclick))
                __M_writer(u'">')
                __M_writer(mako_websafe(title))
                __M_writer(u'</a>\n  ')
            finally:
                __M_buf = context._pop_buffer()
                context.caller_stack._pop_frame()
            return __M_buf.getvalue()
        __M_writer = context.writer()
        # SOURCE LINE 360
        __M_writer(u'\n\n  ')
        # SOURCE LINE 368
        __M_writer(u'\n  ')
        # SOURCE LINE 369

        link = _link()
        if fmt:
            link = fmt % {fmt_param: link}
            ## preserve spaces before and after < & > for space compression
            link = link.replace(" <", "&#32;<").replace("> ", ">&#32;")
           
        
        # SOURCE LINE 375
        __M_writer(u'   \n\n')
        # SOURCE LINE 377
        if clicked:
            # SOURCE LINE 378
            __M_writer(u'    ')
            __M_writer(mako_websafe(executed))
            __M_writer(u'\n')
            # SOURCE LINE 379
        else:
            # SOURCE LINE 380
            __M_writer(u'    <form action="/post/')
            __M_writer(mako_websafe(name))
            __M_writer(u'" method="post" \n          class="state-button ')
            # SOURCE LINE 381
            __M_writer(mako_websafe(name))
            __M_writer(u'-button">\n        <input type="hidden" name="executed" value="')
            # SOURCE LINE 382
            __M_writer(mako_websafe(executed))
            __M_writer(u'" />\n')
            # SOURCE LINE 383
            for key, value in hidden_data.iteritems():
                # SOURCE LINE 384
                __M_writer(u'          <input type="hidden" name="')
                __M_writer(mako_websafe(key))
                __M_writer(u'" value="')
                __M_writer(mako_websafe(value))
                __M_writer(u'" />\n')
                pass
            # SOURCE LINE 386
            __M_writer(u'        <span>\n          ')
            # SOURCE LINE 387
            __M_writer(mako_websafe(unsafe(link)))
            __M_writer(u'\n        </span>\n    </form>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_give_gold(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 125
        __M_writer(u'\n')
        # SOURCE LINE 126
        if thing.show_givegold:
            # SOURCE LINE 127
            __M_writer(u'    <li>\n    <a href="/gold?goldtype=gift&months=1&thing=')
            # SOURCE LINE 128
            __M_writer(mako_websafe(thing.thing._fullname))
            __M_writer(u'"\n        title="')
            # SOURCE LINE 129
            __M_writer(mako_websafe(_("give reddit gold in appreciation of this post.")))
            __M_writer(u'"\n        class="give-gold login-required"\n        >')
            # SOURCE LINE 131
            __M_writer(mako_websafe(_("give gold")))
            __M_writer(u'</a>\n    </li>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_messagebuttons(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        def ynbutton(title,executed,op,callback='null',question=None,post_callback='null',format='%(link)s',format_arg='link',hidden_data={},_class=''):
            return render_ynbutton(context,title,executed,op,callback,question,post_callback,format,format_arg,hidden_data,_class)
        __M_writer = context.writer()
        # SOURCE LINE 329
        __M_writer(u' \n')
        # SOURCE LINE 330
        if thing.was_comment:
            # SOURCE LINE 331
            __M_writer(u'    <li>\n      ')
            # SOURCE LINE 332
            __M_writer(mako_websafe(self.bylink_button(_("context"), thing.permalink + "?context=3")))
            __M_writer(u'\n    </li>\n')
            # SOURCE LINE 334
        else:
            # SOURCE LINE 335
            __M_writer(u'    <li class="first">\n      ')
            # SOURCE LINE 336
            __M_writer(mako_websafe(self.bylink_button(_("permalink"), thing.permalink)))
            __M_writer(u'\n    </li>\n')
            pass
        # SOURCE LINE 339
        if thing.recipient:
            # SOURCE LINE 340
            __M_writer(u'    ')
            __M_writer(mako_websafe(self.banbuttons()))
            __M_writer(u'\n')
            # SOURCE LINE 341
            if (not thing.was_comment or thing.thing.message_style == "mention") and thing.thing.author_id != c.user._id and thing.thing.author_id not in c.user.enemies:
                # SOURCE LINE 342
                __M_writer(u'        <li>\n          ')
                # SOURCE LINE 343
                __M_writer(mako_websafe(ynbutton(_("block user"), _("blocked"), "block", "hide_thing")))
                __M_writer(u'\n        </li>\n')
                pass
            # SOURCE LINE 346
            __M_writer(u'    <li class="unread">\n     ')
            # SOURCE LINE 347
            __M_writer(mako_websafe(self.state_button("unread", _("mark unread"), \
        "return change_state(this, 'unread_message', unread_thing, true);", \
         _("unread"))))
            # SOURCE LINE 349
            __M_writer(u'\n    </li>\n')
            pass
        # SOURCE LINE 352
        if thing.can_reply:
            # SOURCE LINE 353
            __M_writer(u'    <li>\n       ')
            # SOURCE LINE 354
            __M_writer(mako_websafe(self.simple_button(_("reply {verb}"), "reply")))
            __M_writer(u'\n    </li>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bylink_button(context,title,link):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 497
        __M_writer(u'\n ')
        # SOURCE LINE 498
        __M_writer(mako_websafe(plain_link(title, link, _class="bylink", rel="nofollow")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_banbuttons(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        def ynbutton(title,executed,op,callback='null',question=None,post_callback='null',format='%(link)s',format_arg='link',hidden_data={},_class=''):
            return render_ynbutton(context,title,executed,op,callback,question,post_callback,format,format_arg,hidden_data,_class)
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        if thing.show_delete:
            # SOURCE LINE 32
            __M_writer(u'    <li>\n      ')
            # SOURCE LINE 33
            __M_writer(mako_websafe(ynbutton(_("delete"), _("deleted"), "del", "hide_thing")))
            __M_writer(u'\n    </li>\n')
            pass
        # SOURCE LINE 36
        if thing.can_ban:
            # SOURCE LINE 37
            if not getattr(thing.thing, "use_big_modbuttons", False):
                # SOURCE LINE 38
                if not thing.show_spam:
                    # SOURCE LINE 39
                    __M_writer(u'        <li>\n           ')
                    # SOURCE LINE 40
                    __M_writer(mako_websafe(ynbutton(_("spam"), _("spammed"), "remove")))
                    __M_writer(u'\n        </li>\n        <li>\n           ')
                    # SOURCE LINE 43
                    __M_writer(mako_websafe(ynbutton(_("remove"), _("removed"), "remove", hidden_data=dict(spam=False))))
                    __M_writer(u'\n        </li>\n')
                    pass
                # SOURCE LINE 46
                __M_writer(u'\n')
                # SOURCE LINE 47
                if thing.show_approve:
                    # SOURCE LINE 48
                    __M_writer(u'        <li>\n           ')
                    # SOURCE LINE 49
                    __M_writer(mako_websafe(self.state_button("approve", _("approve"),
              "return change_state(this, 'approve');", _("approved"))))
                    # SOURCE LINE 50
                    __M_writer(u'\n        </li>\n')
                    pass
                pass
            # SOURCE LINE 54
        elif thing.show_report:
            # SOURCE LINE 55
            __M_writer(u'    <li>\n      ')
            # SOURCE LINE 56
            __M_writer(mako_websafe(ynbutton(_("report"), _("reported"), "report", "hide_thing")))
            __M_writer(u'\n    </li>\n')
            pass
        # SOURCE LINE 59
        if thing.show_marknsfw:
            # SOURCE LINE 60
            __M_writer(u'    <li>')
            __M_writer(mako_websafe(ynbutton(_("nsfw"), _("marked"), "marknsfw")))
            __M_writer(u'</li>\n')
            pass
        # SOURCE LINE 62
        if thing.show_unmarknsfw:
            # SOURCE LINE 63
            __M_writer(u'    <li>')
            __M_writer(mako_websafe(ynbutton(_("un-nsfw"), _("unmarked"), "unmarknsfw")))
            __M_writer(u'</li>\n')
            pass
        # SOURCE LINE 65
        if not getattr(thing, 'promoted', None) and c.site.link_flair_position and thing.show_flair:
            # SOURCE LINE 66
            __M_writer(u'    <li>\n      <a class="flairselectbtn" href="javascript://void(0)">')
            # SOURCE LINE 67
            __M_writer(mako_websafe(_('flair')))
            __M_writer(u'</a>\n      <div class="flairselector drop-choices"></div>\n    </li>\n')
            pass
        # SOURCE LINE 71
        if thing.show_rescrape:
            # SOURCE LINE 72
            __M_writer(u'    <li>')
            __M_writer(mako_websafe(ynbutton(_("retry thumb"), _("retrying"), "rescrape")))
            __M_writer(u'</li>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ynbutton(context,title,executed,op,callback='null',question=None,post_callback='null',format='%(link)s',format_arg='link',hidden_data={},_class=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        __M_writer = context.writer()
        # SOURCE LINE 420
        __M_writer(u'\n  ')
        # SOURCE LINE 421

        if question is None:
            question = _("are you sure?")
        link = ('<a href="#" class="togglebutton" onclick="return toggle(this)">'
                + title + '</a>')
        link = format % {format_arg : link}
        link = unsafe(link.replace(" <", "&#32;<").replace("> ", ">&#32;"))
           
        
        # SOURCE LINE 428
        __M_writer(u'\n  <form class="toggle ')
        # SOURCE LINE 429
        __M_writer(mako_websafe(op))
        __M_writer(u'-button ')
        __M_writer(mako_websafe(_class))
        __M_writer(u'" action="#" method="get">\n    <input type="hidden" name="executed" value="')
        # SOURCE LINE 430
        __M_writer(mako_websafe(executed))
        __M_writer(u'"/>\n')
        # SOURCE LINE 431
        for k, v in hidden_data.iteritems():
            # SOURCE LINE 432
            __M_writer(u'      <input type="hidden" name="')
            __M_writer(mako_websafe(k))
            __M_writer(u'" value="')
            __M_writer(mako_websafe(v))
            __M_writer(u'"/>\n')
            pass
        # SOURCE LINE 434
        __M_writer(u'    <span class="option main active">\n      ')
        # SOURCE LINE 435
        __M_writer(mako_websafe(link))
        __M_writer(u'\n    </span>\n    <span class="option error">\n      ')
        # SOURCE LINE 438
        __M_writer(mako_websafe(question))
        __M_writer(u'\n      &#32;<a href="javascript:void(0)" class="yes"\n         onclick=\'change_state(this, "')
        # SOURCE LINE 440
        __M_writer(mako_websafe(op))
        __M_writer(u'", ')
        __M_writer(mako_websafe(callback))
        __M_writer(u', undefined, ')
        __M_writer(mako_websafe(post_callback))
        __M_writer(u")'>\n        ")
        # SOURCE LINE 441
        __M_writer(mako_websafe(_("yes")))
        __M_writer(u'\n      </a>&#32;/&#32;\n      <a href="javascript:void(0)" class="no"\n         onclick="return toggle(this)">')
        # SOURCE LINE 444
        __M_writer(mako_websafe(_("no")))
        __M_writer(u'</a>\n    </span>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_commentbuttons(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        def big_modbuttons(thing):
            return render_big_modbuttons(context,thing)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        def ignore_reports_toggle(thing):
            return render_ignore_reports_toggle(context,thing)
        __M_writer = context.writer()
        # SOURCE LINE 267
        __M_writer(u'\n')
        # SOURCE LINE 268
        if not thing.deleted:
            # SOURCE LINE 269
            __M_writer(u'    <li class="first">\n      ')
            # SOURCE LINE 270
            __M_writer(mako_websafe(self.bylink_button(_("permalink"), thing.permalink)))
            __M_writer(u'\n    </li>\n')
            # SOURCE LINE 272
            if thing.can_save:
                # SOURCE LINE 273
                if thing.saved:
                    # SOURCE LINE 274
                    __M_writer(u'          <li class="comment-unsave-button save-button">\n            <a href="javascript:void(0)">')
                    # SOURCE LINE 275
                    __M_writer(mako_websafe(_("unsave")))
                    __M_writer(u'</a>\n          </li>\n')
                    # SOURCE LINE 277
                else:
                    # SOURCE LINE 278
                    __M_writer(u'          <li class="comment-save-button save-button">\n            <a href="javascript:void(0)">')
                    # SOURCE LINE 279
                    __M_writer(mako_websafe(_("save")))
                    __M_writer(u'</a>\n          </li>\n')
                    pass
                pass
            # SOURCE LINE 283
            if c.profilepage:
                # SOURCE LINE 284
                __M_writer(u'      <li>\n        ')
                # SOURCE LINE 285
                __M_writer(mako_websafe(self.bylink_button(_("context"), thing.permalink + "?context=3")))
                __M_writer(u'\n      </li>\n      <li class="first">\n      ')
                # SOURCE LINE 288
                __M_writer(mako_websafe(self.comment_button("comment",
                            _("full comments") + " (%d)" % thing.full_comment_count, 
                            thing.full_comment_path,
                            _sr_path=True,
                            a_class="may-blank")))
                # SOURCE LINE 292
                __M_writer(u'\n      </li>\n')
                pass
            # SOURCE LINE 295
            if not thing.profilepage:
                # SOURCE LINE 296
                if thing.parent_permalink:
                    # SOURCE LINE 297
                    __M_writer(u'        <li>\n          ')
                    # SOURCE LINE 298
                    __M_writer(mako_websafe(self.bylink_button(_("parent"), thing.parent_permalink)))
                    __M_writer(u'\n        </li>\n')
                    pass
                # SOURCE LINE 301
                if thing.is_author:
                    # SOURCE LINE 302
                    __M_writer(u'        <li>\n          ')
                    # SOURCE LINE 303
                    __M_writer(mako_websafe(self.simple_button(_("edit"), "edit_usertext", css_class="edit-usertext")))
                    __M_writer(u'\n        </li>\n')
                    pass
                pass
            # SOURCE LINE 307
            __M_writer(u'    ')
            __M_writer(mako_websafe(self.banbuttons()))
            __M_writer(u'\n    ')
            # SOURCE LINE 308
            __M_writer(mako_websafe(self.distinguish()))
            __M_writer(u'\n    ')
            # SOURCE LINE 309
            __M_writer(mako_websafe(self.give_gold()))
            __M_writer(u'\n')
            # SOURCE LINE 310
            if not thing.profilepage and thing.can_reply:
                # SOURCE LINE 311
                __M_writer(u'      <li>\n        ')
                # SOURCE LINE 312
                __M_writer(mako_websafe(self.simple_button(_("reply {verb}"), "reply")))
                __M_writer(u'\n      </li>\n')
                pass
            # SOURCE LINE 315
            if thing.show_reports and not thing.show_spam:
                # SOURCE LINE 316
                __M_writer(u'     <li class="rounded reported-stamp stamp">\n       ')
                # SOURCE LINE 317
                __M_writer(mako_websafe(strings.reports % thing.thing.reported))
                __M_writer(u'\n     </li>\n')
                pass
            # SOURCE LINE 320
            if getattr(thing.thing, "use_big_modbuttons", False):
                # SOURCE LINE 321
                __M_writer(u'       ')
                __M_writer(mako_websafe(big_modbuttons(thing.thing)))
                __M_writer(u'\n')
                # SOURCE LINE 322
            elif thing.ignore_reports and thing.can_ban:
                # SOURCE LINE 323
                __M_writer(u'      ')
                __M_writer(mako_websafe(ignore_reports_toggle(thing.thing)))
                __M_writer(u'\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_big_modbuttons(context,thing):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        def ignore_reports_toggle(thing):
            return render_ignore_reports_toggle(context,thing)
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        pretty_button = _import_ns.get('pretty_button', context.get('pretty_button', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 145
        __M_writer(u'\n  <span class="big-mod-buttons">\n    <span role="radiogroup">\n')
        # SOURCE LINE 148
        if not getattr(thing, "moderator_banned", None):
            # SOURCE LINE 149
            __M_writer(u'        ')
            __M_writer(mako_websafe(pretty_button(_("spam"), "big_mod_action", -2, "negative")))
            __M_writer(u'\n        ')
            # SOURCE LINE 150
            __M_writer(mako_websafe(pretty_button(_("remove"), "big_mod_action", -1, "neutral")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 152
        __M_writer(u'  \n')
        # SOURCE LINE 153
        if getattr(thing, "approval_checkmark", None):
            # SOURCE LINE 154
            __M_writer(u'        ')
            __M_writer(mako_websafe(pretty_button(_("reapprove"), "big_mod_action",  1, "positive")))
            __M_writer(u'\n')
            # SOURCE LINE 155
        else:
            # SOURCE LINE 156
            __M_writer(u'        ')
            __M_writer(mako_websafe(pretty_button(_("approve"), "big_mod_action",  1, "positive")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 158
        __M_writer(u'    </span>\n\n')
        # SOURCE LINE 160
        if not thing._spam:
            # SOURCE LINE 161
            __M_writer(u'      ')
            __M_writer(mako_websafe(ignore_reports_toggle(thing)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 163
        __M_writer(u'\n    &#32;\n    <span class="status-msg spammed">\n      ')
        # SOURCE LINE 166
        __M_writer(mako_websafe(_("spammed")))
        __M_writer(u'\n    </span>\n    <span class="status-msg removed">\n      ')
        # SOURCE LINE 169
        __M_writer(mako_websafe(_("removed")))
        __M_writer(u'\n    </span>\n    <span class="status-msg approved">\n      ')
        # SOURCE LINE 172
        __M_writer(mako_websafe(_("approved")))
        __M_writer(u'\n    </span>\n  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ignore_reports_toggle(context,thing):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        pretty_button = _import_ns.get('pretty_button', context.get('pretty_button', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 136
        __M_writer(u'\n  ')
        # SOURCE LINE 137

        label = _("ignore reports")
        if thing.ignore_reports and thing.reported > 0:
          label += " ({0})".format(thing.reported)
          
        
        # SOURCE LINE 141
        __M_writer(u'\n  ')
        # SOURCE LINE 142
        __M_writer(mako_websafe(pretty_button(label, "big_mod_toggle", "'ignore_reports', 'unignore_reports'", "neutral" + (" pressed" if thing.ignore_reports else ""))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_simple_button(context,title,nameFunc,css_class=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        __M_writer = context.writer()
        # SOURCE LINE 449
        __M_writer(u'\n <a class="')
        # SOURCE LINE 450
        __M_writer(mako_websafe(css_class))
        __M_writer(u'" href="javascript:void(0)" \n    onclick="return ')
        # SOURCE LINE 451
        __M_writer(mako_websafe(nameFunc))
        __M_writer(u'(this)">')
        __M_writer(mako_websafe(title))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_button(context,name,link_text,link,_sr_path=True,a_class='',title=''):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 491
        __M_writer(u'\n  ')
        # SOURCE LINE 492
        __M_writer(mako_websafe(plain_link(link_text, link, 
               _sr_path = _sr_path,
               _class=a_class, title=title)))
        # SOURCE LINE 494
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_distinguish(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        def distinguish_setter(name,value=None):
            return render_distinguish_setter(context,name,value)
        __M_writer = context.writer()
        # SOURCE LINE 81
        __M_writer(u'\n')
        # SOURCE LINE 82
        if thing.show_distinguish:
            # SOURCE LINE 83
            __M_writer(u'  <li class="toggle">\n    <form method="post" action="/post/distinguish">\n      <input type="hidden" value="')
            # SOURCE LINE 85
            __M_writer(mako_websafe(_('distinguishing...')))
            __M_writer(u'" name="executed"/>\n      <a href="javascript:void(0)"\n         onclick="return toggle_distinguish_span(this)">')
            # SOURCE LINE 87
            __M_writer(mako_websafe(_("distinguish")))
            __M_writer(u'</a>\n      <span class="option error">\n         ')
            # SOURCE LINE 89
            __M_writer(mako_websafe(_("distinguish this?")))
            __M_writer(u'\n\n')
            # SOURCE LINE 92
            if thing.can_ban:
                # SOURCE LINE 93
                __M_writer(u'         &#32;\n         ')
                # SOURCE LINE 94
                __M_writer(mako_websafe(distinguish_setter('yes')))
                __M_writer(u'\n         &#32;/\n')
                pass
            # SOURCE LINE 97
            __M_writer(u'         \n         &#32;\n         ')
            # SOURCE LINE 99
            __M_writer(mako_websafe(distinguish_setter('no')))
            __M_writer(u'\n         &#32;\n\n')
            # SOURCE LINE 102
            if c.user.employee:
                # SOURCE LINE 103
                __M_writer(u'         /&#32;\n         ')
                # SOURCE LINE 104
                __M_writer(mako_websafe(distinguish_setter('admin')))
                __M_writer(u'\n         &#32;\n')
                pass
            # SOURCE LINE 107
            __M_writer(u'         \n')
            # SOURCE LINE 108
            if c.user_special_distinguish:
                # SOURCE LINE 109
                __M_writer(u'         /&#32;\n         ')
                # SOURCE LINE 110
                __M_writer(mako_websafe(distinguish_setter(c.user_special_distinguish['name'], 'special')))
                __M_writer(u'\n         &#32;\n')
                pass
            # SOURCE LINE 113
            __M_writer(u'\n         /&#32;\n         <a class="nonbutton" href="/wiki/moderation#wiki_distinguishing">\n           help\n         </a>\n         &#32;\n      </span>\n    </form>\n  </li>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_linkbuttons(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        def toggle_button(class_name,title,alt_title,callback,cancelback,css_class='',alt_css_class='',reverse=False,login_required=False,style='',data_attrs=None):
            return render_toggle_button(context,class_name,title,alt_title,callback,cancelback,css_class,alt_css_class,reverse,login_required,style,data_attrs)
        def ignore_reports_toggle(thing):
            return render_ignore_reports_toggle(context,thing)
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        def ynbutton(title,executed,op,callback='null',question=None,post_callback='null',format='%(link)s',format_arg='link',hidden_data={},_class=''):
            return render_ynbutton(context,title,executed,op,callback,question,post_callback,format,format_arg,hidden_data,_class)
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        def big_modbuttons(thing):
            return render_big_modbuttons(context,thing)
        plain_link = _import_ns.get('plain_link', context.get('plain_link', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 177
        __M_writer(u'\n')
        # SOURCE LINE 178
        if thing.show_comments:
            # SOURCE LINE 179
            __M_writer(u'    <li class="first">\n    ')
            # SOURCE LINE 180
            __M_writer(mako_websafe(self.comment_button("comment", thing.comment_label, thing.permalink,
                          _sr_path=(thing.promoted is None),
                          a_class=thing.commentcls)))
            # SOURCE LINE 182
            __M_writer(u'\n    </li>\n')
            pass
        # SOURCE LINE 185
        if thing.editable:
            # SOURCE LINE 186
            __M_writer(u'    <li>\n      ')
            # SOURCE LINE 187
            __M_writer(mako_websafe(self.simple_button(_("edit"), "edit_usertext", css_class="edit-usertext")))
            __M_writer(u'\n    </li>\n')
            pass
        # SOURCE LINE 190
        if c.user_is_loggedin or not g.read_only_mode:
            # SOURCE LINE 191
            __M_writer(u'  <li class="share">\n    ')
            # SOURCE LINE 192
            __M_writer(mako_websafe(self.toggle_button("share-button", _("share"), _("cancel"),
                         "share", "cancelShare", login_required = True)))
            # SOURCE LINE 193
            __M_writer(u'\n  </li>\n')
            pass
        # SOURCE LINE 196
        if thing.is_loggedin:
            # SOURCE LINE 197
            if thing.saved:
                # SOURCE LINE 198
                __M_writer(u'      <li class="link-unsave-button save-button"><a href="#">')
                __M_writer(mako_websafe(_("unsave")))
                __M_writer(u'</a></li>\n')
                # SOURCE LINE 199
            else:
                # SOURCE LINE 200
                __M_writer(u'      <li class="link-save-button save-button"><a href="#">')
                __M_writer(mako_websafe(_("save")))
                __M_writer(u'</a></li>\n')
                pass
            # SOURCE LINE 202
            __M_writer(u'    <li>\n')
            # SOURCE LINE 203
            if thing.hidden:
                # SOURCE LINE 204
                __M_writer(u'      ')
                __M_writer(mako_websafe(self.state_button("unhide", _("unhide"), \
        "change_state(this, 'unhide', hide_thing);", _("unhidden"))))
                # SOURCE LINE 205
                __M_writer(u'\n')
                # SOURCE LINE 206
            else:
                # SOURCE LINE 207
                __M_writer(u'      ')
                __M_writer(mako_websafe(self.state_button("hide", _("hide"), \
         "change_state(this, 'hide', hide_thing);", _("hidden"))))
                # SOURCE LINE 208
                __M_writer(u'\n')
                pass
            # SOURCE LINE 210
            __M_writer(u'    </li>\n')
            pass
        # SOURCE LINE 212
        __M_writer(u'\n  ')
        # SOURCE LINE 213
        __M_writer(mako_websafe(self.distinguish()))
        __M_writer(u'\n  ')
        # SOURCE LINE 214
        __M_writer(mako_websafe(self.give_gold()))
        __M_writer(u'\n  ')
        # SOURCE LINE 215
        __M_writer(mako_websafe(self.banbuttons()))
        __M_writer(u'\n')
        # SOURCE LINE 216
        if thing.promoted is not None:
            # SOURCE LINE 217
            if thing.user_is_sponsor or thing.is_author:
                # SOURCE LINE 218
                __M_writer(u'       <li>\n         ')
                # SOURCE LINE 219
                __M_writer(mako_websafe(plain_link(_("edit"), thing.promo_url, _sr_path = False)))
                __M_writer(u'\n       </li>\n')
                pass
            # SOURCE LINE 222
            if c.user_is_sponsor:
                # SOURCE LINE 223
                __M_writer(u'       <li>\n         <form action="/post/reject" class="rejection-form"\n               style="display:none"\n               method="post" onsubmit="reject post_form(this, \'unpromote\')">\n           <br/>\n           <input type="hidden" name="executed" value="rejected" />\n           <label>Reason:</label><br/>\n           <textarea name="reason" value="" ></textarea>\n           <br/>\n           <a href="#" \n              onclick="change_state(this, \'unpromote\', complete_reject_promo)">\n             submit\n           </a>/\n         </form>\n         ')
                # SOURCE LINE 237
                __M_writer(mako_websafe(toggle_button("reject_promo", \
                         _("reject"), _("cancel"), \
                         "reject_promo", "cancel_reject_promo")))
                # SOURCE LINE 239
                __M_writer(u'\n       </li>\n')
                # SOURCE LINE 241
                if thing.promote_status in (PROMOTE_STATUS.unpaid, PROMOTE_STATUS.unseen, PROMOTE_STATUS.rejected):
                    # SOURCE LINE 242
                    __M_writer(u'        <li>\n          ')
                    # SOURCE LINE 243
                    __M_writer(mako_websafe(ynbutton(_("accept"), _("accepted"), "promote")))
                    __M_writer(u'\n        </li>\n')
                    pass
                pass
            # SOURCE LINE 247
            if thing.user_is_sponsor or thing.is_author:
                # SOURCE LINE 248
                __M_writer(u'      <li>\n        ')
                # SOURCE LINE 249
                __M_writer(mako_websafe(plain_link(_("traffic"), thing.traffic_url, _sr_path = False)))
                __M_writer(u'\n      </li>\n')
                pass
            pass
        # SOURCE LINE 253
        __M_writer(u'\n')
        # SOURCE LINE 254
        if thing.show_reports and not thing.show_spam:
            # SOURCE LINE 255
            __M_writer(u'   <li class="rounded reported-stamp stamp">\n     ')
            # SOURCE LINE 256
            __M_writer(mako_websafe(strings.reports % thing.thing.reported))
            __M_writer(u'\n   </li>\n')
            pass
        # SOURCE LINE 259
        __M_writer(u'\n')
        # SOURCE LINE 260
        if getattr(thing.thing, "use_big_modbuttons", False):
            # SOURCE LINE 261
            __M_writer(u'     ')
            __M_writer(mako_websafe(big_modbuttons(thing.thing)))
            __M_writer(u'\n')
            # SOURCE LINE 262
        elif thing.ignore_reports and thing.can_ban:
            # SOURCE LINE 263
            __M_writer(u'    ')
            __M_writer(mako_websafe(ignore_reports_toggle(thing.thing)))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ajax_ynbutton(context,title,op,question=None,_class='',hidden_data={}):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f8c8d9de1d0')._populate(_import_ns, [u'plain_link', u'pretty_button', u'data'])
        __M_writer = context.writer()
        # SOURCE LINE 394
        __M_writer(u'\n  <form method="post" action="/api/')
        # SOURCE LINE 395
        __M_writer(mako_websafe(op))
        __M_writer(u'"\n        class="toggle ajax-yn-button ')
        # SOURCE LINE 396
        __M_writer(mako_websafe(op))
        __M_writer(u'-button ')
        __M_writer(mako_websafe(_class))
        __M_writer(u'">\n    <input type="hidden" name="_op" value="')
        # SOURCE LINE 397
        __M_writer(mako_websafe(op))
        __M_writer(u'" />\n')
        # SOURCE LINE 398
        for k, v in hidden_data.iteritems():
            # SOURCE LINE 399
            __M_writer(u'      <input type="hidden" name="')
            __M_writer(mako_websafe(k))
            __M_writer(u'" value="')
            __M_writer(mako_websafe(v))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 401
        __M_writer(u'    <span class="option main active">\n      <a href="javascript:void(0)" class="togglebutton">')
        # SOURCE LINE 402
        __M_writer(mako_websafe(title))
        __M_writer(u'</a>\n    </span>\n    <span class="option error">\n      ')
        # SOURCE LINE 405
        __M_writer(mako_websafe(_("are you sure?") if question is None else question))
        __M_writer(u'\n      &#32;\n      <a href="javascript:void(0)" class="yes">')
        # SOURCE LINE 407
        __M_writer(mako_websafe(_("yes")))
        __M_writer(u'</a>\n      &#32;/&#32;\n      <a href="javascript:void(0)" class="no">')
        # SOURCE LINE 409
        __M_writer(mako_websafe(_("no")))
        __M_writer(u'</a>\n    </span>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


