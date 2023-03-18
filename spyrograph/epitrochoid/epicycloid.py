"""Model of an epicycloid. An epicycloid is a specific case of an epitrochoid
where the distance from the rolling circle is equal to its radius.
"""

from typing import List
from numbers import Number

from spyrograph.epitrochoid.epitrochoid import Epitrochoid

class Epicycloid(Epitrochoid):
    """Model of a epicycloid which is a special case of a epitrochoid where the
    circle is rolling around the outside of the fixed circle and has 1/3 the
    radius of the fixed circle
    """
    def __init__(
            self, R: Number, r: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None
        ) -> None:
        super().__init__(R, r, r, thetas, theta_start, theta_stop, theta_step)
