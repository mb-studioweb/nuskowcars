(function (global) {
  var WA = "33637002045";

  function lang() {
    return global.NuskowI18n ? global.NuskowI18n.getLang() : "fr";
  }

  function t(key) {
    return global.NuskowI18n ? global.NuskowI18n.t(key, lang()) : key;
  }

  function prefix() {
    return global.NuskowI18n ? global.NuskowI18n.assetPrefix() : "";
  }

  function vehicles() {
    var data = global.NUSKOW_LOCALES || {};
    return data.vehicles || [];
  }

  function offerLabel(label, l) {
    var data = global.NUSKOW_LOCALES || {};
    var map = (data.offerLabels && data.offerLabels[l]) || {};
    return map[label] || label;
  }

  function vehicleField(v, field, l) {
    if (v.i18n && v.i18n[l] && v.i18n[l][field]) return v.i18n[l][field];
    return v[field] || "";
  }

  function waUrl(text) {
    return "https://wa.me/" + WA + "?text=" + encodeURIComponent(text);
  }

  function waMessage(v, l) {
    var data = global.NUSKOW_LOCALES || {};
    var intro = (data.waIntro && data.waIntro[l]) || data.waIntro.fr;
    return intro + " " + vehicleField(v, "title", l);
  }

  function renderFleet() {
    var mount = document.querySelector("[data-fleet-list]");
    if (!mount) return;
    var l = lang();
    var p = prefix();
    var perfLabels = ((global.NUSKOW_LOCALES.fleetPerfLabels || {})[l]) || ["Puissance", "0-100", "Vitesse max"];

    mount.innerHTML = vehicles()
      .map(function (v) {
        var title = vehicleField(v, "title", l);
        var tag = vehicleField(v, "category", l);
        var desc = vehicleField(v, "desc_short", l) + " · " + (v.power || "");
        var perfs = v.perfs || ["", "", ""];
        var pricing = (v.pricing || [])
          .slice(0, 2)
          .map(function (row) {
            return (
              '<div class="fleet-pricing__item"><span class="fleet-pricing__label">' +
              offerLabel(row[0], l) +
              '</span><span class="fleet-pricing__value">' +
              row[1] +
              "</span></div>"
            );
          })
          .join("");
        return (
          '<article class="fleet-list__item">' +
          '<div class="fleet-list__media"><img src="' +
          p +
          "assets/vehicules/" +
          v.slug +
          '/1.jpg" alt="' +
          title.replace(/"/g, "&quot;") +
          '" /></div>' +
          '<div class="fleet-list__body">' +
          '<p class="fleet-list__tag">' +
          tag +
          "</p>" +
          '<h2 class="fleet-list__title">' +
          title +
          "</h2>" +
          '<p class="fleet-list__desc">' +
          desc +
          "</p>" +
          '<div class="fleet-list__perfs">' +
          '<div class="fleet-list__perf"><span class="fleet-list__perf-value">' +
          perfs[0] +
          '</span><span class="fleet-list__perf-label">' +
          perfLabels[0] +
          '</span></div><div class="fleet-list__perf"><span class="fleet-list__perf-value">' +
          perfs[1] +
          '</span><span class="fleet-list__perf-label">' +
          perfLabels[1] +
          '</span></div><div class="fleet-list__perf"><span class="fleet-list__perf-value">' +
          perfs[2] +
          '</span><span class="fleet-list__perf-label">' +
          perfLabels[2] +
          "</span></div></div>" +
          '<div class="fleet-pricing">' +
          pricing +
          '<div class="fleet-pricing__item"><span class="fleet-pricing__label">' +
          t("common.deposit") +
          '</span><span class="fleet-pricing__value">' +
          v.deposit +
          "</span></div></div>" +
          '<div class="fleet-list__actions">' +
          '<a href="' +
          p +
          "vehicules/" +
          v.slug +
          '.html" class="a fleet-list__btn fleet-list__btn--outline">' +
          t("common.see_sheet") +
          '</a><a href="' +
          waUrl(waMessage(v, l)) +
          '" class="a fleet-list__btn fleet-list__btn--wa" target="_blank" rel="noopener">' +
          t("common.reserve_wa") +
          "</a></div></div></article>"
        );
      })
      .join("");
  }

  function updateVehiclePage() {
    var slug = document.body.getAttribute("data-vehicle-slug");
    if (!slug) return;
    var v = vehicles().find(function (item) {
      return item.slug === slug;
    });
    if (!v) return;
    var l = lang();
    var p = prefix();
    var title = vehicleField(v, "title", l);
    var tag = vehicleField(v, "tag", l);
    var descLong = vehicleField(v, "desc_long", l);
    var perfLabels = ((global.NUSKOW_LOCALES.perfLabels || {})[l]) || [];
    var perfs = v.perfs || ["", "", ""];

    var back = document.querySelector(".vehicle-back");
    if (back) back.textContent = t("common.back_fleet");

    var heroSub = document.querySelector(".vehicle-hero .small-description");
    if (heroSub) heroSub.textContent = tag;

    var introTag = document.querySelector(".vehicle-intro__tag");
    if (introTag) introTag.textContent = "NuskowCars · " + v.brand + " · " + v.power;

    var introTitle = document.querySelector(".vehicle-intro__title");
    if (introTitle) introTitle.textContent = title;

    var introText = document.querySelector(".vehicle-intro__text");
    if (introText) introText.textContent = descLong;

    var perfTitle = document.querySelector(".vehicle-perfs h2");
    if (perfTitle) perfTitle.textContent = t("vehicle.performances");

    document.querySelectorAll(".vehicle-perf__label").forEach(function (el, i) {
      if (perfLabels[i]) el.textContent = perfLabels[i];
    });
    document.querySelectorAll(".vehicle-perf__value").forEach(function (el, i) {
      if (perfs[i]) el.textContent = perfs[i];
    });

    var galleryTitle = document.getElementById("vehicle-gallery-title");
    if (galleryTitle) galleryTitle.textContent = t("common.gallery");

    var pricingTitle = document.querySelector(".vehicle-pricing h2");
    if (pricingTitle) pricingTitle.textContent = t("common.pricing_title");

    var pricingList = document.querySelector(".vehicle-pricing__list");
    if (pricingList) {
      var rows = (v.pricing || [])
        .map(function (row) {
          return "<li><span>" + offerLabel(row[0], l) + "</span><span>" + row[1] + "</span></li>";
        })
        .join("");
      rows +=
        '<li class="is-caution"><span>' +
        t("common.deposit") +
        "</span><span>" +
        v.deposit +
        "</span></li>";
      pricingList.innerHTML = rows;
    }

    var pricingNote = document.querySelector(".vehicle-pricing__note");
    if (pricingNote) pricingNote.textContent = t("common.pricing_note");

    var ctaTitle = document.querySelector(".vehicle-cta h2");
    if (ctaTitle) ctaTitle.textContent = title;

    var fleetBtn = document.querySelector(".vehicle-btn--outline");
    if (fleetBtn) {
      fleetBtn.textContent = t("common.see_fleet");
      fleetBtn.setAttribute("href", p + "flotte.html");
    }

    var waBtn = document.querySelector(".vehicle-btn--wa");
    if (waBtn) {
      waBtn.textContent = t("common.reserve_wa");
      waBtn.setAttribute("href", waUrl(waMessage(v, l)));
    }

    document.title = t("vehicle.page_title_prefix") + " " + title + " — NuskowCars";
  }

  function updateHomeFleet() {
    var l = lang();
    document.querySelectorAll(".fleet-card, .project-card").forEach(function (card) {
      var link = card.querySelector('a[href*="vehicules/"]');
      if (!link) return;
      var m = link.getAttribute("href").match(/vehicules\/([^/]+)\.html/);
      if (!m) return;
      var v = vehicles().find(function (item) {
        return item.slug === m[1];
      });
      if (!v) return;
      var loc = card.querySelector(".location");
      var desc = card.querySelector(".desc");
      var btn = card.querySelector(".btn");
      if (loc) loc.textContent = vehicleField(v, "category", l);
      if (desc) desc.textContent = vehicleField(v, "desc_short", l);
      if (btn) btn.textContent = t("common.see_sheet");
      card.querySelectorAll(".fleet-pricing__label").forEach(function (el, i) {
        el.textContent = i === 0 ? t("common.24h_week") : t("common.deposit");
      });
    });
  }

  function updateHomeReviews() {
    document.querySelectorAll(".review-card__stars[data-i18n-aria], .review-card__stars").forEach(function (el) {
      if (el.hasAttribute("data-i18n-aria") || el.getAttribute("aria-label")) {
        var stars = t("home.reviews_stars");
        if (stars) el.setAttribute("aria-label", stars);
      }
    });
    var circle = document.querySelector("textPath[data-i18n]");
    if (circle) {
      var txt = t(circle.getAttribute("data-i18n"));
      if (txt) circle.textContent = txt;
    }
  }

  function onLangChange() {
    renderFleet();
    updateVehiclePage();
    updateHomeFleet();
    updateHomeReviews();
  }

  function boot() {
    renderFleet();
    updateVehiclePage();
    updateHomeFleet();
    updateHomeReviews();
    global.addEventListener("nuskow:langchange", onLangChange);
  }

  global.NuskowPages = {
    boot: boot,
    onLangChange: onLangChange,
    renderFleet: renderFleet,
    updateVehiclePage: updateVehiclePage,
    updateHomeFleet: updateHomeFleet,
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})(window);
