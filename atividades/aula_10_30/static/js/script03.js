document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.getElementById('table-body');
    const numRows = 997;

    for (let i = 1; i <= numRows; i++) {
        const row = document.createElement('div');
        row.classList.add('row');

        row.innerHTML = `
            <div class="cell">${i}</div>
            <div class="cell">Nome ${i}</div>
            <div class="cell">Sobrenome ${i}</div>
            <div class="cell">nome${i}@exemplo.com</div>
            <div class="cell">
                <button>Ação</button>
            </div>
        `;

        tableBody.appendChild(row);
    }
});
