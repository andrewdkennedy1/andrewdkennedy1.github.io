---
layout: default
---

<section class="hero">
  <p class="eyebrow">Notes on building in the agent era</p>
  <h2>Minimal signals, thoughtful pacing.</h2>
  <p>One stream of writing lives here. No archives, no clutter—just the latest draft of what I'm learning.</p>
</section>

<section class="recent">
  <div class="section-heading">
    <h3>Latest entry</h3>
    <p class="meta-note">Updated whenever something new is worth keeping.</p>
  </div>
  <div class="post-list">
    {% for post in site.posts %}
      <article class="post-card">
        <p class="meta">{{ post.date | date: "%B %-d, %Y" }}</p>
        <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
        <p class="excerpt">{{ post.excerpt | strip_html | truncatewords: 28 }}</p>
        <a href="{{ post.url }}" class="read-link">Read the piece</a>
      </article>
    {% endfor %}
  </div>
</section>
