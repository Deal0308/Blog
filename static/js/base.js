// gradient-background.js
document.addEventListener('DOMContentLoaded', function () {
    const background = document.getElementById('particles-js');

    document.addEventListener('mousemove', function (e) {
        const x = e.clientX / window.innerWidth - 0.5;
        const y = e.clientY / window.innerHeight - 0.5;

        background.style.background = `radial-gradient(at ${x * 100}% ${y * 100}%, #ff8a00, #003366)`;
    });
});
