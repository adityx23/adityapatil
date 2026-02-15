(function () {
  function makeToggle() {
    const btn = document.createElement("button");
    btn.className = "theme-toggle";
    btn.type = "button";
    btn.innerHTML = `<span class="dot"></span><span id="themeLabel">Dark</span>`;
    document.body.appendChild(btn);

    function setTheme(next) {
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch(e) {}
      const label = btn.querySelector("#themeLabel");
      if (label) label.textContent = next === "dark" ? "Dark" : "Light";
    }

    const current = document.documentElement.getAttribute("data-theme") || "dark";
    setTheme(current);

    btn.addEventListener("click", () => {
      const cur = document.documentElement.getAttribute("data-theme") || "dark";
      setTheme(cur === "dark" ? "light" : "dark");
    });
  }

  function addReveal() {
    const main = document.querySelector("main") || document.body;
    const targets = main.querySelectorAll("h1, h2, h3, p, ul, ol, .card, img");
    targets.forEach((el, i) => {
      el.classList.add("reveal");
      el.style.animationDelay = Math.min(i * 25, 220) + "ms";
    });
  }

  window.addEventListener("DOMContentLoaded", () => {
    makeToggle();
    addReveal();
  });
})();
