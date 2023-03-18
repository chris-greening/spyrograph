import pytest

import numpy as np

class _TestGeneral:
    @pytest.fixture()
    def thetas(self) -> "np.array":
        """Return a numpy array of theta values"""
        return np.arange(0, np.pi*2, .1)

    def test_theta_range(self) -> None:
        """Test that passing theta start, stop, step creates an expected list of theta values"""
        obj = self.class_name(
            R = 300,
            r = 200,
            d = 100,
            theta_start=1,
            theta_stop=10,
            theta_step=1
        )
        assert all(obj.thetas == np.arange(1,10,1))

    def test_theta_range_default_step(self) -> None:
        """Test that passing theta start, stop, step creates an expected list of theta values"""
        obj = self.class_name(
            R = 300,
            r = 200,
            d = 100,
            theta_start=0,
            theta_stop=1
        )

    def test_multiple_thetas_exception(self, thetas: "np.array") -> None:
        """Test that passing multiple definitions of setting theta raises a ValueError"""
        with pytest.raises(ValueError):
            obj = self.class_name(
                R = 300,
                r = 200,
                d = 100,
                thetas=thetas,
                theta_start=1,
                theta_stop=10,
                theta_step=1
            )

class _TestSpecial:
    @pytest.fixture()
    def thetas(self) -> "np.array":
        """Return a numpy array of theta values"""
        return np.arange(0, np.pi*2, .1)

    def test_theta_range(self) -> None:
        """Test that passing theta start, stop, step creates an expected list of theta values"""
        obj = self.class_name(
            R = 300,
            r = 200,
            theta_start=1,
            theta_stop=10,
            theta_step=1
        )
        assert all(obj.thetas == np.arange(1,10,1))

    def test_theta_range_default_step(self) -> None:
        """Test that passing theta start, stop, step creates an expected list of theta values"""
        obj = self.class_name(
            R = 300,
            r = 200,
            theta_start=0,
            theta_stop=1
        )

    def test_multiple_thetas_exception(self, thetas: "np.array") -> None:
        """Test that passing multiple definitions of setting theta raises a ValueError"""
        with pytest.raises(ValueError):
            obj = self.class_name(
                R = 300,
                r = 200,
                thetas=thetas,
                theta_start=1,
                theta_stop=10,
                theta_step=1
            )