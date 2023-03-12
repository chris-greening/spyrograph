---
permalink: /blog/
title: "Blog"
excerpt: "spyrograph is a lightweight Python package that provides an expressive and flexible set of tools for drawing beautiful mathematically driven art"
---

<h2> Blog posts </h2>

{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}