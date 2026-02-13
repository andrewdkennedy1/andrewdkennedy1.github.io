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

  const setMenuStatus = (button) => {
    if (!button || !button.classList.contains('share-menu-item')) return;
    const label = button.dataset.confirmLabel;
    const status = button.querySelector('.menu-status');
    if (label && status) status.textContent = label;
    button.classList.add('is-confirmed');
    clearTimeout(button._confirmTimer);
    button._confirmTimer = setTimeout(() => {
      button.classList.remove('is-confirmed');
    }, 2000);
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
              setMenuStatus(button);
            } catch (err) {
              setStatus(container, 'Share canceled.', true);
            }
          } else {
            try {
              await copyToClipboard(payload.url);
              setStatus(container, 'Link copied.');
              trackEvent('share_completed', { method: 'copy', url: payload.url });
              setMenuStatus(button);
            } catch (err) {
              setStatus(container, 'Copy failed.', true);
            }
          }
          const menu = button.closest('[data-share-menu]');
          if (menu) menu.classList.remove('is-open');
          return;
        }

        if (action === 'copy') {
          trackEvent('share_clicked', { method: 'copy', url: payload.url });
          try {
            await copyToClipboard(payload.url);
            setStatus(container, 'Link copied.');
            trackEvent('share_completed', { method: 'copy', url: payload.url });
            setMenuStatus(button);
          } catch (err) {
            setStatus(container, 'Copy failed.', true);
          }
          const menu = button.closest('[data-share-menu]');
          if (menu) menu.classList.remove('is-open');
        }
      });
    });

    const shareMenus = document.querySelectorAll('[data-share-menu]');
    shareMenus.forEach((menu) => {
      const toggle = menu.querySelector('.share-icon-button');
      const panel = menu.querySelector('.share-menu-panel');
      if (!toggle) return;

      toggle.addEventListener('click', (event) => {
        event.stopPropagation();
        const isOpen = menu.classList.contains('is-open');
        shareMenus.forEach((other) => other.classList.remove('is-open'));
        if (!isOpen) {
          menu.classList.add('is-open');
        }
      });

      if (panel) {
        panel.addEventListener('click', (event) => {
          event.stopPropagation();
        });
      }
    });

    document.addEventListener('click', (event) => {
      if (event.target.closest('[data-share-menu]')) return;
      shareMenus.forEach((menu) => menu.classList.remove('is-open'));
    });

    document.addEventListener('keyup', (event) => {
      if (event.key === 'Escape') {
        shareMenus.forEach((menu) => menu.classList.remove('is-open'));
      }
    });

    const selectionButton = document.createElement('button');
    selectionButton.type = 'button';
    selectionButton.className = 'quote-share-button';
    selectionButton.innerText = 'Copy quote link';
    selectionButton.hidden = true;

    const selectionStatus = document.createElement('span');
    selectionStatus.className = 'quote-share-status';
    selectionStatus.setAttribute('aria-live', 'polite');

    const selectionWrapper = document.createElement('div');
    selectionWrapper.className = 'quote-share-widget';
    selectionWrapper.hidden = true;
    selectionWrapper.appendChild(selectionButton);
    selectionWrapper.appendChild(selectionStatus);

    document.body.appendChild(selectionWrapper);

    let currentQuote = '';
    let currentUrl = '';

    const hideSelectionWidget = () => {
      selectionWrapper.hidden = true;
      selectionButton.hidden = true;
      selectionStatus.textContent = '';
      selectionStatus.dataset.state = '';
    };

    const showSelectionWidget = (rect) => {
      const top = window.scrollY + rect.top - 42;
      const left = window.scrollX + rect.left;
      selectionWrapper.style.top = `${Math.max(top, 8)}px`;
      selectionWrapper.style.left = `${Math.max(left, 8)}px`;
      selectionWrapper.hidden = false;
      selectionButton.hidden = false;
    };

    const normalizeQuote = (text) =>
      text.replace(/\s+/g, ' ').trim().slice(0, 200);

    const buildTextFragmentUrl = (url, quote) => {
      const base = url.split('#')[0];
      return `${base}#:~:text=${encodeURIComponent(quote)}`;
    };

    const updateSelection = () => {
      const postContent = document.querySelector('.post-content');
      if (!postContent) return;

      const selection = window.getSelection();
      if (!selection || selection.isCollapsed) {
        hideSelectionWidget();
        return;
      }

      const range = selection.rangeCount ? selection.getRangeAt(0) : null;
      if (!range) {
        hideSelectionWidget();
        return;
      }

      if (!postContent.contains(range.commonAncestorContainer)) {
        hideSelectionWidget();
        return;
      }

      const quote = normalizeQuote(selection.toString());
      if (quote.length < 24) {
        hideSelectionWidget();
        return;
      }

      currentQuote = quote;
      currentUrl = buildTextFragmentUrl(window.location.href, quote);

      const rect = range.getBoundingClientRect();
      if (rect.width === 0 && rect.height === 0) {
        hideSelectionWidget();
        return;
      }

      showSelectionWidget(rect);
    };

    document.addEventListener('mouseup', () => {
      setTimeout(updateSelection, 0);
    });

    document.addEventListener('keyup', (event) => {
      if (event.key === 'Escape') {
        hideSelectionWidget();
        return;
      }
      setTimeout(updateSelection, 0);
    });

    selectionButton.addEventListener('click', async () => {
      if (!currentQuote || !currentUrl) return;
      trackEvent('quote_share_clicked', { url: currentUrl });
      const shareText = `“${currentQuote}”\n${currentUrl}`;
      try {
        await copyToClipboard(shareText);
        selectionStatus.textContent = 'Quote link copied.';
        selectionStatus.dataset.state = 'success';
        trackEvent('quote_share_copied', { url: currentUrl });
      } catch (err) {
        selectionStatus.textContent = 'Copy failed.';
        selectionStatus.dataset.state = 'error';
      }
      setTimeout(() => {
        selectionStatus.textContent = '';
        selectionStatus.dataset.state = '';
      }, 2200);
    });
  });
})();
