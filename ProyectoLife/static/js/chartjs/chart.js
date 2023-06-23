"use strict";

// New chart
function createChart(chartId, config) {
    const chartElement = document.getElementById(chartId);
    const ctx = chartElement.getContext('2d');

    return new Chart(ctx, config);
};

// Test
const config1 = {
    type: 'bar',
    data: {
        labels: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
        datasets: [{
            label: 'Calorías blabla (1)',
            data: [12, 19, 3, 5, 2, 3, 5],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 3
        }]
    }
};
const config2 = {
    type: 'bar',
    data: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        datasets: [{
            label: 'Ventas mensuales',
            data: [1200, 1500, 900, 1100, 800],
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 3
        }]
    }
};
const config3 = {
    type: 'line',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: 'Puntos de datos',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 3
        }]
    }
};  

// Chart init
const  myChart1 = createChart('myChart1', config1);
const  myChart2 = createChart('myChart2', config2);
const  myChart3 = createChart('myChart3', config3);
