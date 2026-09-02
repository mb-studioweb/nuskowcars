/**
 * Formulaire de réservation NuskowCars — navigation multi-étapes.
 * Reproduit la logique conditionnelle Webflow : l'étape offre dépend du véhicule choisi.
 */
(function () {
  const form = document.querySelector(".form_component, #wf-form-Informations");
  if (!form) return;

  const allSteps = Array.from(form.querySelectorAll(".form_step"));
  if (!allSteps.length) return;

  const vehicleStep = allSteps.find((s) => s.getAttribute("if-step") === "Vehicule choice");
  const infoStep = allSteps.find((s) => s.getAttribute("if-step") === "infos résa");
  const clientStep = allSteps.find((s) => s.getAttribute("if-step") === "Infos client");

  const vehicleToOfferStep = {
    "Mercedes-benz G63 AMG": "G63-Prices",
    "Maybach S680": "Maybach",
    "McLaren 600LT": "Mclaren",
    "MERCEDES-BENZ GLE63s AMG COUPE": "GLE Prices",
    "Lamborghini Urus": "Urus",
    "Lamborghini Urus Performante": "Urus",
    "AUDI RSQ8 APR 2023": "RSQ8",
    "Porsche 911 Carrera": "Carrera",
    "Audi RS3 2024": "Audi RS3",
    "BMW M3 compétition 2025": "M3 2025",
    "Rolls Royce Ghost": "RR Ghost",
    "Lamborghini Huracan Evo": "Huracan",
    "Mercedes GT63 AMG": "GT63",
    "Audi RS6 Performance": "RS6",
    "BMW M5": "M5",
    "Mercedes S500": "S500",
    "Porsche GT3": "GT3",
    "Ferrari 488": "Ferrarri 488",
    "Mercedes C63S": "C63S-Prices",
  };

  let flow = [vehicleStep, infoStep, clientStep].filter(Boolean);
  let current = 0;
  let selectedOfferStep = null;

  function hideAll() {
    allSteps.forEach((s) => {
      s.classList.remove("is-active");
      s.style.display = "none";
    });
  }

  function updateProgress(stepEl) {
    const wrappers = stepEl ? stepEl.querySelectorAll(".niveau-etape") : [];
    form.querySelectorAll(".niveau-etape").forEach((el) => el.classList.remove("is-now"));
    wrappers.forEach((el) => el.classList.add("is-now"));
  }

  function showStepEl(stepEl) {
    hideAll();
    if (!stepEl) return;
    stepEl.classList.add("is-active");
    stepEl.style.display = "block";
    updateProgress(stepEl);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function getActiveFlow() {
    const selected = vehicleStep && vehicleStep.querySelector('input[name="Choix-V-hicule"]:checked');
    const offerName = selected ? vehicleToOfferStep[selected.value] : null;
    selectedOfferStep = offerName ? allSteps.find((s) => s.getAttribute("if-step") === offerName) : null;
    const steps = [vehicleStep, selectedOfferStep, infoStep, clientStep].filter(Boolean);
    return steps;
  }

  function showIndex(index) {
    flow = getActiveFlow();
    current = Math.max(0, Math.min(index, flow.length - 1));
    showStepEl(flow[current]);
  }

  showIndex(0);

  form.addEventListener("click", function (e) {
    const next = e.target.closest('[if-element="button-next"], .button.is-suivant, .is-suivant');
    const back = e.target.closest('[if-element="button-back"], .back-link-block');
    if (next) {
      e.preventDefault();
      flow = getActiveFlow();
      const active = flow[current];
      if (active === vehicleStep) {
        const sel = vehicleStep.querySelector('input[name="Choix-V-hicule"]:checked');
        if (!sel) {
          alert(document.documentElement.lang === "de" ? "Bitte wählen Sie ein Fahrzeug." : document.documentElement.lang === "en" ? "Please select a vehicle." : "Veuillez sélectionner un véhicule.");
          return;
        }
      }
      if (active && active !== clientStep) {
        const radios = active.querySelectorAll('input[type="radio"]');
        const groups = new Set([...radios].map((r) => r.name));
        for (const name of groups) {
          if (name && !active.querySelector(`input[name="${CSS.escape(name)}"]:checked`)) {
            /* optional offer step may have no pre-selection required */
          }
        }
      }
      if (current < flow.length - 1) showIndex(current + 1);
    }
    if (back) {
      e.preventDefault();
      if (current > 0) showIndex(current - 1);
    }
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const done = form.parentElement.querySelector(".w-form-done") || document.querySelector(".w-form-done");
    form.style.display = "none";
    if (done) {
      done.style.display = "block";
    } else {
      const msg =
        document.documentElement.lang === "de"
          ? "Anfrage gespeichert! Wir melden uns in Kürze."
          : document.documentElement.lang === "en"
            ? "Request saved! We will contact you shortly."
            : "Demande enregistrée ! Nous vous recontactons rapidement.";
      alert(msg);
    }
  });
})();
