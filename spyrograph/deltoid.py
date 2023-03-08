from numbers import Number
from typing import List

from spyrograph.hypocycloid import Hypocycloid

class Deltoid(Hypocycloid):
    def __init__(self, R: Number, thetas: List[Number]) -> None:
        super().__init__(R, R/3, thetas)