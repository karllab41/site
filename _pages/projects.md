---
layout: page
title: teaching
permalink: /teaching/
description: A growing collection our video blogs
---

<ul class="post-list">
  {% for project in site.projects reversed %}
    <li>
      <a href="{{ project.url | prepend: site.baseurl }}"> 
      <img src="{{ project.img }}" style="float:right;width:368px;height:184px;"/></a>
      <h3><a class="post-title" href="{{ project.url | prepend: site.baseurl }}"><h3>{{ project.title }}</h3></a></h3>
      <p class="post-meta">{{ project.date | date: '%B %-d, %Y — %H:%M' }}</p>
      <p>{{ post.description }}</p>
    </li>
    <p> </p> 
  {% endfor %}
</ul>

