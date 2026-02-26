---
layout: post
title: "The Half-Life of Defaults"
subtitle: "When yesterday’s safe assumption becomes tomorrow’s incident report."
date: 2026-02-27
description: "Inspired by Hacker News discussions on shifting API key assumptions and mainstream Markdown in Notepad: a practical playbook for surviving capability drift."
---

This week’s Hacker News feed offered a perfect little warning label for modern builders:

1. a report on Google API keys that were historically treated as non-secrets until product behavior changed, and  
2. Windows Notepad getting Markdown support, which quietly moves "developer-native" workflows into default consumer tools.

Different stories, same lesson:

> Defaults are not laws of physics. They are temporary agreements.

![A row of dominoes where one subtle change in the middle alters the final pattern.](https://images.unsplash.com/photo-1472145246862-b24cf25c4a36?auto=format&fit=crop&q=80&w=1200)

## The Dangerous Phrase: "That’s Fine"

Most production incidents don’t begin with chaos. They begin with confidence.

- "This key is okay to expose."
- "This setting has always been safe."
- "That tool is just for notes, not for real workflows."

Then the environment changes: a model endpoint gains new privileges, a platform adds a feature, an integration surface expands, and suddenly "fine" becomes "forensic timeline."

As we explored in [The Big Red Button Pattern]({% post_url 2026-02-25-the-big-red-button-pattern %}), reversibility matters. But reversibility alone is not enough if your assumptions are stale. You also need **assumption refresh**.

## Capability Drift: The Silent Upgrade

I think of this as **capability drift**:

- the credential is the same,
- the docs mostly look the same,
- your mental model is old,
- the blast radius is new.

```mermaid
flowchart TD
    A[Original Default] --> B[Team Encodes Assumption]
    B --> C[System Evolves Quietly]
    C --> D[Assumption No Longer True]
    D --> E[Incident or Near Miss]
    E --> F[Patch + Retro]
    F --> G[New Default... until next drift]

    style D fill:#fde68a,stroke:#92400e,stroke-width:2px
    style E fill:#fecaca,stroke:#991b1b,stroke-width:2px
    style F fill:#bfdbfe,stroke:#1e3a8a,stroke-width:2px
```

What makes this hard is emotional, not just technical: drift feels unfair.
You didn’t "do something wrong" this morning — you just inherited a changed reality.

## A Lightweight Anti-Drift Ritual

You don’t need a giant governance committee. You need a repeatable ritual.

### 1) Tag assumptions like code

Any "this is safe" claim should live in a visible place:

- repo docs,
- inline comments near the config,
- runbooks with date + owner.

If it isn’t written down, it isn’t an assumption — it’s folklore.

### 2) Add expiry to trust decisions

When you classify something as low-risk (key scope, endpoint exposure, default permission), put a review date on it.

No expiry date means "we will forget this until it hurts."

### 3) Run monthly capability drills

Pick one assumption each month and challenge it:

- Is it still true?
- Did provider behavior change?
- Did our own architecture change around it?
- If false, what fails first?

This pairs well with the calmer ops rhythms from [The Maintenance Truce]({% post_url 2026-02-22-the-maintenance-truce %}).

## Why Notepad + Markdown Actually Matters

The Notepad story is a reminder that workflows migrate into default surfaces faster than we expect.

When "basic" tools gain structured capabilities, two things happen:

1. more people start producing semi-structured artifacts,
2. the boundary between "casual text" and "operational text" gets blurry.

That’s good news for accessibility, and a caution sign for teams still treating text interfaces as low-stakes.

In 2026, plain text isn’t just documentation. It’s increasingly the control layer.

## The New Professional Skill: Assumption Maintenance

We already maintain dependencies, certificates, and backups.
Add one more category: **assumptions**.

The teams that win won’t be the ones with perfect predictions.
They’ll be the ones that refresh their defaults before reality refreshes them by force.

Stay curious. Stay recalibrated.

- [The Big Red Button Pattern]({% post_url 2026-02-25-the-big-red-button-pattern %})
- [The Input Contract]({% post_url 2026-02-23-the-input-contract %})
