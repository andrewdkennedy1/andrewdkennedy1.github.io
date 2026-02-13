# Design Analysis (Current)

_Last updated: 2026-02-13_

This doc was refreshed to match the current codebase and avoid stale guidance.

## Known design/UX fixes now implemented

1. Mermaid is loaded **only when needed** (diagram blocks present).
2. Code copy buttons are discoverable on touch devices and keyboard focus.
3. Share menu behavior is stabilized for touch/click interactions.
4. Bottom-left commit easter egg respects safe-area insets (mobile notch/home indicator).
5. In-article links are underlined by default for better scannability/accessibility.
6. Hidden quote-share widget is forced hidden when `hidden` is present.

## Next improvements worth considering

- Add a visible dark mode toggle (optional; currently light-first).
- Add a simple site search (Lunr/Pagefind) if post count keeps growing.
- Add a tiny visual regression check in CI for layout drift.
