---
layout: default
title: "Home"
description: "Hardware, software, and the systems between."
---

<section class="hero">
  <p class="eyebrow">Notes on computing</p>
  <h2>What I'm thinking about.</h2>
  <p>Hardware, software, and the systems between.</p>
</section>

<section class="recent">
  <div class="section-heading">
    <h3>Latest</h3>
    <p class="meta-note">New posts when I have something to say.</p>
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
    <p>AI, product design, and developer tools.</p>
    <div class="tag-row">
      <span class="pill">AI workflows</span>
      <span class="pill">Product craft</span>
      <span class="pill">Writing systems</span>
      <span class="pill">Tooling</span>
    </div>
  </div>
  <div class="about-card">
    <h3>More</h3>
    <p>All posts in one place.</p>
    <div class="tag-row">
      <a class="pill" href="{{ '/archive.html' | relative_url }}">Archive</a>
      <a class="pill" href="{{ '/term.html' | relative_url }}">Terminal</a>
    </div>
  </div>
</section>
