---
layout: default
title: Welcome to My Blog
---
# Welcome to Hieu blog

## Tran Bao Hieu | [👤 About](/about)

<!-- <figure style="text-align: right;">
  <img src="/assets/images/logo.png" alt="Logo" width=300>
</figure> -->

<!-- ## 📢 Latest Blog Posts -->

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url }})**  
  _Published on {{ post.date | date: "%B %d, %Y" }}_
{% endfor %}

---
- [📩 Email](hieubkls98@gmail.com).

