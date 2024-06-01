document.addEventListener("DOMContentLoaded", function() {
  function update_header_col(elem, color) {
    elem.style.color = color;
  }
  let header_color = document.querySelector("header");
  update_header_col(header_color, "#FF0000");
});
