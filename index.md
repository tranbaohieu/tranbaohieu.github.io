---
layout: default
title: Welcome to My Blog
---
<p align="center">
  <img src="/assets/images/logo.png" alt="Logo" width="150">
</p>

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

