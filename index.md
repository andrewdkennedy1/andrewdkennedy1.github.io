---
layout: default
title: "Home"
description: "Hardware, software, and the systems between."
---

{% assign latest = site.posts.first %}

<section class="hero" id="signal">
  <p class="eyebrow">Signal desk</p>
  <h1>Hardware, software, and the systems between.</h1>
  <p class="hero-lead">Daily dispatches from the bench, where microelectronics, product sense, and a restless curiosity about tooling intersect. Think of this space as a studio log—short essays, riffs, and experiments that keep the rhythm steady.</p>
  <div class="hero-actions">
    <a class="primary" href="{{ latest.url | relative_url }}">Read the latest signal</a>
    <a class="secondary" href="#notes">Open the notebook</a>
  </div>
</section>

<section class="spotlight-grid" aria-label="Spotlight">
  <article class="glass-panel">
    <p class="eyebrow">{{ latest.date | date: "%B %-d" }}</p>
    <h3><a href="{{ latest.url | relative_url }}">{{ latest.title }}</a></h3>
    <p>Day 27 is finally captured—the missing pulse from this January run. The gap is gone, the streak is whole, and the latest note is waiting with a mix of analog care and system-level curiosity.</p>
    <div class="stat-grid">
      <div class="stat">
        <strong>{{ site.posts | size }}</strong>
        <small>dispatches logged</small>
      </div>
      <div class="stat">
        <strong>{{ latest.date | date: "%B %-d" }}</strong>
        <small>fresh signal</small>
      </div>
    </div>
  </article>
  <article class="glass-panel">
    <p class="eyebrow">Studio focal points</p>
    <h3>The craft I keep returning to</h3>
    <p>The terminal is gone. In its place is a slow, tactile focus on systems that feel meaningful, not performative.</p>
    <ul class="focus-list">
      <li>Analog textures and tactile keyboards that remind me why machines feel alive.</li>
      <li>Product decisions that respect human attention and avoid shimmer.</li>
      <li>Tooling experiments that lean hard on reuse, resilience, and clarity.</li>
    </ul>
  </article>
</section>

<section class="post-section" id="notes">
  <div class="section-heading">
    <h3>Latest dispatches</h3>
    <p class="meta-note">What landed on the desk this week.</p>
  </div>
  <div class="post-grid">
    {% for post in site.posts limit:4 %}
      <article class="post-card">
        <p class="meta">{{ post.date | date: "%B %-d, %Y" }}</p>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | strip_html | truncatewords: 28 }}</p>
        <div class="post-card-footer">
          <a class="read-link" href="{{ post.url | relative_url }}">Read</a>
          {% if post.subtitle %}
            <span class="meta-note">{{ post.subtitle }}</span>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<section class="insight" id="notebook">
  <div class="section-heading">
    <h3>The notebook</h3>
    <p class="meta-note">Micro-updates, systems sketches, and curiosities.</p>
  </div>
  <div class="insight-stack">
    <article class="insight-card">
      <strong>Signals</strong>
      <p>Every signal starts with listening. I fold in the hum of hardware, how keyboards flex, and which parts of software feel indulgent versus necessary.</p>
    </article>
    <article class="insight-card">
      <strong>Tools</strong>
      <p>Scripts that stay simple, layouts that breathe, and tabs that respect muscle memory. The goal is always to keep the craft lightweight.</p>
    </article>
    <article class="insight-card">
      <strong>People</strong>
      <p>Notes on my reading, what I’m following, and where the systems community is pushing hard. There’s plenty of opinion, but only the useful kind.</p>
    </article>
  </div>
</section>
