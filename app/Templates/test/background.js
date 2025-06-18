const canvas = document.getElementById('bg-canvas');
const ctx = canvas.getContext('2d');

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

let gradientTime = 0;
function drawGradient() {
  const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  gradient.addColorStop(0, `hsl(0, 0%, ${10 + Math.sin(gradientTime * 0.01) * 5}%)`);
  gradient.addColorStop(0.5, `hsl(0, 0%, ${20 + Math.sin(gradientTime * 0.01 + 1) * 5}%)`);
  gradient.addColorStop(1, `hsl(0, 0%, ${10 + Math.sin(gradientTime * 0.01 + 2) * 5}%)`);
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

const shapes = [];
for (let i = 0; i < 8; i++) {
  shapes.push({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    size: Math.random() * 40 + 15,
    vx: (Math.random() - 0.5) * 0.4,
    vy: (Math.random() - 0.5) * 0.4,
    type: Math.random() > 0.5 ? 'circle' : 'square',
    opacity: Math.random() * 0.15 + 0.05,
  });
}

function drawShapes() {
  shapes.forEach(shape => {
    ctx.beginPath();
    ctx.fillStyle = `rgba(255, 255, 255, ${shape.opacity})`;
    if (shape.type === 'circle') {
      ctx.arc(shape.x, shape.y, shape.size / 2, 0, Math.PI * 2);
    } else {
      ctx.rect(shape.x - shape.size / 2, shape.y - shape.size / 2, shape.size, shape.size);
    }
    ctx.fill();

    shape.x += shape.vx;
    shape.y += shape.vy;
    if (shape.x < 0 || shape.x > canvas.width) shape.vx *= -1;
    if (shape.y < 0 || shape.y > canvas.height) shape.vy *= -1;
  });
}

const particles = [];
for (let i = 0; i < 40; i++) {
  particles.push({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    size: Math.random() * 2 + 0.5,
    vx: (Math.random() - 0.5) * 0.2,
    vy: (Math.random() - 0.5) * 0.2,
    opacity: Math.random() * 0.2 + 0.05,
  });
}

function drawParticles() {
  particles.forEach(p => {
    ctx.beginPath();
    ctx.fillStyle = `rgba(255, 255, 255, ${p.opacity})`;
    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
    ctx.fill();

    p.x += p.vx;
    p.y += p.vy;
    if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
    if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
  });
}

function animateBackground() {
  if (document.hidden) {
    requestAnimationFrame(animateBackground);
    return;
  }
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawGradient();
  drawShapes();
  drawParticles();
  gradientTime += 0.3;
  requestAnimationFrame(animateBackground);
}
animateBackground();