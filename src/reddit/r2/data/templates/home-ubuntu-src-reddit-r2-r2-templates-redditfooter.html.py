# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1401918235.627544
_template_filename='/home/ubuntu/src/reddit/r2/r2/templates/redditfooter.html'
_template_uri='/redditfooter.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from r2.lib.filters import websafe, unsafe, mako_websafe
from pylons import c, g, request
from pylons.i18n import _, ungettext
_exports = []


# SOURCE LINE 23

from r2.lib.strings import strings
import datetime


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 27
    ns = runtime.TemplateNamespace('__anon_0x7f1dd5badd90', context._clean_inheritance_tokens(), templateuri=u'utils.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f1dd5badd90')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f1dd5badd90')._populate(_import_ns, [u'text_with_links'])
        thing = _import_ns.get('thing', context.get('thing', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        text_with_links = _import_ns.get('text_with_links', context.get('text_with_links', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n<div class="footer-parent">\n  <div by-zero class="footer rounded">\n')
        # SOURCE LINE 31
        for toolbar in thing.nav:
            # SOURCE LINE 32
            __M_writer(u'      <div class="col">\n        ')
            # SOURCE LINE 33
            __M_writer(mako_websafe(toolbar))
            __M_writer(u'\n      </div>\n')
            pass
        # SOURCE LINE 36
        __M_writer(u'  </div>\n')
        # SOURCE LINE 37
        if g.domain != "reddit.com":
            # SOURCE LINE 38
            __M_writer(u'    <!-- http://code.reddit.com/LICENSE see Exhibit B -->\n    <a href="http://www.reddit.com/code/" style="text-align:center;display:block">\n      <img src="https://s3.amazonaws.com/sp.reddit.com/powered_by_reddit.png"\n           alt="Powered by reddit."\n           style="width:140px; height:47px; margin-bottom: 5px"/>\n    </a>\n')
            pass
        # SOURCE LINE 45
        __M_writer(u'  <p class="bottommenu">\n    ')
        # SOURCE LINE 46
        __M_writer(mako_websafe(text_with_links(
            _("Use of this site constitutes acceptance of our "
              "%(user_agreement)s and %(privacy_policy)s"), nocname=True,
      user_agreement = dict(link_text=_("User Agreement {Genitive}"),
                            path="/help/useragreement"),
      privacy_policy = dict(link_text=_("Privacy Policy {Genitive}"),
                            path="/help/privacypolicy"))))
        # SOURCE LINE 52
        __M_writer(u'.\n    &copy; ')
        # SOURCE LINE 53
        __M_writer(mako_websafe(_("%(year)d reddit inc. All rights reserved.") % \
    dict(year=datetime.datetime.now().timetuple()[0])))
        # SOURCE LINE 54
        __M_writer(u'\n  </p>\n  <p class="bottommenu">REDDIT and the ALIEN Logo are registered trademarks of reddit inc.</p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


