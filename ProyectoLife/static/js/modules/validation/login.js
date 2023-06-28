import {Password, Email} from "./fields/fields.js"

export default function ValidacionDeLogin() {
    const form = document.getElementById("form-login");
    
    form.addEventListener("submit", (e) => {
        Email(e)
        Password(e)
    });
}

ValidacionDeLogin()
