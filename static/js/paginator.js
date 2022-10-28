function getQuery(pgNbr){
  let formData = new FormData();
  formData.append('name', document.querySelector("#id_name").value);
  formData.append('type', document.querySelector("#id_type").value);
  formData.append('element', document.querySelector("#id_element").value);
  formData.append('administrators', document.querySelector("#id_administrators").value);
  formData.append('owner', document.querySelector("#id_owner").value);
  formData.append('build_after', document.querySelector("#id_build_after").value);
  if (document.querySelector("#id_archived").checked){formData.append('archived', document.querySelector("#id_archived").value);}
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