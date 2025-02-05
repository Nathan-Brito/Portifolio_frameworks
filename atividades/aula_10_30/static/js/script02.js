document.addEventListener("DOMContentLoaded", () => {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const photo = document.getElementById('photo');
    const captureButton = document.getElementById('capture');

    // Acessa a webcam
    navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        video.srcObject = stream;
    })
    .catch((error) => {
        console.error("Erro ao acessar a webcam:", error);
    });

    // Captura a imagem quando o botão é pressionado
    captureButton.addEventListener('click', () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    const dataUrl = canvas.toDataURL('image/png');
    photo.src = dataUrl;
    });
});