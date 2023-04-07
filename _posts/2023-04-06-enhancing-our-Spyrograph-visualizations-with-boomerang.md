---
title: "Enhancing our Spyrograph animations with boomerang"
date: 2023-04-06 01:18:00 -0500
categories: Python
header:
  overlay_image: /images/spirograph_boomerang_example_3.gif
---

## Introduction
Spirographs are captivating geometric designs created by rolling a circle inside or outside another circle. These mesmerizing patterns have fascinated artists, mathematicians, and enthusiasts alike for centuries. With the power of Python and the spyrograph library, we can create complex spirograph animations that visualize the evolution of these intricate patterns.

In this blog post, we will explore the `boomerang` effect, a newly introduced feature in the `spyrograph` library, which allows us to create mesmerizing animations that play forward and then in reverse. We'll provide examples and explanations on how to harness this feature to create captivating spirograph animations

## The boomerang effect
The boomerang effect is achieved by playing the animation sequence in reverse after it reaches the end, creating a back-and-forth effect. This feature is particularly useful when you want to visualize the evolution of a spirograph pattern with changing parameters and then observe how it returns to its initial state

To enable the `boomerang` effect, we need to set the `boomerang` argument to True when calling the `animate` method of the `spyrograph` library. In the following sections, we will demonstrate how to use this feature with various examples.

## Example 1: basic boomerang animation
In this example, we will create a simple spirograph animation with the boomerang effect. We will use the `Hypotrochoid` class from the `spyrograph` library to generate our animation

{% highlight python %}
from spyrograph import Hypotrochoid
import numpy as np

# Animate a hypotrochoid by incrementally changing the rolling radius r
Hypotrochoid.animate(
    R=200,
    r=np.arange(113.75, 114.25, .01),
    d=133,
    thetas=np.arange(0,100, .05),
    frame_pause=.01,
    boomerang=True,
)
{% endhighlight %}

<p align="center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/spirograph_boomerang_example_1.gif" alt="An animation of a tracing of a star that is rotating back and forth">
</p>
