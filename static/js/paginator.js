function getQuery(pgNbr) {

  let request = new XMLHttpRequest();
  let method = 'GET';
  let query = "?page=" + pgNbr
  let url = query;
  request.open(method, url);
  request.onload = function () {
    // the response is the rendered HTML
    // which django sends as return render(response, "your_template.html", context)
    let myHTML = request.response;
    var parser = new DOMParser();
    var doc = parser.parseFromString(myHTML, "text/html");
    console.log()
    // This is the important part
    // Set that HTML to the new, templated HTML returned by the server
    document.getElementById('pgDiv').innerHTML = doc.getElementById('pgDiv').innerHTML;
    document.getElementById('navElem').innerHTML = doc.getElementById('navElem').innerHTML;
  };
  request.send();
}
