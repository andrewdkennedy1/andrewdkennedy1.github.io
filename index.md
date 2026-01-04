---
layout: default
title: "Home"
description: "Essays on software craft, AI tooling, and building with intention."
---

<section class="hero">
  <p class="eyebrow">Notes on building in the agent era</p>
  <h2>Quiet software, bold ideas.</h2>
  <p>Short essays on making software that feels deliberate: clear prompts, sharp taste, and systems that age well.</p>
</section>

<section class="recent">
  <div class="section-heading">
    <h3>Latest writing</h3>
    <p class="meta-note">Fresh drafts whenever something new earns the space.</p>
  </div>
  <div class="post-list">
    {% for post in site.posts limit:3 %}
      <article class="post-card">
        <p class="meta">{{ post.date | date: "%B %-d, %Y" }}</p>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | strip_html | truncatewords: 26 }}</p>
        <a href="{{ post.url | relative_url }}" class="read-link">Read the piece</a>
      </article>
    {% endfor %}
  </div>
</section>

<section class="about">
  <div class="about-card">
    <h3>What I am exploring</h3>
    <p>How AI changes creative work, how teams ship with taste, and how to make tools that feel human.</p>
    <div class="tag-row">
      <span class="pill">AI workflows</span>
      <span class="pill">Product craft</span>
      <span class="pill">Writing systems</span>
      <span class="pill">Tooling</span>
    </div>
  </div>
  <div class="about-card">
    <h3>Start here</h3>
    <p>The archive is short and curated. Every piece is meant to stand on its own.</p>
    <div class="tag-row">
      <a class="pill" href="{{ '/archive.html' | relative_url }}">Browse the archive</a>
      <a class="pill" href="{{ '/term.html' | relative_url }}">Open the terminal</a>
    </div>
  </div>
</section>
