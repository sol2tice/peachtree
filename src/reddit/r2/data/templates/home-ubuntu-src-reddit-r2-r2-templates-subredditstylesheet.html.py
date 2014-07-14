# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402129408.49811
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/subredditstylesheet.html'
_template_uri='/subredditstylesheet.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['make_li']


# SOURCE LINE 23

from r2.lib.filters import keep_space
from r2.lib.template_helpers import add_sr, static
import os



def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 29
    ns = runtime.TemplateNamespace('__anon_0x7fabdc738410', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fabdc738410')] = ns

    # SOURCE LINE 30
    ns = runtime.TemplateNamespace('__anon_0x7fabdc738910', context._clean_inheritance_tokens(), templateuri=u'printablebuttons.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fabdc738910')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabdc738410')._populate(_import_ns, [u'error_field', u'image_upload'])
        _mako_get_namespace(context, '__anon_0x7fabdc738910')._populate(_import_ns, [u'ynbutton', u'toggle_button'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        image_upload = _import_ns.get('image_upload', context.get('image_upload', UNDEFINED))
        def make_li(name='',img=None,prototype=False):
            return render_make_li(context.locals_(__M_locals),name,img,prototype)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n<div class="stylesheet-customize-container">\n  <form\n     onsubmit="return post_form(this, \'subreddit_stylesheet\')"\n     name="subreddit_stylesheet" id="subreddit_stylesheet"\n     class="pretty-form sr-form"\n     action="/post/subreddit_stylesheet" method="post" >\n    \n  <input type="hidden" name="r"  value="')
        # SOURCE LINE 39
        __M_writer(mako_websafe(thing.site.name))
        __M_writer(u'" />\n  <input type="hidden" name="op"  value="" />\n\n  <h2>')
        # SOURCE LINE 42
        __M_writer(mako_websafe(_("stylesheet")))
        __M_writer(u'</h2>\n  <div class="sheets">\n    <div class="col">\n      <div>\n        <textarea\n           rows="20"\n           cols="20"\n           id="stylesheet_contents"\n           name="stylesheet_contents"\n           >\n          ')
        # SOURCE LINE 52
        __M_writer(mako_websafe(keep_space(thing.stylesheet_contents) or ''))
        __M_writer(u'\n        </textarea>\n        <div>\n            <label for="reason">')
        # SOURCE LINE 55
        __M_writer(mako_websafe(_('reason for revision')))
        __M_writer(u'</label>\n            <input type="text" name="reason" maxlength="256">\n')
        # SOURCE LINE 57
        if thing.site.prev_stylesheet:
            # SOURCE LINE 58
            __M_writer(u'                <span class="btn right"><a target="_blank" href="')
            __M_writer(mako_websafe(add_sr("/wiki/revisions/config/stylesheet/")))
            __M_writer(u'">')
            __M_writer(mako_websafe(_("see previous versions")))
            __M_writer(u'</a></span>\n')
            pass
        # SOURCE LINE 60
        __M_writer(u'        </div>\n      </div>\n    </div>\n    <div class="clearleft"></div>\n    <div class="buttons">\n      <button class="btn" name="save" type="submit" \n             onclick="this.form.op.value=\'save\'; return true;">\n        ')
        # SOURCE LINE 67
        __M_writer(mako_websafe(_('save')))
        __M_writer(u'\n      </button>\n      <button class="btn" name="preview" type="submit" \n             onclick="this.form.op.value=\'preview\'; return true;">\n        ')
        # SOURCE LINE 71
        __M_writer(mako_websafe(_('preview')))
        __M_writer(u'\n      </button>\n      <span class="status error"></span>\n    </div>\n  </div>\n  <div class="errors" style="display:none">\n    <h2>')
        # SOURCE LINE 77
        __M_writer(mako_websafe(_("errors")))
        __M_writer(u'</h2>\n    <ul><li></li>\n      <!-- populated from AJAX requests to /api/subreddit_stylesheet -->\n    </ul>\n  </div>\n  \n  </form>\n\n  <div id="preview-table" style="display:none">\n    <h2><a name="preview">')
        # SOURCE LINE 86
        __M_writer(mako_websafe(_("preview")))
        __M_writer(u'</a></h2>\n    <table>\n      <tr>\n        <th>')
        # SOURCE LINE 89
        __M_writer(mako_websafe(_("normal link")))
        __M_writer(u'</th>\n        <td id="preview_link_normal"></td>\n      </tr>\n      <tr>\n        <th>')
        # SOURCE LINE 93
        __M_writer(mako_websafe(_("compressed link")))
        __M_writer(u'</th>\n        <td id="preview_link_compressed"></td>\n      </tr>\n      <tr>\n        <th>')
        # SOURCE LINE 97
        __M_writer(mako_websafe(_("link with thumbnail")))
        __M_writer(u'</th>\n        <td id="preview_link_media"></td>\n      </tr>\n      <tr>\n        <th>')
        # SOURCE LINE 101
        __M_writer(mako_websafe(_("stickied link")))
        __M_writer(u'</th>\n        <td id="preview_link_stickied"></td>\n      </tr>\n      <tr>\n        <th>')
        # SOURCE LINE 105
        __M_writer(mako_websafe(_("comment")))
        __M_writer(u'</th>\n        <td id="preview_comment"></td>\n      </tr>\n      <tr>\n        <th>')
        # SOURCE LINE 109
        __M_writer(mako_websafe(_("gilded comment")))
        __M_writer(u'</th>\n        <td id="preview_comment_gilded"></td>\n      </tr>\n    </table>\n  </div>\n\n  <div id="images">\n    <h2><a name="images">')
        # SOURCE LINE 116
        __M_writer(mako_websafe(_("images")))
        __M_writer(u'</a></h2>\n\n  ')
        def ccall(caller):
            def body():
                error_field = _import_ns.get('error_field', context.get('error_field', UNDEFINED))
                __M_writer = context.writer()
                # SOURCE LINE 120
                __M_writer(u'\n    \n    <br/>\n    <label for="img-name">')
                # SOURCE LINE 123
                __M_writer(mako_websafe(_("new image name:")))
                __M_writer(u'</label>\n    <input id="img-name" name="name" value="" type="text"/>\n    ')
                # SOURCE LINE 125
                __M_writer(mako_websafe(error_field("BAD_CSS_NAME", "name")))
                __M_writer(u'\n    <br/>\n    <span class="little gray">\n      ')
                # SOURCE LINE 128
                __M_writer(mako_websafe(_("(image names should consist of alphanumeric characters and '-' only)")))
                __M_writer(u'\n    </span>\n  ')
                return ''
            return [body]
        __M_caller = context.caller_stack._get_caller()
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            # SOURCE LINE 118
            __M_writer(mako_websafe(image_upload('/api/upload_sr_img', '', 
                              onchange='return file_changed(this)',
                              label = _('image file'), ask_type=True)))
        finally:
            context.caller_stack.nextcaller = None
        # SOURCE LINE 130
        __M_writer(u'\n<p class="error">\n  ')
        # SOURCE LINE 132
        __M_writer(mako_websafe(_("Note: any changes to images here will be reflected immediately on reload and cannot be undone.")))
        __M_writer(u'\n</p>\n    <script type="text/javascript">\n      /* <![CDATA[ */\n        function create_new_image(name) {\n              var list = $(".image-list:first");\n              var new_li = list.children("li:first")\n                  .clone(true).attr("id", "")\n                  .find(".img-name").html(name).end()\n                  .find(".img-url").html("url(%%" + name + "%%)").end()\n                  .find("form input[name=img_name]").val(name).end()\n                  .find("img").attr("id", "img-preview-" + name).end();\n              \n              list.append(new_li);\n              img = new_li.find("img");\n              \n              $("#old-names").append("<option>" + name + "</option>");\n              return img;           \n        }\n\n        function on_image_success(img) {\n           $(img).parents("li:first").fadeIn();\n           $(img).parent("a").attr("href", $(img).attr("src"));\n        }\n\n\n        function too_big() {\n            $(".IMAGE_ERROR").innerHTML = "image too big: there is a 500k cap";\n            $(".img-status").innerHTML = "";\n        }\n\n        function paste_url(source) {\n            var txt = $(source).siblings("pre:first").html();\n            $("#stylesheet_contents").insertAtCursor(txt);\n            return false; \n        }\n        function delete_img(button) {\n            $(button).parents("li:first").fadeOut(function() {\n                $(this).remove();\n            })\n        }\n        function file_changed(file_input) {\n            $("#submit-header-img").show();\n            $(".img-status").html("");\n            if(file_input.value) {\n                if(! $(\'#img-name\').val()) {\n                   var f = file_input.value\n                        .replace(/.*[\\/\\\\]/, "").split(\'.\')[0]\n                        .replace(/[ _]/g, "-");\n                    $(\'#img-name\').val(f);\n                }\n\n                var ext = file_input.value\n                    .split(\'.\').pop().toLowerCase()\n                    .replace("jpeg", "jpg");\n                if (ext == \'png\' || ext == \'jpg\') {\n                    $(\'input:radio[name=img_type]\').attr(\'checked\', false);\n                    $(\'input:radio[name=img_type][value="\' + ext + \'"]\').attr(\'checked\', true);\n                }\n            }\n        }\n        function check_name(form) {\n           var name = form.name.value;\n           var r = new RegExp(/[^a-zA-Z0-9\\-]/);\n           if (name == "" || name.match(r)) { \n              $(".img-status").html("").hide();\n              $(".BAD_CSS_NAME").show().html("')
        # SOURCE LINE 198
        __M_writer(mako_websafe(_('bad image name')))
        __M_writer(u'");\n              return false; \n           }\n           else if(form.srfile.value) {\n              $(".BAD_CSS_NAME").html("").hide();\n              $(".IMAGE_ERROR").html("").hide();\n              return true;\n           } else {\n              $(".img-status").html("").hide();\n              $(".IMAGE_ERROR").show().html("')
        # SOURCE LINE 207
        __M_writer(mako_websafe(_('please select an image')))
        __M_writer(u'");\n              return false; \n           }\n        }\n    /* ]]> */\n    </script>\n    <ul id="image-preview-list" class="image-list">\n      ')
        # SOURCE LINE 237
        __M_writer(u'\n      ')
        # SOURCE LINE 238
        __M_writer(mako_websafe(make_li(prototype=True)))
        __M_writer(u'\n')
        # SOURCE LINE 239
        for name, url in thing.images.iteritems():
            # SOURCE LINE 240
            __M_writer(u'         ')
            __M_writer(mako_websafe(make_li(name=name, img=url)))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 242
        __M_writer(u'    </ul>\n\n    <iframe src="about:blank" width="600" height="200" style="display: none;"\n            name="upload-iframe" id="upload-iframe"></iframe>\n    \n  </div>\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_make_li(context,name='',img=None,prototype=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fabdc738410')._populate(_import_ns, [u'error_field', u'image_upload'])
        _mako_get_namespace(context, '__anon_0x7fabdc738910')._populate(_import_ns, [u'ynbutton', u'toggle_button'])
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        ynbutton = _import_ns.get('ynbutton', context.get('ynbutton', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 214
        __M_writer(u'\n        <li ')
        # SOURCE LINE 215
        __M_writer(mako_websafe("style='display:none'" if img is None else ""))
        __M_writer(u'>\n          <a href="')
        # SOURCE LINE 216
        __M_writer(mako_websafe(img))
        __M_writer(u'" class="preview">\n            <img id="img-preview-')
        # SOURCE LINE 217
        __M_writer(mako_websafe(name))
        __M_writer(u'" src="')
        __M_writer(mako_websafe(img))
        __M_writer(u'" \n                 alt="Image ')
        # SOURCE LINE 218
        __M_writer(mako_websafe(name))
        __M_writer(u'" title="click to preview"/>\n          </a>\n          <div class="description">\n            <b class="img-name">\n              ')
        # SOURCE LINE 222
        __M_writer(mako_websafe(name))
        __M_writer(u'\n            </b>\n            <br/>\n            <span>link:</span>\n            <pre class="img-url">url(%%')
        # SOURCE LINE 226
        __M_writer(mako_websafe(name))
        __M_writer(u'%%)</pre>\n            <br/>\n            <a href="javascript:void(0)" onclick="return paste_url(this)">\n              ')
        # SOURCE LINE 229
        __M_writer(mako_websafe(_("paste into stylesheet")))
        __M_writer(u'\n            </a>\n            <br/>\n            ')
        # SOURCE LINE 232
        __M_writer(mako_websafe(ynbutton(_("delete this image"), _("deleted"),
                       "delete_sr_img", callback = "delete_img",
                        hidden_data = dict(img_name = name))))
        # SOURCE LINE 234
        __M_writer(u'\n          </div>\n        </li>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


