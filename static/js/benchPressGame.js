// Create a stick figure object
const stickFigure = {
    x: 50,
    y: 200,
    speed: 5,
    benchPressSpeed: 1,
};

// Get the canvas element and its context
const canvas = document.getElementById('benchPressCanvas');
const ctx = canvas.getContext('2d');

// Event listener for mouse clicks
canvas.addEventListener('click', function () {
    stickFigure.benchPressSpeed += 1;
});

// Function to draw the stick figure
function drawStickFigure() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw stick figure body
    ctx.beginPath();
    ctx.arc(stickFigure.x, stickFigure.y - 20, 20, 0, Math.PI * 2);
    ctx.stroke();

    // Draw stick figure arms
    ctx.beginPath();
    ctx.moveTo(stickFigure.x - 20, stickFigure.y - 20);
    ctx.lineTo(stickFigure.x + 20, stickFigure.y - 20);
    ctx.stroke();

    // Draw bench press bar
    ctx.beginPath();
    ctx.moveTo(stickFigure.x - 30, stickFigure.y - 40);
    ctx.lineTo(stickFigure.x + 30, stickFigure.y - 40);
    ctx.stroke();

    // Draw bench press weight
    ctx.beginPath();
    ctx.arc(stickFigure.x, stickFigure.y - 40, 5, 0, Math.PI * 2);
    ctx.fill();
}

// Function to update stick figure position
function updateStickFigure() {
    stickFigure.x += stickFigure.speed;
    if (stickFigure.x > canvas.width) {
        stickFigure.x = -20;
    }
}

// Main game loop
function gameLoop() {
    updateStickFigure();
    drawStickFigure();
    requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();
