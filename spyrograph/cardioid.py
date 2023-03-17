"""Model of a cardioid. A cardioid is a specific case of an epicycloid
where the distance from the rolling circle is equal to its radius.
"""

from typing import List
from numbers import Number

from spyrograph.epicycloid import Epicycloid

class Cardioid(Epicycloid):
    """Model of a cardioid which is a special case of an epicycloid where the
    circle is rolling around the outside of the fixed circle and d = r
    """
    def __init__(
            self, R: Number, r: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None
        ) -> None:
        super().__init__(R, r, thetas, theta_start, theta_stop, theta_step)
