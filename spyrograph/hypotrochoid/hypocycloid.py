"""Model of a hypocycloid. Specific case of a hypotrochoid where the distance
from the rolling circle is equal to the radius of the rolling circle
"""

from spyrograph.hypotrochoid.hypotrochoid import Hypotrochoid
from spyrograph.core._cycloid import _Cycloid

class Hypocycloid(_Cycloid, Hypotrochoid):
    """
    Model of a hypocycloid, which is a mathematical curve traced by a point on
    a circle as it rolls around the inside of another fixed circle. This class
    represents a special case of a hypotrochoid, where the distance from the
    point to the rolling circle is equal to the radius of the rolling circle.

    The Hypocycloid class allows you to generate points along the curve using
    mathematical equations and visualize the curve in a plot. It also provides
    properties and methods for plotting and animating the curve.

    The Hypocycloid class is a useful tool for exploring the properties and
    behaviors of hypocycloids, and can be used in a variety of applications
    such as in mechanical engineering and mathematics education. If you need to
    work with hypocycloids for a project or research, the Hypocycloid class
    provides a simple and intuitive interface to generate these curves and 
    explore their properties.
    """
    # pylint: disable=pointless-string-statement
