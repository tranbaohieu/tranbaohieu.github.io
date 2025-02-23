---
layout: default
title: Welcome to My Blog
---

[🏠 Home](/) | [📝 Blog](/blog) | [👤 About](/about) | [📩 Contact](/contact)

<figure style="text-align: center;">
  <img src="/assets/images/logo.png" alt="Logo" class="logo">
</figure>

# 📢 Latest Blog Posts

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url }})**  
  _Published on {{ post.date | date: "%B %d, %Y" }}_
{% endfor %}

---

## 📬 Get in Touch
You can reach out to me via [Email](hieubkls98@gmail.com).

