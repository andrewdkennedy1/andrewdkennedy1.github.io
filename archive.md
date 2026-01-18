---
layout: default
title: "Archive"
description: "All posts."
---

<section class="hero">
  <p class="eyebrow">Everything</p>
  <h2>Archive</h2>
  <p>All posts, by date.</p>
</section>

<section class="archive">
  <div class="section-heading">
    <h3>Posts</h3>
    <p class="meta-note">{{ site.posts | size }} total</p>
  </div>
  <div class="archive-list">
    {% for post in site.posts %}
      <article class="archive-item">
        <div class="archive-date">{{ post.date | date: "%b %-d, %Y" }}</div>
        <div>
          <h3 class="archive-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
          <p class="meta-note">{{ post.excerpt | strip_html | truncatewords: 24 }}</p>
        </div>
      </article>
    {% endfor %}
  </div>
</section>
