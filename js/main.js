// Match globe diameter to the main title box (ticker sits below; ignored for align).
function syncGlobeToBrand() {
  const brand = document.querySelector(".brand");
  if (!brand) return;
  const height = brand.getBoundingClientRect().height;
  if (height > 0) {
    document.documentElement.style.setProperty("--globe-size", `${height}px`);
  }
}

function boot() {
  document.body.classList.add("is-live");
  syncGlobeToBrand();
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(syncGlobeToBrand);
  }
  window.addEventListener("resize", syncGlobeToBrand);
}

requestAnimationFrame(boot);
