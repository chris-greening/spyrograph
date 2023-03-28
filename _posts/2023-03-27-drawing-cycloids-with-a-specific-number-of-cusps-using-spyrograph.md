---
title: "Drawing cycloids with a specific number of cusps using spyrograph"
date: 2023-03-28 12:38:00 -0500
categories: Python, tutorial
header:
  overlay_image: /images/rgb.gif
---

# Drawing cycloids with a specific number of cusps using spyrograph

## Introduction

In this blog post, we will explore a powerful feature of the `spyrograph` package: the ability to create and draw cycloids with a **specified number of cusps**

Cycloids are **special cases** of trochoids where the **distance** parameter `d` is **equal** to the rolling circle **radius** `r`

By using the `n_cusps` class method provided in the `Hypocycloid` and `Epicycloid` classes, we can easily create beautiful **cycloid** shapes with a desired number of cusps

## Prerequisite imports

Before we begin, let's make sure we have the `spyrograph` package **installed**:

{% highlight bash %}
pip3 install spyrograph
{% endhighlight %}

## Creating a cycloid with a specified number of cusps

To create a cycloid with a specified number of cusps, we can use the `n_cusps` class method. Here's a quick example of how to create a **hypocycloid** with **5 cusps**:

{% highlight python %}
from spyrograph import Hypocycloid
import numpy as np

R = 50
n = 5
thetas = np.arange(0, 2 * np.pi, 0.01)

hypocycloid = Hypocycloid.n_cusps(R=R, n=n, thetas=thetas)
{% endhighlight %}

In this example, we set the radius of the fixed circle `R` to `50` and the desired number of cusps `n` to `5`. The `n_cusps` method calculates the rolling circle radius `r` as `R/n` and instantiates a cycloid object with the provided parameters

## Tracing the cycloid with `trace`

Now that we have created a hypocycloid with 5 cusps, let's **trace** it using the `trace` method provided by the `spyrograph` package

{% highlight python %}
hypocycloid.trace(exit_on_click=True)
{% endhighlight %}

<p align="center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/5cusp_shape.gif" alt="Tracing of a hypocycloid with 5 cusps being drawn">
</p>

The `trace` method will display an animation of the cycloid shape being drawn

The `exit_on_click` argument ensures that the **animation window remains open** until you click on it

## Conclusion
The `n_cusps` class method in the `Hypocycloid` class is a powerful and **easy-to-use** feature for creating and drawing cycloid shapes with a specified number of cusps

By using this method, artists and educators alike can create **visually stunning** and mathematically precise cycloids in a matter of seconds

Give it a try and unlock your creativity with the `spyrograph` package today!