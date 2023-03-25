---
title: "Creating a range of hypotrochoids with the `create_range` method"
date: 2023-03-24 23:35:00 -0500
categories: Python, tutorial
header:
  overlay_image: /images/rgb.gif
---

# Creating a range of hypotrochoids with the `create_range` method

When working with the `spyrograph` package, we often want to create a **range of different shapes** by varying one of the input parameters while keeping the others constant

This is where the `create_range` class method comes in handy!

In this blog post let's walk through how to use the `create_range` method to generate a list of instantiated `Hypotrochoid` objects with varying input parameters

## Understanding the `create_range` method

The `create_range` method allows us to create a range of different hypotrochoids and epitrochoids by varying one of the input parameters (`R`, `r`, or `d`) while keeping the others constant

This method accepts the following parameters:

- `R`: The radius of the **fixed circle**, either a single number or a list of numbers.
- `r`: The radius of the **rolling circle**, either a single number or a list of numbers.
- `d`: The **distance** of the trace point from the rolling circle, either a single number or a list of numbers.
- `thetas`: An optional list of values for **theta** for inputting into parametric equations.
- `theta_start`: An optional starting theta value for creating a list of thetas.
- `theta_stop`: An optional stop theta value for creating a list of thetas, where the stop value is not included in the final array.
- `theta_step`: An optional incremental step value for stepping from start to stop.
- `origin`: An optional custom origin to center the shapes at, with the default being (0, 0).

The method returns a list of instantiated `Hypotrochoid` objects where one of the input parameters is a **list of increments** and the others are fixed

## Using the `create_range` Method

Let's say we want to create a range of hypotrochoids with **varying radii** of the **rolling** circle (`r`) while keeping the radii of the **fixed** circle (`R`) and the **distance** of the trace point from the rolling circle (`d`) constant

To do this we can use the `create_range` method as follows:

{% highlight python %}
from spyrograph import Hypotrochoid
import numpy as np
import turtle

arr = Hypotrochoid.create_range(
    R=600,
    r=np.arange(295,300,.2),
    d=51,
    theta_start=0,
    theta_stop=35*np.pi,
    theta_step=.1
)
{% endhighlight %}

Now, hypotrochoids contains a list of `Hypotrochoid` objects with varying `r` values

We can then use the `trace` method to visualize these shapes:

{% highlight python %}
screen = None
for shape in arr:
    screen = shape.trace(
      screen=screen,
      color="white",
      screen_color="black"
    )
turtle.exitonclick()
{% endhighlight %}

This will display the hypotrochoids one after the other on the same screen resulting in a more complex looking image

<p align="center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/create_range_image_spirograph.gif" alt="White lines on a black background tracing looping geometric pattern">
</p>

## Conclusion

In this post, we explored the powerful `create_range` method provided by the `spyrograph` package, which allows us to generate a wide variety of beautiful hypotrochoids and epitrochoids with just a **few lines of code**

By specifying a range of values for `R`, `r`, or `d` we can quickly create and visualize **multiple shapes**, making it an excellent tool for **artists, educators, and anyone interested** in exploring the fascinating world of spirograph patterns

With `spyrograph`, the possibilities for creating captivating designs are **virtually endless** - we hope this method inspires your creativity and leads to the discovery of stunning spirograph patterns unique to you!
