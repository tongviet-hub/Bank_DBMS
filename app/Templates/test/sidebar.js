const sidebar = document.getElementById('sidebar');
const mainContent = document.getElementById('main-content');
const toggleSidebarBtn = document.getElementById('toggle-sidebar');
const openSidebarBtn = document.getElementById('open-sidebar');

toggleSidebarBtn.addEventListener('click', () => {
  const isHidden = sidebar.classList.toggle('hidden');
  mainContent.classList.toggle('full');
  toggleSidebarBtn.setAttribute('aria-expanded', !isHidden);
});

openSidebarBtn.addEventListener('click', () => {
  const isHidden = sidebar.classList.toggle('hidden');
  mainContent.classList.toggle('full');
  toggleSidebarBtn.setAttribute('aria-expanded', !isHidden);
});