---
layout: page
title: interests 
permalink: /interests/
description: music, paintings, and food
---

{% for interest in site.interests %}

{% if interest.redirect %}
<div class="interest">
    <div class="thumbnail">
        <a href="{{ interest.redirect }}" target="_blank">
        {% if interest.img %}
        <img class="thumbnail" src="{{ interest.img | prepend: site.baseurl | prepend: site.url }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <span>
            <h1>{{ interest.title }}</h1>
            <br/>
            <p>{{ interest.description }}</p>
        </span>
        </a>
    </div>
</div>
{% else %}

<div class="interest ">
    <div class="thumbnail">
        <a href="{{ interest.url | prepend: site.baseurl | prepend: site.url }}">
        {% if interest.img %}
        <img class="thumbnail" src="{{ interest.img | prepend: site.baseurl | prepend: site.url }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <span>
            <h1>{{ interest.title }}</h1>
            <br/>
            <p>{{ interest.description }}</p>
        </span>
        </a>
    </div>
</div>

{% endif %}

{% endfor %}
