---
title: "Unlock the power of method chaining for elegant and efficient Spyrograph transformations"
date: 2023-04-18 00:18:00 -0500
categories: Python
header:
  overlay_image: /images/translate_and_rotate.gif
---

# Unlock the power of method chaining for elegant and efficient Spyrograph transformations

## Introduction to Method Chaining in Spyrograph

Creating captivating geometric art using Spyrograph is an engaging way to explore the world of mathematics and programming. One of the key aspects that make working with Spyrograph a smooth experience is its support for method chaining. This powerful technique allows us to perform multiple operations on a single shape in a concise and elegant manner, making our code more readable and efficient

Method chaining is a programming technique that enables us to call multiple methods on an object in a single line of code. Each method returns a new instance of the object with the applied transformation, allowing us to call subsequent methods on the returned object. This approach not only improves code readability but also eliminates the need for excessive intermediary variables, making our code cleaner and more concise

<p align="center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/translate_and_rotate_example.gif" alt="A translating, rotating, and scaling shape fading into darkness">
</p>

In the context of Spyrograph, method chaining allows us to create and manipulate geometric shapes seamlessly. We can easily chain together various transformation methods such as translation, scaling, and rotation to achieve the desired shape and appearance. By mastering method chaining, we can unlock the full potential of the Spyrograph library and create intricate geometric art with minimal effort

In the upcoming sections, we will dive deeper into the world of method chaining in Spyrograph, demonstrating its power and flexibility through examples and explanations of the core transformation methods. Stay tuned to explore the fascinating world of geometric art and method chaining in Spyrograph!

## Creating a simple shape

Before diving into the world of method chaining and applying various transformations to our shapes, we first need to create a base shape to work with. This shape will serve as the foundation for all the transformations we will apply later

In this section, we will discuss how to create a basic spirograph shape using Spyrograph. To do this, we will be using the Hypocycloid class

{% highlight python %}
from spyrograph import Hypocycloid
import numpy as np

base_obj = Hypocycloid(
    R=147,
    n=5
    thetas=np.arange(0, 2*np.pi, .1)
)
base_obj.trace(exit_on_click=True)
{% endhighlight %}

<p align="center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/base_shape_drawing_5_cusps.gif" alt="A tracing with 5 cusps is traced by a rolling circle on a fixed circle">
</p>

With the base shape created, we are now ready to explore the various transformations and method chaining techniques that the Spyrograph library has to offer. In the upcoming sections, we will discuss different transformations, such as translation, scaling, and rotation, and how to chain these methods together for a smooth, streamlined coding experience

## Chaining multiple transformations together

With method chaining, we can apply several transformations to our base shape in a concise and readable manner. When we call a transformation method, it returns a new instance of the shape with the applied transformation. We can then immediately call another transformation method on this new instance, and so on.

Let's start with our base shape from the last section and apply multiple transformations to our shape using method chaining:

{% highlight python %}
# Translate, scale, and rotate the shape in a single line of code
transformed_obj = (
    base_obj
    .translate(x=200, y=200)
    .scale(2)
    .rotate(np.pi/4)
)
{% endhighlight %}

In this example, we first translate the base shape by 200 units in the x-direction and 200 units in the y-direction. Next, we scale the translated shape by a factor of 2. Finally, we rotate the scaled shape by 45 degrees (pi/4 radians) around its origin.

<p align="center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/showing_chained_methods1.gif" alt="A tracing with 5 cusps shifted, scaled, and then rotated">
</p>

With method chaining, we can quickly and easily apply a series of transformations to our Spyrograph shapes, creating intricate designs in just a few lines of code

## Chaining transformations together for a complex visualization

{% highlight python %}
from spyrograph import Hypocycloid
import numpy as np
import time
import turtle

# Trace an initial shape and set the screen conditions
shape = Hypocycloid.n_cusps(
    R=147,
    n=5,
    thetas=np.arange(0, 2*np.pi+.1, .1),
)
screen = shape.trace(screen_color="black", color="red", screen_size=(1000, 1000))

# Iterate and chain transformations
i = 1
while i < 110:
    shape = shape.translate(x=4).rotate(angle=2, degrees=True).scale(factor=1/1.01)
    screen = shape.trace(color="red", screen=screen, width=2)
    i += 1
    time.sleep(.01)
turtle.exitonclick()
{% endhighlight %}
