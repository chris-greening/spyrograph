import pytest

from tests._roulette import _TestGeneral, _TestSpecial
from spyrograph.epitrochoid.epitrochoid import Epitrochoid
from spyrograph.epitrochoid.epicycloid import Epicycloid

class TestEpitrochoid(_TestGeneral):
    class_name = Epitrochoid

class TestEpicycloid(_TestSpecial, TestEpitrochoid):
    class_name = Epicycloid
