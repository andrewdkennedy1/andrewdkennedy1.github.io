---
layout: default
---

<div class="terminal-header">
<pre class="ascii-art">
   ___    _   ______  ____  _______       __
  /   |  / | / / __ \/ __ \/ ____/ |     / /
 / /| | /  |/ / / / / /_/ / __/  | | /| / / 
/_/  |_/_/ |_/_____/_/ |_/_____/  |__/|__/   
</pre>
</div>

<div class="intro-blurb glass-panel">
    <div>
        <span class="prompt">&gt;</span> <span class="typing">Welcome, Traveler.</span>
    </div>
    
    <p class="bio">
        Accessing secure archives... <br>
        <span class="highlight">Encryption:</span> DISABLED. <span class="highlight">Protocol:</span> OPEN.
    </p>

    <div class="status-bar">
        <span><span class="blink">▮</span> ONLINE</span>
        <span>LOC: GRID_NODE_7</span>
        <span>UPTIME: 99.9%</span>
    </div>
</div>

<hr class="neon-divider">

<h2 class="glitch-hover">> RECENT_TRANSMISSIONS</h2>

<div class="post-grid">
  {% for post in site.posts %}
    <article class="post-card">
      <div class="meta">{{ post.date | date: "%Y.%m.%d" }} // LOG_ENTRY</div>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <div class="excerpt">
        {{ post.excerpt | strip_html | truncatewords: 20 }}
      </div>
      <a href="{{ post.url }}" class="read-link">READ_FULL_LOG >></a>
    </article>
  {% endfor %}
</div>
