import pytest

from tests._roulette import _TestGeneral, _TestSpecial
from spyrograph.epitrochoid.epitrochoid import Epitrochoid
from spyrograph.epitrochoid.epicycloid import Epicycloid

class TestHypotrochoid(_TestGeneral):
    class_name = Epitrochoid

class TestHypocycloid(_TestSpecial):
    class_name = Epicycloid
