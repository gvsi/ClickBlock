var images = document.getElementsByTagName('img');


function replaceText() {
	$("div._6m3:not(.clickblocked)").each(function(div) {
		var a = $(this).find("> div > a, > a");
		var prev = null;
		var mouseOver = $(a).attr("onmouseover");
		if (mouseOver) {
			var mouseOverAttr =$(a).attr('onmouseover');
			var refPattern = /LinkshimAsyncLink.swap\(this\, \"(.*)\"\);/;
	    mouseOverAttr = mouseOverAttr.replace(/&quot;/g,'"');
	    var realHref = unescape(refPattern.exec(mouseOverAttr)[1]);
	    realHref = realHref.replace(/\\\//g, "/");

			console.log(realHref);

			$(this).addClass('clickblocked');

			data = {link: realHref};

			chrome.runtime.sendMessage({
			    method: 'GET',
					action: "xhttp",
			    url: 'https://cryptic-shelf-41509.herokuapp.com/verifybait',
			    data: data
			}, function(response) {
					if (response && response['clickbait'] >= 0.60) {
						userContent = $(a).closest(":has(.userContent)").find('.userContent');
						userContent.html("<b>" + Math.round(response['clickbait'] * 100) + "% probability of being a clickbait</b> <br><br>" + response["summary"] + "<br><br><div class='tooltip'>Summary of the article<span class='tooltiptext'>"+response["long_summary"]+"</span></div>");

						var opacity = 0.20 * response['clickbait']
						$(a).closest(":has(._1dwg)").find('._1dwg').css("background-color", "rgba(255,0,0,"+opacity+")");
						$(a).closest(":has(._ohe)").find('._ohe').css("background-color", "rgba(255,0,0,"+opacity+")");

						console.log(response["summary"]);

						$(a).html("<div>Loading new title...</div>");
						$(a).html("<div>"+response["title"]+"</div>");
					}
			});
		}
	});
}
$(document).scroll(_.debounce(function() {
	replaceText();
}, 500));

//Initialize
replaceText();
