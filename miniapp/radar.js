console.log("Радар загружен");

// Простейшая функция для точки на радаре
function showRadarPoint() {
    const radar = document.getElementById("radar");
    if (!radar) return;

    // Красная точка случайно появляется/пропадает
    const point = document.createElement("div");
    point.className = "radar-point";
    point.style.top = Math.random() * 100 + "%";
    point.style.left = Math.random() * 100 + "%";
    radar.appendChild(point);

    setTimeout(() => {
        radar.removeChild(point);
    }, 3000);
}

// Пример: каждые 5 секунд
setInterval(showRadarPoint, 5000);