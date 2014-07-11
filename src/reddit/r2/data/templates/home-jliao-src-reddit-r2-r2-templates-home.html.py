# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405083566.046664
_template_filename='/home/jliao/src/reddit/r2/r2/templates/home.html'
_template_uri='/home.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = ['googleanalytics', 'stylesheet', 'javascript', 'javascript_bottom']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n<meta name="gwt:property" content="locale=en_US">\n<title>Peachtrees</title>\n<meta name="description" content="Peachtrees is a place for your interests. It lets you organize, explore and share everything you like.">\n    ')
        # SOURCE LINE 7
        __M_writer(mako_websafe(self.stylesheet()))
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(mako_websafe(self.javascript()))
        __M_writer(u'\n<!-- Google Analytics>\n    ')
        # SOURCE LINE 10
        __M_writer(mako_websafe(self.googleanalytics()))
        __M_writer(u'\n-->\n</head>\n\n<body id="home-body">\n\t<div id="content-container">\n\t\t<div id="background">\t\t\t\n\t\t</div>\n\t\t<div id=\'dimitriLarge\' class=\'waitforimages sprite-home-dimitriLarge\'></div>\n\t\t<div id="logo-carousel-signin-footer-container" class=\'waitforimages\'>\n\t\t\t<div id="logo-carousel-signin-footer-inner-container">\n\t\t\t\t<div id="logo-container">\n        \t\t    \t<div id="signin_button" class="form_button" onclick="PearltreesHomeSign.showPage(\'signin_page\');">\n        \t\t    \t<span>\u767b\u5f55</span>\n        \t\t    \t</div>\t\t\t\t    \n\t\t\t\t<p id= "logoText">\n\t\t\t\t\tPearltrees cultivate your interests\n\t\t\t\t</p>\n\t\t\t\t<div id="logo-inner-container">\n\t\t\t\t\t<div id=\'logoHome\' class=\'sprite-home-logoHomeWebEn\'></div>\t\t\t\t\t\t\t\t\t</div>\n\t\t\t</div>\n\t\t    <div id="carousel-signin-container">\n\t\t    ')
        # SOURCE LINE 32
        runtime._include_file(context, u'carousel.html', _template_uri)
        __M_writer(u'\n                    <div id ="signin-container">\n                        ')
        # SOURCE LINE 34
        runtime._include_file(context, u'signin.html', _template_uri)
        __M_writer(u'\n                        ')
        # SOURCE LINE 35
        runtime._include_file(context, u'signup.html', _template_uri)
        __M_writer(u'\n                        ')
        # SOURCE LINE 36
        runtime._include_file(context, u'invitation.html', _template_uri)
        __M_writer(u'\n                    </div>\n                </div>\n            </div>    \n\t</div>\n    </div>\n    ')
        # SOURCE LINE 42
        runtime._include_file(context, u'featurebar.html', _template_uri)
        __M_writer(u'\n    <div id="footer-container" class="waitforimages">\n    \t')
        # SOURCE LINE 44
        runtime._include_file(context, u'footer.html', _template_uri)
        __M_writer(u'\n    </div>\n\n\t<div class="modal fade" id="central-window" tabindex="-1" role="dialog" show="false" data-backdrop="true">\n\t    <div class="modal-dialog">\n\t        <div class="modal-content">\n\t            <div class="modal-header">\n\t                <div class="close-window sprite-common-close_window" data-dismiss="modal" aria-hidden="true"></div>\n\t                <h4 class="modal-title" id="myModalLabel"></h4>\n\t            </div>\n\t            <div class="modal-body">\n\t            </div>\n\t        </div><!-- /.modal-content -->\n\t    </div><!-- /.modal-dialog -->\n\t</div><!-- /.modal -->\n\t<form id="social-form" action="s/signup" method="post" target="" style="display:none">\n\t  username: <input type="text" name="username" id="form-username">\n\t  bio: <input type="text" name="bio" id="form-bio">\n\t  realname: <input type="text" name="realname" id="form-realname">\n\t  email: <input type="text" name="email" id="form-email">\n\t  signuptype: <input type="text" name="signuptype" id="form-signuptype"><br>\n\t  tid: <input type="text" name="tid" id="form-tid">\n\t  <input type="submit" value="Submit">\n\t</form>\n    ')
        # SOURCE LINE 68
        __M_writer(mako_websafe(self.javascript_bottom()))
        __M_writer(u'\n</body>\n\n</html>\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n\n')
        # SOURCE LINE 176
        __M_writer(u'\n\n')
        # SOURCE LINE 209
        __M_writer(u'\n\n')
        # SOURCE LINE 224
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_googleanalytics(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(u'\n   <script type="text/javascript">\n      // Initialize script\n      var _gaq = _gaq || [];\n      _gaq.push([\'_setAccount\', \'UA-22267644-1\']);\n         \n      // Don\'t send stats if the page load with the nostats param.\n      if(self.location.href.indexOf("nostats=1") != -1) {\n         noStats = true;\n      }\n      // Don\'t send stats if the embed preload embed window\n      else if(self.location.href.indexOf("/#/embedWindow=1") != -1) {\n         // no stats sent\n      }\n      else if(typeof noStats == "undefined" || !noStats) {\n         _gaq.push([\'_trackPageview\']);\n      }<link rel="stylesheet" href="../public/css/homePageStyle.css" type="text/css" media="screen" title="no title" charset="utf-8">\n      \n\n      (function() {\n         var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n         ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\n         var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n      })();\n   </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheet(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 211
        __M_writer(u'\n    <link href=\'http://fonts.googleapis.com/css?family=Open+Sans:400,300&subset=latin,latin-ext\' rel=\'stylesheet\' type=\'text/css\'>\n    <style>\n       @font-face {\n          font-family: "VollkornRegular";\n          src: url(\'http://cdn.pearltrees.com/v2/styles/font/Vollkorn-Regular.ttf\') format(\'truetype\');\n       }\n    </style>\n    <link rel="stylesheet" type="text/css" href="static/vendor/bootstrap.min.css">\n    <link rel="stylesheet" type="text/css" href="static/css/homePageStyle.css">\n    <link rel="stylesheet" type="text/css" href="static/css/homeSlideShowStyle.css">\n    <link rel="stylesheet" type="text/css" href="static/css/homeSignFormsStyle.css">\n    <link rel="stylesheet" type="text/css" href="static/css/custom_style.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 100
        __M_writer(u'\n    <script>\n    \tvar PearltreesLocale = 0;\n    \tvar PearltreesUserId = -1;\n    \tvar PearltreesRawData = false;\n    \tvar PearltreesInviteKey = "";\n    \tvar PearltreesRbRequestId = "";\n    \tvar PearltreesContext = 0;\n    \tvar PearltreesEmbed = false;\n    \tvar PearltreesMobileApp = false;\n    \tvar PearltreesOtherMobile = false;\n    \tvar PearltreesStartTime = new Date().getTime();\n    \tvar PearltreesBetaMode = false;\n    \tvar PearltreesV2User = false;\n    \tvar PearltreesAbTestParams = {\n    \t\t\thomeAndSignUpBanner: 1\n    \t};\n    </script>\n    <script>baseurl = "192.168.1.71";</script>\n    <script src="static/vendor/js/modernizr.js"></script>\n    <script src="static/vendor/js/jquery.min.js"></script>\n    <script src="static/vendor/js/require.js"></script>\n    <script src="static/vendor/js/jquery.placeholder.js"></script>\n    <script src="static/vendor/js/jquery.waitforimages.js"></script>    \n    <script>\n    $(window).load(function(){\n    \t$.getScript("static/js/homeall.js");\n    });\n\n    $(document).ready(function(){\n\n    \tvar identifier = window.location.hash; \n\t$(\'#signin_page\').hide();\n    \tif (identifier === "#login") {\n    \t\tPearltreesHomeSign.showPage(\'signin_page\');\n    \t}\n    \telse {\n    \t\tif (PearltreesHomeSpecial.isSpecialSignupFb()) {\n    \t\t\t$.getScript("http://crypto-js.googlecode.com/svn/tags/3.1.2/build/components/core-min.js", \n    \t\t\t\tfunction() {\n    \t\t\t\t\t$.getScript("http://crypto-js.googlecode.com/svn/tags/3.1.2/build/components/enc-utf16-min.js",\n    \t\t\t\t\t\tfunction() {\n    \t\t\t\t\t\t\t\t\t$.getScript("http://crypto-js.googlecode.com/svn/tags/3.1.2/build/components/enc-base64-min.js", function() {\n    \t\t\t\t\t\t\t\t\t\t\tPearltreesHomeSpecial.update();\n    \t\t\t\t\t\t\t\t\t\t\tPearltreesHomeSign.showPage(\'special-home-invitation-page\');\n    \t\t\t\t\t});\n    \t\t\t\t});\n    \t\t\t});\t\t\t\n    \t\t}\n    \t\t//else {\n    \t\t//\tPearltreesHomeSign.showPage(\'signup_page\');\n    \t\t//}\n    \t}\n    \t$(\'input, textarea\').placeholder();\n    \tPearltreesHomeSign.initPlaceholderFocusColor();\n    \tPearltreesHomeSign.initFormsValidation(\'#signup_form\', PearltreesHomeSign.fieldsToValidate);\n    \tPearltreesHomeSign.initUsernameSanitization(\'#username\', \'#username_error\');\n    \tPearltreesHomeSign.initSignUpSubmission();\n    \tPearltreesHomeSign.initTextFieldKeyPress();\n\t\n    \t$(\'html\').waitForImages({\n    \t\tfinished: function() {    \n    \t\t\t$(\'.waitforimages\').css(\'visibility\', \'visible\');\n    \t\t\t$(\'#homeAsset2\').attr( \'src\', \'static/homeAsset2.png\');\n    \t\t\t$(\'#homeAsset3\').attr( \'src\', \'static/homeAsset3.png\');\n    \t\t\t$(\'#homeAsset4\').attr( \'src\', \'static/homeAsset4.png\');\n    \t\t\t$(\'#homeAsset5\').attr( \'src\', \'static/homeAsset5.png\');\n    \t\t},\n    \t\teach: function() {\n\t\t\t\n    \t\t},\n\n    \t    waitForAll: true\n    \t});\n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_bottom(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 178
        __M_writer(u'\n    <script>\n\tPearltreesHomeCommon = {\n\t\t\tgetServicesUrl : function() {\n\t\t\t\treturn "http://www.pearltrees.com/s";\n\t\t\t},\n\t\t\tgetTunnelUrl : function() {\n\t\t\t\treturn "http://www.pearltrees.com/s/signup";\n\t\t\t},\n\t\t\t\n\t\t\tgetPublicUrl : function() {\n\t\t\t\treturn "http://www.pearltrees.com";\n\t\t\t},\n\t\t\t\n\t\t\tgetClientLang : function() {\n\t\t\t\treturn "en_US";\n\t\t\t}\n\t}\n\tPearltreesSignFormErrors = {\n\t\t\tserverError:"Something went wrong, please try again",\n\t\t\tusernameTooShort:"3 characters minimum",\n\t\t\tusernameTooLong:"40 characters maximum",\n\t\t\tusernameTaken:"username not available",\n\t\t\tmailInvalid:"enter a valid email",\n\t\t\tpasswordTooShort:"5 characters minimum",\n\t\t\tsigninIncorrect:"Username or password incorrect"\n\t}\n\t</script>\n    <script src="static/vendor/js/jquery.validate.min.js"></script>\n    <script src="static/js/signForm.js"></script>\n    <script src="static/js/inviteSignup.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


