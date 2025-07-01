const sidebar = document.getElementById('sidebar');
const mainContent = document.getElementById('main-content');
const toggleSidebarBtn = document.getElementById('toggle-sidebar');
const openSidebarBtn = document.getElementById('open-sidebar');
const sidebarResizer = document.getElementById('sidebar-resizer');

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

// Kéo sidebar
let isResizing = false;

sidebarResizer.addEventListener('mousedown', function(e) {
  isResizing = true;
  document.body.style.cursor = 'ew-resize';
});

document.addEventListener('mousemove', function(e) {
  if (!isResizing) return;
  let newWidth = e.clientX - sidebar.getBoundingClientRect().left;
  if (newWidth < 120) newWidth = 120; // min width
  if (newWidth > 400) newWidth = 400; // max width
  sidebar.style.width = newWidth + 'px';
});

document.addEventListener('mouseup', function(e) {
  if (isResizing) {
    isResizing = false;
    document.body.style.cursor = '';
  }
});