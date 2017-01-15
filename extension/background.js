chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  // chrome.extension.getBackgroundPage().console.log('yo background')
  if (request.action == "xhttp") {

    // chrome.extension.getBackgroundPage().console.log(request.data)
    $.ajax({
      type: 'POST',
      url: request.url,
      data: request.data,
      success: function(data) {console.log(data); sendResponse(data)},
      error: function(err) {console.log(err);},
      dataType: "jsonp",
    });

    return true;
    // sendResponse(d);

    //
    // var xhr = new XMLHttpRequest();
    // xhr.open('POST', 'http://localhost:5000/verifybait', true);
    // xhr.setRequestHeader("Content-Type","application/json");
    // xhr.send(request.data);
    // xhr.onreadystatechange = function()
    // {
    //     if(xhr.readyState == 4 && xhr.status == 204)
    //     {
    //             callback({msg: "okkk"})
    //     }
    // }
  }
});
