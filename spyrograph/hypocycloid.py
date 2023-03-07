"""Model of a hypocycloid. Specific case of a hypotrochoid where the distance
from the rolling circle is equal to the radius of the rolling circle
"""

from typing import List
from numbers import Number

from spyrograph.hypotrochoid import Hypotrochoid

class Hypocycloid(Hypotrochoid):
    def __init__(self, R: Number, r: Number, thetas: List[Number]) -> None:
        super().__init__(R, r, r, thetas)
