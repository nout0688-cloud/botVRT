console.log("Настройки загружены");

// Пасхалка: трактор
document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("tractor-btn");
    if (!button) return;

    button.addEventListener("click", () => {
        const audio = new Audio("../assets/tractor.mp3");
        audio.play();
    });
});