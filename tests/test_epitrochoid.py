import pytest

from tests._roulette import _TestGeneral, _TestSpecial
from spyrograph.epitrochoid.epitrochoid import Epitrochoid
from spyrograph.epitrochoid.epicycloid import Epicycloid

class TestEpitrochoid(_TestGeneral):
    class_name = Epitrochoid

    def test_circle_offset(self, instance):
        assert instance._circle_offset() == 500

class TestEpicycloid(_TestSpecial, TestEpitrochoid):
    class_name = Epicycloid
