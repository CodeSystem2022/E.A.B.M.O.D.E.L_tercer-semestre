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