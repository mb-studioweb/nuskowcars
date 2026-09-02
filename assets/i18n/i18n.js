(function (global) {
  var STORAGE_KEY = "nuskow-lang";
  var SUPPORTED = ["fr", "de", "en"];

  function normalizeLang(code) {
    if (!code) return "fr";
    code = String(code).toLowerCase();
    if (code.indexOf("de") === 0) return "de";
    if (code.indexOf("en") === 0) return "en";
    return "fr";
  }

  function readQueryLang() {
    try {
      return new URLSearchParams(global.location.search).get("lang");
    } catch (e) {
      return null;
    }
  }

  function assetPrefix() {
    var path = global.location.pathname.replace(/\\/g, "/");
    if (/\/vehicules\//.test(path) || /^vehicules\//.test(path.replace(/^\//, ""))) {
      return "../";
    }
    return "";
  }

  function resolveAssetPath(relative) {
    return assetPrefix() + relative;
  }

  function getStrings(lang) {
    var data = global.NUSKOW_LOCALES || {};
    return (data.strings && data.strings[lang]) || (data.strings && data.strings.fr) || {};
  }

  function t(key, lang) {
    lang = lang || currentLang;
    var strings = getStrings(lang);
    if (strings[key] != null) return strings[key];
    if (lang !== "fr") return t(key, "fr");
    return null;
  }

  function htmlLang(code) {
    if (code === "de") return "de-DE";
    if (code === "en") return "en";
    return "fr-FR";
  }

  var currentLang = "fr";

  function applyToDom(lang) {
    lang = normalizeLang(lang);
    currentLang = lang;
    document.documentElement.lang = htmlLang(lang);

    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var key = el.getAttribute("data-i18n");
      var value = t(key, lang);
      if (value == null) return;
      el.textContent = value;
    });

    document.querySelectorAll("[data-i18n-html]").forEach(function (el) {
      var key = el.getAttribute("data-i18n-html");
      var value = t(key, lang);
      if (value == null) return;
      el.innerHTML = value;
    });

    document.querySelectorAll("[data-i18n-placeholder]").forEach(function (el) {
      var key = el.getAttribute("data-i18n-placeholder");
      var value = t(key, lang);
      if (value != null) el.placeholder = value;
    });

    document.querySelectorAll("[data-i18n-title]").forEach(function (el) {
      var key = el.getAttribute("data-i18n-title");
      var value = t(key, lang);
      if (value != null) el.title = value;
    });

    document.querySelectorAll("[data-i18n-aria]").forEach(function (el) {
      var key = el.getAttribute("data-i18n-aria");
      var value = t(key, lang);
      if (value != null) el.setAttribute("aria-label", value);
    });

    document.querySelectorAll(".header__lang-btn").forEach(function (btn) {
      btn.classList.toggle("is-active", btn.getAttribute("data-lang") === lang);
    });

    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch (e) {}

    var pageTitleKey = document.body && document.body.getAttribute("data-i18n-page-title");
    if (pageTitleKey) {
      var title = t(pageTitleKey, lang);
      if (title) document.title = title;
    }

    global.dispatchEvent(new CustomEvent("nuskow:langchange", { detail: { lang: lang } }));
  }

  function setLang(lang, options) {
    options = options || {};
    lang = normalizeLang(lang);
    if (SUPPORTED.indexOf(lang) === -1) lang = "fr";
    applyToDom(lang);
    if (options.updateUrl !== false) {
      try {
        var url = new URL(global.location.href);
        if (lang === "fr") url.searchParams.delete("lang");
        else url.searchParams.set("lang", lang);
        global.history.replaceState({}, "", url.toString());
      } catch (e) {}
    }
    if (global.NuskowPages && typeof global.NuskowPages.onLangChange === "function") {
      global.NuskowPages.onLangChange(lang);
    }
  }

  function initSwitcher() {
    document.querySelectorAll(".header__lang-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        setLang(btn.getAttribute("data-lang"));
      });
    });
  }

  function detectLang() {
    var fromQuery = readQueryLang();
    if (fromQuery) return normalizeLang(fromQuery);
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      if (stored) return normalizeLang(stored);
    } catch (e) {}
    return normalizeLang(document.documentElement.lang);
  }

  function boot() {
    initSwitcher();
    setLang(detectLang(), { updateUrl: false });
  }

  global.NuskowI18n = {
    t: t,
    getLang: function () {
      return currentLang;
    },
    setLang: setLang,
    apply: applyToDom,
    assetPrefix: assetPrefix,
    resolveAssetPath: resolveAssetPath,
    boot: boot,
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})(window);
