var images = document.getElementsByTagName('img');

function replaceImage() {
	for (var i = 0, l = images.length; i < l; i++) {
		images[i].src = 'http://placekitten.com/' + images[i].width + '/' + images[i].height;
	}
}

function replaceText() {
	$("div._6m3:not(.clickblocked)").each(function(div) {
		console.log('changed')
		var a = $(this).find("> div > a, > a");
		var prev = null;
		var mouseOver = $(a).attr("onmouseover");
		if (mouseOver) {

			if (!prev) prev = a;
			else if (prev == a) return;
			prev = a;
			$(a).html("<div>This is my text</div>");
		}
		$(this).addClass('clickblocked');
	});
}

$(div._6m3 .clickblocked).hover(function() {

})
$(document).scroll(_.debounce(function() {
	replaceText();
}, 500));

//Initialize
replaceText();

/*
$(document).keypress(function(e) {
if(e.which == 13) {
replaceText();
}
}); */
