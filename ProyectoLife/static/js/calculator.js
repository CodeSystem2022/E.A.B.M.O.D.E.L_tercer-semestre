"use strict";

let pepe = document.querySelector("#form-peso_ideal > div > form > div > div:nth-child(4) > article > article > input[type=range]")

pepe.addEventListener("change", function(e) {
    console.log(pepe.value)
})