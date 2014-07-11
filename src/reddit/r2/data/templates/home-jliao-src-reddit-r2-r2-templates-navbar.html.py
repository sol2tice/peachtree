# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1405082276.118093
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/navbar.html'
_template_uri=u'/navbar.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

        items = [
            (u'留学在线问答', '/forum', 'static/messages.png', 'Messages'),
            (u'美国大学搜索', '/college_search', 'static/videocall.png', 'Video &amp; Voice Calls'),
            (u'留美录取申请', '/college_admission', 'static/channels_icon.png', 'Channels'),
            (u'留学校园生活', '/college_life', 'static/photo.png', 'Photo Sharing'),
            (u'美国高中生夏令营', '/summercamp', 'static/music.png', 'Music'),
            (u'专家升学指导', '/consulting', 'static/games.png', 'Games')
        ]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['items'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 10
        __M_writer(u'\n<nav class="navbar navbar-default" role="navigation" style="margin-bottom: 10px">\n\t<div class="navbar-header">\n\t    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".sidebar-collapse">\n\t\t<span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n           \t<span class="icon-bar"></span>\n           \t<span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand" href="index.html"> <img alt="PeachTree Logo" src="static/blog_snoo.gif" /> <span></span></a>\n  \t</div>\n\t<!-- /.navbar-header -->\n\t<ul class="nav navbar-nav">\n')
        # SOURCE LINE 23
        for i, item in enumerate(items):
            # SOURCE LINE 24
            __M_writer(u'            <li>')
            # SOURCE LINE 25
            __M_writer(u'            <a href="')
            __M_writer(mako_websafe(item[1]))
            __M_writer(u'">')
            __M_writer(mako_websafe(item[0]))
            __M_writer(u'</a>\n\t    </li>\n')
            pass
        # SOURCE LINE 28
        __M_writer(u'\t</ul>\n')
        # SOURCE LINE 29
        if c.user_is_loggedin:
            # SOURCE LINE 30
            __M_writer(u'    <ul class="nav navbar-top-links navbar-right">\n        <li class="dropdown">\n            <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n                <i class="fa fa-envelope fa-fw"></i>  <i class="fa fa-caret-down"></i>\n            </a>\n            <ul class="dropdown-menu dropdown-messages">\n                <li>\n                    <a href="#">\n                        <div>\n                            <strong>John Smith</strong>\n                            <span class="pull-right text-muted">\n                                <em>Yesterday</em>\n                            </span>\n                        </div>\n                        <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eleifend...</div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a href="#">\n                        <div>\n                            <strong>John Smith</strong>\n                            <span class="pull-right text-muted">\n                                <em>Yesterday</em>\n                            </span>\n                        </div>\n                        <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eleifend...</div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a href="#">\n                        <div>\n                            <strong>John Smith</strong>\n                            <span class="pull-right text-muted">\n                                <em>Yesterday</em>\n                            </span>\n                        </div>\n                        <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eleifend...</div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a class="text-center" href="#">\n                        <strong>Read All Messages</strong>\n                        <i class="fa fa-angle-right"></i>\n                    </a>\n                </li>\n            </ul>\n            <!-- /.dropdown-messages -->\n        </li>\n        <!-- /.dropdown -->\n        <li class="dropdown">\n            <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n                <i class="fa fa-tasks fa-fw"></i>  <i class="fa fa-caret-down"></i>\n            </a>\n            <ul class="dropdown-menu dropdown-tasks">\n                <li>\n                    <a href="#">\n                        <div>\n                            <p>\n                                <strong>Task 1</strong>\n                                <span class="pull-right text-muted">40% Complete</span>\n                            </p>\n                            <div class="progress progress-striped active">\n                                <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: 40%">\n                                    <span class="sr-only">40% Complete (success)</span>\n                                </div>\n                            </div>\n                        </div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a href="#">\n                        <div>\n                            <p>\n                                <strong>Task 2</strong>\n                                <span class="pull-right text-muted">20% Complete</span>\n                            </p>\n                            <div class="progress progress-striped active">\n                                <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 20%">\n                                    <span class="sr-only">20% Complete</span>\n                                </div>\n                            </div>\n                        </div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a href="#">\n                        <div>\n                            <p>\n                                <strong>Task 3</strong>\n                                <span class="pull-right text-muted">60% Complete</span>\n                            </p>\n                            <div class="progress progress-striped active">\n                                <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">\n                                    <span class="sr-only">60% Complete (warning)</span>\n                                </div>\n                            </div>\n                        </div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a href="#">\n                        <div>\n                            <p>\n                                <strong>Task 4</strong>\n                                <span class="pull-right text-muted">80% Complete</span>\n                            </p>\n                            <div class="progress progress-striped active">\n                                <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 80%">\n                                    <span class="sr-only">80% Complete (danger)</span>\n                                </div>\n                            </div>\n                        </div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a class="text-center" href="#">\n                        <strong>See All Tasks</strong>\n                        <i class="fa fa-angle-right"></i>\n                    </a>\n                </li>\n            </ul>\n            <!-- /.dropdown-tasks -->\n        </li>\n        <!-- /.dropdown -->\n        <li class="dropdown">\n            <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n                <i class="fa fa-bell fa-fw"></i>  <i class="fa fa-caret-down"></i>\n            </a>\n            <ul class="dropdown-menu dropdown-alerts">\n                <li>\n                    <a href="#">\n                        <div>\n                            <i class="fa fa-comment fa-fw"></i> New Comment\n                            <span class="pull-right text-muted small">4 minutes ago</span>\n                        </div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a href="#">\n                        <div>\n                            <i class="fa fa-twitter fa-fw"></i> 3 New Followers\n                            <span class="pull-right text-muted small">12 minutes ago</span>\n                        </div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a href="#">\n                        <div>\n                            <i class="fa fa-envelope fa-fw"></i> Message Sent\n                            <span class="pull-right text-muted small">4 minutes ago</span>\n                        </div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a href="#">\n                        <div>\n                            <i class="fa fa-tasks fa-fw"></i> New Task\n                            <span class="pull-right text-muted small">4 minutes ago</span>\n                        </div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a href="#">\n                        <div>\n                            <i class="fa fa-upload fa-fw"></i> Server Rebooted\n                            <span class="pull-right text-muted small">4 minutes ago</span>\n                        </div>\n                    </a>\n                </li>\n                <li class="divider"></li>\n                <li>\n                    <a class="text-center" href="#">\n                        <strong>See All Alerts</strong>\n                        <i class="fa fa-angle-right"></i>\n                    </a>\n                </li>\n            </ul>\n            <!-- /.dropdown-alerts -->\n        </li>\n        <!-- /.dropdown -->\n        <li class="dropdown">\n            <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n                <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>\n            </a>\n            <ul class="dropdown-menu dropdown-user">\n                <li><a href="#"><i class="fa fa-user fa-fw"></i> User Profile</a>\n                </li>\n                <li><a href="#"><i class="fa fa-gear fa-fw"></i> Settings</a>\n                </li>\n                <li class="divider"></li>\n                <li><a href="login.html"><i class="fa fa-sign-out fa-fw"></i> Logout</a>\n                </li>\n            </ul>\n            <!-- /.dropdown-user -->\n        </li>\n        <!-- /.dropdown -->\n    </ul>\n')
            # SOURCE LINE 238
        else:
            # SOURCE LINE 239
            __M_writer(u'    <ul class="nav navbar-top-links navbar-right">\n        <li class="dropdown">\n            <a href="#" class="dropdown-toggle" data-toggle="dropdown"><small>Have an account?</small> Sign in<span class="caret"></span></a> \n            <div class="dropdown-menu dropdown-form" id="signin-dropdown">\n            ')
            # SOURCE LINE 243
            runtime._include_file(context, u'signin.html', _template_uri)
            __M_writer(u' \n\t    ')
            # SOURCE LINE 244
            runtime._include_file(context, u'signup.html', _template_uri)
            __M_writer(u'\n\t    </div>\n        </li>\n    </ul>\n')
            pass
        # SOURCE LINE 249
        __M_writer(u'</nav>\t\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


