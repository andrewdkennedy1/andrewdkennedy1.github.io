---
layout: post
title: "We Live in the Era of Instant Apps"
subtitle: "Or: Why I Refused to Install AutoHotkey"
date: 2026-01-06
description: "Why write a 3-line script when you can engineer a high-performance Rust system utility? Welcome to the era of Instant Apps."
---

It started with a simple, innocent question to ChatGPT:

> **"Is there a Windows keyboard shortcut to UPPERCASE text?"**

The answer was a disappointing "No."

ChatGPT, being helpful, immediately followed up with: *"But you can paste into Word and press Shift+F3, or you can install AutoHotkey and write a script..."*

**AutoHotkey.**

The logical, proven, sensible solution. A tool designed exactly for this purpose. A 3-line script that would have solved my problem in 30 seconds.

But we don't do "sensible" here. We live in the era of **Instant Apps**. If you can dream it, you can prompt it, and then you can pair-program it into existence with an AI agent until it's a compiled binary running native Win32 code.

Why write a script when you can write a **dedicated, high-performance, memory-safe system utility in Rust**?

So we built **RUpper**.

It’s not just a script. It’s a *Service*.

- **It runs in the tray.** (Because we're professional).
- **It uses direct Win32 APIs.** (No heavy frameworks here, we're calling `CreateWindowExW` and manually casting `HMENU` pointers like it's 1998, baby).
- **It features a custom Hotkey Picker.** (Hardcoding keys is for amateurs. We used `msctls_hotkey32`).
- **It has Registry Persistence.** (Your settings survive a reboot. We live in a society).
- **It handles race conditions.** (We have atomic busy flags. For a text uppercaser. Yes.)

When I press `Ctrl + Shift + F3`, it doesn't just "press keys." It intelligently waits for modifiers to release, polls the clipboard sequence number for changes, and surgically injects the uppercased text.

Is it overkill? **Absolutely.**
Is it better than installing AutoHotkey? **100%.**

Welcome to the future.
