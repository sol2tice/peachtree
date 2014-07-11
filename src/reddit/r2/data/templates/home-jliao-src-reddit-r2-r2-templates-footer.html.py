# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1404039727.967762
_template_filename=u'/home/jliao/src/reddit/r2/r2/templates/footer.html'
_template_uri=u'/footer.html'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'        <div id="footer-container-placeholder">\n    \t\t<div id="footer-container-placeholder-inner">\n\t\t        <footer>\n\t\t            <a id=\'first_footer_link\' class=\'link\' href="https://itunes.apple.com/app/pearltrees/id463462134?mt=8" target="_blank">\n\t\t                iOS app</a>\n\t\t            <a class=\'link\' href="https://play.google.com/store/apps/details?id=com.pearltrees.android.prod" target="_blank">\n\t\t                Android app</a>\n\t\t            <a class=\'link\' href="http://www.pearltrees.com/s/faq/en" target="_blank">\n\t\t                FAQs</a>\n\t\t            <a class=\'link\' href="http://blog.pearltrees.com/" target="_blank">\n\t\t                Blog</a>\n\t\t            <a class=\'link\' href="http://blog.pearltrees.com/?page_id=6637" target="_blank">\n\t\t                Contact</a>\n\t\t            <a class=\'link\' href="http://blog.pearltrees.com/?page_id=8119" target="_blank">\n\t\t                Jobs</a>\n\t\t            <a class=\'link\' href="http://blog.pearltrees.com/?page_id=7414" target="_blank">\n\t\t                Press</a>\n\t\t            <a class=\'link\' href="http://www.pearltrees.com/s/premium/presentation?l=EN_US" target="_blank">\n\t\t                Premium</a>\n\t\t            <a id=\'last_footer_link\' class=\'link\' href="#popular_pearltrees" onclick="toggleLinks()">\n\t\t                More</a>\n\t\t            <div id="popular_pearltrees" class="items">\n\t\t                 <a id="first_link" href="/k/en/music" class="pearlTree">music</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/art" class="pearlTree">art</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/news" class="pearlTree">news</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/games" class="pearlTree">games</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/design" class="pearlTree">design</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/education" class="pearlTree">education</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/food" class="pearlTree">food</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/photography" class="pearlTree">photography</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/science" class="pearlTree">science</a> \n<a id="first_link" href="/k/en/shopping" class="pearlTree">shopping</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/tools" class="pearlTree">tools</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/travel" class="pearlTree">travel</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/recipes" class="pearlTree">recipes</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/web" class="pearlTree">web</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/books" class="pearlTree">books</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/twitter" class="pearlTree">Twitter</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/social-media" class="pearlTree">social media</a>&nbsp;<span class="bluedot">&bull;</span>&nbsp;<a href="/k/en/health" class="pearlTree">health</a>\n                     </div>\n\t\t        </footer>\n\t        </div>\n        </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


