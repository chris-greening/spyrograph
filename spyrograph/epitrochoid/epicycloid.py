"""Model of an epicycloid. An epicycloid is a specific case of an epitrochoid
where the distance from the rolling circle is equal to its radius.
"""

from typing import List, Tuple
from numbers import Number

from spyrograph.epitrochoid.epitrochoid import Epitrochoid
from spyrograph._cycloid import _Cycloid

class Epicycloid(_Cycloid, Epitrochoid):
    """Model of a epicycloid which is a special case of a epitrochoid where the
    circle is rolling around the outside of the fixed circle and has 1/3 the
    radius of the fixed circle
    """
    # pylint: disable=pointless-string-statement
    def __init__(
            self, R: Number, r: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0)
        ) -> None:
        super().__init__(R, r, r, thetas, theta_start, theta_stop, theta_step, origin)
        """Instantiate an epicycloid curve from given input parameters. A
        epicycloid is a curve drawn by tracing a point from a circle as it
        rolls around the outside of a fixed circle where the distance
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
