import numpy as np
import pytest

from tests._cycloid import _TestSpecial
from tests.test_trochoid import TestHypotrochoid, TestEpitrochoid
from spyrograph.hypotrochoid.hypocycloid import Hypocycloid
from spyrograph.epitrochoid.epicycloid import Epicycloid

class TestHypocycloid(_TestSpecial, TestHypotrochoid):
    class_name = Hypocycloid

class TestEpicycloid(_TestSpecial, TestEpitrochoid):
    class_name = Epicycloid