/**
 * Infinite logo marquees — duplicates logo groups until the track
 * always covers the viewport, then animates by exactly one group width.
 */
(function () {
  function measureShift(track, base) {
    var styles = window.getComputedStyle(track);
    var gap = parseFloat(styles.columnGap || styles.gap || "0") || 0;
    return base.offsetWidth + gap;
  }

  function fill(track) {
    var wrap = track.parentElement;
    if (!wrap) return;
    var base = track.querySelector(".cx-marquee__group");
    if (!base) return;

    Array.prototype.slice.call(track.querySelectorAll(".cx-marquee__group")).forEach(function (g, i) {
      if (i > 0) g.remove();
    });

    var need = Math.max(wrap.clientWidth * 2.4, base.offsetWidth * 2 + 1);
    var guard = 0;
    while (track.scrollWidth < need && guard < 14) {
      var clone = base.cloneNode(true);
      clone.setAttribute("aria-hidden", "true");
      clone.querySelectorAll("[alt]").forEach(function (img) {
        img.setAttribute("alt", "");
      });
      track.appendChild(clone);
      guard += 1;
    }

    var shift = measureShift(track, base);
    track.style.setProperty("--cx-marquee-shift", shift + "px");
    var duration = Math.max(20, Math.round(shift / 26));
    track.style.setProperty("--cx-marquee-duration", duration + "s");
    track.dataset.marqueeReady = "1";
  }

  function initTrack(track) {
    if (!track || track.dataset.marqueeInit === "1") return;
    track.dataset.marqueeInit = "1";

    var items = Array.prototype.slice.call(track.children);
    if (!items.length) return;

    if (!track.querySelector(".cx-marquee__group")) {
      var group = document.createElement("div");
      group.className = "cx-marquee__group";
      items.forEach(function (el) {
        group.appendChild(el);
      });
      track.appendChild(group);
    }

    function run() {
      fill(track);
    }

    run();

    var imgs = track.querySelectorAll("img");
    var pending = 0;
    imgs.forEach(function (img) {
      if (img.complete) return;
      pending += 1;
      img.addEventListener("load", function () {
        pending -= 1;
        if (pending <= 0) run();
      });
      img.addEventListener("error", function () {
        pending -= 1;
        if (pending <= 0) run();
      });
    });

    var resizeTimer;
    window.addEventListener("resize", function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(run, 160);
    });
  }

  function boot() {
    document.querySelectorAll(".cx-marquee__track").forEach(initTrack);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
  window.addEventListener("load", boot);
})();
