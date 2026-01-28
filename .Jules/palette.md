## 2024-07-25 - CSS for Hover Effects
**Learning:** When adding UI elements that should only appear on hover, it's not enough to just set `opacity: 1` on the parent's `:hover` state. The element also needs a base style with `opacity: 0`, `position: absolute`, and a `transition` to ensure it's hidden by default and appears smoothly. Without these, the element may be visible at all times, leading to a cluttered and unprofessional UI.
**Action:** Always ensure that hover-triggered elements have a complete set of CSS properties to manage their visibility and positioning.

## 2026-01-28 - Micro-interactions for Navigation
**Learning:** Adding a subtle `transform: scale()` to navigation links on hover and focus-visible states provides immediate, delightful feedback that goes beyond simple color changes. It makes the UI feel more "alive" and responsive. Additionally, increasing `outline-offset` on focus states ensures that the focus ring doesn't crowd the element, improving accessibility for keyboard users by making the focused state unmistakable.
**Action:** Use scale transforms sparingly but effectively to enhance interactivity in high-value areas like navigation.
