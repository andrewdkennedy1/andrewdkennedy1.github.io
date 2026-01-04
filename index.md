---
layout: default
---

<div class="terminal-header">
<pre class="ascii-art">
    ___    _   ______  ____  _______       __
   /   |  / | / / __ \/ __ \/ ____/ |     / /
  / /| | /  |/ / / / / /_/ / __/  | | /| / / 
 / ___ |/ /|  / /_/ / _, _/ /___  | |/ |/ /  
/_/  |_/_/ |_/_____/_/ |_/_____/  |__/|__/   
</pre>
</div>

<div class="intro-blurb">
<span class="prompt">&gt;</span> <span class="typing">Welcome, fellow traveler.</span>

<p class="bio">
Some things are better <span class="highlight">discovered</span> than explained.
</p>

<p class="status">
<span class="blink">▮</span> <em>Status: Online</em> | <em>Location: The Grid</em>
</p>
</div>

<hr class="neon-divider">

# > ACCESSING_ARCHIVES...

<ul class="posts">
  {% for post in site.posts %}
    <li>
      <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span> &raquo; 
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
