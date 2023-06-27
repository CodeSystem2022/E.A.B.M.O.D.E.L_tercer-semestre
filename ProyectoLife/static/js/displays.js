"use strict";

let activeChartId = null;

function chart_visibility(chartId) {
    let chartContainer = document.getElementById(chartId);
    let allChartContainers;

    if(chartId == "canvas-container_one" || chartId == "canvas-container_two" || chartId == "canvas-container_three"){
        allChartContainers = document.querySelectorAll(".canvas-container");
    };

    if (activeChartId === chartId) {
        chartContainer.style.display = "none";
        activeChartId = null;
    }else{
        if(chartId == "canvas-container_one" || chartId == "canvas-container_two" || chartId == "canvas-container_three"){
            for (let i = 0; i < allChartContainers.length; i++) {
                allChartContainers[i].style.display = "none";
            };
        };

        chartContainer.style.display = "flex";
        activeChartId = chartId;
    };
};

document.getElementById("second_section_row_first").addEventListener("click", function() {
    chart_visibility("canvas-container_one");
});
document.getElementById("second_section_row_second").addEventListener("click", function() {
    chart_visibility("canvas-container_two");
});
document.getElementById("second_section_row_third").addEventListener("click", function() {
    chart_visibility("canvas-container_three");
});
document.querySelector("#first_form").addEventListener("click", function() {
    chart_visibility("form-imc");
});


/*test */
// Obtenemos los elementos del DOM
const formulariosLink = document.getElementById('formularios');
const formularioPeso = document.getElementById("calorias_quemadas");
const formularioPesoLink = document.getElementById("form-peso_ideal");
const formularioPesoIdeal = document.querySelector("#calorias_consumidas");
const graficosLink = document.getElementById('graficos');
const threeSection = document.querySelector('.three_section');
const secondSection = document.querySelector('.second_section');
const fourthSection = document.querySelector("#form-fourth_form");
// Text decorations on section
const first_section  = document.querySelector("#formularios");
const second_section = document.querySelector("#calorias_quemadas");
const third_section  = document.querySelector("#graficos");
const fourth_section = document.querySelector("#calorias_consumidas")

formulariosLink.addEventListener('click', function(event) {
    event.preventDefault();

    // Display
    threeSection.style.display = 'flex';
    formularioPesoLink.style.display = "none";
    secondSection.style.display = 'none';
    fourthSection.style.display = 'none';

    // Decotation
    first_section.style.textUnderlineOffset = '10px';
    first_section.style.textDecoration = 'underline';
    first_section.style.listStyle = '1px solid #82c337';
    second_section.style.textDecoration = 'none';
    fourth_section.style.textDecoration = 'none';
    third_section.style.textDecoration = 'none';

    let allChartContainers;
    allChartContainers = document.querySelectorAll(".canvas-container");
    for (let i = 0; i < allChartContainers.length; i++) {
        allChartContainers[i].style.display = "none";
    };
});
formularioPeso.addEventListener('click', function(event) {
    event.preventDefault();

    threeSection.style.display = 'none';
    formularioPesoLink.style.display = "flex";
    document.querySelector("#form-peso_ideal").style.display = "flex";
    secondSection.style.display = 'none';
    fourthSection.style.display = 'none';

    second_section.style.textUnderlineOffset = '10px';
    second_section.style.textDecoration = 'underline';
    second_section.style.listStyle = '1px solid #82c337';
    first_section.style.textDecoration = 'none';
    third_section.style.textDecoration = 'none';
    fourth_section.style.textDecoration = 'none';

    let allChartContainers;
    allChartContainers = document.querySelectorAll(".canvas-container");
    for (let i = 0; i < allChartContainers.length; i++) {
        allChartContainers[i].style.display = "none";
    };
});
graficosLink.addEventListener('click', function(event) {
    event.preventDefault();

    secondSection.style.display = 'flex';
    formularioPesoLink.style.display = "none";
    threeSection.style.display = 'none';
    fourthSection.style.display = 'none';

    third_section.style.textUnderlineOffset = '10px';
    third_section.style.textDecoration = 'underline';
    third_section.style.listStyle = '1px solid #82c337';
    first_section.style.textDecoration = 'none';
    second_section.style.textDecoration = 'none';
    fourth_section.style.textDecoration = 'none';
});
formularioPesoIdeal.addEventListener('click', function(event) {
    event.preventDefault();

    threeSection.style.display = 'none';
    formularioPesoLink.style.display = "none";
    document.querySelector("#form-peso_ideal").style.display = "none";
    secondSection.style.display = 'none';
    fourthSection.style.display = 'flex';

    second_section.style.textDecoration = 'none';
    first_section.style.textDecoration = 'none';
    third_section.style.textDecoration = 'none';
    fourth_section.style.textUnderlineOffset = '10px';
    fourth_section.style.textDecoration = 'underline';
    fourth_section.style.listStyle = '1px solid #82c337';

    let allChartContainers;
    allChartContainers = document.querySelectorAll(".canvas-container");
    for (let i = 0; i < allChartContainers.length; i++) {
    allChartContainers[i].style.display = "none";
};

});