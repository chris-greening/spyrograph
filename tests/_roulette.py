import pytest

import numpy as np
import pandas as pd

class _TestGeneral:
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
            d = 100,
            thetas=thetas
        )

    def test_set_int_to_list(self):
        """Test that setting int to list"""
        num_test = self.class_name._set_int_to_list(1)
        list_test = self.class_name._set_int_to_list([2])
        assert isinstance(num_test, list)
        assert isinstance(list_test, list)
        assert num_test[0] == 1
        assert list_test[0] == 2

    def test_create_range_multiple_arguments_exception(self, thetas):
        """Test that passing multiple parameters raises an error"""
        with pytest.raises(ValueError):
            arr = self.class_name.create_range(
                R=list(range(10)),
                r=list(range(10)),
                d=10,
                thetas=thetas
            )

    def test_custom_origin_offsets(self, thetas):
        """Test custom origin offsets"""
        base_obj = self.class_name(
            R = 300,
            r = 200,
            d = 100,
            thetas=thetas
        )
        custom_origin_obj = self.class_name(
            R = 300,
            r = 200,
            d = 100,
            thetas=thetas,
            origin = (54, -233)
        )
        assert ((custom_origin_obj.x - base_obj.x).round() == 54.0).all()
        assert ((custom_origin_obj.y - base_obj.y).round() == -233.0).all()

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

    def test_coords(self, instance) -> None:
        """Test that coordinates attribute matches x, y, and theta values"""
        assert instance.coords[0] == (instance.x[0], instance.y[0], instance.thetas[0])
        assert instance.coords[-1] == (instance.x[-1], instance.y[-1], instance.thetas[-1])

    def test_dataframe_property(self, instance) -> None:
        """Test that DataFrame property is working as expected"""
        assert isinstance(instance.df, pd.DataFrame)
        assert list(instance.df.columns) == ["x", "y", "theta"]
        assert all(instance.df["x"].to_numpy() == instance.x)
        assert all(instance.df["y"].to_numpy() == instance.y)
        assert all(instance.df["theta"].to_numpy() == instance.thetas)

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

    def test_create_range_multiple_arguments_exception(self, thetas):
        """Test that passing multiple parameters raises an error"""
        with pytest.raises(ValueError):
            arr = self.class_name.create_range(
                R=list(range(10)),
                r=list(range(10)),
                thetas=thetas
            )

    def test_custom_origin_offsets(self, thetas):
        """Test custom origin offsets vertically"""
        base_obj = self.class_name(
            R = 300,
            r = 200,
            thetas=thetas
        )
        custom_origin_obj = self.class_name(
            R = 300,
            r = 200,
            thetas=thetas,
            origin = (54, -233)
        )
        assert ((custom_origin_obj.x - base_obj.x).round() == 54).all()
        assert ((custom_origin_obj.y - base_obj.y).round() == -233).all()

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