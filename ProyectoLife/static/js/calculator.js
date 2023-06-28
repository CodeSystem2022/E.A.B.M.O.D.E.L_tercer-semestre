// "use strict";

// // IMC
// const imc_gender= document.querySelector("#gender-icn-btn-wrapper");
// const imc_age   = document.querySelector("#form-imc > form > div > div:nth-child(2) > article.form-option-date > article > input[type=date]");
// const imc_height = document.querySelector("#form-imc > form > div > div:nth-child(3) > article:nth-child(1) > article > input[type=number]");
// const imc_weigth= document.querySelector("#form-imc > form > div > div:nth-child(3) > article:nth-child(2) > article > input[type=number]");
// const imc_submit = document.querySelector("#form-imc > form");

// imc_submit.addEventListener("click", function(e) {
//     e.preventDefault();
//     e.stopPropagation();

//     if (!imc_gender) {
//         alert("Por favor, selecciona tu género.");
//         return;
//     }

//     if (!imc_age || !imc_height || !imc_weigth) {
//         alert("Por favor, completa todos los campos.");
//         return;
//     }

//     const heightInMeters = imc_height / 100; // Convertir altura a metros
//     const bmi = imc_weigth / (heightInMeters * heightInMeters);

//     let bmiCategory;
//     if (bmi < 18.5) {
//         bmiCategory = "Bajo peso";
//     } else if (bmi < 25) {
//         bmiCategory = "Normal";
//     } else if (bmi < 30) {
//         bmiCategory = "Sobrepeso";
//     } else {
//         bmiCategory = "Obesidad";
//     }

//     alert(`Tu IMC es ${bmi.toFixed(2)} (${bmiCategory})`);
// });



// // LAS CALORIAS QUEMADAS (a terminar)
// const age_input   = document.querySelector("#form-peso_ideal > div > form > div > div:nth-child(2) > article.form-option-number > article > input[type=number]");
// const weight_input = document.querySelector("#form-peso_ideal > div > form > div > div:nth-child(3) > article:nth-child(2) > article > input[type=number]");
// const height_input = document.querySelector("#form-peso_ideal > div > form > div > div:nth-child(3) > article:nth-child(1) > article > input[type=number]");
// const gender_input = document.querySelector("#gender-icn-btn-wrapper");
// const sport_activity = document.querySelector("#form-peso_ideal > div > form > div > div:nth-child(4) > article > article > input[type=range]");
// const burned_calories = document.querySelector("#form-peso_ideal > div > form");

// burned_calories.addEventListener("click", function(e) {
//     e.preventDefault();
//     e.stopPropagation();

//     const age = parseInt(age_input.value);
//     const weight = parseFloat(weight_input.value);
//     const height = parseFloat(height_input.value);
//     const gender = gender_input
//     const activityLevel = parseFloat(sport_activity.value);

//     console.log(age);
//     console.log(weight);
//     console.log(height);
//     console.log(gender);
//     console.log(activityLevel);

//     // Formula
//     let tasa_metabolica_basal;
//     if (gender === "male") {
//         tasa_metabolica_basal = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age);
//     } else if (gender === "female") {
//         tasa_metabolica_basal = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age);
//     } else {
//         alert("Por favor, selecciona tu género.");
//         return;
//     }

//     const caloriesBurned = tasa_metabolica_basal * activityLevel;

//     alert("Calorías quemadas durante el día: " + caloriesBurned.toFixed(2));
// });








// Peso ideal
const ideal_gender= document.querySelector("#gender-icn-btn-wrapper");
const ideal_age = document.querySelector("#form-fourth_form > div > form > div > div:nth-child(2) > article.form-option-number > article > input[type=number]");
const ideal_height = document.querySelector("#form-fourth_form > div > form > div > div:nth-child(3) > article > article > input[type=number]");
const ideal_form = document.querySelector("#form-fourth_form > div > form");
const ideal_submit = document.querySelector("#form-fourth_form > div > form > div > button");

// ideal_form.addEventListener("submit", function(e) {
//     e.preventDefault();
//     e.stopPropagation();
// });

ideal_submit.addEventListener("click", function(e) {
   // e.preventDefault();
    // e.stopPropagation();

    console.log(ideal_gender);
    console.log(ideal_age.value);
    console.log(ideal_height.value);

    if (!ideal_gender) {
        alert("Por favor, selecciona tu género.");
        return;
    };
    if (!ideal_age || !ideal_height) {
        alert("Por favor, completa todos los campos.");
        return;
    };
    
    let weight;
    //cambiar GENDER, NO OPTIMIZADO
    let gender = "male";

    if (gender === "male") {
      weight = 50 + 0.91 * (ideal_height.value - 152.4) + (ideal_age.value - 30) / 10;
    } else if (gender === "female") {
      weight = 45.5 + 0.91 * (ideal_height.value - 152.4) + (ideal_age.value - 30) / 10;
    } else {
        alert("Por favor, selecciona tu género.");
        return;
    }

    // Showing on DOM
    document.querySelector("#ideal_weigth").style.display = "flex";
    document.querySelector("#ideal_weigth > article > h4").innerHTML = `Tu peso ideal es: ${weight.toFixed(2)}.`;
    document.querySelector("#form-fourth_form > div > form > div > button > div > div.button-name").innerHTML = "Re-calcular";
});