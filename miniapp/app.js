console.log("Mini App стартует");

document.addEventListener("DOMContentLoaded", () => {
    // Первый запуск
    if (!localStorage.getItem("firstLaunch")) {
        alert("Привет! Добро пожаловать в Mini App!");
        localStorage.setItem("firstLaunch", "true");
    }

    // Синхронизация профиля (заглушка)
    const profile = document.getElementById("profile");
    if (profile) {
        profile.innerHTML = `
            <img src="../assets/logo.png" class="avatar">
            <div class="nick">Non Premium</div>
        `;
    }

    // Обработка кнопок
    const radarBtn = document.getElementById("radar-btn");
    if (radarBtn) {
        radarBtn.addEventListener("click", () => alert("Радар активирован"));
    }
});