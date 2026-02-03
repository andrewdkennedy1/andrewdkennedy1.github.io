(() => {
  const getFallbackSrc = () => {
    if (typeof window.IMAGE_FALLBACK_SRC === 'string') {
      return window.IMAGE_FALLBACK_SRC;
    }
    return '/assets/images/image-unavailable.svg';
  };

  const applyFallback = (img) => {
    if (!img || img.dataset.fallbackApplied === 'true') return;
    img.dataset.fallbackApplied = 'true';
    img.src = getFallbackSrc();
    if (!img.alt) {
      img.alt = 'Image unavailable';
    }
    img.classList.add('image-fallback');
  };

  document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('img');
    images.forEach((img) => {
      if (img.complete && img.naturalWidth === 0) {
        applyFallback(img);
      }
      img.addEventListener('error', () => applyFallback(img));
    });
  });
})();
