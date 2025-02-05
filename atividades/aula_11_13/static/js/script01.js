async function submitLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    console.log (username)
    console.log (password)

    const response = await fetch('/atividades/aula_13_11/authenticate', {  // Atualizamos o caminho da rota
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    });

    const result = await response.json();
    document.getElementById("message").textContent = result.message;


}
