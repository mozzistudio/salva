const header = document.querySelector('.header');
const revealElements = document.querySelectorAll('.reveal');

const toggleHeader = () => {
  if (!header) {
    return;
  }
  if (window.scrollY > 30) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }
};

toggleHeader();
window.addEventListener('scroll', toggleHeader);

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 }
);

revealElements.forEach((element) => {
  revealObserver.observe(element);
});
