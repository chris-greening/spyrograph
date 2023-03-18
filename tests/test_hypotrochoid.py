import numpy as np
import pytest

from tests._roulette import _TestGeneral, _TestSpecial
from spyrograph.hypotrochoid.hypotrochoid import Hypotrochoid
from spyrograph.hypotrochoid.hypocycloid import Hypocycloid

class TestHypotrochoid(_TestGeneral):
    class_name = Hypotrochoid

class TestHypocycloid(_TestSpecial):
    class_name = Hypocycloid
