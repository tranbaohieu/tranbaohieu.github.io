---
layout: default
title: Welcome to My Blog
---
<figure style="text-align: center;">
  <img src="/assets/images/logo.png" alt="Logo" class="logo">
  <figcaption>Me after 3 months became a chill guy</figcaption>
</figure>

# 🌟 Welcome to My Blog!

Hi! This is my personal space where I share my thoughts and experiences. Feel free to explore!

## 📢 Latest Blog Posts

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url }})**  
  _Published on {{ post.date | date: "%B %d, %Y" }}_
{% endfor %}

---

## ✨ About Me
I am passionate about technology, coding, and sharing knowledge. Stay tuned for my latest blog posts!

## 📬 Get in Touch
You can reach out to me via email or social media.

## 🔗 Navigation
[🏠 Home](/) | [📝 Blog](/blog) | [👤 About](/about) | [📩 Contact](/contact)

