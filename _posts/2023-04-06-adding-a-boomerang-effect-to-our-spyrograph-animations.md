---
title: "Adding a boomerang effect to our Spyrograph animations"
date: 2023-04-06 01:18:00 -0500
categories: Python
header:
  overlay_image: /images/spirograph_boomerang_header.gif
---

## Introduction
Spirographs are captivating geometric designs created by rolling a circle inside or outside another circle. These mesmerizing patterns have fascinated artists, mathematicians, and enthusiasts alike for centuries. With the power of Python and the spyrograph library, we can create complex spirograph animations that visualize the evolution of these intricate patterns.

In this blog post, we will explore the `boomerang` effect, a newly introduced feature in the `spyrograph` library, which allows us to create mesmerizing animations that play forward and then in reverse. We'll provide examples and explanations on how to harness this feature to create captivating spirograph animations

## The boomerang effect
The boomerang effect is achieved by playing the animation sequence in reverse after it reaches the end, creating a back-and-forth effect. This feature is particularly useful when you want to visualize the evolution of a spirograph pattern with changing parameters and then observe how it returns to its initial state

To enable the `boomerang` effect, we need to set `boomerang=True` when calling the `animate` method of the `spyrograph` library. In the following sections, we will demonstrate how to use this feature with various examples.

## Example 1: Basic boomerang animation
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

This example generates a `Hypotrochoid` animation with varying `r` values while keeping `R` and `d` the same. After reaching the end of the sequence, the animation plays in reverse, creating a boomerang effect.

## Example 2: Combining boomerang with looping
The boomerang effect can also be combined with looping, allowing the animation to play continuously. To achieve this, set both the `boomerang` and `repeat` arguments to `True` in the `animate` method

{% highlight python %}
from spyrograph import Hypotrochoid
import numpy as np

# Repeating animation of a hypotrochoid by incrementally changing the rolling radius r
Hypotrochoid.animate(
    R=200,
    r=np.arange(113.75, 114.25, .01),
    d=133,
    thetas=np.arange(0,100, .05),
    boomerang=True,
    repeat=True
)
{% endhighlight %}

With these settings, the animation will loop indefinitely, playing forwards and then in reverse, creating an entrancing visual experience

## Example 3: boomerang effect with custom configurations
The boomerang effect can be combined with other custom configurations, such as changing the background color, line color, or line width. In this example, we will create an animation with a black background, a neon green tracing line, and a thicker line width

{% highlight python %}
from spyrograph import Hypotrochoid
import numpy as np

# Neon green hypotrochoid boomerang animation on black background
Hypotrochoid.animate(
    R=200,
    r=np.arange(113.75, 114.25, .01),
    d=133,
    thetas=np.arange(0,100, .05),
    frame_pause=.01,
    repeat=True,
    boomerang=True,
    screen_color="black",
    color="#39FF14",
    width=3
)
{% endhighlight %}

<p align="center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/spirograph_boomerang_example_3.gif" alt="An animation of a neon green tracing of a star that is rotating back and forth on a black background">
</p>

This animation will feature a striking contrast between the neon green spirograph patterns and the black background. The boomerang effect adds another layer of visual interest to this already captivating animation