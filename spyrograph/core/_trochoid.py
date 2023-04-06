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

from spyrograph.core._misc import (
    _get_products_of_inputs, _validate_only_one_iterable, _draw_animation, _validate_theta
)

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
        self.thetas = _validate_theta(thetas, theta_start, theta_stop, theta_step)
        self.origin = origin

        if self.R <= 0 or self.r <= 0 or self.d <= 0:
            raise ValueError((
                "Negative and/or zero input parameters were passed. "
                "Please only pass positive values"
            ))

        self.x = np.array([self._calculate_x(theta) for theta in self.thetas])
        self.y = np.array([self._calculate_y(theta) for theta in self.thetas])
        self.x += self.origin[0]
        self.y += self.origin[1]
        self.coords = list(zip(self.x, self.y, self.thetas))

    def transform(self, x: Number = 0, y: Number = 0) -> "_Trochoid":
        """
        Return a new shape translated by the given x and y offsets.

        Parameters
        ----------
        x : Number, optional, default=0
            The x-offset to shift the shape by.
        y : Number, optional, default=0
            The y-offset to shift the shape by.

        Returns
        -------
        _Trochoid
            A new instance of the shape translated by the given x and y offsets.

        Examples
        --------
        >>> shape = Trochoid(R=5, r=2, d=3, thetas=thetas)
        >>> transformed_shape = shape.transform(x=10, y=5)
        """
        # pylint: disable=no-value-for-parameter
        try:
            transformed_shape = self.__class__(
                R=self.R,
                r=self.r,
                d=self.d,
                thetas=self.thetas,
                origin=(self.origin[0]+x, self.origin[1]+y)
            )
        except TypeError:
            transformed_shape = self.__class__(
                R=self.R,
                r=self.r,
                thetas=self.thetas,
                origin=(self.origin[0]+x, self.origin[1]+y)
            )
        return transformed_shape

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
        # pylint: disable=no-value-for-parameter
        try:
            scaled_shape = self.__class__(
                R=self.R*factor,
                r=self.r*factor,
                d=self.d*factor,
                thetas=self.thetas,
                origin=self.origin
            )
        except TypeError:
            scaled_shape = self.__class__(
                R=self.R*factor,
                r=self.r*factor,
                thetas=self.thetas,
                origin=self.origin
            )
        return scaled_shape

    def plot(self, **kwargs) -> Tuple["matplotlib.matplotlib.Figure", "matplotlib.axes._axes.Axes"]:
        """
        Plot the shape and return the associated matplotlib Figure and Axes objects.

        This method plots the shape using the `x` and `y` attributes of the object,
        which are defined by the parametric equations from the given input parameters.
        It returns the Figure and Axes objects of the created plot for further
        customization if needed.

        Parameters
        ----------
        **kwargs
            Keyword arguments passed to the matplotlib.pyplot.plot function. For a
            full list of available options, refer to:
            https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

        Returns
        -------
        fig : matplotlib.matplotlib.Figure
            The Figure object associated with the created plot.
        ax : matplotlib.axes._axes.Axes
            The Axes object associated with the created plot.

        Raises
        ------
        ImportError
            If matplotlib is not installed on the user's machine.

        Examples
        --------
        >>> from spyrograph import Hypotrochoid
        >>> import numpy as np
        >>> shape = Hypotrochoid(R=300, r=200, d=200, thetas=np.arange(0, 2*np.pi, .01))
        >>> fig, ax = shape.plot()
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
            repeat: bool = False, screen_coords = (0, 0)
        ) -> "turtle.Screen":
        """
        Trace the shape using the turtle graphics library and return the turtle.Screen object.

        This method visually traces the shape using turtle graphics, allowing for various
        customization options, such as colors, line width, and frame pause time.

        Parameters
        ----------
        screen_size : Tuple[Number, Number], optional
            The length and width of the output screen, default is (1000, 1000).
        screen_color : str, optional
            The color of the background screen, default is "white".
        exit_on_click : bool, optional
            If True, pause the final animation until the user clicks to exit
            the window, default is False.
        color : str, optional
            The color of the primary tracing, default is "black".
        width : Number, optional
            The width of the turtle tracing, default is 1.
        hide_turtle : bool, optional
            If True, hide the turtle icon while tracing, default is True.
        show_circles : bool, optional
            If True, show the inner and outer circles that compose the trace, default is False.
        frame_pause : Number, optional
            The time in seconds to pause each individual frame, default is 0.
        screen : turtle.Screen, optional
            An existing turtle screen, default is None.
        circle_color : str, optional
            The color of the circles, default is "black".
        show_full_path : bool, optional
            If True, show the full path prior to tracing, default is False.
        full_path_color : str, optional
            The color of the full path drawing, default is "grey".
        repeat : bool, optional
            If True, infinitely repeat the animation so it starts over from the
            beginning, default is False.
        screen_coords : Tuple[int, int] = (0, 0)
            Location of the screen coordinates

        Returns
        -------
        screen : turtle.Screen
            The screen that the turtle is drawn on.

        Examples
        --------
        >>> from spyrograph import Hypotrochoid
        >>> import numpy as np
        >>> shape = Hypotrochoid(R=300, r=200, d=200, thetas=np.arange(0, 2*np.pi, .01))
        >>> screen = shape.trace(show_circles=True, exit_on_click=True)
        """
        # pylint: disable=no-member,too-many-locals
        screen = self._init_screen(screen, screen_size, screen_color, screen_coords)
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
        return screen, turtles

    @classmethod
    def animate(
            cls, R: Union[Number, List[Number]], r: Union[Number, List[Number]],
            d: Union[Number, List[Number]], thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0),
            screen_size: Tuple[Number, Number] = (1000, 1000),
            screen_color: str = "white", exit_on_click: bool = False,
            color: str = "black", width: Number = 1,
            frame_pause: Number = 0.1, screen: "turtle.Screen" = None, screen_coords = (0, 0)
        ) -> List["_Trochoid"]:
        """
        Animate a sequence of _Trochoid shapes with varying input parameters,
        drawn one after the other.

        Parameters
        ----------
        R : Union[Number, List[Number]]
            Radius of the fixed circle.
        r : Union[Number, List[Number]]
            Radius of the rolling circle.
        d : Union[Number, List[Number]]
            Distance of the trace point from the rolling circle.
        thetas : List[Number], optional
            Input list of values for theta for inputting into parametric equations.
            This argument cannot be set at the same time as theta_start,
            theta_stop, theta_step.
        theta_start : Number, optional
            Starting theta value for creating a list of thetas (similar syntax
            to built-in range or np.arange). This argument cannot be set at the
            same time as thetas argument.
        theta_stop : Number, optional
            Stop theta value for creating a list of thetas, stop value is not
            included in the final array (similar syntax to built-in range or
            np.arange). This argument cannot be set at the same time as thetas
            argument.
        theta_step : Number, optional
            Incremental step value for stepping from start to stop
            (similar syntax to built-in range or np.arange). This argument
            cannot be set at the same time as thetas argument.
        origin : Tuple[Number, Number], optional, default (0, 0)
            Custom origin to center the shapes at. Default is (0,0).
        screen_size : Tuple[Number, Number], optional, default (1000, 1000)
            Length and width of the output screen.
        screen_color : str, optional, default "white"
            Color of the background screen.
        exit_on_click : bool, optional, default False
            Pause the final animation until the user clicks to exit the window.
        color : str, optional, default "black"
            Color of the primary tracing.
        width : Number, optional, default 1
            Width of the turtle tracing.
        frame_pause : Number, optional, default 0.1
            Time in seconds to pause between each shape in the animation.
        screen : turtle.Screen, optional
            Existing turtle screen.

        Returns
        -------
        shapes : List[_Trochoid]
            A list of instantiated _Trochoid shapes with varying input parameters.

        Examples
        --------
        >>> from spyrograph import Hypotrochoid
        >>> import numpy as np
        >>> thetas = np.linspace(0, 2 * np.pi, num=1000)
        >>> shapes = Hypotrochoid.animate(R=10, r=[4, 5, 6], d=8, thetas=thetas)
        """
        # pylint: disable=too-many-locals
        shapes_arr = cls.create_range(
            R, r, d, thetas, theta_start,
            theta_stop, theta_step, origin
        )
        _draw_animation(
            shapes_arr=shapes_arr, screen_size=screen_size,
            screen_color=screen_color, exit_on_click=exit_on_click, color=color,
            width=width, frame_pause=frame_pause, screen=screen,
            screen_coords=screen_coords
        )
        return shapes_arr

    @property
    def df(self) -> "pd.DataFrame":
        """
        Return a pandas DataFrame containing all relevant information
        pertaining to the parametrized shape.

        This property creates a pandas DataFrame with columns for the x and y
        coordinates, as well as the
        angular positions (theta) of the parametrized shape.

        Raises
        ------
        ImportError
            If pandas is not installed on the user's machine.

        Returns
        -------
        df : pd.DataFrame
            A DataFrame with columns 'x', 'y', and 'theta', containing the x and y coordinates and
            angular positions of the parametrized shape.

        Examples
        --------
        >>> from spyrograph import Hypotrochoid
        >>> import numpy as np
        >>> thetas = np.linspace(0, 2 * np.pi, num=1000)
        >>> shape = Hypotrochoid(R=10, r=6, d=8, thetas=thetas)
        >>> shape_df = shape.df
        >>> shape_df.head()
            x         y     theta
        0  12.000  2.000000  0.000000
        1  11.998  1.999217  0.006283
        2  11.993  1.996869  0.012566
        3  11.985  1.993056  0.018849
        4  11.974  1.987778  0.025132
        """
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
        """
        Return a list of instantiated shapes where one of the input parameters
        (R, r, or d) is a list of increments, and the rest are fixed.

        Parameters
        ----------
        R : Union[Number, List[Number]]
            Radius of the fixed circle.
        r : Union[Number, List[Number]]
            Radius of the rolling circle.
        d : Union[Number, List[Number]]
            Distance of the trace point from the rolling circle.
        thetas : List[Number], optional
            Input list of values for theta for inputting into parametric
            equations. This argument cannot be set at the same time as
            theta_start, theta_stop, theta_step.
        theta_start : Number, optional
            Starting theta value for creating a list of thetas (similar syntax
            to built-in range or np.arange). This argument cannot be set at the
            same time as thetas argument.
        theta_stop : Number, optional
            Stop theta value for creating a list of thetas, stop value is not
            included in the final array (similar syntax to built-in range or
            np.arange). This argument cannot be set at the same time as thetas
            argument.
        theta_step : Number, optional
            Incremental step value for stepping from start to stop
            (similar syntax to built-in range or np.arange). This argument
            cannot be set at the same time as thetas argument.
        origin : Tuple[Number, Number], optional, default (0, 0)
            Custom origin to center the shapes at. Default is (0,0).

        Returns
        -------
        shapes : List[_Trochoid]
            A list of instantiated _Trochoid shapes with varying input parameters.

        Raises
        ------
        ValueError
            If more than one input variable (R, r, or d) is a list of varying inputs.

        Examples
        --------
        >>> from spyrograph import Hypotrochoid
        >>> import numpy as np
        >>> thetas = np.linspace(0, 2 * np.pi, num=1000)
        >>> shapes = Hypotrochoid.create_range(R=10, r=[4, 5, 6], d=8, thetas=thetas)
        >>> len(shapes)
        3
        """
        # pylint: disable=line-too-long,redefined-argument-from-local,invalid-name,fixme

        _validate_only_one_iterable(R, r, d)
        input_params = _get_products_of_inputs(R, r, d)

        shapes = []
        for R, r, d in input_params:
            shapes.append(cls(
                R, r, d, thetas, theta_start, theta_stop, theta_step, origin
            ))
        return shapes

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

    def _init_screen(
            self, screen: "turtle.Screen", screen_size: Tuple[Number, Number],
            screen_color: str, screen_coords: Tuple[Number, Number]
        ) -> "turtle.Screen":
        """Initializes the turtle screen with the given size and color"""
        if screen is None:
            screen = turtle.Screen()
            screen.setup(*screen_size)
            screen.bgcolor(screen_color)
            canvas = screen.getcanvas()
            root = canvas.winfo_toplevel()
            root.geometry(f"+{screen_coords[0]}+{screen_coords[1]}")
        return screen

    def _init_turtles(
            self, color: str, circle_color: str, full_path_color: str,
            hide_turtle: bool, width: Number
        ) -> Tuple["turtle.Turtle", "turtle.Turtle", "turtle.Turtle", "turtle.Turtle"]:
        """
        Initialize four turtle objects with the specified color, width, and visibility.

        The returned tuple contains four turtles:
        - shape_turtle: the main turtle shape.
        - rolling_circle_turtle: a turtle used for drawing a rolling circle.
        - fixed_circle_turtle: a turtle used for drawing a fixed circle.
        - pre_draw_turtle: a turtle used for drawing the full path.
        """

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
    def _create_turtles_namedtuple(
            shape_turtle: "turtle.Turtle", rolling_circle_turtle: "turtle.Turtle",
            fixed_circle_turtle: "turtle.Turtle", pre_draw_turtle: "turtle.Turtle"
        ) -> "collections.namedtuple":
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
        rolling_circle_x, rolling_circle_y = self._draw_rolling_circle(
            turtles.rolling_circle_turtle, theta
        )
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
        turtles.rolling_circle_turtle.seth(
            turtles.rolling_circle_turtle.towards(turtles.shape_turtle)
        )
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

    def __repr__(self) -> str:
        """Return formatted string with useful information about the current object"""
        # pylint: disable=line-too-long
        if len(self.thetas) < 4:
            thetas_str_list = map(str, self.thetas)
            thetas_str = f"[{', '.join(thetas_str_list)}]"
        else:
            thetas_str = f"[{self.thetas[0]}, {self.thetas[1]}, ... {self.thetas[-1]}]"
        return f"{self.__class__.__name__}(R={self.R}, r={self.r}, d={self.d}, thetas={thetas_str}, origin=({self.origin[0]},{self.origin[1]}))"
