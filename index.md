---
layout: default
---

<div class="hero">
  <p class="eyebrow">Fresh notes and learnings</p>
  <h2>Thoughtful write-ups, experiments, and things I'm building.</h2>
  <p>Browse the latest posts below or jump back into a recent deep dive. Everything is spaced out and easy to read on any device.</p>
</div>

<div class="section-heading">
  <h2>Recent Posts</h2>
  <p class="meta-note">A curated stream of the newest entries</p>
</div>

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
