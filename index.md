---
layout: home
title: "Welcome to My Blog"
description: "A place where I share my thoughts on technology, personal growth, and more."
---

# Welcome to My Blog!

This blog covers various topics that I'm passionate about. Here are my latest posts:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%B %d, %Y" }}
    </li>
  {% endfor %}
</ul>
