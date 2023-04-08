---
title: "Tracing multiple shapes on the same screen with Spyrograph"
date: 2023-04-08 01:18:00 -0500
categories: Python
header:
  overlay_image: /images/spirograph_boomerang_header.gif
---

## Introduction
Unleash your inner artist by creating beautiful geometric designs with Spyrograph. In this tutorial, we'll demonstrate how to chain screens for multiple traces, allowing us to create captivating artwork by layering different spirograph shapes on the same canvas

Follow along as we use a custom code snippet to showcase this technique in action.

## Creating our first spirograph
To begin, let's create our first spirograph shape using the `Hypotrochoid` class. Import the necessary libraries and define the required parameters for the shape

{% highlight python %}
from spyrograph import Hypotrochoid
import numpy as np

first_shape = Hypotrochoid(
    R=233,
    r=200,
    d=233,
    thetas=np.arange(0, 100*np.pi, .5)
)
{% endhighlight %}

## Tracing the first shape
Next, trace the first shape and keep the screen open by calling the `trace` method. By default, the `exit_on_click` option is set to False, which ensures that the `screen` remains active after tracing the first shape

{% highlight python %}
screen, turtles = first_shape.trace()
{% endhighlight %}

## Creating a second shape
Now, let's create a second shape by using the `scale` method to adjust the size of the first shape into a  slightly smaller copy

{% highlight python %}
second_shape = first_shape.scale(.85)
{% endhighlight %}

## Trace the second shape on the same screen
Trace the second shape on the same screen by passing the existing `screen` to the `trace` function. Additionally, set the `exit_on_click` option to `True` and choose a different `color` for the second shape

{% highlight python %}
second_shape.trace(
    exit_on_click=True,
    color="red",
    screen=screen
)
{% endhighlight %}

## Experiment with different shapes and colors
Feel free to experiment with different shapes, sizes, and colors to create your unique spirograph artwork. You can create and layer multiple shapes on the same screen by following the steps outlined above

## Conclusion
Chaining screens for multiple traces is a powerful technique to create visually stunning spirograph designs

By layering different shapes and colors on the same canvas, you can produce eye-catching and intricate artwork

Don't be afraid to explore various patterns and unleash your creativity with Spyrograph!