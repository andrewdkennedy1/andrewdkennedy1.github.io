---
layout: post
title: "The Bizarre Resilience of QR Codes"
subtitle: "Why a damaged QR code can still be read and what it teaches us about error correction."
date: 2026-01-04
description: "Exploring Reed‑Solomon error correction, finder patterns, and the surprising robustness that lets you tear a QR code apart and still scan it."
---

QR codes are everywhere now—on receipts, airline boarding passes, and even on your fridge. But most people never stop to wonder **how** a damaged square of black‑and‑white pixels can still be decoded.

### The Core Idea: Reed‑Solomon

At the heart of a QR code lies a **Reed‑Solomon** code. It treats the encoded data as a polynomial over a finite field and adds *parity* symbols. Those extra symbols let a decoder recover lost data, just like a crossword puzzle where missing letters can be inferred from the surrounding words.

* **Data capacity** – depends on the version (size) and error‑correction level (L, M, Q, H).
* **Error‑correction level** – each level reserves a different percentage of codewords for recovery:
  * L  – 7 % recovery
  * M  – 15 % recovery
  * Q  – 25 % recovery
  * H  – 30 % recovery

This means an **H‑level QR code** can lose almost a third of its symbols and still be readable.

### Finder, Alignment, and Timing Patterns

Beyond the raw data, a QR code contains *structure* that guides the scanner:

* **Finder patterns** – the three large squares in the corners; they let the reader locate orientation.
* **Alignment patterns** – small squares distributed across the grid for larger versions; they keep the grid straight.
* **Timing patterns** – alternating black/white modules that let the scanner count rows and columns.

These patterns are **never corrupted** by the error‑correction algorithm – they’re placed in fixed positions and serve as anchors.

### Real‑World Demo: Tearing a QR Code Apart

> **Try it:** Print a QR code at `H` level, cut out up to 30 % of the squares, and scan. You’ll be amazed that the scanner still recovers the original URL.

The reason is simple: the Reed‑Solomon code can reconstruct missing *codewords* (groups of 8 bits). As long as the number of damaged codewords stays below the recovery threshold, the original data is mathematically recoverable.

### Diagram – Error‑Correction Flow

```mermaid
flowchart LR
    A[Input data] --> B[Encode to binary]
    B --> C[Add Reed‑Solomon parity]
    C --> D[Place modules (finder, alignment, timing)]
    D --> E[Render QR image]
    E --> F[Physical damage (optional)]
    F --> G[Scanner reads modules]
    G --> H[Reed‑Solomon decoder recovers data]
    H --> I[Output original payload]
```

### Takeaways

* **Robustness by design** – QR codes deliberately sacrifice visual fidelity for resilience.
* **Design trade‑offs** – Higher error‑correction means fewer data bytes. For a URL, the loss is trivial; for high‑density payloads, you may need to balance size vs. resilience.
* **Inspiration for other systems** – The same Reed‑Solomon approach powers satellite communications and data‑center storage (RAID‑6). QR codes remind us that well‑chosen redundancy can make seemingly fragile systems surprisingly durable.

---

*This post is part of a series exploring the hidden engineering behind everyday tech.*
