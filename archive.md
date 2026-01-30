---
layout: default
title: "Archive"
description: "All posts."
---

<header class="list-header">
  <h1>Archive</h1>
  <p>{{ site.posts | size }} posts</p>
</header>

<ul class="post-list">
  {% for post in site.posts %}
    <li class="post-item">
      <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <div class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</div>
      {% if post.excerpt %}
        <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 24 }}</p>
      {% endif %}
    </li>
  {% endfor %}
</ul>
