// Apply the saved appearance before the first paint.
(() => {
  const root = document.documentElement;
  const system = matchMedia('(prefers-color-scheme: dark)');
  let mode = 'system';
  try { mode = localStorage.getItem('appearance') || mode; } catch {}
  function apply() {
    root.dataset.appearance = mode === 'system' ? (system.matches ? 'dark' : 'light') : mode;
  }
  apply();
  system.addEventListener('change', apply);
  document.addEventListener('DOMContentLoaded', () => {
    const select = document.querySelector('#theme');
    select.value = mode;
    select.addEventListener('change', () => {
      mode = select.value;
      try { localStorage.setItem('appearance', mode); } catch {}
      apply();
    });
  });
})();
