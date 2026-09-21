/**
 * Affiche le poster immédiatement ; charge la vidéo en arrière-plan.
 * Réduit le flash blanc / latence perçue sur 4G.
 */
(function () {
  function enhanceVideos() {
    var videos = document.querySelectorAll(".w-background-video video, .background-video video, .background-video-phone video");
    for (var i = 0; i < videos.length; i++) {
      var v = videos[i];
      try {
        v.setAttribute("playsinline", "");
        v.muted = true;
        // Poster déjà en CSS / attribut — forcer un paint rapide
        if (v.getAttribute("poster")) {
          v.style.backgroundImage = "url('" + v.getAttribute("poster").replace(/'/g, "\\'") + "')";
          v.style.backgroundSize = "cover";
          v.style.backgroundPosition = "center";
        }
        var play = v.play();
        if (play && typeof play.catch === "function") play.catch(function () {});
      } catch (e) {}
    }
  }

  function reveal() {
    document.body.classList.add("nuskow-ix-fallback");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enhanceVideos);
  } else {
    enhanceVideos();
  }

  window.addEventListener("load", function () {
    setTimeout(reveal, 900);
  });
  setTimeout(reveal, 2500);
})();
