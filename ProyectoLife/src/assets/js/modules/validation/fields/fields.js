function Name(e) {
    const name = document.getElementById("name")
    if (!name.value || name.value.trim().length <= 1) {
        e.preventDefault(); 
        console.log("Error - El nombre no cumple con el protocolo");
        return;
    }
}

function LastName(e) {
    const lastName = document.getElementById("lastName");

    if (!lastName.value || lastName.value.trim().length <= 1) {
        e.preventDefault(); 
        console.log("Error - - El apellido no cumple con el protocolo");
        return;
    }
}

function Password(e){

    const password = document.getElementById("password");
    if (!password.value || password.value.trim().length <= 5) {
        e.preventDefault(); 
        console.log("Error - - La contraseña no cumple con los 6 caracteres.");
        return;
    }
}

function ConfirmPassword(e) {
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");
    Password(e)

    if (!confirmPassword.value || confirmPassword.value.trim() != password.value.trim()) {
        e.preventDefault(); 
        console.log("Error - - La contraseña no cumple con los 6 caracteres.");
        return;
    }
}

function Email(e) {
    const email = document.getElementById("email");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!email.value || !emailRegex.test(email.value)) {
        e.preventDefault();
        console.log("Error - Correo electrónico inválido.");
        return;
    }
}


export {Name, LastName, Password, ConfirmPassword, Email}