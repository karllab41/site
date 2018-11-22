---
layout: page
title: short stories
description: my streams of consciousness
img: /assets/img/interests/short-story4x.jpg
---

<ul class="post-list">
  {% for story in site.stories reversed %}
    <li>
      <h3><a class="post-title" href="{{ story.url | prepend: site.baseurl }}"><h3>{{ story.title }}</h3></a></h3>
      <p class="story-meta">{{ story.date | date: '%B %-d, %Y' }}--
      {{ story.description }}</p>
    </li>
  {% endfor %}
</ul>

{% include pagination.html %}
