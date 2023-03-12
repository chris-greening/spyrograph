---
title: "Draw beautiful geometric visualizations with Python and spyrograph"
date: 2023-03-11 11:02:31 -0500
categories: Python
header:
  overlay_image: /images/header_image.PNG
---

In the world of mathematics there is a limitless supply of patterns, visualizations, and concepts just waiting to be explored

Some of those concepts are known as hypotrochoids and epitrochoids - beautiful patterns traced by a point extending from a circle rolling around another fixed circle

<p align="center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logo.PNG" alt="Pattern drawn from a hypotrochoid" width="450px">
</p>

Let's dive in and explore how `spyrograph` helps us analyze and explore these simple mathematical concepts in just a few lines of code!

## What are hypotrochoids and epitrochoids?

Simply put, hypotrochoids and epitrochoids are curves formed by tracing a point extending from the center of a circle as it rolls around the inside (for the hypotrochoid) or the outside (for the epitrochoid) of a fixed circle

<p align="center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/simple_epitrochoid.gif" alt="Circle rolling around the exterior of a fixed circle and drawing a looping pattern" width="450px">
</p>

The resulting curves can be incredibly intricate, elegant, and pleasing to the eye and have a surprisingly wide range of applications ranging from engineering and astronomy to even patterns printed on banknotes and passports as security measures against counterfeiting

## Exploring the math behind these patterns

Hypotrochoids and epitrochoids can be broken down to a few key inputs and a set of parametric equations

The inputs are:

- $R$: the radius of the fixed circle
- $r$: the radius of the rolling circle
- $d$: the distance from the interior of the rolling circle
- $\theta$: the angle formed by the horizontal and the center of the rolling circle

with the parametric equations defined as:

### Hypotrochoid

$ x(\theta) = (R - r)cos\theta + d cos(\frac{R - r}{r}\theta) $
$ y(\theta) = (R - r)sin\theta - d sin(\frac{R - r}{r}\theta) $

### Epitrochoid

$ x(\theta) = (R + r)cos\theta - d cos(\frac{R + r}{r}\theta) $
$ y(\theta) = (R + r)sin\theta - d sin(\frac{R + r}{r}\theta) $

Given this information, we can draw our curves using the output $(x,y)$ coordinates calculated by the parametric equations



## Using `spyrograph` for effortless modeling

## Animating and visualizing beautiful geometries

## Conclusion

## Additional references

{% highlight python %}
print()
{% endhighlight %}
