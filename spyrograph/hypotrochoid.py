"""Model of a hypotrochoid. A hypotrochoid is a geometric shape drawn from a line
attached to a circle rolling around the interior of a fixed circle
"""

import math
from numbers import Number

from spyrograph._roulette import _Roulette

class Hypotrochoid(_Roulette):
    """Model of a hypotrochoid"""
    def _circle_offset(self) -> Number:
        """Return rolling circle offset from fixed circle"""
        return self.R - self.r

    def _calculate_x(self, theta: Number) -> Number:
        """Return calculated x-value from parametrized equation"""
        # pylint: disable=line-too-long
        return self._circle_offset()*math.cos(theta) + self.d*math.cos((self._circle_offset()/self.r)*theta)

    def _calculate_y(self, theta: Number) -> Number:
        """Return calculated y-value from parametrized equation"""
        # pylint: disable=line-too-long
        return self._circle_offset()*math.sin(theta) - self.d*math.sin((self._circle_offset()/self.r)*theta)
