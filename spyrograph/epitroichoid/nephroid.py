"""Model of a nephroid. A nephroid is a specific case of an epicycloid
where the fixed circle radius equals half of the rolling circle.
"""

from typing import List
from numbers import Number

from spyrograph.epitrochoid.epicycloid import Epicycloid

class Nephroid(Epicycloid):
    """Model of a nephroid which is a special case of an epicycloid where the
    rolling circle is half the radius of the fixed circle
    """
    def __init__(
            self, R: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None
        ) -> None:
        super().__init__(R, R/2, thetas, theta_start, theta_stop, theta_step)
