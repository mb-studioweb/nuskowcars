/**
 * NuskowCars — formulaires statiques → WhatsApp
 * Remplace reCAPTCHA / envoi Webflow (inopérants hors Webflow).
 */
(function () {
  var WA_NUMBER = "33637002045";

  function lang() {
    var l = (document.documentElement.lang || "fr").toLowerCase();
    var path = (location.pathname || "").toLowerCase();
    if (l.indexOf("de") === 0 || path.indexOf("/german") !== -1 || path.indexOf("german.html") !== -1) return "de";
    if (l.indexOf("en") === 0 || path.indexOf("/en/") !== -1 || /\/en\.html$/.test(path)) return "en";
    return "fr";
  }

  function labels() {
    var L = lang();
    if (L === "de") {
      return {
        titleContact: "Neue Kontaktanfrage (Website)",
        titleReservation: "Neue Reservierungsanfrage (Website)",
        sent: "Weiterleitung zu WhatsApp…",
        fail: "WhatsApp konnte nicht geöffnet werden. Schreiben Sie uns unter +33 6 37 00 20 45.",
      };
    }
    if (L === "en") {
      return {
        titleContact: "New contact request (website)",
        titleReservation: "New reservation request (website)",
        sent: "Opening WhatsApp…",
        fail: "Could not open WhatsApp. Message us at +33 6 37 00 20 45.",
      };
    }
    return {
      titleContact: "Nouvelle demande de contact (site)",
      titleReservation: "Nouvelle demande de réservation (site)",
      sent: "Ouverture de WhatsApp…",
      fail: "Impossible d’ouvrir WhatsApp. Écrivez-nous au 06 37 00 20 45.",
    };
  }

  function fieldLabel(el) {
    var id = el.getAttribute("id");
    if (id) {
      var lab = document.querySelector('label[for="' + id.replace(/"/g, "") + '"]');
      if (lab && lab.textContent.trim()) return lab.textContent.trim();
    }
    return (
      el.getAttribute("data-name") ||
      el.getAttribute("placeholder") ||
      el.getAttribute("name") ||
      "Champ"
    );
  }

  function collect(form) {
    var lines = [];
    var els = form.querySelectorAll("input, select, textarea");
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      var type = (el.getAttribute("type") || "").toLowerCase();
      if (type === "submit" || type === "button" || type === "hidden" || type === "reset") continue;
      if (el.disabled) continue;
      var name = el.getAttribute("name");
      if (!name) continue;
      var value = "";
      if (type === "radio" || type === "checkbox") {
        if (!el.checked) continue;
        value = el.value || "oui";
      } else {
        value = (el.value || "").trim();
      }
      if (!value) continue;
      lines.push(fieldLabel(el) + " : " + value);
    }
    return lines;
  }

  function openWhatsApp(text) {
    var url = "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(text);
    var win = window.open(url, "_blank", "noopener,noreferrer");
    if (!win) location.href = url;
  }

  function isReservationForm(form) {
    var id = (form.id || "").toLowerCase();
    var name = (form.getAttribute("data-name") || form.getAttribute("name") || "").toLowerCase();
    if (id.indexOf("information") !== -1 || name.indexOf("information") !== -1) return true;
    if (form.querySelector('[name="Choix-V-hicule"], [name="Choix Véhicule"], [name="Choix-Offre"]')) return true;
    return false;
  }

  function stripRecaptcha(root) {
    var nodes = (root || document).querySelectorAll(
      ".g-recaptcha, .w-form-formrecaptcha, .grecaptcha-badge"
    );
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].remove();
    }
  }

  function showDone(form, msg) {
    var wrap = form.closest(".w-form") || form.parentElement;
    if (!wrap) return;
    var done = wrap.querySelector(".w-form-done");
    var fail = wrap.querySelector(".w-form-fail");
    if (fail) fail.style.display = "none";
    if (done) {
      var text = done.querySelector("div");
      if (text && msg) text.textContent = msg;
      done.style.display = "block";
      form.style.display = "none";
    }
  }

  function showFail(form, msg) {
    var wrap = form.closest(".w-form") || form.parentElement;
    if (!wrap) return;
    var fail = wrap.querySelector(".w-form-fail");
    if (fail) {
      var text = fail.querySelector("div");
      if (text && msg) text.textContent = msg;
      fail.style.display = "block";
    }
  }

  function onSubmit(e) {
    var form = e.target;
    if (!form || form.tagName !== "FORM") return;
    // Skip if intentionally marked
    if (form.hasAttribute("data-no-whatsapp")) return;

    e.preventDefault();
    e.stopPropagation();

    var t = labels();
    var lines = collect(form);
    if (!lines.length) {
      showFail(form, t.fail);
      return;
    }

    var title = isReservationForm(form) ? t.titleReservation : t.titleContact;
    var message = title + "\n\n" + lines.join("\n");
    try {
      openWhatsApp(message);
      showDone(form, t.sent);
    } catch (err) {
      showFail(form, t.fail);
    }
  }

  function init() {
    stripRecaptcha(document);
    var forms = document.querySelectorAll("form");
    for (var i = 0; i < forms.length; i++) {
      forms[i].addEventListener("submit", onSubmit, true);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
