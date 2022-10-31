function getQuery(pgNbr){
    x = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    const request = new Request('/' + "?page=" + pgNbr, {method: 'POST', body: formData, headers: {'X-CSRFToken': x}});
    const parser = new DOMParser();
    fetch(request)
    .then(response => response.text())
    .then(result => {
      var doc = parser.parseFromString(result, "text/html");
      document.getElementById('pgDiv').innerHTML = doc.getElementById('pgDiv').innerHTML;
      document.getElementById('navElem').innerHTML = doc.getElementById('navElem').innerHTML;
    })
  }