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

def _apply_rotation(x: "np.array", y: "np.array", angle: Number):
    """Return rotated parametrized values"""
    cos_angle, sin_angle = np.cos(angle), np.sin(angle)
    rotation_matrix = np.array([[cos_angle, -sin_angle], [sin_angle, cos_angle]])
    rotated_coords = np.dot(rotation_matrix, np.array([x, y]))
    return rotated_coords[0], rotated_coords[1]

def _validate_theta(
        thetas: List[Number], theta_start: Number, theta_stop: Number,
        theta_step: Number
    ) -> np.ndarray:
    """Return a numpy array of theta values after validating & standartising
        the input list of theta values"""
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

def _validate_only_one_iterable(*args) -> None:
    """Validation check that only one argument passed to create_range is an iterable"""
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

def _get_animate_screen_size(shapes_arr, padding) -> Tuple[Number, Number]:
    """Return screen size calculated from the largest x and y values"""
    min_x = min(shapes_arr, key=lambda x: x.min_x).min_x
    max_x = max(shapes_arr, key=lambda x: x.max_x).max_x
    min_y = min(shapes_arr, key=lambda x: x.min_y).min_y
    max_y = max(shapes_arr, key=lambda x: x.max_y).max_y
    screen_size = (
        max_x - min_x + padding,
        max_y - min_y + padding
    )
    return screen_size

def _trace_loop(
        shapes_arr, screen: "turtle.Screen", turtles: "namedtuple",
        screen_size: Tuple[Number, Number], screen_color: str, color: str,
        width: Number, screen_coords: Tuple[Number, Number], padding: Number,
        frame_pause: Number
    ) -> Tuple["turtle.Screen", "namedtuple"]:
    """Returns a turtle screen and namedtuple containing turtles..."""
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
    if screen is not None:
        turtles.shape_turtle.clear()
    return screen, turtles

def _draw_animation(
        shapes_arr, screen_size: Tuple[Number, Number] = (1000, 1000),
        screen_color: str = "white", exit_on_click: bool = False,
        color: str = "black", width: Number = 1,
        frame_pause: Number = 0.1, screen: "turtle.Screen" = None,
        screen_coords = (0, 0), padding: Number = 100, repeat: bool = False,
        reverse: bool = False, boomerang: bool = False
    ) -> None:
    """Draw the animation from a given set of shapes"""
    if reverse:
        shapes_arr = shapes_arr[::-1]
    if boomerang:
        reverse_arr = shapes_arr[::-1]
    turtles = None
    while True:
        screen, turtles = _trace_loop(
            shapes_arr=shapes_arr, screen=screen, turtles=turtles,
            screen_size=screen_size, screen_color=screen_color, color=color, width=width,
            screen_coords=screen_coords, padding=padding, frame_pause=frame_pause
        )
        if boomerang:
            screen, turtles = _trace_loop(
                shapes_arr=reverse_arr, screen=screen, turtles=turtles,
                screen_size=screen_size, screen_color=screen_color, color=color,
                width=width, screen_coords=screen_coords, padding=padding,
                frame_pause=frame_pause
            )
        if not repeat:
            break
    if exit_on_click:
        turtle.Screen().exitonclick()
