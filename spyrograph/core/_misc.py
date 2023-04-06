"""Miscellaneous helper functions"""

import itertools
import collections
from typing import Tuple, List, Union
from numbers import Number
import turtle
import time

import numpy as np

try:
    from PIL import ImageGrab
except ImportError:
    ImageGrab = None

def _validate_theta(
        thetas: List[Number], theta_start: Number, theta_stop: Number,
        theta_step: Number
    ) -> "np.array":
    theta_values = (theta_start, theta_stop, theta_step)
    multiple_thetas = thetas is not None and any(theta_values)
    if multiple_thetas:
        raise ValueError((
            "Multiple definitions of theta were passed in as argument "
            "which is ambiguous - please define only one set of theta values."
        ))
    if thetas is None:
        if theta_step is None:
            theta_step = .1
        thetas = np.arange(theta_start, theta_stop, theta_step)
    thetas = np.array(thetas)
    if len(thetas) == 0:
        raise ValueError("An empty list of thetas was passed in as argument.")
    return thetas

def _get_products_of_inputs(*args) -> Tuple[Number]:
    """Return a list of tuples that contains all of the input arguments"""
    list_of_lists = [_set_int_to_list(el) for el in args]
    product = list(itertools.product(*list_of_lists))
    return product

def _validate_only_one_iterable(*args) -> bool:
    """Return validation check that only one argument passed to create_range is an iterable"""
    inputs = collections.Counter([isinstance(el, collections.abc.Iterable) for el in args])
    if inputs[True] > 1:
        raise ValueError((
            "More than one input variable was varied."
            "Please only pass one list of varying inputs and try again."
        ))

def _set_int_to_list(input_val: Union[Number, List[Number]]) -> List[Number]:
    """Return list of numbers from given input parameter"""
    if isinstance(input_val, Number):
        input_val = [input_val]
    return input_val

def _save_trace(screen: "turtle.Turtle", fpath: str):
    """Save trace to PNG using PIL"""
    # pylint: disable=invalid-name
    if ImageGrab is None:
        raise ImportError((
            "PIL is required but is not installed on your machine, "
            "please install and try again"
        ))
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.update()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    time.sleep(1)
    image = ImageGrab.grab((
        x0+8,
        y0+8,
        x0 + root.winfo_width()-8,
        y0 + root.winfo_height()-8
    ))
    image.save(fpath)

def _draw_animation(
        shapes_arr, screen_size: Tuple[Number, Number] = (1000, 1000),
        screen_color: str = "white", exit_on_click: bool = False,
        color: str = "black", width: Number = 1,
        frame_pause: Number = 0.1, screen: "turtle.Screen" = None,
        screen_coords = (0, 0), padding: Number = 100
    ) -> None:
    for shape in shapes_arr:
        if screen is not None:
            turtles.shape_turtle.clear()
        screen, turtles = shape.trace(
            screen = screen, screen_size = screen_size,
            screen_color = screen_color,
            color = color, width=width, screen_coords=screen_coords,
            padding=padding
        )
        time.sleep(frame_pause)
    if exit_on_click:
        turtle.Screen().exitonclick()
