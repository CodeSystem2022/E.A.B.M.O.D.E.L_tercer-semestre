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
            label: 'Calorías quemadas en la semana',
            data: [1577.5, 1577.5, 1577.5, 1577.5, 1577.5, 1577.5, 1577.5],
            backgroundColor: '#9F9F9FAD',
            borderColor: 'white',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                grid: {
                    color: '#9cc670'
                },
                ticks: {
                    color: 'white',
                    padding: 10
                }
            },
            y: {
                grid: {
                    color: '#9cc670'
                },
                ticks: {
                    color: 'white',
                    padding: 10
                }
            }
        }
    }
};

fetch('/salva_datos_user')
  .then(response => response.json())
  .then(data => {
    // Aquí puedes trabajar con los datos obtenidos en data
    console.log(data);
  })
  .catch(error => {
    // Manejo de errores
    console.error(error);
  });

const config2 = {
    type: 'bar',
    data: {
        labels: ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', "Domingo"],
        datasets: [{
            label: 'Ventas mensuales',
            data: [1200, 1500, 900, 1100, 800, 500, 400],
            backgroundColor: '#9F9F9FAD',
            borderColor: 'white',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                grid: {
                    color: '#9cc670'
                },
                ticks: {
                    color: 'white',
                    padding: 10
                }
            },
            y: {
                grid: {
                    color: '#9cc670'
                },
                ticks: {
                    color: 'white',
                    padding: 10,
                }
            }
        }
    }
};
const config3 = {
    type: 'line',
    data: {
        labels: ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', "Domingo"],
        datasets: [{
            label: 'Puntos de datos',
            data: [0, 19, 3, 5, 2, 3, 5],
            backgroundColor: '#474747D9',
            borderColor: '#474747D9',
            borderWidth: 3
        },{
            label: 'Puntos de gatos',
            data: [2, 9, 10, 7, 20, 4 ,9],
            backgroundColor: 'green',
            borderColor: 'green',
            borderWidth: 3
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                grid: {
                    color: '#9cc670'
                },
                ticks: {
                    color: 'white',
                    padding: 25
                }
            },
            y: {
                grid: {
                    color: '#9cc670'
                },
                ticks: {
                    color: 'white',
                    padding: 25
                }
            }
        }
    }
};

// Chart init
const myChart1 = createChart('myChart1', config3);
const myChart2 = createChart('myChart2', config2);
const myChart3 = createChart('myChart3', config1);