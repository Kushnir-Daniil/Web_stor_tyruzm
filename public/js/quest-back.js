/** Кнопка «Назад» поверх Unity WebGL (підключається в builds/game-*/index.html) */
(function () {
  if (window.self !== window.top) return;

  var backUrl =
    sessionStorage.getItem("gamesReturn") ||
    sessionStorage.getItem("questReturn") ||
    "/public/games.html";

  var bar = document.createElement("div");
  bar.id = "quest-back-bar";
  bar.style.cssText =
    "position:fixed;top:0;left:0;right:0;z-index:100000;padding:10px 12px;" +
    "background:#F6E1AB;border-bottom:4px solid #E2CB92;" +
    "font-family:system-ui,sans-serif;box-sizing:border-box;";
  bar.innerHTML =
    '<a href="' +
    backUrl +
    '" style="display:inline-flex;align-items:center;min-height:40px;padding:8px 14px;' +
    "font-weight:700;font-size:15px;color:#CA4E5D;text-decoration:none;" +
    'background:#FEF5DA;border-radius:12px;">← Назад</a>';

  function mount() {
    if (document.body) {
      document.body.insertBefore(bar, document.body.firstChild);
      document.body.style.paddingTop = "56px";
    }
  }

  if (document.body) mount();
  else document.addEventListener("DOMContentLoaded", mount);
})();
