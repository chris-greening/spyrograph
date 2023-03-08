from numbers import Number

from spyrograph.hypocycloid import Hypocycloid

class Deltoid(Hypocycloid):
    def __init__(self, R: Number, thetas: List[Number]) -> None:
        super().__init__(R, R/3, R/3, thetas)