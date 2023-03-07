"""Model of an epicycloid. An epicycloid is a specific case of an epitrochoid 
where the distance from the rolling circle is equal to its radius. 
"""

from typing import List
from numbers import Number

from spyrograph.epitrochoid import Epitrochoid

class Epicycloid(Epitrochoid):
    def __init__(self, R: Number, r: Number, thetas: List[Number]) -> None:
        super().__init__(R, r, r, thetas)
