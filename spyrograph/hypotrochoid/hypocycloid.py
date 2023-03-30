"""Model of a hypocycloid. Specific case of a hypotrochoid where the distance
from the rolling circle is equal to the radius of the rolling circle
"""

from typing import List, Tuple
from numbers import Number

from spyrograph.hypotrochoid.hypotrochoid import Hypotrochoid
from spyrograph._cycloid import _Cycloid

class Hypocycloid(_Cycloid, Hypotrochoid):
    """
    Model of a hypocycloid, which is a mathematical curve traced by a point on a circle as
    it rolls around the inside of another fixed circle. This class represents a special case of
    a hypotrochoid, where the distance from the point to the rolling circle is equal to the radius
    of the rolling circle.

    The Hypocycloid class allows you to generate points along the curve using mathematical
    equations and visualize the curve in a plot. It also provides properties and methods for
    computing the length, area, and curvature of the curve, as well as for plotting and animating
    the curve.

    The Hypocycloid class is a useful tool for exploring the properties and behaviors of hypocycloids,
    and can be used in a variety of applications such as in mechanical engineering and mathematics
    education. If you need to work with hypocycloids for a project or research, the Hypocycloid class
    provides a simple and intuitive interface to generate these curves and explore their properties.
    """
    # pylint: disable=pointless-string-statement
    def __init__(
            self, R: Number, r: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0)
        ) -> None:
        super().__init__(R, r, r, thetas, theta_start, theta_stop, theta_step, origin)
        """Instantiate a hypocycloid curve from given input parameters. A
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
