function editPop(url) {
  newwindow=window.open(url,'{{title}}','height=600,width=800');
  if (window.focus) {newwindow.focus()}
  return false;
}