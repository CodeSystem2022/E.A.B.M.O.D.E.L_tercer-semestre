"use strict";

const text_to_change = document.querySelector("body > main > section.first_section > div > article.first_section_two > h6");
const section_one   = document.querySelector("#formularios");
const section_two   = document.querySelector("#calorias_quemadas");
const section_three = document.querySelector("#graficos");
const section_fourth = document.querySelector("#calorias_consumidas");

section_one.addEventListener("click", function() {
    text_to_change.innerHTML = "Nuestra página cuenta con una calculadora de peso y grasa corporal que te permitirá llevar un control de las calorías que consumes y quemas. Podrás registrar y monitorear tu balance calórico diario, así como obtener información sobre tu composición corporal. ¡Comienza a tomar el control de tu bienestar ahora mismo!"
});
section_two.addEventListener("click", function() {
    text_to_change.innerHTML = "Calcula las calorías quemadas de forma sencilla. Proporciona información básica sobre ti, como tu sexo, edad, altura, peso y nivel de actividad diaria, y obtén un cálculo preciso de las calorías que quemas. Mantén un seguimiento de tus objetivos de salud y bienestar, y descubre cómo llevar un estilo de vida más activo.";
});
section_three.addEventListener("click", function() {
    text_to_change.innerHTML = "Nuestros gráficos te permiten visualizar fácilmente la quema de calorías y el índice de masa corporal (IMC) a lo largo del tiempo. Podrás ver tu progreso diario en la quema de calorías, lo que te ayudará a mantener una actividad física constante. Además, el gráfico del IMC te mostrará cómo tu composición corporal se ha ido transformando. Observa tu evolución y motívate para alcanzar tus metas de salud y bienestar día a día.";
});
section_fourth.addEventListener("click", function() {
    text_to_change.innerHTML = "Descubre tu peso ideal con nuestra calculadora especializada. Proporciona información básica sobre ti, como tu sexo, edad, altura, peso actual y nivel de actividad diaria, y obtén un cálculo preciso de tu peso ideal. Mantén un control saludable de tu cuerpo y trabaja hacia alcanzar tu peso objetivo. Nuestra herramienta te brindará las pautas necesarias para lograr un equilibrio adecuado y te ayudará a tomar decisiones informadas sobre tu bienestar. ¡Comienza tu viaje hacia un peso ideal y una vida saludable ahora mismo!"
});