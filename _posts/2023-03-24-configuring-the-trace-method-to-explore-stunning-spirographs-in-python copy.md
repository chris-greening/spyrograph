---
title: "Creating a range of hypotrochoids with the `create_range` method"
date: 2023-03-24 23:35:00 -0500
categories: Python, tutorial
header:
  overlay_image: /images/header_image.PNG
---

# Creating a range of hypotrochoids with the `create_range` method

When working with the `spyrograph` package, we often want to create a range of different shapes by varying one of the input parameters while keeping the others constant

This is where the `create_range` class method comes in handy!

In this blog post let's walk through how to use the `create_range` method to generate a list of instantiated `Hypotrochoid` objects with varying input parameters

## Understanding the `create_range` method

The `create_range` method allows us to create a range of different hypotrochoids and epitrochoids by varying one of the input parameters (R, r, or d) while keeping the others constant

This method accepts the following parameters:

- `R`: The radius of the fixed circle, either a single number or a list of numbers.
- `r`: The radius of the rolling circle, either a single number or a list of numbers.
- `d`: The distance of the trace point from the rolling circle, either a single number or a list of numbers.
- `thetas`: An optional list of values for theta for inputting into parametric equations.
- `theta_start`: An optional starting theta value for creating a list of thetas.
- `theta_stop`: An optional stop theta value for creating a list of thetas, where the stop value is not included in the final array.
- `theta_step`: An optional incremental step value for stepping from start to stop.
- `origin`: An optional custom origin to center the shapes at, with the default being (0, 0).

The method returns a list of instantiated `Hypotrochoid` objects where one of the input parameters is a list of increments and the others are fixed

## Using the `create_range` Method

Let's say we want to create a range of hypotrochoids with varying radii of the fixed circle (R) while keeping the radii of the rolling circle (r) and the distance of the trace point from the rolling circle (d) constant

To do this we can use the `create_range` method as follows:

{% highlight python %}
from spyrograph import Hypotrochoid

R_values = [50, 60, 70, 80]
r = 10
d = 5
theta_values = np.arange(0, 2 * np.pi, 0.01)

hypotrochoids = Hypotrochoid.create_range(R=R_values, r=r, d=d, thetas=theta_values)
{% endhighlight %}

Now, hypotrochoids contains a list of four Hypotrochoid objects with varying R values.
We can then use the trace method to visualize these shapes:

```python
for hypotrochoid in hypotrochoids:
    hypotrochoid.trace(exit_on_click=True)
```

This will display the hypotrochoids one after the other on the same screen resulting in a more complex looking image

## Conclusion

In this post, we explored the powerful `create_range` method provided by the `spyrograph` package, which allows us to generate a wide variety of beautiful hypotrochoids and epitrochoids with just a few lines of code

By specifying a range of values for R, r, or d, we can quickly create and visualize multiple shapes, making it an excellent tool for artists, educators, and anyone interested in exploring the fascinating world of spirograph patterns

With `spyrograph`, the possibilities for creating captivating designs are virtually endless - we hope this method inspires your creativity and leads to the discovery of stunning spirograph patterns unique to you!
