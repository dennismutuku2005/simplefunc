// Intersection Observer for scroll animations
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, observerOptions);

document.querySelectorAll('.scrolled-reveal').forEach(el => {
    observer.observe(el);
});

// Cursor tracking for glow effect
document.addEventListener('mousemove', (e) => {
    const orb1 = document.querySelector('.orb-1');
    const orb2 = document.querySelector('.orb-2');
    
    const x = e.clientX / window.innerWidth;
    const y = e.clientY / window.innerHeight;
    
    orb1.style.transform = `translate(${x * 50}px, ${y * 50}px)`;
    orb2.style.transform = `translate(${-x * 50}px, ${-y * 50}px)`;
});

console.log("HyperInsight Neuro-Symbolic Engine initialized...");
