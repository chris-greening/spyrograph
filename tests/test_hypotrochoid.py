import numpy as np
import pytest

from spyrograph.hypotrochoid.hypotrochoid import Hypotrochoid
from spyrograph.hypotrochoid.hypocycloid import Hypocycloid
from spyrograph.hypotrochoid.deltoid import Deltoid
from spyrograph.hypotrochoid.astroid import Astroid
from spyrograph.hypotrochoid.ellipse import Ellipse
from spyrograph.hypotrochoid.tusi_couple import TusiCouple

@pytest.fixture()
def thetas() -> "np.array":
    """Return a numpy array of theta values"""
    return np.arange(0, np.pi*2, .1)

@pytest.fixture()
def hypotrochoid_obj(thetas: "np.array") -> "hypotrochoid.Hypotrochoid":
    """Return an instantiated hypotrochoid for testing"""
    return Hypotrochoid(
        R=300,
        r=200,
        d=100,
        thetas=thetas
    )

def test_multiple_thetas_exception(thetas: "np.array") -> None:
    """Test that passing multiple definitions of setting theta raises a ValueError"""
    with pytest.raises(ValueError):
        hypotrochoid_obj = Hypotrochoid(
            R = 300,
            r = 200,
            d = 100,
            thetas=thetas,
            theta_start=1,
            theta_stop=10,
            theta_step=1
        )
