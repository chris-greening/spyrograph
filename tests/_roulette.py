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

    @pytest.mark.parametrize("R, r, d", [
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, -1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ])
    def test_invalid_arguments_exception(self, R, r, d, thetas):
        with pytest.raises(ValueError, match="Negative and/or zero input parameters were passed. Please only pass positive values"):
            self.class_name(
                R=R,
                r=r,
                d=d,
                thetas=thetas
            )

    def test_dunder_repr_doesnt_break_on_repr_call(self, instance):
        repr_val = repr(instance)
        assert isinstance(repr_val, str)

    def test_transform_shape(self, instance):
        left_transformed_instance = instance.transform(x=-100)
        up_transformed_instance = instance.transform(y=100)
        up_and_left_transform_instance = instance.transform(x=100, y=-100)
        assert instance.origin[0] - 100 == left_transformed_instance.origin[0]
        assert instance.origin[1] + 100 == up_transformed_instance.origin[1]
        assert instance.origin[0] + 100 == up_and_left_transform_instance.origin[0]
        assert instance.origin[1] - 100 == up_and_left_transform_instance.origin[1]

    def test_dunder_repr_values(self, instance):
        repr_val = repr(instance)
        assert f"R={instance.R}" in repr_val
        assert f"r={instance.r}" in repr_val
        assert f"d={instance.d}" in repr_val

    def test_scale_return_instance_is_same_class(self, instance):
        """Test that the return instance is from the same class"""
        scaled_instance = instance.scale(factor=2)
        assert scaled_instance.__class__ is instance.__class__

    def test_scale_factor_parameters(self, instance):
        """Test that scaling is actually working as expected"""
        larger_scaled_instance = instance.scale(factor=2)
        smaller_scaled_instance = instance.scale(factor=.5)

        assert larger_scaled_instance.R == instance.R*2
        assert larger_scaled_instance.r == instance.r*2
        assert larger_scaled_instance.d == instance.d*2
        assert (larger_scaled_instance.thetas == instance.thetas).all()

        assert smaller_scaled_instance.R == instance.R*.5
        assert smaller_scaled_instance.r == instance.r*.5
        assert smaller_scaled_instance.d == instance.d*.5
        assert (smaller_scaled_instance.thetas == instance.thetas).all()

    def test_create_range_theta_inputs(self, thetas):
        R = 5
        r = 3
        d = 2
        shapes = self.class_name.create_range(R, r, d, thetas)
        assert shapes[0].R == R
        assert shapes[0].r == r
        assert shapes[0].d == d

    def test_create_range_custom_origin(self, thetas):
        R = 5
        r = 3
        d = 1
        shapes = self.class_name.create_range(R, r, d, thetas, origin=(100, 233))
        assert shapes[0].origin == (100, 233)
        assert shapes[0].origin[0] == 100
        assert shapes[0].origin[1] == 233

    def test_create_range_single_input(self, thetas):
        """Test single input for create range"""
        R = 5
        r = 3
        d = 2
        shapes = self.class_name.create_range(R, r, d, thetas)
        assert len(shapes) == 1
        assert isinstance(shapes[0], self.class_name)

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

    def test_create_range_custom_origin(self, thetas):
        R = 5
        r = 3
        shapes = self.class_name.create_range(R, r, thetas, origin=(100, 233))
        assert shapes[0].origin == (100, 233)
        assert shapes[0].origin[0] == 100
        assert shapes[0].origin[1] == 233

    def test_create_range_single_input(self, thetas):
        """Test single input for create range"""
        R = 5
        r = 3
        shapes = self.class_name.create_range(R, r, thetas)
        assert len(shapes) == 1
        assert isinstance(shapes[0], self.class_name)

    def test_create_range_theta_inputs(self, thetas):
        R = 5
        r = 3
        shapes = self.class_name.create_range(R, r, thetas)
        assert shapes[0].R == R
        assert shapes[0].r == r

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