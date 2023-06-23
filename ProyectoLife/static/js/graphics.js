"use strict";

let activeChartId = null;

function chart_visibility(chartId) {
    let chart = document.getElementById(chartId);
    let allCharts = document.querySelectorAll("canvas");

    if (activeChartId === chartId) {
        chart.style.display = "none";
        activeChartId = null;
    }else{

    for (let i = 0; i < allCharts.length; i++) {
        allCharts[i].style.display = "none";
    };

        // Mostrar el gráfico seleccionado
        chart.style.display = "block";
        activeChartId = chartId;
    } ;
};

document.getElementById("second_section_row_first").addEventListener("click", function() {
    chart_visibility("myChart1");
});
document.getElementById("second_section_row_second").addEventListener("click", function() {
    chart_visibility("myChart2");
});
document.getElementById("second_section_row_third").addEventListener("click", function() {
    chart_visibility("myChart3");
});
