// Rimuove l'animazione drop dalla navbar
document.addEventListener("DOMContentLoaded", function() {
  var nav = document.getElementById("primary-nav");
  if (nav) {
    nav.classList.remove("animated");
    nav.classList.remove("drop");
  }
});
