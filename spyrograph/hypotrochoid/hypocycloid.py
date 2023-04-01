"""Model of a hypocycloid. Specific case of a hypotrochoid where the distance
from the rolling circle is equal to the radius of the rolling circle
"""

from typing import List, Tuple
from numbers import Number

from spyrograph.hypotrochoid.hypotrochoid import Hypotrochoid
from spyrograph._cycloid import _Cycloid

class Hypocycloid(_Cycloid, Hypotrochoid):
    """Model of a hypocycloid which is a special case of a hypotrochoid where
    the circle is rolling around the inside of the fixed circle and has 1/3
    the radius of the fixed circle
    """
    # pylint: disable=pointless-string-statement