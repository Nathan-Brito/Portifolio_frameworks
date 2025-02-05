let attemptCount = 0;

async function submitLogin() {
    console.log(username);
    console.log(password);

    if (attemptCount >= 1) {
        document.getElementById("message").textContent = "Limite de tentativas excedido. Tente novamente mais tarde.";
        return; 
    }

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch('/atividades/aula_06_11/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    });

    const result = await response.text();

    if (result === "Bem-vindo, usuário!") {
        document.getElementById("message").textContent = result;
        attemptCount = 0; 
    } else {
        attemptCount++; 
        document.getElementById("message").textContent = `Login inválido. Você tem ${2 - attemptCount} tentativa(s) restante(s).`;
    }
}

function submitForm(event) {
    event.preventDefault();

    let inputs = document.querySelectorAll("form input");
    let allFilled = true;

    inputs.forEach(input => {
        if (input.value.trim() === "") {
            allFilled = false;
            input.classList.add("error");
        } else {
            input.classList.remove("error");
        }
    });

    if (allFilled) {
        alert("Formulário Enviado com Sucesso!");
        document.querySelector("form").submit();
    } else {
        alert("Erro! Preencha todos os campos antes de enviar.");
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", submitForm);
    }
});
