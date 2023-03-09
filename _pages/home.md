---
layout: splash
permalink: /
title: spyrograph
header: 
  cta_label: "<i class='fa fa-download'></i> pip3 install spyrograph"
  cta_url: "https://pypi.org/project/spyrograph/"
excerpt: Elegant mathematics and beautiful geometries

---

<h2> Recent Blog Posts </h2>

{% for post in site.posts limit:3 %}
  {% include archive-single.html %}
{% endfor %}

[See all blog posts...]({{site.url}}{{site.baseurl}}/blog/){: .btn .btn--info}