(function () {
  if (document.querySelector("[data-wa-float]")) return;

  var WA_URL = "https://wa.me/33637002045";

  var TEXT = {
    fr: { aria: "Contacter NuskowCars sur WhatsApp" },
    de: { aria: "NuskowCars auf WhatsApp kontaktieren" },
    en: { aria: "Contact NuskowCars on WhatsApp" },
  };

  var lang = (document.documentElement.lang || "fr").toLowerCase();
  var path = (location.pathname || "").toLowerCase();
  if (lang.indexOf("de") === 0 || path.indexOf("/german") !== -1 || path.indexOf("german.html") !== -1) lang = "de";
  else if (lang.indexOf("en") === 0 || path.indexOf("/en/") !== -1 || /\/en\.html$/.test(path)) lang = "en";
  else lang = "fr";
  var t = TEXT[lang] || TEXT.fr;

  var root = document.createElement("div");
  root.className = "wa-float";
  root.setAttribute("data-wa-float", "");

  var btn = document.createElement("a");
  btn.className = "wa-float__btn";
  btn.href = WA_URL;
  btn.target = "_blank";
  btn.rel = "noopener noreferrer";
  btn.setAttribute("aria-label", t.aria);
  btn.innerHTML =
    '<svg class="wa-float__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">' +
    '<path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.89.49 3.73 1.42 5.35L2 22l4.89-1.28a9.86 9.86 0 0 0 5.15 1.32h.01c5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2zm5.83 14.24c-.24.68-1.4 1.25-1.93 1.33-.49.07-1.1.1-1.77-.11-.41-.13-.93-.3-1.6-.59-2.81-1.22-4.64-4.06-4.78-4.25-.13-.19-1.1-1.46-1.1-2.79s.7-1.98.94-2.25c.24-.27.53-.34.7-.34h.5c.16 0 .37-.06.58.44.22.53.73 1.83.8 1.96.07.13.11.29.02.47-.09.18-.14.29-.27.45-.14.15-.29.34-.41.46-.14.13-.28.27-.12.53.16.26.7 1.15 1.5 1.86 1.03.91 1.9 1.19 2.17 1.32.27.13.43.11.59-.07.16-.18.69-.8.87-1.08.18-.27.37-.23.62-.14.26.09 1.64.77 1.92.91.28.14.47.21.54.33.07.12.07.68-.17 1.36z"/>' +
    "</svg>";

  root.appendChild(btn);
  document.body.appendChild(root);

  var link = document.createElement("link");
  link.rel = "stylesheet";
  var scripts = document.getElementsByTagName("script");
  var self = scripts[scripts.length - 1];
  if (self && self.src) {
    link.href = self.src.replace(/wa-float\.js.*$/, "wa-float.css");
  } else {
    link.href = "assets/wa-float.css";
  }
  document.head.appendChild(link);
})();
