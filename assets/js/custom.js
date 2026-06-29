
(function() {
  function removeDropAnimation() {
    var nav = document.getElementById("primary-nav");
    if (nav) {
      nav.classList.remove("animated");
      nav.classList.remove("drop");
    }
  }

  removeDropAnimation();


  var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      if (mutation.attributeName === "class") {
        var nav = mutation.target;
        if (nav.classList.contains("animated") || nav.classList.contains("drop")) {
          nav.classList.remove("animated");
          nav.classList.remove("drop");
        }
      }
    });
  });

  var nav = document.getElementById("primary-nav");
  if (nav) {
    observer.observe(nav, { attributes: true });
  }

  setTimeout(removeDropAnimation, 100);
  setTimeout(removeDropAnimation, 300);
  setTimeout(removeDropAnimation, 500);
})();

document.addEventListener("DOMContentLoaded", function() {
  var nav = document.getElementById("primary-nav");
  if (nav) {
    nav.classList.remove("animated");
    nav.classList.remove("drop");
  }
});
