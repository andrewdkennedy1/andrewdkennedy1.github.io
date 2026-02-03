(() => {
  const trackEvent = (name, detail = {}) => {
    const payload = { name, detail, ts: Date.now() };

    try {
      const key = `metrics:${name}`;
      const current = Number(localStorage.getItem(key) || 0);
      localStorage.setItem(key, String(current + 1));
      localStorage.setItem('metrics:last', JSON.stringify(payload));
    } catch (err) {
      // ignore storage issues
    }

    if (typeof window.plausible === 'function') {
      window.plausible(name, { props: detail });
    }

    window.dispatchEvent(new CustomEvent('analytics', { detail: payload }));
  };

  const setStatus = (container, message, isError = false) => {
    if (!container) return;
    const status = container.querySelector('.share-status');
    if (!status) return;
    status.textContent = message;
    status.dataset.state = isError ? 'error' : 'success';
    if (message) {
      clearTimeout(status._clearTimer);
      status._clearTimer = setTimeout(() => {
        status.textContent = '';
        status.dataset.state = '';
      }, 2400);
    }
  };

  const getSharePayload = (button) => {
    const title = button.dataset.shareTitle || document.title || '';
    const url = button.dataset.shareUrl || window.location.href;
    const text = button.dataset.shareText || title;
    return { title, url, text };
  };

  const copyToClipboard = async (text) => {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(text);
      return true;
    }
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'absolute';
    textarea.style.left = '-9999px';
    document.body.appendChild(textarea);
    textarea.select();
    const success = document.execCommand('copy');
    document.body.removeChild(textarea);
    return success;
  };

  document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('[data-share-action]');
    buttons.forEach((button) => {
      button.addEventListener('click', async () => {
        const action = button.dataset.shareAction;
        const container = button.closest('[data-share-container]');
        const payload = getSharePayload(button);

        if (action === 'native') {
          trackEvent('share_clicked', { method: 'native', url: payload.url });
          if (navigator.share) {
            try {
              await navigator.share(payload);
              setStatus(container, 'Shared!');
              trackEvent('share_completed', { method: 'native', url: payload.url });
            } catch (err) {
              setStatus(container, 'Share canceled.', true);
            }
          } else {
            try {
              await copyToClipboard(payload.url);
              setStatus(container, 'Link copied.');
              trackEvent('share_completed', { method: 'copy', url: payload.url });
            } catch (err) {
              setStatus(container, 'Copy failed.', true);
            }
          }
          return;
        }

        if (action === 'copy') {
          trackEvent('share_clicked', { method: 'copy', url: payload.url });
          try {
            await copyToClipboard(payload.url);
            setStatus(container, 'Link copied.');
            trackEvent('share_completed', { method: 'copy', url: payload.url });
          } catch (err) {
            setStatus(container, 'Copy failed.', true);
          }
        }
      });
    });
  });
})();
