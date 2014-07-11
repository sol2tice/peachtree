# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918232.518727
_template_filename=u'/home/ubuntu/src/reddit/r2/r2/templates/utils.html'
_template_uri=u'/utils.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['round_field', 'checkbox', 'img_link', '_a_buffered', 'pretty_button', 'error_field', 'js_setup', 'googleanalytics', 'first_defined', 'thing_timestamp', 'inline_radio_type', 'image_upload', 'post_link', 'tags', 'block_field', 'submit_form', 'percentage', 'plain_link', '_a', 'edited', 'ajax_upload', 'optionalstyle', 'language_checkboxes', 'timestamp', 'text_with_links', 'radio_type', 'line_field', 'logout', 'data', 'md', 'success_field', 'language_tool', 'classes', 'separator', '_md', '_id']


# SOURCE LINE 23

import json
from r2.models import FakeSubreddit
from r2.lib.filters import spaceCompress, unsafe, safemarkdown
from r2.lib.template_helpers import add_sr, js_config, static, html_datetime, simplified_timesince
from r2.lib.utils import cols, long_datetime
from r2.lib import tracking
from datetime import datetime


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'\n\n\n')
        # SOURCE LINE 54
        __M_writer(u'\n\n')
        # SOURCE LINE 58
        __M_writer(u'\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n\n')
        # SOURCE LINE 81
        __M_writer(u'\n\n')
        # SOURCE LINE 87
        __M_writer(u'\n\n')
        # SOURCE LINE 97
        __M_writer(u'\n\n')
        # SOURCE LINE 113
        __M_writer(u'\n\n')
        # SOURCE LINE 133
        __M_writer(u'\n\n')
        # SOURCE LINE 157
        __M_writer(u'\n\n')
        # SOURCE LINE 179
        __M_writer(u'\n\n\n')
        # SOURCE LINE 194
        __M_writer(u'\n\n')
        # SOURCE LINE 218
        __M_writer(u'\n\n')
        # SOURCE LINE 257
        __M_writer(u'\n\n')
        # SOURCE LINE 261
        __M_writer(u'\n\n')
        # SOURCE LINE 267
        __M_writer(u'\n\n')
        # SOURCE LINE 274
        __M_writer(u'\n\n')
        # SOURCE LINE 306
        __M_writer(u'\n\n')
        # SOURCE LINE 413
        __M_writer(u'\n\n\n')
        # SOURCE LINE 420
        __M_writer(u'\n\n')
        # SOURCE LINE 446
        __M_writer(u'\n\n')
        # SOURCE LINE 468
        __M_writer(u'\n\n')
        # SOURCE LINE 485
        __M_writer(u'\n\n')
        # SOURCE LINE 502
        __M_writer(u'\n\n')
        # SOURCE LINE 508
        __M_writer(u'\n\n')
        # SOURCE LINE 514
        __M_writer(u'\n\n')
        # SOURCE LINE 532
        __M_writer(u'\n\n')
        # SOURCE LINE 547
        __M_writer(u'\n\n')
        # SOURCE LINE 558
        __M_writer(u'\n\n')
        # SOURCE LINE 564
        __M_writer(u'\n\n')
        # SOURCE LINE 572
        __M_writer(u'\n\n')
        # SOURCE LINE 586
        __M_writer(u'\n\n')
        # SOURCE LINE 594
        __M_writer(u'\n\n')
        # SOURCE LINE 598
        __M_writer(u'\n\n')
        # SOURCE LINE 602
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_round_field(context,title,description='',css_class='',**kw):
    context.caller_stack._push_frame()
    try:
        def block_field(kind,title,description='',css_class='',**kw):
            return render_block_field(context,kind,title,description,css_class,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 504
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 505
                __M_writer(u'\n     ')
                # SOURCE LINE 506
                __M_writer(mako_websafe(caller.body()))
                __M_writer(u'\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 505
            __M_writer(mako_websafe(block_field('roundfield', title, description = description, css_class= css_class, **kw)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 507
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_checkbox(context,name,text,val):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 269
        __M_writer(u'\n  <input type="checkbox" ')
        # SOURCE LINE 270
        __M_writer(mako_websafe('checked="checked"' if val else ''))
        __M_writer(u'\n    name="')
        # SOURCE LINE 271
        __M_writer(mako_websafe(name))
        __M_writer(u'">\n    ')
        # SOURCE LINE 272
        __M_writer(mako_websafe(text))
        __M_writer(u'\n  </input>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_img_link(context,link_text,img,path,_id='',target='',img_id=None,size=None,**kw):
    context.caller_stack._push_frame()
    try:
        def _a(**kw):
            return render__a(context,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 115
        __M_writer(u'\n  ')
        # SOURCE LINE 116
 
        if (not target or target == '_parent') and c.cname:
            target = '_top'
        if target:
            kw['target'] = target
        
        path = add_sr(path, sr_path = False)
        kw['target'] = target
        
        if size is None:
            size_str = ""
        else:
            size_str = "width='%d' height='%d'" % (size[0], size[1])
          
        
        # SOURCE LINE 129
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 130
                __M_writer(u'\n    <img ')
                # SOURCE LINE 131
                __M_writer(mako_websafe(("id='%s'" % img_id) if img_id else ''))
                __M_writer(u' src="')
                __M_writer(mako_websafe(img))
                __M_writer(u'" ')
                __M_writer(mako_websafe(size_str))
                __M_writer(u' alt="')
                __M_writer(mako_websafe(link_text))
                __M_writer(u'"/>\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 130
            __M_writer(mako_websafe(_a(href=path, _id=_id, **kw)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 132
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__a_buffered(context,body,**kw):
    context.caller_stack._push_frame()
    try:
        context._push_buffer()
        def tags(**kw):
            return render_tags(context,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n<a ')
        # SOURCE LINE 47
        __M_writer(mako_websafe(tags(**kw)))
        __M_writer(u'>')
        __M_writer(mako_websafe(body))
        __M_writer(u'</a>\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_pretty_button(context,label,func=None,func_vars='',extra_class=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 574
        __M_writer(u'\n  <a class="pretty-button ')
        # SOURCE LINE 575
        __M_writer(mako_websafe(extra_class))
        __M_writer(u'" href="#"\n')
        # SOURCE LINE 576
        if func is None:
            # SOURCE LINE 577
            __M_writer(u'       onclick="alert(\'please don\\\'t do that again\');return false;"\n')
            # SOURCE LINE 578
        elif func_vars:
            # SOURCE LINE 579
            __M_writer(u'       onclick="return ')
            __M_writer(mako_websafe(func))
            __M_writer(u'($(this), ')
            __M_writer(mako_websafe(func_vars))
            __M_writer(u')"\n')
            # SOURCE LINE 580
        else:
            # SOURCE LINE 581
            __M_writer(u'       onclick="return ')
            __M_writer(mako_websafe(func))
            __M_writer(u'($(this))"\n')
            pass
        # SOURCE LINE 583
        __M_writer(u'     >\n       ')
        # SOURCE LINE 584
        __M_writer(mako_websafe(label))
        __M_writer(u'\n  </a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_error_field(context,error_name,field_name,kind='span'):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 89
        __M_writer(u'\n  ')
        # SOURCE LINE 90
        error_key = (error_name, field_name) 
        
        __M_writer(u'\n  <')
        # SOURCE LINE 91
        __M_writer(mako_websafe(kind))
        __M_writer(u' class="error ')
        __M_writer(mako_websafe(error_name))
        __M_writer(u' field-')
        __M_writer(mako_websafe(field_name))
        __M_writer(u'" \n  style="')
        # SOURCE LINE 92
        __M_writer(mako_websafe('' if error_key in c.errors else 'display:none'))
        __M_writer(u'">\n')
        # SOURCE LINE 93
        if error_key in c.errors:
            # SOURCE LINE 94
            __M_writer(u'     ')
            __M_writer(mako_websafe(c.errors[error_key].message))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 96
        __M_writer(u'  </')
        __M_writer(mako_websafe(kind))
        __M_writer(u'>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_setup(context,extra_config=None):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 416
        __M_writer(u'\n  <script type="text/javascript" id="config">\n    r.setup(')
        # SOURCE LINE 418
        __M_writer(mako_websafe(unsafe(json.dumps(js_config(extra_config)))))
        __M_writer(u')\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_googleanalytics(context,uitype):
    context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 422
        __M_writer(u'\n')
        # SOURCE LINE 423
        if g.googleanalytics and thing.site_tracking:
            # SOURCE LINE 424
            __M_writer(u'  <script type="text/javascript">\n\n    var user_type = \'')
            # SOURCE LINE 426
            __M_writer(mako_websafe("guest" if not c.user_is_loggedin else "goldloggedin" if c.user.gold else "loggedin"))
            __M_writer(u"';\n    var _gaq = _gaq || [];\n    _gaq.push(\n        ['_setAccount', '")
            # SOURCE LINE 429
            __M_writer(mako_websafe(g.googleanalytics))
            __M_writer(u"'],\n        ['_setDomainName', '")
            # SOURCE LINE 430
            __M_writer(mako_websafe(g.domain))
            __M_writer(u"'],\n        ['_setCustomVar', 1, 'site', '")
            # SOURCE LINE 431
            __M_writer(mako_websafe(tracking.get_site()))
            __M_writer(u"', 3],\n        ['_setCustomVar', 2, 'srpath', '")
            # SOURCE LINE 432
            __M_writer(mako_websafe(tracking.get_srpath()))
            __M_writer(u"', 3],\n        ['_setCustomVar', 3, 'usertype', user_type, 2],\n        ['_setCustomVar', 4, 'uitype', '")
            # SOURCE LINE 434
            __M_writer(mako_websafe(uitype))
            __M_writer(u"', 3],\n        ['_trackPageview']\n    );\n\n    (function() {\n      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;\n      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';\n      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);\n    })();\n\n  </script>\n")
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_first_defined(context,*kw):
    context.caller_stack._push_frame()
    try:
        def first_defined(*kw):
            return render_first_defined(context,*kw)
        __M_writer = context.writer()
        # SOURCE LINE 83
        __M_writer(u'\n')
        # SOURCE LINE 84
        if not kw or kw[0] == UNDEFINED or not kw[0]:
            # SOURCE LINE 85
            __M_writer(mako_websafe(first_defined(kw[1:])))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_thing_timestamp(context,thing,since=None,live=False,include_tense=False):
    context.caller_stack._push_frame()
    try:
        def timestamp(date,since=None,live=False,include_tense=False):
            return render_timestamp(context,date,since,live,include_tense)
        __M_writer = context.writer()
        # SOURCE LINE 560
        __M_writer(u'\n')
        # SOURCE LINE 563
        __M_writer(u'  ')
        __M_writer(mako_websafe(timestamp(thing._date, since=since, live=live, include_tense=include_tense)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_inline_radio_type(context,field_name,val_name,text=None,checked=False):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 534
        __M_writer(u'\n\t')
        # SOURCE LINE 535
        full_name = field_name + "_" + val_name 
        
        __M_writer(u'\n\t<label>\n\t<input class="nomargin" type="radio" name="')
        # SOURCE LINE 537
        __M_writer(mako_websafe(field_name))
        __M_writer(u'"\n\t\tid="')
        # SOURCE LINE 538
        __M_writer(mako_websafe(full_name))
        __M_writer(u'" value="')
        __M_writer(mako_websafe(val_name))
        __M_writer(u'"\n')
        # SOURCE LINE 539
        if checked:
            # SOURCE LINE 540
            __M_writer(u'\t\t\tchecked="checked"\n')
            pass
        # SOURCE LINE 542
        __M_writer(u'\t>\n')
        # SOURCE LINE 543
        if text:
            # SOURCE LINE 544
            __M_writer(u'\t\t')
            __M_writer(mako_websafe(text))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 546
        __M_writer(u'\t</label>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_image_upload(context,post_target,current_image=None,onsubmit='',onchange='',label='',form_id='image-upload',ask_type=False,hidden_data=None):
    context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        def error_field(error_name,field_name,kind='span'):
            return render_error_field(context,error_name,field_name,kind)
        __M_writer = context.writer()
        # SOURCE LINE 310
        __M_writer(u'\n  <form id="')
        # SOURCE LINE 311
        __M_writer(mako_websafe(form_id))
        __M_writer(u'" enctype="multipart/form-data"\n        class="image-upload"\n        target="upload-iframe"\n')
        # SOURCE LINE 314
        if onsubmit:
            # SOURCE LINE 315
            __M_writer(u'           onsubmit="')
            __M_writer(mako_websafe(onsubmit))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 317
        __M_writer(u'        action="')
        __M_writer(mako_websafe(post_target))
        __M_writer(u'" method="post">\n')
        # SOURCE LINE 318
        if label:
            # SOURCE LINE 319
            __M_writer(u'         <label for="file">')
            __M_writer(mako_websafe(label))
            __M_writer(u'</label>\n')
            pass
        # SOURCE LINE 321
        __M_writer(u'          <input type="hidden" name="uh" value="')
        __M_writer(mako_websafe(c.modhash))
        __M_writer(u'" />\n')
        # SOURCE LINE 322
        if not c.default_sr:
            # SOURCE LINE 323
            __M_writer(u'            <input type="hidden" name="r"  value="')
            __M_writer(mako_websafe(c.site.name))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 325
        __M_writer(u'          <input type="hidden" name="formid" value="')
        __M_writer(mako_websafe(form_id))
        __M_writer(u'" />\n')
        # SOURCE LINE 326
        if hidden_data:
            # SOURCE LINE 327
            for name, value in hidden_data.iteritems():
                # SOURCE LINE 328
                __M_writer(u'              <input type="hidden" name="')
                __M_writer(mako_websafe(name))
                __M_writer(u'" value="')
                __M_writer(mako_websafe(value))
                __M_writer(u'" />\n')
                pass
            pass
        # SOURCE LINE 331
        __M_writer(u'          <br/>\n')
        # SOURCE LINE 332
        if ask_type:
            # SOURCE LINE 333
            __M_writer(u'            <label for="img_type">')
            __M_writer(mako_websafe(_("Type: ")))
            __M_writer(u'</label>\n            <label><input type="radio" name="img_type" value="jpg" />JPEG</label>\n            &nbsp;&nbsp;\n            <label><input type="radio" name="img_type" checked value="png" />PNG</label>\n            <br/>\n')
            pass
        # SOURCE LINE 339
        __M_writer(u'          <input type="file" name="file" id="file" \n                 onchange="$(this).next().show(); ')
        # SOURCE LINE 340
        __M_writer(mako_websafe(onchange))
        __M_writer(u'"/>\n          <button id="submit-img" class="submit-img"\n                  type="submit" name="upload" \n                  onclick="$(this).siblings(\'.img-status\').show().html(\'')
        # SOURCE LINE 343
        __M_writer(mako_websafe(_('uploading')))
        __M_writer(u'\'); return true;"\n                  style="display: none;" >\n            ')
        # SOURCE LINE 345
        __M_writer(mako_websafe(_('upload')))
        __M_writer(u'\n          </button>\n\n          <span style="display: none;" class="error img-status"></span>\n          ')
        # SOURCE LINE 349
        __M_writer(mako_websafe(error_field("IMAGE_ERROR", "span")))
        __M_writer(u'\n          <script type="text/javascript">\n       function on_image_success(img) {}\n       function create_new_image(name) {}\n\n       function completedUploadImage(status, img_src, name, errors, form_id) {\n           form_id = $.with_default(form_id, "')
        # SOURCE LINE 355
        __M_writer(mako_websafe(form_id))
        __M_writer(u'");\n           var form = $("#" + form_id);\n           if (status) \n               form.find(".img-status").show().html(status);\n           else\n               form.find(".img-status").hide().html("");\n           $.map(errors, function(e) {\n                   if(e[1]) \n                       form.find("." + e[0]).html(e[1]).show();\n                   else\n                       form.find("." + e[0]).html(\'\').hide();\n               });\n           if(img_src) {\n              form.get(0).reset();\n              var img = (name) ? $("#img-preview-" + name) :\n                  form.find("img.img-preview:first");\n              if(!$.defined(img) || img.length == 0) \n                  img = create_new_image(name);\n              if(img)\n                  img.attr("src", "").attr("src", img_src);\n              img.show().parent().show();\n              form.find(".delete-img").show();\n              form.find(".submit-img").hide();\n              on_image_success(img);\n          }\n       }\n          </script>\n          \n          <iframe src="about:blank" width="600" height="200" \n                  style="display: none;"\n                  name="upload-iframe" id="upload-iframe"></iframe>\n\n          <div id="img-preview-container" class="img-preview-container"\n               style="')
        # SOURCE LINE 388
        __M_writer(mako_websafe('' if current_image else 'display:none;'))
        __M_writer(u'">\n            <img id="img-preview-upload" alt="header preview" \n                 class="img-preview"\n')
        # SOURCE LINE 391
        if current_image:
            # SOURCE LINE 392
            __M_writer(u'                   src="')
            __M_writer(mako_websafe(current_image))
            __M_writer(u'"\n')
            # SOURCE LINE 393
        else:
            # SOURCE LINE 394
            __M_writer(u'                   src="')
            __M_writer(mako_websafe(static('kill.png')))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 396
        __M_writer(u'                 /><br />\n          </div>\n')
        # SOURCE LINE 398
        if caller:
            # SOURCE LINE 399
            __M_writer(u'       ')
            __M_writer(mako_websafe(caller.body()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 401
        __M_writer(u'  </form>\n  <script type="text/javascript">\n    $(function() {\n      var max_width = 0;\n      $(".preftable th *").each(function() {\n        max_width = Math.max(max_width, $(this).width());\n      }).each(function() {\n        $(this).width(max_width);\n      });\n    });\n       \n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_post_link(context,link_text,post_path,redir_path,params,_sr_path=True,nocname=False,fmt='',target='',**kw):
    context.caller_stack._push_frame()
    try:
        def _a_buffered(body,**kw):
            return render__a_buffered(context,body,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 160
        __M_writer(u'\n  ')
        # SOURCE LINE 161

        action = add_sr(post_path, sr_path=_sr_path, nocname=nocname)
        href = add_sr(redir_path, sr_path=_sr_path, nocname=nocname)
        if (not target or target == '_parent') and c.cname:
            target = '_top'
        if c.cname and redir_path.startswith('http://'):
            target = '_top'
        if target:
            kw['target'] = target
        onclick = "$(this).parent().submit(); return false;"
        link = _a_buffered(link_text, href=href, onclick=onclick, **kw)
          
        
        # SOURCE LINE 172
        __M_writer(u'\n  <form method="POST" action="')
        # SOURCE LINE 173
        __M_writer(mako_websafe(action))
        __M_writer(u'">\n')
        # SOURCE LINE 174
        for k, v in params.iteritems():
            # SOURCE LINE 175
            __M_writer(u'      <input type="hidden" name="')
            __M_writer(mako_websafe(k))
            __M_writer(u'" value="')
            __M_writer(mako_websafe(v))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 177
        __M_writer(u'    ')
        __M_writer(mako_websafe(unsafe((fmt % link) if fmt else link)))
        __M_writer(u'\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tags(context,**kw):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        for k, v in kw.iteritems():
            # SOURCE LINE 34
            if v:
                # SOURCE LINE 35
                __M_writer(u'    ')
                __M_writer(mako_websafe(k.strip('_')))
                __M_writer(u'="')
                __M_writer(mako_websafe(v))
                __M_writer(u'" ')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_block_field(context,kind,title,description='',css_class='',**kw):
    context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 487
        __M_writer(u'\n  <div class="')
        # SOURCE LINE 488
        __M_writer(mako_websafe(kind))
        __M_writer(u' ')
        __M_writer(mako_websafe(css_class))
        __M_writer(u'"\n')
        # SOURCE LINE 489
        for k, v in kw.iteritems():
            # SOURCE LINE 490
            __M_writer(u'         ')
            __M_writer(mako_websafe(k))
            __M_writer(u'="')
            __M_writer(mako_websafe(v))
            __M_writer(u'"\n')
            pass
        # SOURCE LINE 492
        __M_writer(u'       >\n    <span class="title">')
        # SOURCE LINE 493
        __M_writer(mako_websafe(title))
        __M_writer(u'</span>\n    &#32;\n')
        # SOURCE LINE 495
        if description:
            # SOURCE LINE 496
            __M_writer(u'      <span class="gray">')
            __M_writer(mako_websafe(description))
            __M_writer(u'</span>\n')
            pass
        # SOURCE LINE 498
        __M_writer(u'    <div class="')
        __M_writer(mako_websafe(kind))
        __M_writer(u'-content">\n      ')
        # SOURCE LINE 499
        __M_writer(mako_websafe(caller.body()))
        __M_writer(u'\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_submit_form(context,onsubmit='',action='',_class='',method='post',_id='',**params):
    context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 66
        __M_writer(u'\n<form class="')
        # SOURCE LINE 67
        __M_writer(mako_websafe(_class or ''))
        __M_writer(u'" onsubmit="')
        __M_writer(mako_websafe(onsubmit or ''))
        __M_writer(u'" \n      action="')
        # SOURCE LINE 68
        __M_writer(mako_websafe(action or ''))
        __M_writer(u'" ')
        __M_writer(mako_websafe(_id and "id='" + _id + "'" or ""))
        __M_writer(u' method="')
        __M_writer(mako_websafe(method))
        __M_writer(u'"\n')
        # SOURCE LINE 69
        if c.cname:
            # SOURCE LINE 70
            __M_writer(u'        target="_top"\n')
            pass
        # SOURCE LINE 72
        __M_writer(u'      >\n')
        # SOURCE LINE 73
        if c.user_is_loggedin:
            # SOURCE LINE 74
            __M_writer(u'  <input type="hidden" name="uh" value="')
            __M_writer(mako_websafe(c.user.modhash()))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 76
        for key, value in params.iteritems():
            # SOURCE LINE 77
            __M_writer(u'  <input type="hidden" name="')
            __M_writer(mako_websafe(key))
            __M_writer(u'" value="')
            __M_writer(mako_websafe(value))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 79
        __M_writer(u'  ')
        __M_writer(mako_websafe(caller.body()))
        __M_writer(u'\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_percentage(context,slice,total):
    context.caller_stack._push_frame()
    try:
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 566
        __M_writer(u'\n')
        # SOURCE LINE 567
        if total is None or total == "" or total == 0 or slice is None or slice == "":
            # SOURCE LINE 568
            __M_writer(u'    --\n')
            # SOURCE LINE 569
        else:
            # SOURCE LINE 570
            __M_writer(u'    ')
            __M_writer(mako_websafe(int(100 * slice / total)))
            __M_writer(u'%\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_plain_link(context,link_text,path,_sr_path=True,nocname=False,fmt='',target='',**kw):
    context.caller_stack._push_frame()
    try:
        def _a_buffered(body,**kw):
            return render__a_buffered(context,body,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 135
        __M_writer(u'\n')
        # SOURCE LINE 143
        __M_writer(u'  ')
 
        if (not target or target == '_parent') and c.cname:
            target = '_top'
        if c.cname and path and path.startswith('http://'):
            target = '_top'
        if target:
            kw['target'] = target
        
        link = _a_buffered(link_text, 
                           href=path and add_sr(path, sr_path=_sr_path, nocname=nocname),
                           **kw) 
          
        
        # SOURCE LINE 154
        __M_writer(u'\n\n  ')
        # SOURCE LINE 156
        __M_writer(mako_websafe(unsafe((fmt % link) if fmt else link)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__a(context,**kw):
    context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        def tags(**kw):
            return render_tags(context,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\n<a ')
        # SOURCE LINE 43
        __M_writer(mako_websafe(tags(**kw)))
        __M_writer(u'>')
        __M_writer(mako_websafe(caller.body()))
        __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_edited(context,thing,lastedited=None):
    context.caller_stack._push_frame()
    try:
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 588
        __M_writer(u'\n')
        # SOURCE LINE 589
        if isinstance(thing.editted, datetime):
            # SOURCE LINE 590
            __M_writer(u'    <time class="edited-timestamp" title="')
            __M_writer(mako_websafe(_('last edited')))
            __M_writer(u' ')
            __M_writer(mako_websafe(unsafe(lastedited or simplified_timesince(thing.editted))))
            __M_writer(u'" datetime="')
            __M_writer(mako_websafe(html_datetime(thing.editted)))
            __M_writer(u'">*</time>\n')
            # SOURCE LINE 591
        elif thing.editted:
            # SOURCE LINE 592
            __M_writer(u'    <em>*</em>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_ajax_upload(context,target,form_id):
    context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        def error_field(error_name,field_name,kind='span'):
            return render_error_field(context,error_name,field_name,kind)
        __M_writer = context.writer()
        # SOURCE LINE 276
        __M_writer(u'\n  <form method="post" enctype="multipart/form-data" target="')
        # SOURCE LINE 277
        __M_writer(mako_websafe(form_id))
        __M_writer(u'-iframe"\n        id="')
        # SOURCE LINE 278
        __M_writer(mako_websafe(form_id))
        __M_writer(u'" class="ajax-upload-form pretty-form" action="')
        __M_writer(mako_websafe(target))
        __M_writer(u'"\n        onsubmit="return post_multipart_form(this, \'')
        # SOURCE LINE 279
        __M_writer(mako_websafe(target))
        __M_writer(u'\')">\n    <input type="hidden" name="id" value="#')
        # SOURCE LINE 280
        __M_writer(mako_websafe(form_id))
        __M_writer(u'" />\n    <input type="hidden" name="uh" value="')
        # SOURCE LINE 281
        __M_writer(mako_websafe(c.modhash))
        __M_writer(u'" />\n    <input type="file" name="file" />\n    <button type="submit">\n      ')
        # SOURCE LINE 284
        __M_writer(mako_websafe(_('upload')))
        __M_writer(u'\n    </button>\n    ')
        # SOURCE LINE 286
        __M_writer(mako_websafe(error_field('IMAGE_ERROR', '')))
        __M_writer(u'\n')
        # SOURCE LINE 287
        if caller:
            # SOURCE LINE 288
            __M_writer(u'      ')
            __M_writer(mako_websafe(caller.body()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 290
        __M_writer(u'    <span class="status"></span>\n    <script type="text/javascript">\n      function completedUploadImage (status, img_src, name, errors, form_id) {\n        /* should only be called when the uploaded file is too large */\n        if (status == "failed") {\n          $("#')
        # SOURCE LINE 295
        __M_writer(mako_websafe(form_id))
        __M_writer(u'").find(".status").html("");\n          for (var i in errors) {\n            $("#')
        # SOURCE LINE 297
        __M_writer(mako_websafe(form_id))
        __M_writer(u'").find(".error." + errors[i][0])\n                .show().text(errors[i][1]);\n          }\n        }\n      }\n    </script>\n    <iframe src="about:blank" name="')
        # SOURCE LINE 303
        __M_writer(mako_websafe(form_id))
        __M_writer(u'-iframe" id="')
        __M_writer(mako_websafe(form_id))
        __M_writer(u'-iframe">\n    </iframe>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_optionalstyle(context,style):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 263
        __M_writer(u'\n')
        # SOURCE LINE 264
        if request.GET.get('style') != "off":
            # SOURCE LINE 265
            __M_writer(u'    style="')
            __M_writer(mako_websafe(style))
            __M_writer(u'"\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_language_checkboxes(context,default='all'):
    context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 220
        __M_writer(u'\n')
        # SOURCE LINE 221

        all_checked, some_checked = "checked='checked'", "" 
        if default != "all":
          all_checked, some_checked = some_checked, all_checked
        
        
        # SOURCE LINE 225
        __M_writer(u'\n<input type="radio" name="all-langs" id="all-langs" value="all"\n       onclick="clear_all_langs(this)" ')
        # SOURCE LINE 227
        __M_writer(mako_websafe(all_checked))
        __M_writer(u'/>\n<label for="all-langs">')
        # SOURCE LINE 228
        __M_writer(mako_websafe(_("all languages")))
        __M_writer(u'</label>\n<br/>\n<input type="radio" name="all-langs" id="some-langs" value="some"\n       ')
        # SOURCE LINE 231
        __M_writer(mako_websafe(some_checked))
        __M_writer(u'/>\n<label for="some-langs">')
        # SOURCE LINE 232
        __M_writer(mako_websafe(_("some languages")))
        __M_writer(u'</label>\n<hr/>\n<table>\n')
        # SOURCE LINE 235

        all_langs = [x for x in g.all_languages if len(x) == 2]
         
        
        # SOURCE LINE 237
        __M_writer(u'\n')
        # SOURCE LINE 238
        for col in cols(all_langs, 3):
            # SOURCE LINE 239
            __M_writer(u'  <tr>\n')
            # SOURCE LINE 240
            for lang in col:
                # SOURCE LINE 241
                __M_writer(u'    <td style="padding-right: 15px; white-space: nowrap;">\n    ')
                # SOURCE LINE 242

                idname = "lang-" + lang
                if default != "all" and lang in default:
                  checked = "checked='checked'"
                else:
                  checked = ""
                    
                
                # SOURCE LINE 248
                __M_writer(u'\n    <input type="checkbox" name="')
                # SOURCE LINE 249
                __M_writer(mako_websafe(idname))
                __M_writer(u'" id="')
                __M_writer(mako_websafe(idname))
                __M_writer(u'"\n           onclick="check_some_langs(this)" ')
                # SOURCE LINE 250
                __M_writer(mako_websafe(checked))
                __M_writer(u'/>\n    <label for="')
                # SOURCE LINE 251
                __M_writer(mako_websafe(idname))
                __M_writer(u'">')
                __M_writer(mako_websafe(g.lang_name[lang][0]))
                __M_writer(u'</label>\n    </td>\n')
                pass
            # SOURCE LINE 254
            __M_writer(u'  </tr>\n')
            pass
        # SOURCE LINE 256
        __M_writer(u'</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_timestamp(context,date,since=None,live=False,include_tense=False):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 549
        __M_writer(u'\n')
        # SOURCE LINE 552
        __M_writer(u'  ')

        timestamp_class = unsafe(' class="live-timestamp"') if live else ''
          
        
        # SOURCE LINE 554
        __M_writer(u'\n  <time title="')
        # SOURCE LINE 555
        __M_writer(mako_websafe(long_datetime(date)))
        __M_writer(u'" datetime="')
        __M_writer(mako_websafe(html_datetime(date)))
        __M_writer(u'"')
        __M_writer(mako_websafe(timestamp_class))
        __M_writer(u'>\n    ')
        # SOURCE LINE 556
        __M_writer(mako_websafe(unsafe(since or simplified_timesince(date, include_tense))))
        __M_writer(u'\n  </time>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_text_with_links(context,txt,_sr_path=False,nocname=False,**kw):
    context.caller_stack._push_frame()
    try:
        capture = context.get('capture', UNDEFINED)
        def plain_link(link_text,path,_sr_path=True,nocname=False,fmt='',target='',**kw):
            return render_plain_link(context,link_text,path,_sr_path,nocname,fmt,target,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 182
        __M_writer(u'\n')
        # SOURCE LINE 183

        from r2.lib.filters import _force_unicode
        for key, link_args in kw.iteritems():
           link_args.setdefault("_sr_path", _sr_path)
           link_args.setdefault("nocname", nocname)
           kw[key]=spaceCompress(capture(plain_link, **link_args))
        txt = _force_unicode(txt) % kw
        txt = txt.replace(" <", "&#32;<").replace("> ", ">&#32;")
        
        
        
        # SOURCE LINE 192
        __M_writer(u'\n')
        # SOURCE LINE 193
        __M_writer(mako_websafe(unsafe(txt)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_radio_type(context,field_name,val_name,title,text=None,checked=False):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 516
        __M_writer(u'\n  ')
        # SOURCE LINE 517
        full_name = field_name + "_" + val_name 
        
        __M_writer(u'\n  <tr>\n    <td class="nowrap nopadding">\n      <input name="')
        # SOURCE LINE 520
        __M_writer(mako_websafe(field_name))
        __M_writer(u'" type="radio" id="')
        __M_writer(mako_websafe(full_name))
        __M_writer(u'"\n             value="')
        # SOURCE LINE 521
        __M_writer(mako_websafe(val_name))
        __M_writer(u'" class="nomargin"\n')
        # SOURCE LINE 522
        if checked:
            # SOURCE LINE 523
            __M_writer(u'               checked="checked"\n')
            pass
        # SOURCE LINE 525
        __M_writer(u'             />\n      <label for="')
        # SOURCE LINE 526
        __M_writer(mako_websafe(full_name))
        __M_writer(u'">')
        __M_writer(mako_websafe(title))
        __M_writer(u'</label>\n    </td>\n')
        # SOURCE LINE 528
        if text:
            # SOURCE LINE 529
            __M_writer(u'      <td class="leftpad"><span class="gray">')
            __M_writer(mako_websafe(text))
            __M_writer(u'</span></td>\n')
            pass
        # SOURCE LINE 531
        __M_writer(u'  </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_line_field(context,title,description='',css_class='',**kw):
    context.caller_stack._push_frame()
    try:
        def block_field(kind,title,description='',css_class='',**kw):
            return render_block_field(context,kind,title,description,css_class,**kw)
        __M_writer = context.writer()
        # SOURCE LINE 510
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                # SOURCE LINE 511
                __M_writer(u'\n     ')
                # SOURCE LINE 512
                __M_writer(mako_websafe(caller.body()))
                __M_writer(u'\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 511
            __M_writer(mako_websafe(block_field('linefield', title, description = description, css_class= css_class, **kw)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 513
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_logout(context,top=False,dest=None,a_class=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 448
        __M_writer(u'\n  <form method="post" action="')
        # SOURCE LINE 449
        __M_writer(mako_websafe(add_sr('/logout', sr_path=False)))
        __M_writer(u'" class="logout hover"\n')
        # SOURCE LINE 450
        if top:
            # SOURCE LINE 451
            __M_writer(u'      target="_top"\n')
            pass
        # SOURCE LINE 453
        __M_writer(u'    >\n    <input type="hidden" name="uh" value="')
        # SOURCE LINE 454
        __M_writer(mako_websafe(c.modhash))
        __M_writer(u'"/>\n    <input type="hidden" name="top" value="')
        # SOURCE LINE 455
        __M_writer(mako_websafe('on' if top else 'off'))
        __M_writer(u'"/>\n')
        # SOURCE LINE 456
        if dest:
            # SOURCE LINE 457
            __M_writer(u'      <input type="hidden" name="dest" value="')
            __M_writer(mako_websafe(dest))
            __M_writer(u'"/>\n')
            pass
        # SOURCE LINE 459
        __M_writer(u'    \n    <a href="javascript:void(0)" onclick="$(this).parent().submit()"\n')
        # SOURCE LINE 461
        if a_class:
            # SOURCE LINE 462
            __M_writer(u'         class="')
            __M_writer(mako_websafe(a_class))
            __M_writer(u'" \n')
            pass
        # SOURCE LINE 464
        __M_writer(u'    >\n      ')
        # SOURCE LINE 465
        __M_writer(mako_websafe(_("logout")))
        __M_writer(u'\n    </a>\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_data(context,**data_attrs):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 60
        __M_writer(u'\n')
        # SOURCE LINE 61
        for name, value in data_attrs.iteritems():
            # SOURCE LINE 62
            __M_writer(u'data-')
            __M_writer(mako_websafe(name))
            __M_writer(u'="')
            __M_writer(mako_websafe(value))
            __M_writer(u'"\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_md(context,text,wrap=False):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 596
        __M_writer(u'\n  ')
        # SOURCE LINE 597
        __M_writer(mako_websafe(unsafe(safemarkdown(text, wrap=wrap))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_success_field(context,success_str,kind='p',successful=False,hide=''):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 99
        __M_writer(u'\n<')
        # SOURCE LINE 100
        __M_writer(mako_websafe(kind))
        __M_writer(u' class="error success">\n')
        # SOURCE LINE 101
        if successful:
            # SOURCE LINE 102
            __M_writer(u'  ')
            __M_writer(mako_websafe(success_str))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 104
        __M_writer(u'</')
        __M_writer(mako_websafe(kind))
        __M_writer(u'>\n<script type="text/javascript">\n  function fire_success() {\n  $(\'success\').innerHTML = "')
        # SOURCE LINE 107
        __M_writer(mako_websafe(success_str))
        __M_writer(u'";\n')
        # SOURCE LINE 108
        if hide:
            # SOURCE LINE 109
            __M_writer(u"  hide(document.getElementById('")
            __M_writer(mako_websafe(hide))
            __M_writer(u"'));\n")
            pass
        # SOURCE LINE 111
        __M_writer(u'  }\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_language_tool(context,name='lang',allow_blank=False,default_lang=g.lang,show_regions=False,all_langs=False):
    context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 199
        __M_writer(u'\n')
        # SOURCE LINE 200
 
        langs = g.all_languages if all_langs else g.languages 
        if not show_regions:
            langs = [x for x in langs if len(x) == 2]
        
        
        # SOURCE LINE 204
        __M_writer(u'\n')
        # SOURCE LINE 205
        if langs:
            # SOURCE LINE 206
            __M_writer(u'<select id="')
            __M_writer(mako_websafe(name))
            __M_writer(u'" name="')
            __M_writer(mako_websafe(name))
            __M_writer(u'">\n')
            # SOURCE LINE 207
            if allow_blank:
                # SOURCE LINE 208
                __M_writer(u'  <option ')
                __M_writer(mako_websafe((not default_lang) and "selected='selected'" or ""))
                __M_writer(u'>\n  </option>\n')
                pass
            # SOURCE LINE 211
            for x in langs:
                # SOURCE LINE 212
                __M_writer(u'  <option ')
                __M_writer(mako_websafe(x == default_lang  and "selected='selected'" or ""))
                __M_writer(u' value="')
                __M_writer(mako_websafe(x))
                __M_writer(u'">\n    ')
                # SOURCE LINE 213
                __M_writer(mako_websafe(g.lang_name[x][0]))
                __M_writer(u' [')
                __M_writer(mako_websafe(x))
                __M_writer(u'] ')
                __M_writer(mako_websafe(g.lang_name[x][1]))
                __M_writer(u'\n  </option>\n')
                pass
            # SOURCE LINE 216
            __M_writer(u'</select>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_classes(context,*class_names):
    context.caller_stack._push_frame()
    try:
        filter = context.get('filter', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\nclass="')
        # SOURCE LINE 57
        __M_writer(mako_websafe(" ".join(filter(None, class_names))))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_separator(context,separator_char):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 259
        __M_writer(u'\n  <span class="separator">')
        # SOURCE LINE 260
        __M_writer(mako_websafe(separator_char))
        __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__md(context,text,wrap=False):
    context.caller_stack._push_frame()
    try:
        def md(text,wrap=False):
            return render_md(context,text,wrap)
        __M_writer = context.writer()
        # SOURCE LINE 600
        __M_writer(u'\n  ')
        # SOURCE LINE 601
        __M_writer(mako_websafe(md(_(text), wrap=wrap)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render__id(context,arg):
    context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer(u'\nid="')
        # SOURCE LINE 53
        __M_writer(mako_websafe(arg))
        __M_writer(u'_')
        __M_writer(mako_websafe(thing and thing._fullname or ''))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


