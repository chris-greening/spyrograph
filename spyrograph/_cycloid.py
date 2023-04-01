"""Abstract base class for generalizing the hypocycloid and epicycloid
shape's methods i.e. tracing, calculating, etc.
"""

from numbers import Number
from typing import List, Tuple, Union
import collections

from spyrograph._trochoid import _Trochoid

class _Cycloid(_Trochoid):
    # pylint: disable=too-few-public-methods
    def __init__(
            self, R: Number, r: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0)
        ) -> None:
        super().__init__(R, r, r, thetas, theta_start, theta_stop, theta_step, origin)
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
        inputs = collections.Counter([
            isinstance(R, collections.abc.Iterable),
            isinstance(r, collections.abc.Iterable)
        ])
        if inputs[True] > 1:
            raise ValueError("More than one input variable was varied. Please only pass one list of varying inputs and try again.")
        R_arr = cls._set_int_to_list(R)
        r_arr = cls._set_int_to_list(r)

        # TODO: this is fairly ugly, need to come up with better way of handling
        # this
        shapes = []
        for R in R_arr:
            for r in r_arr:
                shapes.append(cls(
                    R, r, thetas, theta_start, theta_stop, theta_step,
                    origin
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
