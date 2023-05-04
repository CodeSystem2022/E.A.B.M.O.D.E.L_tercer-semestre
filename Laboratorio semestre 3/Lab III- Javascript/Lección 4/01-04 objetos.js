// Definir el objeto "persona"
let persona = {
  nombre: "Leandro",
  apellido: "Saint Bonnet",
  edad: 27,
  genero: "masculino",
  profesion: "ingeniero",
};

// Acceder a las propiedades del objeto
console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.profesion);

// Modificar las propiedades del objeto
persona.edad = 31;
persona.profesion = "programador";

// Añadir nuevas propiedades al objeto
persona.email = "leandro@gmail.com";

// Eliminar propiedades del objeto
delete persona.genero;
