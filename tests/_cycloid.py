import pytest

import numpy as np
import pandas as pd

class _TestSpecial:
    # Define this class attr in subclasses
    class_name = None
    @pytest.fixture()
    def thetas(self) -> "np.array":
        """Return a numpy array of theta values"""
        return np.arange(0, np.pi*2, .1)

    @pytest.fixture()
    def instance(self, thetas):
        """Return an instance of the shape"""
        return self.class_name(
            R = 300,
            r = 200,
            thetas=thetas
        )

    @pytest.mark.parametrize("R, r", [
        (-1, 1),
        (1, -1),
        (0, 1),
        (1, 0),
    ])
    def test_invalid_arguments_exception(self, R, r, thetas):
        with pytest.raises(ValueError, match="Negative and/or zero input parameters were passed. Please only pass positive values"):
            self.class_name(
                R=R,
                r=r,
                thetas=thetas
            )

    def test_rolling_radius_equals_distance(self, instance):
        """Test radius of rolling circle is equal to distance"""
        assert instance.r == instance.d

    def test_n_cusps(self, thetas):
        """Test the n cusps factory method"""
        for n in range(2, 5):
            obj = self.class_name.n_cusps(
                R = 300,
                n = n,
                thetas = thetas
            )
            assert obj.r == obj.R/n

    def test_n_cusps_custom_origin(self, thetas):
        """Test that custom origin is working with n cusp classmethod"""
        base_obj = self.class_name.n_cusps(
            R = 300,
            n = 2,
            thetas=thetas
        )
        custom_origin_obj = self.class_name.n_cusps(
            R = 300,
            n = 2,
            thetas=thetas,
            origin = (54, -233)
        )
        assert ((custom_origin_obj.x - base_obj.x).round() == 54.0).all()
        assert ((custom_origin_obj.y - base_obj.y).round() == -233.0).all()
