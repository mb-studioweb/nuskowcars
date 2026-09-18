(function () {
  if (document.querySelector("[data-wa-float]")) return;

  var WA_URL = "https://wa.me/33637002045";
  var STORAGE_KEY = "nuskow-wa-hint-dismissed";

  var TEXT = {
    fr: {
      label: "Une question ? Demande-nous sur WhatsApp",
      hint: "Une demande ? Un conseil ? Un conseiller NuskowCars vous répond sous 5 minutes.",
      close: "Fermer",
      aria: "Contacter NuskowCars sur WhatsApp",
    },
    de: {
      label: "Eine Frage? Schreib uns auf WhatsApp",
      hint: "Eine Anfrage? Ein Rat? Ein NuskowCars-Berater antwortet innerhalb von 5 Minuten.",
      close: "Schließen",
      aria: "NuskowCars auf WhatsApp kontaktieren",
    },
    en: {
      label: "A question? Message us on WhatsApp",
      hint: "A request? Some advice? A NuskowCars advisor will reply within 5 minutes.",
      close: "Close",
      aria: "Contact NuskowCars on WhatsApp",
    },
  };

  var lang = (document.documentElement.lang || "fr").toLowerCase();
  if (window.NuskowI18n && window.NuskowI18n.getLang) {
    lang = window.NuskowI18n.getLang();
  } else {
    if (lang.indexOf("de") === 0) lang = "de";
    else if (lang.indexOf("en") === 0) lang = "en";
    else lang = "fr";
  }
  var t = TEXT[lang];

  var root = document.createElement("div");
  root.className = "wa-float";
  root.setAttribute("data-wa-float", "");
  root.innerHTML =
    '<div class="wa-float__hint" data-wa-hint role="status">' +
    '<button type="button" class="wa-float__close" data-wa-close aria-label="' +
    t.close +
    '">×</button>' +
    '<p><span class="wa-float__hint-title">' +
    t.label +
    "</span>" +
    t.hint +
    "</p></div>" +
    '<a href="' +
    WA_URL +
    '" class="wa-float__btn" target="_blank" rel="noopener noreferrer" aria-label="' +
    t.aria +
    '">' +
    '<span class="wa-float__dot" aria-hidden="true"></span>' +
    '<svg class="wa-float__icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>' +
    '<span class="wa-float__label">' +
    t.label +
    "</span></a>";

  document.body.appendChild(root);

  var hint = root.querySelector("[data-wa-hint]");
  var closeBtn = root.querySelector("[data-wa-close]");

  function hideHint() {
    if (!hint) return;
    hint.hidden = true;
    try {
      sessionStorage.setItem(STORAGE_KEY, "1");
    } catch (e) {}
  }

  try {
    if (sessionStorage.getItem(STORAGE_KEY)) hideHint();
  } catch (e) {}

  if (closeBtn) closeBtn.addEventListener("click", hideHint);

  window.addEventListener("nuskow:langchange", function (e) {
    var newLang = (e.detail && e.detail.lang) || "fr";
    if (newLang.indexOf("de") === 0) newLang = "de";
    else if (newLang.indexOf("en") === 0) newLang = "en";
    else newLang = "fr";
    t = TEXT[newLang];
    var label = root.querySelector(".wa-float__label");
    if (label) label.textContent = t.label;
    if (hint) {
      hint.innerHTML =
        '<button type="button" class="wa-float__close" data-wa-close aria-label="' +
        t.close +
        '">×</button><p><span class="wa-float__hint-title">' +
        t.label +
        "</span>" +
        t.hint +
        "</p>";
      root.querySelector("[data-wa-close]").addEventListener("click", hideHint);
    }
    var btn = root.querySelector(".wa-float__btn");
    if (btn) btn.setAttribute("aria-label", t.aria);
  });

  var link = document.createElement("link");
  link.rel = "stylesheet";
  var scripts = document.getElementsByTagName("script");
  var self = scripts[scripts.length - 1];
    if (self && self.src) {
    link.href = self.src.replace(/wa-float\.js.*$/, "wa-float.css");
  } else {
    link.href = (window.NuskowI18n ? window.NuskowI18n.resolveAssetPath("assets/wa-float.css") : "/assets/wa-float.css");
  }
  document.head.appendChild(link);
})();
