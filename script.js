'use strict';

const projectData = JSON.parse(document.getElementById('project-data').textContent);
const dialog = document.getElementById('project-modal');
let previouslyFocused;

document.querySelectorAll('[data-project]').forEach(button => {
  button.addEventListener('click', () => {
    const project = projectData[Number(button.dataset.project)];
    previouslyFocused = button;
    document.getElementById('modal-title').textContent = project.title;
    document.getElementById('modal-description').textContent = project.desc;
    const image = document.getElementById('modal-image');
    image.src = project.img;
    image.alt = project.title;
    const link = document.getElementById('modal-link');
    link.href = project.link;
    document.getElementById('modal-link-label').textContent = project.link.endsWith('/HasinduBimsara') ? 'Visit GitHub profile' : 'View source code';
    document.getElementById('modal-tech').replaceChildren(...project.tech.split(', ').map(tech => {
      const tag = document.createElement('span');
      tag.textContent = tech;
      return tag;
    }));
    dialog.showModal();
    document.body.style.overflow = 'hidden';
  });
});
document.querySelector('.modal-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => {
  const bounds = dialog.getBoundingClientRect();
  if (event.target === dialog && (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom)) dialog.close();
});
dialog.addEventListener('close', () => {
  if (dialog.open) return;
  document.body.style.overflow = '';
  previouslyFocused?.focus();
});

const filters = document.querySelectorAll('.filter');
filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(filter => filter.setAttribute('aria-pressed', String(filter === button)));
  let count = 0;
  document.querySelectorAll('.project-row').forEach(project => {
    project.hidden = button.dataset.filter !== 'all' && !project.dataset.category.split(' ').includes(button.dataset.filter);
    if (!project.hidden) count++;
  });
  document.getElementById('project-count').textContent = String(count).padStart(2, '0') + ' PROJECTS';
}));

const navigation = [...document.querySelectorAll('.nav-dock a')];
if ('IntersectionObserver' in window) {
  const sections = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const active = navigation.find(link => link.hash === '#' + entry.target.id);
      if (!active) return;
      navigation.forEach(link => link.removeAttribute('aria-current'));
      active.setAttribute('aria-current', 'location');
    });
  }, {rootMargin: '-12% 0px -55% 0px', threshold: 0});
  navigation.forEach(link => {
    const section = document.querySelector(link.hash);
    if (section) sections.observe(section);
  });
}

const email = 'bimsarapremarathna123@gmail.com';
let toastTimer;
function notify(message) {
  clearTimeout(toastTimer);
  document.getElementById('toast').textContent = message;
  toastTimer = setTimeout(() => { document.getElementById('toast').textContent = ''; }, 5000);
}
document.getElementById('copy-email').addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(email);
    notify('Email address copied. Let’s talk!');
  } catch {
    notify('Email me at ' + email);
  }
});
document.getElementById('contact-form').addEventListener('submit', event => {
  event.preventDefault();
  const data = new FormData(event.currentTarget);
  const subject = String(data.get('subject')).trim();
  const body = 'Hi Hasindu,\n\n' + String(data.get('message')).trim() + '\n\nFrom: ' + String(data.get('name')).trim() + '\nEmail: ' + String(data.get('email')).trim();
  const destination = 'mailto:' + email + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  window.location.href = destination;
  notify('Your email draft is ready to open. Send it from your email app.');
});
document.getElementById('year').textContent = new Date().getFullYear();
