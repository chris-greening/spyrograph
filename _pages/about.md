---
permalink: /about/
title: "About"
excerpt: "spyrograph is a lightweight Python package that provides an expressive and flexible set of tools for drawing beautiful mathematically driven art"
---

## What is it?

{% highlight python %}
import spyrograph
{% endhighlight %}

`spyrograph` is a lightweight Python package that provides an expressive and flexible set of tools for drawing beautiful mathematically driven art

[pip3 install spyrograph](https://pypi.org/project/spyrograph/){: .btn .btn--success}
[Official GitHub repo](https://github.com/chris-greening/spyrograph){: .btn .btn--success}

<p align="center">
  <img src="https://github.com/chris-greening/spyrograph/blob/gh-pages/images/circle_spinning.gif?raw=true" alt="Sample hypotrochoid drawing showing a circle rolling around the interior of another circle drawing a geometric shape" width="410px">
</p>

## Key Features
- Expressive and consistent syntax
- Robust underlying mathematics
- Clear visualizations and animations
- Flexible to a wide range of usecases
- Lightweight, just plug and play

## Quickstart

`spyrograph` is designed to be expressive and easy-to-use - simply `import spyrograph` and jump right into drawing elegant, complex shapes in just a few lines of code!

{% highlight python %}
from spyrograph import Hypotrochoid

# Trace a hypotrochoid from 0 to 2pi where
# the fixed circle radius is 300, rolling circle
# radius is 200, and the distance from the rolling
# circle is 100
hypotrochoid = Hypotrochoid(
    R=300,
    r=200,
    d=100,
    thetas=np.arange(0, 2*np.pi, .1)
)
hypotrochoid.trace(
    show_circles=True,
    frame_pause=.05,
    circle_color="grey"
)
{% endhighlight %}

## The philosophy

{% highlight python %}
import this
{% endhighlight %}

`spyrograph` was designed with [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) at its heart. Every design choice is carefully considered to make drawing and analyzing beautiful geometries as smooth as possible. The syntax is expressive and concise, allowing for beautiful and explicit code that is clean and immediately obvious. There should never be a moment where you're questioning why the API does what it does; it is fluid and intuitive, designed for you the developer.

## About the author

{% highlight python %}
from chris_greening import bio
{% endhighlight %}

Chris Greening is a software engineer from the New York metropolitan area with a wide range of engineering experience - he is especially fond of Python and R

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/chrisgreening)