"""Abstract base class for generalizing the hypocycloid and epicycloid
shape's methods i.e. tracing, calculating, etc.
"""

from abc import ABC
from numbers import Number
from typing import List

class _Cycloid(ABC):
    # pylint: disable=too-few-public-methods
    @classmethod
    def n_cusps(
            cls, R: Number, n: int, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None
        ) -> "Cycloid":
        """Return a cycloid with n number of cusps"""
        return cls(
            R=R,
            r=R/n,
            thetas=thetas,
            theta_start=theta_start,
            theta_stop=theta_stop,
            theta_step=theta_step
        )
