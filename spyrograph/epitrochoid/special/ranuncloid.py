"""Model of a ranuncloid. A ranuncloid is a specific case of an epicycloid
where the fixed circle radius equals 1/5 of the rolling circle.
"""

from typing import List
from numbers import Number

from spyrograph.epitrochoid.epicycloid import Epicycloid

class Ranuncloid(Epicycloid):
    """Model of a ranuncloid which is a special case of an epicycloid where the
    rolling circle is 1/5 the radius of the fixed circle
    """
    def __init__(
            self, R: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None
        ) -> None:
        super().__init__(R, R/5, thetas, theta_start, theta_stop, theta_step)
