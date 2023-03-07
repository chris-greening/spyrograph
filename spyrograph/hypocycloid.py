from typing import List
from numbers import Number

from spyrograph.hypotrochoid import Hypotrochoid

class Hypocycloid(Hypotrochoid):
    def __init__(self, R: Number, r: Number, thetas: List[Number]) -> None:
        super().__init__(R, r, r, thetas)