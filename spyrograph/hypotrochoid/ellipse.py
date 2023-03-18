"""Model of an ellipse. An ellipse is a special case of a hypotrochoid where the
rolling circle is 1/2 the radius of the fixed circle and the distance traced
from the rolling circle is not equal to the radius of the rolling circle"""

import math
from numbers import Number
from typing import List

from spyrograph.hypotrochoid.hypotrochoid import Hypotrochoid

class Ellipse(Hypotrochoid):
    """Model of an ellipse which is a special case of a hypotrochoid where the
    rolling circle has 1/2 the radius of the fixed circle
    """
    def __init__(
            self, R: Number, d: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None) -> None:
        super().__init__(R, R/2, d, thetas, theta_start, theta_stop, theta_step)

        self.eccentricity = (2*math.sqrt(self.d/self.r))/(1 + (self.d/self.r))
