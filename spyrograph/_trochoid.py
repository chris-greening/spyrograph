"""Abstract base class for generalizing the epitrochoid and hypotrochoid
shape's methods i.e. tracing, calculating, etc. The child classes define
the parametric equations
"""

import math
import turtle
from typing import Tuple, List, Union
from numbers import Number
import time
from abc import ABC, abstractmethod
import collections

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

try:
    import pandas as pd
except ImportError:
    pd = None

class _Trochoid(ABC):
    # pylint: disable=too-many-instance-attributes
    def __init__(
            self, R: Number, r: Number, d: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0)
        ) -> None:
        """Model of a trochoid curve from given input parameters. A trochoid is
        a curve drawn by tracing a point from a circle as it rolls around the
        inside or outside of a fixed circle

        Parameters
        ----------
        R : Number
            Radius of the fixed circle
        r : number
            Radius of the rolling circle
        d : Number
            Distance of the trace point from the rolling circle
        thetas : List[Number] = None
            Input list of values for theta for inputting into parametric equations.
            This argument cannot be set at the same time as theta_start,
            theta_stop, theta_step
        theta_start : Number = None
            Starting theta value for creating a list of thetas (similar syntax
            to built-in range or np.arange). This argument cannot be set at the
            same time as thetas argument
        theta_stop : Number = None
            Stop theta value for creating a list of thetas, stop value is not
            included in the final array (similar syntax to built-in range or
            np.arange). This argument cannot be set at the same time as thetas
            argument
        theta_step : Number = None
            Incremental step value for stepping from start to stop
            (similar syntax to built-in range or np.arange). This argument
            cannot be set at the same time as thetas argument
        origin : Tuple[Number, Number] = (0, 0)
            Custom origin to center the shapes at. Default is (0,0)
        """
        self.R = R
        self.r = r
        self.d = d
        self.thetas = self._validate_theta(thetas, theta_start, theta_stop, theta_step)
        self.origin = origin

        if self.R <= 0 or self.r <= 0 or self.d <= 0:
            raise ValueError("Negative and/or zero input parameters were passed. Please only pass positive values")

        self.x = np.array([self._calculate_x(theta) for theta in self.thetas])
        self.y = np.array([self._calculate_y(theta) for theta in self.thetas])
        self.x += self.origin[0]
        self.y += self.origin[1]
        self.coords = list(zip(self.x, self.y, self.thetas))

    def scale(self, factor: Number) -> Union["_Trochoid", "_Cycloid"]:
        """Return shape with input parameters scaled by a given input factor.

        This method creates a new shape by scaling the input parameters R, r,
        and d (when applicable) by the given factor. The new shape is an
        instance of the same class as the original shape.

        Parameters
        ----------
        factor : Number
            The factor by which to scale the input parameters (R, r, and d).

        Returns
        -------
        Union["_Trochoid", "_Cycloid"]
            A new shape instance with the scaled input parameters.

        Examples
        --------
        >>> hypotrochoid = Hypotrochoid(10, 5, 3, thetas=[0, 1, 2])
        >>> scaled_hypotrochoid = hypotrochoid.scale(2)
        >>> scaled_hypotrochoid.R
        20
        >>> scaled_hypotrochoid.r
        10
        >>> scaled_hypotrochoid.d
        6
        """
        try:
            scaled_shape = self.__class__(
                R=self.R*factor,
                r=self.r*factor,
                d=self.d*factor,
                thetas=self.thetas
            )
        except TypeError:
            scaled_shape = self.__class__(
                R=self.R*factor,
                r=self.r*factor,
                thetas=self.thetas
            )
        return scaled_shape

    def plot(self, **kwargs) -> Tuple["matplotlib.matplotlib.Figure", "matplotlib.axes._axes.Axes"]:
        """Return matplotlib figure and axis objects after plotting the figure

        See available matplotlib.pyplot.plot configurations
        (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
        """
        # pylint: disable=line-too-long
        if plt is None:
            raise ImportError("matplotlib is required but is not installed on your machine, please install and try again")
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y, **kwargs)
        plt.show()
        return fig, ax

    def trace(
            self, screen_size: Tuple[Number, Number] = (1000, 1000),
            screen_color: str = "white", exit_on_click: bool = False,
            color: str = "black", width: Number = 1, hide_turtle: bool = True,
            show_circles: bool = False, frame_pause: Number = 0,
            screen: "turtle.Screen" = None, circle_color: str = "black",
            show_full_path: bool = False, full_path_color: str = "grey",
            repeat: bool = False
        ) -> "turtle.Screen":
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
        width: Number
            Width of the turtle tracing
        hide_turtle: bool = True
            Hide the turtle icon while tracing
        show_circles: bool = False
            Show the inner and outer circles that compose the trace
        frame_pause: Number = 0
            Time in seconds to pause each individual frame for
        screen: turle.Screen
            Existing turtle screen
        circle_color: str = "white"
            Color of the circles
        show_full_path: bool = False
            Show the full path prior to tracing
        full_path_color: str = "grey"
            Color of the full path drawing
        repeat: bool = False
            Infinitely repeat the animation so it starts over from the
            beginning

        Returns
        -------
        screen: turtle.Screen
            Screen that the turtle is drawn on
        """
        # pylint: disable=no-member,too-many-locals
        screen = self._init_screen(screen, screen_size, screen_color)
        turtle.tracer(False)

        turtles = self._init_turtles(color, circle_color, full_path_color, hide_turtle, width)

        if show_full_path:
            self._show_full_path(pre_draw_turtle=turtles.pre_draw_turtle)
        if show_circles:
            self._draw_circle(
                t=turtles.fixed_circle_turtle,
                x=self.origin[0],
                y=self.origin[1]-self.R,
                radius=self.R
            )

        while True:
            first = True
            turtles.shape_turtle.up()
            for x, y, theta in self.coords:
                turtles.shape_turtle.goto(x, y)
                if show_circles:
                    self._trace_rolling_circle(
                        turtles,
                        x,
                        y,
                        theta
                    )
                if first:
                    first = False
                    turtles.shape_turtle.down()
                if frame_pause > 0:
                    turtle.update()
                time.sleep(frame_pause)
            turtle.update()
            if not repeat:
                break
            turtles.shape_turtle.clear()
        if exit_on_click:
            turtle.exitonclick()
        return screen

    @classmethod
    def animate(
            cls, R: Union[Number, List[Number]], r: Union[Number, List[Number]],
            d: Union[Number, List[Number]], thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0)
        ) -> List["_Trochoid"]:
        """Animate the shape where one of the input parameters
        is a list of increments i.e. R, r, d and the rest are fixed

        Parameters
        ----------
        R : Union[Number, List[Number]]
            Radius of the fixed circle
        r : Union[Number, List[Number]]
            Radius of the rolling circle
        d : Union[Number, List[Number]]
            Distance of the trace point from the rolling circle
        thetas : List[Number] = None
            Input list of values for theta for inputting into parametric equations.
            This argument cannot be set at the same time as theta_start,
            theta_stop, theta_step
        theta_start : Number = None
            Starting theta value for creating a list of thetas (similar syntax
            to built-in range or np.arange). This argument cannot be set at the
            same time as thetas argument
        theta_stop : Number = None
            Stop theta value for creating a list of thetas, stop value is not
            included in the final array (similar syntax to built-in range or
            np.arange). This argument cannot be set at the same time as thetas
            argument
        theta_step : Number = None
            Incremental step value for stepping from start to stop
            (similar syntax to built-in range or np.arange). This argument
            cannot be set at the same time as thetas argument
        origin : Tuple[Number, Number] = (0, 0)
            Custom origin to center the shapes at. Default is (0,0)
        """
        shapes_arr = cls.create_range(
            R, r, d, thetas, theta_start,
            theta_stop, theta_step, origin
        )

    @property
    def df(self) -> "pd.DataFrame":
        """Return DataFrame of all relevant information pertaining to the parametrized shape"""
        #pylint: disable=line-too-long
        if pd is None:
            raise ImportError("pandas is required but is not installed on your machine, please install and try again")
        df = pd.DataFrame({
            "x": self.x,
            "y": self.y,
            "theta": self.thetas
        })
        return df

    @classmethod
    def create_range(
            cls, R: Union[Number, List[Number]], r: Union[Number, List[Number]],
            d: Union[Number, List[Number]], thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0)
        ) -> List["_Trochoid"]:
        """Return a list of instantiated shapes where one of the input parameters
        is a list of increments i.e. R, r, d and the rest are fixed

        Parameters
        ----------
        R : Union[Number, List[Number]]
            Radius of the fixed circle
        r : Union[Number, List[Number]]
            Radius of the rolling circle
        d : Union[Number, List[Number]]
            Distance of the trace point from the rolling circle
        thetas : List[Number] = None
            Input list of values for theta for inputting into parametric equations.
            This argument cannot be set at the same time as theta_start,
            theta_stop, theta_step
        theta_start : Number = None
            Starting theta value for creating a list of thetas (similar syntax
            to built-in range or np.arange). This argument cannot be set at the
            same time as thetas argument
        theta_stop : Number = None
            Stop theta value for creating a list of thetas, stop value is not
            included in the final array (similar syntax to built-in range or
            np.arange). This argument cannot be set at the same time as thetas
            argument
        theta_step : Number = None
            Incremental step value for stepping from start to stop
            (similar syntax to built-in range or np.arange). This argument
            cannot be set at the same time as thetas argument
        origin : Tuple[Number, Number] = (0, 0)
            Custom origin to center the shapes at. Default is (0,0)
        """
        # pylint: disable=line-too-long,redefined-argument-from-local,invalid-name,fixme
        inputs = collections.Counter([
            isinstance(R, collections.abc.Iterable),
            isinstance(r, collections.abc.Iterable),
            isinstance(d, collections.abc.Iterable)
        ])
        if inputs[True] > 1:
            raise ValueError("More than one input variable was varied. Please only pass one list of varying inputs and try again.")
        R_arr = cls._set_int_to_list(R)
        r_arr = cls._set_int_to_list(r)
        d_arr = cls._set_int_to_list(d)

        # TODO: this is fairly ugly, need to come up with better way of handling
        # this
        shapes = []
        for R in R_arr:
            for r in r_arr:
                for d in d_arr:
                    shapes.append(cls(
                        R, r, d, thetas, theta_start, theta_stop, theta_step,
                        origin
                    ))
        return shapes

    @staticmethod
    def _set_int_to_list(input_val: Union[Number, List[Number]]) -> List[Number]:
        """Return list of numbers from given input parameter"""
        if isinstance(input_val, Number):
            input_val = [input_val]
        return input_val

    def _show_full_path(self, pre_draw_turtle: "turtle.Turtle") -> None:
        """Draw the full path prior to tracing"""
        # pylint: disable=no-member, unused-variable
        first = True
        pre_draw_turtle.up()
        for x, y, theta in self.coords:
            pre_draw_turtle.goto(x, y)
            if first:
                first = False
                pre_draw_turtle.down()
        turtle.update()
        return pre_draw_turtle

    def _validate_theta(
            self, thetas: List[Number], theta_start: Number, theta_stop: Number,
            theta_step: Number
        ) -> "np.array":
        # pylint: disable=line-too-long
        theta_values = (theta_start, theta_stop, theta_step)
        multiple_thetas = thetas is not None and any(theta_values)
        if multiple_thetas:
            raise ValueError("Multiple definitions of theta were passed in as argument which is ambiguous - please define only one set of theta values.")
        if thetas is None:
            if theta_step is None:
                theta_step = .1
            thetas = np.arange(theta_start, theta_stop, theta_step)
        thetas = np.array(thetas)
        return thetas

    def _init_screen(
            self, screen: "turtle.Screen", screen_size: Tuple[Number, Number],
            screen_color: str
        ) -> "turtle.Screen":
        """Return initialized turtle.Screen"""
        if screen is None:
            screen = turtle.Screen()
            screen.setup(*screen_size)
            screen.bgcolor(screen_color)
        return screen

    def _init_turtles(
            self, color: str, circle_color: str, full_path_color: str,
            hide_turtle: bool, width: Number
        ) -> Tuple["turtle.Turtle", "turtle.Turtle", "turtle.Turtle", "turtle.Turtle"]:
        """Return a shape turtle, rolling circle turtle, and fixed circle turtle"""

        # Instantiate turtle
        shape_turtle = turtle.Turtle()
        rolling_circle_turtle = turtle.Turtle()
        fixed_circle_turtle = turtle.Turtle()
        pre_draw_turtle = turtle.Turtle()

        # Hide circle turtles
        if hide_turtle:
            shape_turtle.hideturtle()
        rolling_circle_turtle.hideturtle()
        fixed_circle_turtle.hideturtle()
        pre_draw_turtle.hideturtle()

        # Set turtle color
        shape_turtle.color(color)
        rolling_circle_turtle.color(circle_color)
        fixed_circle_turtle.color(circle_color)
        pre_draw_turtle.color(full_path_color)

        # Set turtle width
        shape_turtle.width(width)

        # Store turtle's in namedtuple
        turtles = self._create_turtles_namedtuple(
            shape_turtle,
            rolling_circle_turtle,
            fixed_circle_turtle,
            pre_draw_turtle
        )

        return turtles

    @staticmethod
    def _create_turtles_namedtuple(shape_turtle, rolling_circle_turtle, fixed_circle_turtle, pre_draw_turtle) -> "collections.namedtuple":
        """Return namedtuple containing turtles"""
        TraceTurtles = collections.namedtuple(
            "TraceTurtles",
            [
                "shape_turtle",
                "pre_draw_turtle",
                "rolling_circle_turtle",
                "fixed_circle_turtle"
            ]
        )
        turtles = TraceTurtles(
            shape_turtle,
            pre_draw_turtle,
            rolling_circle_turtle,
            fixed_circle_turtle
        )
        return turtles

    def _trace_rolling_circle(
            self, turtles: "collections.namedtuple",
            x: Number, y: Number, theta: Number
        ) -> None:
        """Trace the inner circle of the animation"""
        self._rolling_circle_init(turtles.rolling_circle_turtle)
        self._draw_dot(turtles.rolling_circle_turtle, x, y, "red")
        rolling_circle_x, rolling_circle_y = self._draw_rolling_circle(turtles.rolling_circle_turtle, theta)
        self._draw_dot(
            t=turtles.rolling_circle_turtle,
            x=rolling_circle_x,
            y=rolling_circle_y + self.r,
            color="blue"
        )
        self._connect_focus_to_trace_dots(turtles)

    def _connect_focus_to_trace_dots(self, turtles: "collections.namedtuple") -> None:
        """Draw line from focus to the trace that's drawing the shape"""
        turtles.rolling_circle_turtle.down()
        turtles.rolling_circle_turtle.seth(turtles.rolling_circle_turtle.towards(turtles.shape_turtle))
        turtles.rolling_circle_turtle.fd(self.d)

    def _draw_circle(
            self, t: "turtle.Turtle", x: float, y: float, radius: float
        ) -> None:
        """Draw circle"""
        t.up()
        t.seth(0)
        t.goto(x, y)
        t.down()
        t.circle(radius, steps=200)

    def _draw_rolling_circle(self, t: "turtle.Turtle", theta: Number) -> None:
        """Draw the rolling circle on the screen"""
        x=self._circle_offset()*math.cos(theta) + self.origin[0]
        y=self._circle_offset()*math.sin(theta) - self.r + self.origin[1]
        self._draw_circle(
            t=t,
            x=x,
            y=y,
            radius=self.r
        )
        return x, y

    def _draw_dot(
            self, t: "turtle.Turtle", x: Number, y: Number, color: str
        ) -> None:
        """Draw rolling circle outer trace"""
        t.up()
        t.goto(x, y)
        t.dot(10, color)

    def _rolling_circle_init(self, t: "turtle.Turtle") -> None:
        """Set iteration's initial conditions for rolling circle"""
        t.clear()
        t.seth(0)
        t.up()

    @abstractmethod
    def _circle_offset(self) -> float:
        """Return rolling circle offset from fixed circle"""

    @abstractmethod
    def _calculate_x(self, theta: Number) -> float:
        """Return calculated x-value from parametrized equation"""

    @abstractmethod
    def _calculate_y(self, theta: Number) -> float:
        """Return calculated y-value from parametrized equation"""
