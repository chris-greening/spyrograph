import pytest

from tests._trochoid import _TestGeneral
from spyrograph.hypotrochoid.hypotrochoid import Hypotrochoid
from spyrograph.epitrochoid.epitrochoid import Epitrochoid

class TestHypotrochoid(_TestGeneral):
    class_name = Hypotrochoid

    def test_circle_offset(self, instance):
        assert instance._circle_offset() == 100

class TestEpitrochoid(_TestGeneral):
    class_name = Epitrochoid

    def test_circle_offset(self, instance):
        assert instance._circle_offset() == 500
