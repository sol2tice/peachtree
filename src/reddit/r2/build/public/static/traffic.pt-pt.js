r.traffic={init:function(){$("body").hasClass("traffic-sitewide")&&this.addSubredditSelector()},addSubredditSelector:function(){$("<form>").append($("<fieldset>").append($("<legend>").text(r._("view subreddit traffic")),$('<input type="text" id="srname">'),$('<input type="submit">').attr("value",r._("go")))).submit(r.traffic._onSubredditSelected).prependTo(".traffic-tables-side")},_onSubredditSelected:function(){var a=$(this.srname).val();window.location=window.location.protocol+"//"+r.config.cur_domain+
"/r/"+a+"/about/traffic";return!1}};$(function(){r.traffic.init()});
r.i18n.addMessages({"go": [null, "ir"]});