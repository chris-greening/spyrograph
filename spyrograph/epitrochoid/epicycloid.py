"""Model of an epicycloid. An epicycloid is a specific case of an epitrochoid
where the distance from the rolling circle is equal to its radius.
"""

from spyrograph.epitrochoid.epitrochoid import Epitrochoid
from spyrograph.core._cycloid import _Cycloid

class Epicycloid(_Cycloid, Epitrochoid):
    """
    A class that represents an epicycloid, which is a curve traced by a point on a circle
    that rolls around the outside of a fixed circle. This is a special case of an epitrochoid
    where the rolling circle has a radius.

    The Epicycloid class allows you to generate points along the curve using mathematical
    equations, and visualize the curve in a plot. It also provides properties and methods
    for plotting and animating the curve.

    This class is a powerful tool for exploring the properties and behaviors of epicycloids,
    and can be used in a variety of applications such as in mechanical engineering and
    mathematics education.
    """
    # pylint: disable=pointless-string-statement
