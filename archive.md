---
layout: default
title: "Archive"
description: "All posts."
---

<section class="hero">
  <div>
    <p class="eyebrow">Everything in one place</p>
    <h2>The archive</h2>
    <p>Search every entry, from the newest dispatch to the earliest notes.</p>
  </div>
</section>

<section class="archive">
  <div class="section-heading">
    <h3>All posts</h3>
    <p class="meta-note">{{ site.posts | size }} entries</p>
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
