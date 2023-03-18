"""Model of a cardioid. A cardioid is a specific case of an epicycloid
where the fixed circle radius equals that of the rolling circle.
"""

from typing import List
from numbers import Number

from spyrograph.epitrochoid.epicycloid import Epicycloid

class Cardioid(Epicycloid):
    """Model of a cardioid which is a special case of an epicycloid where the
    two circles are equal in radius
    """
    def __init__(
            self, R: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None
        ) -> None:
        super().__init__(R, R, thetas, theta_start, theta_stop, theta_step)
