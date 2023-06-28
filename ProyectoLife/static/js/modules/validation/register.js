import {Name, LastName, ConfirmPassword, Email} from "./fields/fields.js"

export default function ValidacionDeRegistro() {
    const form = document.getElementById("form-register");

    form.addEventListener("submit", (e) => {
        Name(e);
        LastName(e)
        ConfirmPassword(e)
        Email(e)
    });
}

ValidacionDeRegistro()