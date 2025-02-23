---
layout: default
title: Welcome to My Blog
---

Tran Bao Hieu | [👤 About](/about) | [📩 Contact](/contact)

<figure style="text-align: right;">
  <img src="/assets/images/logo.png" alt="Logo" class="logo">
</figure>

## 📢 Latest Blog Posts

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url }})**  
  _Published on {{ post.date | date: "%B %d, %Y" }}_
{% endfor %}

---

## 📬 Get in Touch
You can reach out to me via [Email](hieubkls98@gmail.com).

