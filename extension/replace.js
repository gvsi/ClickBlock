var images = document.getElementsByTagName('img');

function replaceImage() {
	for (var i = 0, l = images.length; i < l; i++) {
		images[i].src = 'http://placekitten.com/' + images[i].width + '/' + images[i].height;
	}
}

function replaceText() {
	$("div._6m3:not(.clickblocked)").each(function(div) {
		var a = $(this).find("> div > a, > a");
		var prev = null;
		var mouseOver = $(a).attr("onmouseover");
		if (mouseOver) {
			if (!prev) prev = a;
			else if (prev == a) return;
			prev = a;

			var mouseOverAttr =$(a).attr('onmouseover');
			var refPattern = /LinkshimAsyncLink.swap\(this\, \"(.*)\"\);/;
	    mouseOverAttr = mouseOverAttr.replace(/&quot;/g,'"');
	    var realHref = unescape(refPattern.exec(mouseOverAttr)[1]);
	    realHref = realHref.replace(/\\\//g, "/");

			console.log(realHref);

			$(a).html("<div>This is my text</div>");

			$(this).addClass('clickblocked');

			// $.ajax({
			//   type: "GET",
			//   url: "http://localhost:5000/verifybait",
			//   data: '{"link":'+ realHref + '}',
			//   success: function() {console.log('success')},
			//   dataType: "jsonp"
			// });

			data = {link: realHref};

			chrome.runtime.sendMessage({
			    method: 'POST',
					action: "xhttp",
			    url: 'https://cryptic-shelf-41509.herokuapp.com/verifybait',
			    data: data
			}, function(response) {
					console.log('me');
			    console.log(response);
					if (response) {
						$(a).html("<div>"+response["summary"]+"</div>");
					}
			    /*Callback function to deal with the response*/
			});

			// var xhr = new XMLHttpRequest();
			// xhr.open('POST', 'http://localhost:5000/verifybait', true);
			// xhr.setRequestHeader("Content-Type","application/json");
			// xhr.send(JSON.stringify(data));
			// xhr.onreadystatechange = function()
			// {
			//     if(xhr.readyState == 4 && xhr.status == 204)
			//     {
			//             //debugger;
			//             alert("Logged in");
			//             flag = 1;
			//             _callBack(xhr, xhr.readyState);
			//     }
			// }


			// $(this).hover(function () {
			// 	console.log('hover yo');
			// });
		}
	});
}
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
