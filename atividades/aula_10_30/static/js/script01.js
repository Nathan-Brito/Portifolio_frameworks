document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById('myCanvas');
    const ctx = canvas.getContext('2d');
    const img = new Image();
    img.src = './static/img/dvd_logo.png';

    let x=0;
    let y=50;
    const imgWidth = 100; 
    const imgHeight = 100;
    const moveAmout = 5;

    img.onload = function() {
        console.log('Imagem carregada com sucesso');
        ctx.drawImage(img, x, y, imgWidth, imgHeight);
        moveImage();
    };

    function moveImage() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, x, y, imgWidth, imgHeight);
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') {
            x += moveAmout;
            console.log(moveAmout);
            if (x + imgWidth > canvas.width) x = canvas.width - imgWidth;
        } else if (e.key === 'ArrowLeft') {
            x -= moveAmout;
            if (x < 0) x = 0;
        } else if (e.key === 'ArrowUp') {
            y -= moveAmout;
            if (y < 0) y = 0;
        } else if (e.key === 'ArrowDown') {
            y += moveAmout;
            console.log(moveAmout);
            if (y + imgHeight > canvas.height) y = canvas.height - imgHeight;
        }

        console.log(`Posição da imagem: (${x}, ${y})`);
        moveImage();
    });
});