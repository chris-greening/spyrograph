"""Model of an epitrochoid. An epitrochoid is a geometric shape drawn from a line
attached to a circle rolling around the exterior of a fixed circle
"""

import math
from numbers import Number

from spyrograph.core._trochoid import _Trochoid

class Epitrochoid(_Trochoid):
    """
    Model of an epitrochoid, which is a geometric shape drawn by a line attached to a circle
    as it rolls around the exterior of a fixed circle.

    The Epitrochoid class provides methods for calculating the x- and y-values of the epitrochoid
    at a given theta value using parametrized equations. The class takes in parameters such as the
    radius of the fixed circle, the radius of the rolling circle, and the distance between their
    centers, which affect the shape of the curve.

    The Epitrochoid class is a useful tool for exploring the properties and
    behaviors of epitrochoids, and can be used in a variety of applications
    such as in mechanical engineering and mathematics education. If you need to
    work with epitrochoids for a project or research, the Epitrochoid class
    provides a simple and intuitive interface to generate these curves and
    explore their properties.
    """
    def _circle_offset(self) -> Number:
        """Return rolling circle offset from fixed circle"""
        return self.R + self.r

    def _calculate_x(self, theta: Number) -> Number:
        """Return calculated x-value from parametrized equation"""
        # pylint: disable=line-too-long
        return self._circle_offset()*math.cos(theta) - self.d*math.cos((self._circle_offset()/self.r)*theta)

    def _calculate_y(self, theta: Number) -> Number:
        """Return calculated y-value from parametrized equation"""
        # pylint: disable=line-too-long\
        return self._circle_offset()*math.sin(theta) - self.d*math.sin((self._circle_offset()/self.r)*theta)
