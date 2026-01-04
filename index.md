---
layout: default
---

## Recent Posts

<div class="post-grid">
  {% for post in site.posts %}
    <article class="post-card">
      <div class="meta">{{ post.date | date: "%B %-d, %Y" }}</div>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <div class="excerpt">
        {{ post.excerpt | strip_html | truncatewords: 25 }}
      </div>
      <a href="{{ post.url }}" class="read-link">Read more →</a>
    </article>
  {% endfor %}
</div>
