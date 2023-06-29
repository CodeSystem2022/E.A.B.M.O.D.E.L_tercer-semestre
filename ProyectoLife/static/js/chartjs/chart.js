"use strict";

fetch('/salva_datos_user')
.then(response => response.json())
.then(data => {
    // Aquí puedes trabajar con los datos obtenidos en data
    console.log(data);

    const elementsBACK = data;
    //{
    //    "usuario_calorias_quemadas": {
    //        "0": {
    //            "actividad": 0.5,
    //            "altura": 176,
    //            "calorias_quemadas": 77.5,
    //            "dia": "Domingo",
    //            "edad": 25,
    //            "peso": 60,
    //            "sexo": "male",
    //            "user_id": 1
    //        },
    //        "1": {
    //            "actividad": 0.5,
    //            "altura": 176,
    //            "calorias_quemadas": 577.5,
    //            "dia": "Lunes",
    //            "edad": 25,
    //            "peso": 60,
    //            "sexo": "male",
    //            "user_id": 1
    //        },
    //        "2": {
    //            "actividad": 0.5,
    //            "altura": 176,
    //            "calorias_quemadas": 1577.5,
    //            "dia": "Lunes",
    //            "edad": 25,
    //            "peso": 60,
    //            "sexo": "male",
    //            "user_id": 1
    //        },
    //        "5": {
    //            "actividad": 0.5,
    //            "altura": 176,
    //            "calorias_quemadas": 1577.5,
    //            "dia": "Viernes",
    //            "edad": 25,
    //            "peso": 60,
    //            "sexo": "male",
    //            "user_id": 1
    //        }
    //    },
    //    "usuario_imc": {
    //        "0": {
    //            "altura": 176,
    //            "dia": "Domingo",
    //            "edad": 25,
    //            "imc": 800,
    //            "peso": 60,
    //            "sexo": "male",
    //            "user_id": 1
    //        },
    //        "1": {
    //            "altura": 176,
    //            "dia": "Lunes",
    //            "edad": 25,
    //            "imc": 600,
    //            "peso": 60,
    //            "sexo": "male",
    //            "user_id": 1
    //        },
    //        "2": {
    //            "altura": 176,
    //            "dia": "Martes",
    //            "edad": 25,
    //            "imc": 19.37,
    //            "peso": 60,
    //            "sexo": "male",
    //            "user_id": 1
    //        },
    //        "3": {
    //            "altura": 176,
    //            "dia": "Miércoles",
    //            "edad": 26,
    //            "imc": 11.37,
    //            "peso": 60,
    //            "sexo": "male",
    //            "user_id": 1
    //        },
    //        "4": {
    //            "altura": 176,
    //            "dia": "Jueves",
    //            "edad": 25,
    //            "imc": 450,
    //            "peso": 60,
    //            "sexo": "male",
    //            "user_id": 1
    //        }
    //    }
    //} > ESTE ES TU JSON
    
    // New chart
    function createChart(chartId, config) {
        const chartElement = document.getElementById(chartId);
        const ctx = chartElement.getContext('2d');
    
        return new Chart(ctx, config);
    };
    
    function api_call() {
        const config_imc = {
            type: 'bar',
            data: {
                labels: [elementsBACK.usuario_imc[0]?.dia, elementsBACK.usuario_imc[1]?.dia,elementsBACK.usuario_imc[2]?.dia,elementsBACK.usuario_imc[3]?.dia,elementsBACK.usuario_imc[4]?.dia,elementsBACK.usuario_imc[5]?.dia,elementsBACK.usuario_imc[6]?.dia],
                datasets: [{
                    label: 'IMC semanal',
                    data: 
                    [elementsBACK.usuario_imc[0]?.imc,
                    elementsBACK.usuario_imc[1]?.imc,
                    elementsBACK.usuario_imc[2]?.imc,
                    elementsBACK.usuario_imc[3]?.imc,
                    elementsBACK.usuario_imc[4]?.imc,
                    elementsBACK.usuario_imc[5]?.imc,
                    elementsBACK.usuario_imc[6]?.imc],
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
        const config_calorias_quemadas = {
            type: 'bar',
            data: {
                labels: [
                    elementsBACK.usuario_calorias_quemadas[0]?.dia ? elementsBACK.usuario_calorias_quemadas[0].dia : "sin información",
                    elementsBACK.usuario_calorias_quemadas[1]?.dia ? elementsBACK.usuario_calorias_quemadas[1].dia : "sin información",
                    elementsBACK.usuario_calorias_quemadas[2]?.dia ? elementsBACK.usuario_calorias_quemadas[2].dia : "sin información",
                    elementsBACK.usuario_calorias_quemadas[3]?.dia ? elementsBACK.usuario_calorias_quemadas[3].dia : "sin información",
                    elementsBACK.usuario_calorias_quemadas[4]?.dia ? elementsBACK.usuario_calorias_quemadas[4].dia : "sin información",
                    elementsBACK.usuario_calorias_quemadas[5]?.dia ? elementsBACK.usuario_calorias_quemadas[5].dia : "sin información",
                    elementsBACK.usuario_calorias_quemadas[6]?.dia ? elementsBACK.usuario_calorias_quemadas[6].dia : "sin información"
                ],
                datasets: [{
                    label: 'Calorias quemadas',
                    data: 
                    [
                    elementsBACK.usuario_calorias_quemadas[0]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[0]?.calorias_quemadas : "sin información",
                    elementsBACK.usuario_calorias_quemadas[1]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[1]?.calorias_quemadas : "sin información",
                    elementsBACK.usuario_calorias_quemadas[2]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[2]?.calorias_quemadas : "sin información",
                    elementsBACK.usuario_calorias_quemadas[3]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[3]?.calorias_quemadas : "sin información",
                    elementsBACK.usuario_calorias_quemadas[4]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[4]?.calorias_quemadas : "sin información",
                    elementsBACK.usuario_calorias_quemadas[5]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[5]?.calorias_quemadas : "sin información",
                    elementsBACK.usuario_calorias_quemadas[6]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[6]?.calorias_quemadas : "sin información"],
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
        const general = {
            type: 'line',
            data: {
                labels: [elementsBACK.usuario_imc[0]?.dia, elementsBACK.usuario_imc[1]?.dia,elementsBACK.usuario_imc[2]?.dia,elementsBACK.usuario_imc[3]?.dia,elementsBACK.usuario_imc[4]?.dia,elementsBACK.usuario_imc[5]?.dia,elementsBACK.usuario_imc[6]?.dia],
                datasets: [{
                    label: 'IMC',
                    data: [elementsBACK.usuario_imc[0]?.imc,
                    elementsBACK.usuario_imc[1]?.imc,
                    elementsBACK.usuario_imc[2]?.imc,
                    elementsBACK.usuario_imc[3]?.imc,
                    elementsBACK.usuario_imc[4]?.imc,
                    elementsBACK.usuario_imc[5]?.imc,
                    elementsBACK.usuario_imc[6]?.imc],
                    backgroundColor: '#474747D9',
                    borderColor: '#474747D9',
                    borderWidth: 3
                },{
                    label: 'Calorias quemadas',
                    data: [
                        elementsBACK.usuario_calorias_quemadas[0]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[0]?.calorias_quemadas : "sin información",
                        elementsBACK.usuario_calorias_quemadas[1]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[1]?.calorias_quemadas : "sin información",
                        elementsBACK.usuario_calorias_quemadas[2]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[2]?.calorias_quemadas : "sin información",
                        elementsBACK.usuario_calorias_quemadas[3]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[3]?.calorias_quemadas : "sin información",
                        elementsBACK.usuario_calorias_quemadas[4]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[4]?.calorias_quemadas : "sin información",
                        elementsBACK.usuario_calorias_quemadas[5]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[5]?.calorias_quemadas : "sin información",
                        elementsBACK.usuario_calorias_quemadas[6]?.calorias_quemadas ? elementsBACK.usuario_calorias_quemadas[6]?.calorias_quemadas : "sin información"],
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
    
        const myChart1 = createChart('myChart1', general);
        const myChart2 = createChart('myChart2', config_calorias_quemadas);
        const myChart3 = createChart('myChart3', config_imc);
    };
    
    api_call();
})
.catch(error => {
    // Manejo de errores
    console.error(error);
});