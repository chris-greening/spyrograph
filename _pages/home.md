---
layout: splash
permalink: /
title: spyrograph
header:
  overlay_image: images/header_image.PNG
  cta_label: "<i class='fa fa-download'></i> pip install spyrograph"
  cta_url: "https://pypi.org/project/spyrograph/"
excerpt: Elegant mathematics and beautiful geometries

feature_row:
  - image_path: images/partial_circle.PNG
    image_size: 100px
    alt: ""
    title: "Expressive and consistent syntax"
    excerpt: ""
    url: ""
    btn_label: "Learn More"
  - image_path: images/partial_circle.PNG
    alt: ""
    title: "Clear visualizations and animations"
    excerpt: ""
    url: ""
    btn_label: "Learn More"
  - image_path: images/partial_circle.PNG
    alt: "100% free"
    title: "Completely free to use"
    excerpt: ""
    url: "/license/"
    btn_label: "Learn More"
github:
  - excerpt: '{::nomarkdown}<iframe style="display: inline-block;" src="https://ghbtns.com/github-btn.html?user=mmistakes&repo=minimal-mistakes&type=star&count=true&size=large" frameborder="0" scrolling="0" width="160px" height="30px"></iframe> <iframe style="display: inline-block;" src="https://ghbtns.com/github-btn.html?user=mmistakes&repo=minimal-mistakes&type=fork&count=true&size=large" frameborder="0" scrolling="0" width="158px" height="30px"></iframe>{:/nomarkdown}'
---

{% include feature_row %}

<h2> Recent Blog Posts </h2>

{% for post in site.posts limit:3 %}
  {% include archive-single.html %}
{% endfor %}

[See all blog posts...]({{site.url}}{{site.baseurl}}/blog/){: .btn .btn--info}