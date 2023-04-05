"""Abstract base class for generalizing the hypocycloid and epicycloid
shape's methods i.e. tracing, calculating, etc.
"""

from numbers import Number
from typing import List, Tuple, Union
import turtle

from spyrograph.core._trochoid import _Trochoid
from spyrograph.core._misc import (
    _get_products_of_inputs, _validate_only_one_iterable, _draw_animation
)
class _Cycloid(_Trochoid):
    # pylint: disable=too-few-public-methods
    def __init__(
            self, R: Number, r: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0)
        ) -> None:
        super().__init__(R, r, r, thetas, theta_start, theta_stop, theta_step, origin)
        # pylint: disable=pointless-string-statement
        """Instantiate a cycloid curve from given input parameters. A
        hypocycloid is a curve drawn by tracing a point from a circle as it
        rolls around the inside of a fixed circle where the distance
        from the point to the rolling circle is equal to the radius of the
        rolling circle

        Parameters
        ----------
        R : Number
            Radius of the fixed circle
        r : number
            Radius of the rolling circle
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

    @classmethod
    # pylint: disable=arguments-differ, too-many-locals
    def animate(
            cls, R: Union[Number, List[Number]], r: Union[Number, List[Number]],
            thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0),
            screen_size: Tuple[Number, Number] = (1000, 1000),
            screen_color: str = "white", exit_on_click: bool = False,
            color: str = "black", width: Number = 1,
            frame_pause: Number = 0.1, screen: "turtle.Screen" = None
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
        # pylint: disable=duplicate-code
        shapes_arr = cls.create_range(
            R, r, thetas, theta_start,
            theta_stop, theta_step, origin
        )
        _draw_animation(
            shapes_arr=shapes_arr, screen_size=screen_size,
            screen_color=screen_color, exit_on_click=exit_on_click, color=color,
            width=width, frame_pause=frame_pause, screen=screen
        )

    @classmethod
    # pylint: disable=arguments-differ
    def create_range(
            cls, R: Union[Number, List[Number]], r: Union[Number, List[Number]],
            thetas: List[Number] = None, theta_start: Number = None,
            theta_stop: Number = None, theta_step: Number = None,
            origin: Tuple[Number, Number] = (0, 0)
        ) -> List["_Trochoid"]:
        """Return a list of instantiated shapes where one of the input parameters
        is a list of increments i.e. R, r and the rest are fixed

        Parameters
        ----------
        R : Union[Number, List[Number]]
            Radius of the fixed circle
        r : Union[Number, List[Number]]
            Radius of the rolling circle
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
        # pylint: disable=line-too-long,redefined-argument-from-local,invalid-name,no-member,fixme
        _validate_only_one_iterable(R, r)
        input_params = _get_products_of_inputs(R, r)

        shapes = []
        for R, r in input_params:
            shapes.append(cls(
                R, r, thetas, theta_start, theta_stop, theta_step, origin
            ))
        return shapes

    @classmethod
    def n_cusps(
            cls, R: Number, n: int, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0)
        ) -> "Cycloid":
        """
        Create and return a cycloid with a specified number of cusps.

        Parameters
        ----------
        R : Number
            Radius of the fixed circle.
        n : int
            Number of cusps to create in the cycloid.
        thetas : List[Number], optional
            List of theta values for inputting into parametric equations.
        theta_start : Number, optional
            Starting theta value for creating a list of thetas (similar syntax
            to built-in range or np.arange).
        theta_stop : Number, optional
            Stop theta value for creating a list of thetas; the stop value is not
            included in the final array (similar syntax to built-in range or
            np.arange).
        theta_step : Number, optional
            Incremental step value for stepping from start to stop (similar syntax
            to built-in range or np.arange).
        origin : Tuple[Number, Number], optional, default: (0, 0)
            Custom origin to center the shapes at. Default is (0, 0).

        Returns
        -------
        Cycloid
            A Cycloid object with the specified number of cusps.

        Examples
        --------
        >>> from spyrograph import Cycloid
        >>> cycloid = Cycloid.n_cusps(R=10, n=5)
        >>> cycloid.trace(exit_on_click=True)
        """
        return cls(
            R=R,
            r=R/n,
            thetas=thetas,
            theta_start=theta_start,
            theta_stop=theta_stop,
            theta_step=theta_step,
            origin=origin
        )
