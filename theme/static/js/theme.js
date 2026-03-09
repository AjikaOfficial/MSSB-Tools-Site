if (
  localStorage.theme === "dark" ||
  (!localStorage.theme &&
    window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  document.documentElement.classList.add("dark")
} else {
  document.documentElement.classList.remove("dark")
}

document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("theme-toggle");
  const dot = document.getElementById("toggle-dot");

  function updateUI(isDark) {
    if (isDark) {
      dot.style.transform = "translateX(20px)";
      toggle.checked = true;
    } else {
      dot.style.transform = "translateX(0px)";
      toggle.checked = false;
    }
  }

  let isDark =
    localStorage.theme === "dark" ||
    (!localStorage.theme &&
      window.matchMedia("(prefers-color-scheme: dark)").matches);

  updateUI(isDark);

  toggle.addEventListener("change", () => {
    if (toggle.checked) {
      document.documentElement.classList.add("dark");
      localStorage.theme = "dark";
      updateUI(true);
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.theme = "light";
      updateUI(false);
    }
  });
});
