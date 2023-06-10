

// Get the canvas element
const canvas = document.getElementById('background-canvas');
const ctx = canvas.getContext('2d');

// Set the canvas size to match the window size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Create an array to hold the particles
const particles = [];
let mouseX = 0;
let mouseY = 0;

// Function to create a new particle
function createParticle(x, y) {
  const particle = {
    x: x,
    y: y,
    vx: Math.random() * 10 - 5, // Random velocity in the range of -1 to 1
    vy: Math.random() * 10 - 5,
    color: getRandomColor(),
    radius: Math.random() * 6 + 3 // Random radius between 1 and 3
  };
  particles.push(particle);
}

// Function to generate a random RGB color
function getRandomColor() {
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);
  return `rgb(${r}, ${g}, ${b})`;
}

// Function to draw a particle
function drawParticle(particle) {
  ctx.beginPath();
  ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
  ctx.fillStyle = particle.color;
  ctx.fill();
  ctx.closePath();
}

// Function to update the position of particles
function updateParticles() {
  particles.forEach(particle => {
    // Move the particle away from the mouse
    const dx = particle.x - mouseX;
    const dy = particle.y - mouseY;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const moveFactor = 5 / (distance + 3); // Adjust the move factor to control the speed
    
    particle.x += particle.vx * moveFactor;
    particle.y += particle.vy * moveFactor;
    
    // Draw the particle
    drawParticle(particle);
  });
}

// Mousemove event handler
function onMouseMove(event) {
  mouseX = event.clientX;
  mouseY = event.clientY;
}

// Resize event handler
function onResize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

// Add event listeners
window.addEventListener('mousemove', onMouseMove);
window.addEventListener('resize', onResize);

// Function to animate the particles
function animate() {
  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Update and draw the particles
  updateParticles();
  
  // Call animate again
  requestAnimationFrame(animate);
}

// Initialize the particles
for (let i = 0; i < 100; i++) {
  const x = Math.random() * canvas.width;
  const y = Math.random() * canvas.height;
  createParticle(x, y);
}

// Start the animation
animate();

  

