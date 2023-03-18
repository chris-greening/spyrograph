"""Model of a deltoid. A deltoid is a special case of a hypocycloid where the
rolling circle has 1/3 the radius of the fixed circle and the distance traced
from the rolling circle is equal to the radius of the rolling circle"""

from numbers import Number
from typing import List

from spyrograph.hypotrochoid.hypocycloid import Hypocycloid

class Deltoid(Hypocycloid):
    """Model of a deltoid which is a special case of a hypocycloid where the
    rolling circle has 1/3 the radius of the fixed circle
    """
    def __init__(
            self, R: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None
        ) -> None:
        super().__init__(R, R/3, thetas, theta_start, theta_stop, theta_step)
