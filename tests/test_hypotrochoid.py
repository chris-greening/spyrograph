import numpy as np
import pytest

from tests._roulette import _TestGeneral, _TestSpecial
from spyrograph.hypotrochoid.hypotrochoid import Hypotrochoid
from spyrograph.hypotrochoid.hypocycloid import Hypocycloid

class TestHypotrochoid(_TestGeneral):
    class_name = Hypotrochoid

    def test_circle_offset(self, instance):
        assert instance._circle_offset() == 100

class TestHypocycloid(_TestSpecial, TestHypotrochoid):
    class_name = Hypocycloid
