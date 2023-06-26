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

        chartContainer.style.display = "block";
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
document.querySelector("#second_form").addEventListener("click", function() {
    chart_visibility("form-test1");
});
document.querySelector("#third_form").addEventListener("click", function() {
    chart_visibility("form-test2");
});

/*test */
// Obtenemos los elementos del DOM
let formulariosLink = document.getElementById('formularios');
let graficosLink = document.getElementById('graficos');
let threeSection = document.querySelector('.three_section');
let secondSection = document.querySelector('.second_section');

formulariosLink.addEventListener('click', function(event) {
    event.preventDefault();

    threeSection.style.display = 'flex';
    secondSection.style.display = 'none';

    let allChartContainers;
    allChartContainers = document.querySelectorAll(".canvas-container");
    for (let i = 0; i < allChartContainers.length; i++) {
        allChartContainers[i].style.display = "none";
    };
});

graficosLink.addEventListener('click', function(event) {
    event.preventDefault();

    secondSection.style.display = 'flex';
    threeSection.style.display = 'none';
});