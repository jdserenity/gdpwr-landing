// Motion lives in CSS. This only marks the page live after first paint.
requestAnimationFrame(() => {
  document.body.classList.add("is-live");
});
