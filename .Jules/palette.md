## 2024-07-25 - CSS for Hover Effects
**Learning:** When adding UI elements that should only appear on hover, it's not enough to just set `opacity: 1` on the parent's `:hover` state. The element also needs a base style with `opacity: 0`, `position: absolute`, and a `transition` to ensure it's hidden by default and appears smoothly. Without these, the element may be visible at all times, leading to a cluttered and unprofessional UI.
**Action:** Always ensure that hover-triggered elements have a complete set of CSS properties to manage their visibility and positioning.

## 2026-01-28 - Micro-interactions for Navigation
**Learning:** Adding a subtle `transform: scale()` to navigation links on hover and focus-visible states provides immediate, delightful feedback that goes beyond simple color changes. It makes the UI feel more "alive" and responsive. Additionally, increasing `outline-offset` on focus states ensures that the focus ring doesn't crowd the element, improving accessibility for keyboard users by making the focused state unmistakable.
**Action:** Use scale transforms sparingly but effectively to enhance interactivity in high-value areas like navigation.

## 2026-01-29 - Scroll Progress and Reading Context
**Learning:** Providing context for long-form content is key to keeping users engaged. A scroll progress bar at the top of the page offers a subtle, non-intrusive way to communicate "how much is left," which is particularly useful for in-depth technical posts. Similarly, a "Reading Time" indicator helps users manage their expectations before they commit to a post. Both are examples of "empathetic design"—recognizing the user's time and attention as valuable resources.
**Action:** Always include progress indicators or reading time for content exceeding 500 words.

## 2026-01-31 - Code Block Interactivity
**Learning:** For technical blogs, code blocks are primary interaction points. Adding a "Copy" button directly to the `<pre>` tag significantly reduces friction for users who want to try out examples. Using `position: absolute` and `opacity: 0` (revealed on hover) keeps the UI clean until the user shows intent. Crucially, providing immediate visual feedback (changing text to "Copied!") is essential to confirm the action was successful, especially since clipboard operations are otherwise invisible.
**Action:** Always provide "Copied!" feedback and handle `pre` blocks with `overflow-x: auto` by ensuring the button remains pinned to the visible area (or parent container).

## 2026-02-01 - Subtle Information Hierarchies
**Learning:** Secondary actions like "Share" don't always need their own prominent UI block (like a "Share Bar"). Integrating them into existing metadata lines (like the post date and reading time) creates a much more "elegant" and less cluttered experience. However, when nesting complex UI components (like a dropdown menu) into metadata lines, ensure the HTML structure remains valid (e.g., using a `<div>` instead of a `<p>` for metadata if it contains other block-level elements) to prevent the browser from breaking the DOM tree and subsequent JS logic.
**Action:** Look for opportunities to merge secondary controls into existing metadata lines to reduce visual noise, while maintaining strict HTML semantics.
