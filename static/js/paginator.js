function getQuery(pgNbr) {

  x = document.getElementsByName("csrfmiddlewaretoken")[0].value; 




  /*
  let request = new XMLHttpRequest();
  let method = 'GET'
  let query = "?page=" + pgNbr
  let url = query;
  request.open(method, url);
  request.setRequestHeader("X-CSRFToken",x);
  request.onload = function () {

    let myHTML = request.response;
    var parser = new DOMParser();
    var doc = parser.parseFromString(myHTML, "text/html");
    document.getElementById('pgDiv').innerHTML = doc.getElementById('pgDiv').innerHTML;
    document.getElementById('navElem').innerHTML = doc.getElementById('navElem').innerHTML;

  };
  request.send();
  */
}
