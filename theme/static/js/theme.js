(() => {
  const ctrl = document.querySelector('.theme-controller');
  const root = document.documentElement;

  // initialise from storage / prefers‑color‑scheme
  const saved = localStorage.getItem('theme');
  if (saved) {
    root.setAttribute('data-theme', saved);
    ctrl.checked = saved === 'dark';
  } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    root.setAttribute('data-theme', 'dark');
    ctrl.checked = true;
  }

  ctrl.addEventListener('change', () => {
    const theme = ctrl.checked ? 'dark' : 'light';
    root.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  });
})();