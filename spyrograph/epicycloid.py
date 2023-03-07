from typing import List
from numbers import Number

from spyrograph.epitrochoid import Epitrochoid

class Epicycloid(Epitrochoid):
    def __init__(self, R: Number, r: Number, thetas: List[Number]) -> None:
        super().__init__(R, r, r, thetas)