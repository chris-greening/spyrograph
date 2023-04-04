import pytest

from tests._roulette import _TestGeneral, _TestSpecial
from spyrograph.epitrochoid.epitrochoid import Epitrochoid
from spyrograph.epitrochoid.epicycloid import Epicycloid

class TestHypotrochoid(_TestGeneral):
    class_name = Hypotrochoid

    def test_circle_offset(self, instance):
        assert instance._circle_offset() == 100

class TestEpitrochoid(_TestGeneral):
    class_name = Epitrochoid

    def test_circle_offset(self, instance):
        assert instance._circle_offset() == 500
