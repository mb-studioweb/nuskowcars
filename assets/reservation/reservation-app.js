(function () {
  var VEHICLES = [
    {
      id: "g63",
      name: "Mercedes-Benz G63 AMG",
      image: "assets/vehicules/mercedes-benz-g63-amg/1.jpg",
      from: "699 €",
      offers: [
        { label: "24h semaine (250 km)", price: "699 €" },
        { label: "24h semaine (illimité)", price: "999 €" },
        { label: "24h week-end", price: "1 300 €" },
        { label: "48h week-end", price: "2 200 €" },
        { label: "72h", price: "2 800 €" },
        { label: "7 jours", price: "4 500 €" },
      ],
    },
    {
      id: "gle",
      name: "Mercedes GLE 63 S AMG Coupé",
      image: "assets/vehicules/mercedes-benz-gle63s-amg-coupe/1.jpg",
      from: "499 €",
      offers: [
        { label: "24h semaine (250 km)", price: "499 €" },
        { label: "24h semaine (illimité)", price: "699 €" },
        { label: "24h week-end (250 km)", price: "1 000 €" },
        { label: "48h week-end", price: "1 900 €" },
        { label: "7 jours", price: "3 800 €" },
      ],
    },
    {
      id: "rs3",
      name: "Audi RS3 2024",
      image: "assets/vehicules/audi-rs3-2024/1.jpg",
      from: "299 €",
      offers: [
        { label: "24h semaine (250 km)", price: "299 €" },
        { label: "24h semaine (illimité)", price: "399 €" },
        { label: "48h week-end", price: "900 €" },
        { label: "72h", price: "1 100 €" },
        { label: "7 jours", price: "1 770 €" },
      ],
    },
    {
      id: "m3",
      name: "BMW M3 Compétition 2025",
      image: "assets/vehicules/bmw-m3-competition-510ch-2025/1.jpg",
      from: "399 €",
      offers: [
        { label: "24h semaine (250 km)", price: "399 €" },
        { label: "24h semaine (illimité)", price: "499 €" },
        { label: "48h week-end", price: "1 200 €" },
        { label: "72h", price: "1 400 €" },
        { label: "7 jours", price: "2 200 €" },
      ],
    },
    {
      id: "rsq8",
      name: "Audi RSQ8 APR 2023",
      image: "assets/vehicules/audi-rsq8-apr-2023/1.jpg",
      from: "499 €",
      offers: [
        { label: "24h semaine (250 km)", price: "499 €" },
        { label: "24h semaine (illimité)", price: "699 €" },
        { label: "24h week-end (250 km)", price: "1 000 €" },
        { label: "24h week-end (illimité)", price: "1 300 €" },
        { label: "48h week-end", price: "1 900 €" },
        { label: "72h", price: "2 300 €" },
        { label: "7 jours", price: "3 800 €" },
      ],
    },
    {
      id: "urus",
      name: "Lamborghini Urus",
      image: "assets/vehicules/lamborghini-urus/1.jpg",
      from: "1 800 €",
      offers: [
        { label: "24h semaine", price: "1 800 €" },
        { label: "24h week-end", price: "2 000 €" },
        { label: "48h week-end", price: "3 500 €" },
      ],
    },
    {
      id: "urus-perf",
      name: "Lamborghini Urus Performante",
      image: "assets/vehicules/lamborghini-urus-2/1.jpg",
      from: "2 000 €",
      offers: [
        { label: "24h semaine (illimité)", price: "2 000 €" },
        { label: "24h week-end (illimité)", price: "2 500 €" },
        { label: "48h week-end (illimité)", price: "4 000 €" },
      ],
    },
    {
      id: "huracan",
      name: "Lamborghini Huracán Evo",
      image: "assets/vehicules/lamborghini-huracan-evo/1.jpg",
      from: "1 750 €",
      offers: [
        { label: "24h semaine", price: "1 750 €" },
        { label: "24h week-end", price: "1 900 €" },
        { label: "48h week-end", price: "3 500 €" },
      ],
    },
  ];

  var TEXT = {
    fr: {
      title: "Demande de réservation",
      lead: "Sélectionnez votre véhicule et complétez le formulaire. Nous vous confirmons la disponibilité sur WhatsApp.",
      steps: ["Véhicule", "Offre", "Dates", "Coordonnées"],
      panels: ["Choix du véhicule", "Choix de l'offre", "Informations de réservation", "Vos coordonnées"],
      from: "À partir de",
      back: "Retour",
      next: "Suivant",
      submit: "Envoyer la demande",
      pickupDate: "Date de prise en charge",
      pickupTime: "Heure de retrait",
      returnDate: "Date de restitution",
      returnTime: "Heure de restitution",
      location: "Lieu de retrait / livraison",
      locationPh: "Ville, adresse ou aéroport en France",
      firstName: "Prénom",
      lastName: "Nom",
      birthYear: "Année de naissance",
      email: "Adresse e-mail",
      phone: "Téléphone",
      country: "Pays",
      address: "Adresse",
      zip: "Code postal",
      city: "Ville",
      errVehicle: "Veuillez sélectionner un véhicule.",
      errOffer: "Veuillez sélectionner une offre.",
      errRequired: "Veuillez remplir tous les champs obligatoires.",
      successTitle: "Demande envoyée",
      successText: "Merci ! Nous vous recontactons rapidement pour confirmer votre réservation.",
      successWa: "Ouvrir WhatsApp",
      waIntro: "Bonjour, je souhaite réserver chez NuskowCars :",
    },
    de: {
      title: "Reservierungsanfrage",
      lead: "Wählen Sie Ihr Fahrzeug und füllen Sie das Formular aus. Wir bestätigen die Verfügbarkeit per WhatsApp.",
      steps: ["Fahrzeug", "Angebot", "Daten", "Kontakt"],
      panels: ["Fahrzeugwahl", "Angebotswahl", "Reservierungsinformationen", "Ihre Kontaktdaten"],
      from: "Ab",
      back: "Zurück",
      next: "Weiter",
      submit: "Anfrage senden",
      pickupDate: "Abholdatum",
      pickupTime: "Abholzeit",
      returnDate: "Rückgabedatum",
      returnTime: "Rückgabezeit",
      location: "Abhol- / Lieferort",
      locationPh: "Stadt, Adresse oder Flughafen in Frankreich",
      firstName: "Vorname",
      lastName: "Nachname",
      birthYear: "Geburtsjahr",
      email: "E-Mail-Adresse",
      phone: "Telefon",
      country: "Land",
      address: "Adresse",
      zip: "Postleitzahl",
      city: "Stadt",
      errVehicle: "Bitte wählen Sie ein Fahrzeug.",
      errOffer: "Bitte wählen Sie ein Angebot.",
      errRequired: "Bitte füllen Sie alle Pflichtfelder aus.",
      successTitle: "Anfrage gesendet",
      successText: "Vielen Dank! Wir melden uns in Kürze zur Bestätigung Ihrer Reservierung.",
      successWa: "WhatsApp öffnen",
      waIntro: "Hallo, ich möchte bei NuskowCars reservieren:",
    },
    en: {
      title: "Reservation request",
      lead: "Select your vehicle and complete the form. We confirm availability on WhatsApp.",
      steps: ["Vehicle", "Offer", "Dates", "Details"],
      panels: ["Vehicle choice", "Offer choice", "Booking details", "Your details"],
      from: "From",
      back: "Back",
      next: "Next",
      submit: "Send request",
      pickupDate: "Pick-up date",
      pickupTime: "Pick-up time",
      returnDate: "Return date",
      returnTime: "Return time",
      location: "Pick-up / delivery location",
      locationPh: "City, address or airport in France",
      firstName: "First name",
      lastName: "Last name",
      birthYear: "Year of birth",
      email: "Email address",
      phone: "Phone",
      country: "Country",
      address: "Address",
      zip: "Postcode",
      city: "City",
      errVehicle: "Please select a vehicle.",
      errOffer: "Please select an offer.",
      errRequired: "Please fill in all required fields.",
      successTitle: "Request sent",
      successText: "Thank you! We will contact you shortly to confirm your booking.",
      successWa: "Open WhatsApp",
      waIntro: "Hello, I would like to book with NuskowCars:",
    },
  };

  var root = document.querySelector("[data-reservation-app]");
  if (!root) return;

  var lang = (document.documentElement.lang || "fr").slice(0, 2);
  if (!TEXT[lang]) lang = "fr";
  var t = TEXT[lang];
  var assetPrefix = root.getAttribute("data-asset-prefix") || "";

  var state = { step: 0, vehicleId: null, offerIndex: null };
  var els = {
    steps: root.querySelector("[data-res-steps]"),
    panels: Array.from(root.querySelectorAll("[data-res-panel]")),
    vehicles: root.querySelector("[data-res-vehicles]"),
    offers: root.querySelector("[data-res-offers]"),
    back: root.querySelector("[data-res-back]"),
    next: root.querySelector("[data-res-next]"),
    submit: root.querySelector("[data-res-submit]"),
    form: root.querySelector("[data-res-form]"),
    success: root.querySelector("[data-res-success]"),
    waLink: root.querySelector("[data-res-wa]"),
  };

  function img(path) {
    return assetPrefix + path;
  }

  function renderSteps() {
    if (!els.steps) return;
    els.steps.innerHTML = t.steps
      .map(function (label, i) {
        var cls = "res-step";
        if (i === state.step) cls += " is-active";
        if (i < state.step) cls += " is-done";
        return '<div class="' + cls + '" data-step="' + i + '"><span class="res-step__num">' + (i + 1) + "</span><span class=\"res-step__label\">" + label + "</span></div>";
      })
      .join("");
  }

  function renderVehicles() {
    if (!els.vehicles) return;
    els.vehicles.innerHTML = VEHICLES.map(function (v) {
      var checked = state.vehicleId === v.id ? " checked" : "";
      return (
        '<label class="res-vehicle">' +
        '<input type="radio" name="vehicle" value="' + v.id + '"' + checked + " />" +
        '<span class="res-vehicle__card">' +
        '<span class="res-vehicle__img"><img src="' + img(v.image) + '" alt="" loading="lazy" /></span>' +
        '<span class="res-vehicle__body">' +
        '<span class="res-vehicle__name">' + v.name + "</span>" +
        '<span class="res-vehicle__price">' + t.from + " " + v.from + "</span>" +
        "</span></span></label>"
      );
    }).join("");
  }

  function getVehicle() {
    return VEHICLES.find(function (v) {
      return v.id === state.vehicleId;
    });
  }

  function renderOffers() {
    if (!els.offers) return;
    var vehicle = getVehicle();
    if (!vehicle) {
      els.offers.innerHTML = "";
      return;
    }
    els.offers.innerHTML = vehicle.offers
      .map(function (o, i) {
        var checked = state.offerIndex === i ? " checked" : "";
        return (
          '<label class="res-offer">' +
          '<input type="radio" name="offer" value="' + i + '"' + checked + " />" +
          '<span class="res-offer__card"><span class="res-offer__label">' + o.label + '</span><span class="res-offer__price">' + o.price + "</span></span></label>"
        );
      })
      .join("");
  }

  function showStep(index) {
    state.step = Math.max(0, Math.min(index, els.panels.length - 1));
    els.panels.forEach(function (p, i) {
      p.classList.toggle("is-active", i === state.step);
      p.hidden = i !== state.step;
    });
    if (els.back) els.back.hidden = state.step === 0;
    if (els.next) els.next.hidden = state.step === els.panels.length - 1;
    if (els.submit) els.submit.hidden = state.step !== els.panels.length - 1;
    renderSteps();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function readVehicle() {
    var input = root.querySelector('input[name="vehicle"]:checked');
    state.vehicleId = input ? input.value : null;
  }

  function readOffer() {
    var input = root.querySelector('input[name="offer"]:checked');
    state.offerIndex = input ? parseInt(input.value, 10) : null;
  }

  function field(name) {
    var el = root.querySelector('[name="' + name + '"]');
    return el ? el.value.trim() : "";
  }

  function validateStep() {
    if (state.step === 0) {
      readVehicle();
      if (!state.vehicleId) {
        alert(t.errVehicle);
        return false;
      }
      renderOffers();
      return true;
    }
    if (state.step === 1) {
      readOffer();
      if (state.offerIndex === null || isNaN(state.offerIndex)) {
        alert(t.errOffer);
        return false;
      }
      return true;
    }
    if (state.step === 2) {
      if (!field("pickup_date") || !field("pickup_time") || !field("return_date") || !field("return_time") || !field("location")) {
        alert(t.errRequired);
        return false;
      }
      return true;
    }
    return true;
  }

  function buildWaUrl() {
    var vehicle = getVehicle();
    var offer = vehicle && vehicle.offers[state.offerIndex] ? vehicle.offers[state.offerIndex] : null;
    var lines = [
      t.waIntro,
      "",
      "🚗 " + (vehicle ? vehicle.name : ""),
      "📦 " + (offer ? offer.label + " — " + offer.price : ""),
      "📅 " + field("pickup_date") + " " + field("pickup_time") + " → " + field("return_date") + " " + field("return_time"),
      "📍 " + field("location"),
      "",
      "👤 " + field("first_name") + " " + field("last_name"),
      "📧 " + field("email"),
      "📱 " + field("phone"),
      "🎂 " + field("birth_year"),
      "🏠 " + field("address") + ", " + field("zip") + " " + field("city") + ", " + field("country"),
    ];
    return "https://wa.me/33637002045?text=" + encodeURIComponent(lines.join("\n"));
  }

  root.addEventListener("change", function (e) {
    if (e.target.name === "vehicle") {
      readVehicle();
      state.offerIndex = null;
      renderVehicles();
      if (state.step >= 1) renderOffers();
    }
    if (e.target.name === "offer") readOffer();
  });

  if (els.back) {
    els.back.addEventListener("click", function () {
      showStep(state.step - 1);
    });
  }

  if (els.next) {
    els.next.addEventListener("click", function () {
      if (!validateStep()) return;
      showStep(state.step + 1);
    });
  }

  if (els.form) {
    els.form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validateStep()) return;
      var required = ["first_name", "last_name", "birth_year", "email", "phone", "country", "address", "zip", "city"];
      for (var i = 0; i < required.length; i++) {
        if (!field(required[i])) {
          alert(t.errRequired);
          return;
        }
      }
      var wa = buildWaUrl();
      if (els.waLink) els.waLink.href = wa;
      els.form.hidden = true;
      root.querySelector(".res-progress").hidden = true;
      if (els.success) els.success.hidden = false;
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  renderSteps();
  renderVehicles();
  showStep(0);
})();
