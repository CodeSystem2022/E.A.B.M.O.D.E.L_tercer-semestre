let numero;

do {
  numero = prompt("Ingresa un número entre 1 y 10:");
} while (numero < 1 || numero > 10);

alert("El número que ingresaste es " + numero);
