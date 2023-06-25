function Name(e) {
    const name = document.getElementById("name");
    const errorSpan = document.createElement("span");
    errorSpan.id = "error-name";
    errorSpan.style.color = "red";
  
    if (!name.value || name.value.trim().length <= 1) {
      e.preventDefault();
    
      const errorElement = document.getElementById("error-name");
      if (!errorElement) {
        errorSpan.textContent = "Debe completar el campo de nombre.";
        name.parentNode.insertBefore(errorSpan, name.nextSibling);
      }
    
      name.style.border = "1px solid red"; // Cambiar el estilo del borde del input
      return;
    }
    
    else {
      const errorElement = document.getElementById("error-name");
      if (errorElement) {
        errorElement.remove(); // Eliminar el mensaje de error si existe
        name.style.border = ""; // Restaurar el estilo de borde predeterminado
      }
      // Aquí puedes realizar otras validaciones o continuar con el envío del formulario
    }
  }
  

  function LastName(e) {
    const lastName = document.getElementById("lastName");
    const errorSpan = document.createElement("span");
    errorSpan.id = "error-lastName";
    errorSpan.style.color = "red";
  
    if (!lastName.value || lastName.value.trim().length <= 1) {
      e.preventDefault();
    
      const errorElement = document.getElementById("error-lastName");
      if (!errorElement) {
        errorSpan.textContent = "Debe completar el campo de apellido.";
        lastName.parentNode.insertBefore(errorSpan, lastName.nextSibling);
      }
    
      lastName.style.border = "1px solid red"; // Cambiar el estilo del borde del input
      return;
    }
    
    else {
      const errorElement = document.getElementById("error-lastName");
      if (errorElement) {
        errorElement.remove(); // Eliminar el mensaje de error si existe
        lastName.style.border = ""; // Restaurar el estilo de borde predeterminado
      }
      // Aquí puedes realizar otras validaciones o continuar con el envío del formulario
    }
  }
  

  function Password(e) {
    const password = document.getElementById("password");
    const errorSpan = document.createElement("span");
    errorSpan.id = "error-password";
    errorSpan.style.color = "red";
  
    if (!password.value || password.value.trim().length <= 5) {
      e.preventDefault();
  
      errorSpan.textContent = "La contraseña debe tener al menos 6 caracteres.";
      password.parentNode.insertBefore(errorSpan, password.nextSibling);
  
      password.style.border = "1px solid red"; // Cambiar el estilo del borde del input
      return;
    } else {
      const errorElement = document.getElementById("error-password");
      if (errorElement) {
        errorElement.remove(); // Eliminar el mensaje de error si existe
        password.style.border = ""; // Restaurar el estilo de borde predeterminado
      }
      // Aquí puedes realizar otras validaciones o continuar con el envío del formulario
    }
  }
  

  function ConfirmPassword(e) {
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");
    const errorSpan = document.createElement("span");
    errorSpan.id = "error-confirmPassword";
    errorSpan.style.color = "red";
  
    Password(e);
  
    if (!confirmPassword.value || confirmPassword.value.trim() !== password.value.trim()) {
      e.preventDefault();
  
      const errorElement = document.getElementById("error-confirmPassword");
      if (!errorElement) {
        errorSpan.textContent = "Las contraseñas no coinciden.";
        confirmPassword.parentNode.insertBefore(errorSpan, confirmPassword.nextSibling);
        confirmPassword.style.border = "1px solid red"; // Cambiar el estilo del borde del input
      }
  
      confirmPassword.classList.add("error-border"); // Agregar clase para cambiar el estilo del borde del input
      return;
    } else {
      const errorElement = document.getElementById("error-confirmPassword");
      if (errorElement) {
        errorElement.remove(); // Eliminar el mensaje de error si existe
        confirmPassword.classList.remove("error-border"); // Remover clase para restaurar el estilo de borde predeterminado
        confirmPassword.style.border = ""
      }
      // Aquí puedes realizar otras validaciones o continuar con el envío del formulario
    }
  }
  
  
  function Email(e) {
    const email = document.getElementById("email");
    const errorSpan = document.createElement("span");
    errorSpan.id = "error-email";
    errorSpan.style.color = "red";

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!email.value || !emailRegex.test(email.value)) {
      e.preventDefault();

      const errorElement = document.getElementById("error-email");
      if (!errorElement) {
        errorSpan.textContent = "Correo electrónico inválido.";
        email.parentNode.insertBefore(errorSpan, email.nextSibling);
        email.style.border = "1px solid red"; // Cambiar el estilo del borde del input
      }

      email.classList.add("error-border"); // Agregar clase para cambiar el estilo del borde del input
      return;
    } else {
      const errorElement = document.getElementById("error-email");
      if (errorElement) {
        errorElement.remove(); // Eliminar el mensaje de error si existe
        email.classList.remove("error-border"); // Remover clase para restaurar el estilo de borde predeterminado

        email.style.border = ""
      }
      // Aquí puedes realizar otras validaciones o continuar con el envío del formulario
    }
  }



export {Name, LastName, Password, ConfirmPassword, Email}