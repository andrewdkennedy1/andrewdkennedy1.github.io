---
layout: default
title: "Home"
description: "Hardware, software, and the systems between."
---

<section class="hero">
  <div class="hero-grid">
    <div>
      <p class="eyebrow">Daily systems notebook</p>
      <h1>Bold ideas for builders, designers, and the curious.</h1>
      <p class="lede">Short, focused essays on hardware, software, and the systems between. Read the daily drop or explore the archive for long-form thinking.</p>
      <div class="hero-actions">
        <a class="button primary" href="#daily">Read today’s briefing</a>
        <a class="button ghost" href="{{ '/archive.html' | relative_url }}">Browse the archive</a>
      </div>
      <div class="hero-meta">
        <span class="meta-pill">{{ site.posts | size }} essays</span>
        <span class="meta-pill">Updated most days</span>
        <span class="meta-pill">Built for deep focus</span>
      </div>
    </div>
    {% assign latest = site.posts.first %}
    <div class="hero-card">
      <p class="meta">Latest entry · {{ latest.date | date: "%B %-d, %Y" }}</p>
      <h3><a href="{{ latest.url | relative_url }}">{{ latest.title }}</a></h3>
      <p class="excerpt">{{ latest.excerpt | strip_html | truncatewords: 28 }}</p>
      <a href="{{ latest.url | relative_url }}" class="read-link">Open story</a>
    </div>
  </div>
</section>

<section id="daily" class="daily">
  <div class="section-heading">
    <h3>Daily Briefing</h3>
    <p class="meta-note">Newest writing, one click away.</p>
  </div>
  <div class="daily-grid">
    <div class="daily-list">
      {% for post in site.posts limit:7 %}
        <article class="daily-item">
          <div class="daily-date">{{ post.date | date: "%b %-d, %Y" }}</div>
          <div>
            <h3 class="daily-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
            <p class="meta-note">{{ post.excerpt | strip_html | truncatewords: 20 }}</p>
          </div>
        </article>
      {% endfor %}
    </div>
    <aside class="daily-panel">
      <h4>Daily flow</h4>
      <p class="meta-note">A fast path to the newest post, plus the essentials.</p>
      <ul>
        <li>Scan the latest seven entries.</li>
        <li>Jump into the terminal sandbox for experiments.</li>
        <li>Save the archive for deep dives.</li>
      </ul>
      <div class="tag-row">
        <a class="pill" href="{{ '/term.html' | relative_url }}">Terminal</a>
        <a class="pill" href="{{ '/archive.html' | relative_url }}">Archive</a>
      </div>
    </aside>
  </div>
</section>

<section class="recent">
  <div class="section-heading">
    <h3>Featured Reads</h3>
    <p class="meta-note">Hand-picked highlights.</p>
  </div>
  <div class="post-list">
    {% for post in site.posts limit:3 %}
      <article class="post-card">
        <p class="meta">{{ post.date | date: "%B %-d, %Y" }}</p>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | strip_html | truncatewords: 26 }}</p>
        <a href="{{ post.url | relative_url }}" class="read-link">Read</a>
      </article>
    {% endfor %}
  </div>
</section>

<section class="about">
  <div class="about-card">
    <h3>Focus areas</h3>
    <p>AI systems, product design, and developer tooling with a practical lens.</p>
    <div class="tag-row">
      <span class="pill">AI workflows</span>
      <span class="pill">Product craft</span>
      <span class="pill">Writing systems</span>
      <span class="pill">Tooling</span>
    </div>
  </div>
  <div class="about-card">
    <h3>Quick access</h3>
    <p>Jump to the archive or open the terminal playground.</p>
    <div class="tag-row">
      <a class="pill" href="{{ '/archive.html' | relative_url }}">Archive</a>
      <a class="pill" href="{{ '/term.html' | relative_url }}">Terminal</a>
    </div>
  </div>
  <div class="about-card">
    <h3>Stay in the loop</h3>
    <p>Check back daily for fresh notes and concise explorations.</p>
    <div class="tag-row">
      <span class="pill">Daily brief</span>
      <span class="pill">Long-form essays</span>
      <span class="pill">Deep dives</span>
    </div>
  </div>
</section>
