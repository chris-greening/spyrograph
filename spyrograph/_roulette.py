"""Abstract base class for generalizing the epitrochoid and hypotrochoid
shape's methods i.e. tracing, calculating, etc. The child classes define 
the parametric equations
"""

import math
import turtle
from typing import Tuple, List
from numbers import Number
import time
from abc import ABC, abstractmethod

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

try:
    import pandas as pd
except ImportError:
    pd = None

class _Roulette(ABC):
    def __init__(self, R: Number, r: Number, d: Number, thetas: List[Number]) -> None:
        self.R = R
        self.r = r
        self.d = d
        self.thetas = thetas 
    
        self.x = [self._calculate_x(theta) for theta in self.thetas]
        self.y = [self._calculate_y(theta) for theta in self.thetas]
        self.coords = list(zip(self.x, self.y, self.thetas))

    def plot(self, **kwargs) -> Tuple["matplotlib.matplotlib.Figure", "matplotlib.axes._axes.Axes"]:
        """Return matplotlib figure and axis objects after plotting the figure
        
        See available matplotlib.pyplot.plot configurations 
        (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
        """
        if plt is None:
            raise ImportError("matplotlib is required but is not installed on your machine, please install and try again")
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y, **kwargs)
        plt.show()
        return fig, ax

    def trace(self, screen_size: Tuple[Number, Number] = (1000, 1000), screen_color: str = "white", exit_on_click: bool = False, color: str = "black", hide_turtle: bool = True, show_circles: bool = False, frame_pause: Number = 0, screen: "turtle.Screen" = None, circle_color: str = "black") -> "turtle.Screen":
        """Trace the roulette shape using turtle

        Parameters
        ----------
        screen_size: Tuple[Number, Number]
            Length and width of the output screen
        screen_color: str
            Color of the background screen
        exit_on_click: bool = False
            Pause the final animation until the user clicks to exit the window
        color: str = "black"
            Color of the primary tracing
        hide_turtle: bool = True
            Hide the turtle icon while tracing
        show_circles: bool = False
            Show the inner and outer circles that compose the trace
        frame_pause: Number = 0
            Time in seconds to pause each individual frame for
        circle_color: str = "white"
            Color of the circles

        Returns
        -------
        screen: turtle.Screen
            Screen that the turtle is drawn on
        """
        if screen is None:
            screen = turtle.Screen()
            screen.setup(*screen_size)
            screen.bgcolor(screen_color)
        turtle.tracer(False)

        shape_turtle = turtle.Turtle()
        rolling_circle_turtle = turtle.Turtle()
        fixed_circle_turtle = turtle.Turtle()
        rolling_circle_turtle.hideturtle()
        fixed_circle_turtle.hideturtle()
        shape_turtle.color(color)
        rolling_circle_turtle.color(circle_color)
        fixed_circle_turtle.color(circle_color)
        if hide_turtle:
            shape_turtle.hideturtle()
        if show_circles:
            self._trace_fixed_circle(fixed_circle_turtle)
        
        first = True 
        shape_turtle.up()
        for x, y, theta in self.coords:
            shape_turtle.goto(x, y)
            if show_circles:
                self._trace_rolling_circle(rolling_circle_turtle, shape_turtle, x, y, theta)
            if first:
                first = False
                shape_turtle.down()
            turtle.update()
            time.sleep(frame_pause)
        if exit_on_click:
            turtle.exitonclick()
        return screen

    @property
    def df(self) -> "pd.DataFrame":
        """Return DataFrame of all relevant information pertaining to the parametrized shape"""
        if pd is None:
            raise ImportError("pandas is required but is not installed on your machine, please install and try again")
        df = pd.DataFrame({
            "x": self.x,
            "y": self.y,
            "theta": self.theta
        })
        return df

    def _trace_fixed_circle(self, fixed_circle_turtle: "turtle.Turtle") -> None:
        """Trace the outer circle of the animation"""
        fixed_circle_turtle.up()
        fixed_circle_turtle.seth(0)
        fixed_circle_turtle.goto(0,-self.R)
        fixed_circle_turtle.down()
        fixed_circle_turtle.circle(self.R,steps=200)

    def _trace_rolling_circle(
            self, rolling_circle_turtle: "turtle.Turtle", shape_turtle: "turtle.Turtle",
            x: Number, y: Number, theta: Number
        ) -> None:
        """Trace the inner circle of the animation"""
        self._rolling_circle_init(rolling_circle_turtle)
        self._draw_trace_dot(rolling_circle_turtle, x, y)
        rolling_circle_x, rolling_circle_y = self._draw_rolling_circle(rolling_circle_turtle, theta)
        self._draw_rolling_circle_focus(rolling_circle_turtle, rolling_circle_x, rolling_circle_y)
        self._connect_focus_to_trace_dots(rolling_circle_turtle, shape_turtle)

    def _connect_focus_to_trace_dots(self, rolling_circle_turtle: "turtle.Turtle", shape_turtle: "turtle.Turtle") -> None:
        """Draw line from focus to the trace that's drawing the shape"""
        rolling_circle_turtle.down()
        rolling_circle_turtle.seth(rolling_circle_turtle.towards(shape_turtle))
        rolling_circle_turtle.fd(self.d)

    def _draw_rolling_circle_focus(self, rolling_circle_turtle: "turtle.Turtle", rolling_circle_x: Number, rolling_circle_y: Number) -> None:
        """Draw the center of the rolling circle"""
        rolling_circle_turtle.up()
        rolling_circle_turtle.goto(rolling_circle_x, rolling_circle_y + self.r)
        rolling_circle_turtle.dot(10, "blue")

    def _draw_rolling_circle(self, rolling_circle_turtle: "turtle.Turtle", theta: Number) -> None:
        """Draw the rolling circle on the screen"""
        rolling_circle_turtle.seth(0)
        rolling_circle_y=self._circle_offset()*math.sin(theta) - self.r
        rolling_circle_x=self._circle_offset()*math.cos(theta)
        rolling_circle_turtle.goto(rolling_circle_x, rolling_circle_y)
        rolling_circle_turtle.down()
        rolling_circle_turtle.circle(self.r,steps=200)
        return rolling_circle_x, rolling_circle_y

    def _draw_dot(self, turtle: "turtle.Turtle", x: Number, y: Number, color: str) -> None:
        """Draw rolling circle outer trace"""
        turtle.goto(x, y)
        turtle.dot(10, color)

    def _rolling_circle_init(self, rolling_circle_turtle: "turtle.Turtle") -> None:
        """Set iteration's initial conditions for rolling circle"""
        rolling_circle_turtle.clear()
        rolling_circle_turtle.seth(0)
        rolling_circle_turtle.up()

    @abstractmethod
    def _circle_offset(self) -> float:
        """Return rolling circle offset from fixed circle"""

    @abstractmethod
    def _calculate_x(self, theta: Number) -> float:
        """Return calculated x-value from parametrized equation"""

    @abstractmethod
    def _calculate_y(self, theta: Number) -> float:
        """Return calculated y-value from parametrized equation"""
