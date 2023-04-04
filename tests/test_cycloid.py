import numpy as np
import pytest

from tests._cycloid import _TestSpecial
from spyrograph.hypotrochoid.hypotrochoid import Hypotrochoid
from spyrograph.hypotrochoid.hypocycloid import Hypocycloid

class TestHypocycloid(_TestSpecial, TestHypotrochoid):
    class_name = Hypocycloid

class TestEpicycloid(_TestSpecial, TestEpitrochoid):
    class_name = Epicycloid