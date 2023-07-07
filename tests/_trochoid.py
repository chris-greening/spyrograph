import pytest

import numpy as np
import pandas as pd

from spyrograph.core._trochoid import _Trochoid
from spyrograph.core._cycloid import _Cycloid

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

    def test_translate_float_offset(self, instance):
        up_and_left_translate_instance = instance.translate(x=100.33, y=-100.69)
        assert instance.origin[0] + 100.33 == up_and_left_translate_instance.origin[0]
        assert instance.origin[1] - 100.69 == up_and_left_translate_instance.origin[1]

    def test_translate_zero_offset(self, instance):
        zero_translateed_instance = instance.translate(x=0, y=0)
        assert instance.origin[0] == zero_translateed_instance.origin[0]
        assert instance.origin[1] == zero_translateed_instance.origin[1]

    def test_translate_shape_x_direction(self, instance):
        left_translateed_instance = instance.translate(x=-100)
        assert instance.origin[0] - 100 == left_translateed_instance.origin[0]

    def test_translate_shape_y_direction(self, instance):
        up_translateed_instance = instance.translate(y=100)
        assert instance.origin[1] + 100 == up_translateed_instance.origin[1]

    def test_translate_shape_x_and_y_same_translate_call(self, instance):
        up_and_left_translate_instance = instance.translate(x=100, y=-100)
        assert instance.origin[0] + 100 == up_and_left_translate_instance.origin[0]
        assert instance.origin[1] - 100 == up_and_left_translate_instance.origin[1]

    def test_dunder_repr_values(self, instance):
        repr_val = repr(instance)
        assert f"R={instance.R}" in repr_val
        assert f"r={instance.r}" in repr_val
        assert f"d={instance.d}" in repr_val

    def test_add_noise_return_instance_is_same_class(self, instance):
        """Test that the return instance is from the same class"""
        noisy_instance = instance.add_noise(x_scale=2, y_scale=2)
        assert noisy_instance.__class__ is instance.__class__

    def test_scale_return_instance_is_same_class(self, instance):
        """Test that the return instance is from the same class"""
        scaled_instance = instance.scale(factor=2)
        assert scaled_instance.__class__ is instance.__class__

    # @pytest.mark.parametrize("factor", [(-1, 0, 0.0)])
    def test_scale_invalid_values_raises_exception(self, instance):
        with pytest.raises(ValueError):
            instance.scale(-1)
            instance.scale(0)
            instance.scale(0.0)

    def test_scale_factor_parameters_larger(self, instance):
        larger_scaled_instance = instance.scale(factor=2)
        assert larger_scaled_instance.R == instance.R*2
        assert larger_scaled_instance.r == instance.r*2
        assert larger_scaled_instance.d == instance.d*2
        assert (larger_scaled_instance.thetas == instance.thetas).all()

    def test_scale_factor_parameters_smaller(self, instance):
        """Test that scaling is actually working as expected"""
        smaller_scaled_instance = instance.scale(factor=.5)
        assert smaller_scaled_instance.R == instance.R*.5
        assert smaller_scaled_instance.r == instance.r*.5
        assert smaller_scaled_instance.d == instance.d*.5
        assert (smaller_scaled_instance.thetas == instance.thetas).all()

    def test_add_noise_origin_is_preserved(self, thetas):
        if issubclass(self.class_name, _Cycloid):
            shape = self.class_name(
                R=100,
                r=200,
                thetas=thetas,
                origin=(100,100)
            )
        elif issubclass(self.class_name, _Trochoid):
            shape = self.class_name(
                R=100,
                r=200,
                d=300,
                thetas=thetas,
                origin=(100, 100)
            )
        noisy_shape = shape.add_noise(x_scale=10, y_scale=10)
        assert noisy_shape.origin == shape.origin

    def test_scale_origin_is_preserved(self, thetas):
        if issubclass(self.class_name, _Cycloid):
            shape = self.class_name(
                R=100,
                r=200,
                thetas=thetas,
                origin=(100,100)
            )
        elif issubclass(self.class_name, _Trochoid):
            shape = self.class_name(
                R=100,
                r=200,
                d=300,
                thetas=thetas,
                origin=(100, 100)
            )
        scaled_shape = shape.scale(2)
        assert scaled_shape.origin == shape.origin

    def test_rotate_origin_is_preserved(self, thetas):
        if issubclass(self.class_name, _Cycloid):
            shape = self.class_name(
                R=100,
                r=200,
                thetas=thetas,
                origin=(100, 100)
            )
        elif issubclass(self.class_name, _Trochoid):
            shape = self.class_name(
                R=100,
                r=200,
                d=300,
                thetas=thetas,
                origin=(100, 100)
            )
        rotated_shape = shape.rotate(2)
        assert rotated_shape.origin == shape.origin

    def test_create_range_theta_inputs(self, thetas):
        R = 5
        r = 3
        d = 2
        if issubclass(self.class_name, _Cycloid):
            shapes = self.class_name.create_range(R, r, thetas)
        elif issubclass(self.class_name, _Trochoid):
            shapes = self.class_name.create_range(R, r, d, thetas)
            assert shapes[0].d == d
        assert shapes[0].R == R
        assert shapes[0].r == r

    def test_empty_theta_exception_raise_for_thetas_arg(self):
        with pytest.raises(ValueError, match="An empty list of thetas was passed in as argument."):
            if issubclass(self.class_name, _Cycloid):
                instance = self.class_name(
                    R=300,
                    r=200,
                    thetas=[]
                )
            elif issubclass(self.class_name, _Trochoid):
                instance = self.class_name(
                    R=300,
                    r=200,
                    d=100,
                    thetas=[]
                )

    def test_create_range_custom_origin(self, thetas):
        R = 5
        r = 3
        d = 1
        if issubclass(self.class_name, _Cycloid):
            shapes = self.class_name.create_range(R, r, thetas, origin=(100, 233))
        elif issubclass(self.class_name, _Trochoid):
            shapes = self.class_name.create_range(R, r, d, thetas, origin=(100, 233))
        assert shapes[0].origin == (100, 233)
        assert shapes[0].origin[0] == 100
        assert shapes[0].origin[1] == 233

    def test_create_range_single_input(self, thetas):
        """Test single input for create range"""
        R = 5
        r = 3
        d = 2
        if issubclass(self.class_name, _Cycloid):
            shapes = self.class_name.create_range(R, r, thetas)
        elif issubclass(self.class_name, _Trochoid):
            shapes = self.class_name.create_range(R, r, d, thetas)
        assert len(shapes) == 1
        assert isinstance(shapes[0], self.class_name)

    def test_create_range_multiple_arguments_exception(self, thetas):
        """Test that passing multiple parameters raises an error"""
        with pytest.raises(ValueError):
            if issubclass(self.class_name, _Cycloid):
                arr = self.class_name.create_range(
                    R=list(range(10)),
                    r=list(range(10)),
                    thetas=thetas
                )
            elif issubclass(self.class_name, _Trochoid):
                arr = self.class_name.create_range(
                    R=list(range(10)),
                    r=list(range(10)),
                    d=10,
                    thetas=thetas
                )

    def test_custom_origin_offsets(self, thetas):
        """Test custom origin offsets"""
        if issubclass(self.class_name, _Cycloid):
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
        elif issubclass(self.class_name, _Trochoid):
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
        if issubclass(self.class_name, _Cycloid):
            obj = self.class_name(
                R = 300,
                r = 200,
                theta_start=1,
                theta_stop=10,
                theta_step=1
            )
        elif issubclass(self.class_name, _Trochoid):
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
        if issubclass(self.class_name, _Cycloid):
            obj = self.class_name(
                R = 300,
                r = 200,
                theta_start=0,
                theta_stop=1
            )
        elif issubclass(self.class_name, _Trochoid):
            obj = self.class_name(
                R = 300,
                r = 200,
                d = 100,
                theta_start=0,
                theta_stop=1
            )
        assert (obj.thetas[1] - obj.thetas[0]) == .1

    def test_multiple_thetas_exception(self, thetas: "np.array") -> None:
        """Test that passing multiple definitions of setting theta raises a ValueError"""
        with pytest.raises(ValueError):
            if issubclass(self.class_name, _Cycloid):
                obj = self.class_name(
                    R = 300,
                    r = 200,
                    thetas=thetas,
                    theta_start=1,
                    theta_stop=10,
                    theta_step=1
                )
            elif issubclass(self.class_name, _Trochoid):
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

    def test_rotate_orientation(self, instance) -> None:
        rotated_shape = instance.rotate(.1)
        assert instance.orientation == 0
        assert rotated_shape.orientation == .1

    def test_parameters_are_preserved(self, instance) -> None:
        rotated_shape = instance.rotate(1)
        assert instance.R == rotated_shape.R
        assert instance.r == rotated_shape.r

    def test_is_closed(self) -> None:
        if issubclass(self.class_name, _Cycloid):
            open_shape = self.class_name(
                R=312,
                r=150,
                theta_start=0,
                theta_stop=80,
                theta_step=.1
            )
            closed_shape = self.class_name(
                R=312,
                r=150,
                theta_start=0,
                theta_stop=157.1,
                theta_step=.1
            )
        elif issubclass(self.class_name, _Trochoid):
            open_shape = self.class_name(
                R=312,
                r=150,
                d=75,
                theta_start = 0,
                theta_stop = 90,
                theta_step = .1
            )
            closed_shape = self.class_name(
                R=312,
                r=150,
                d=75,
                theta_start = 0,
                theta_stop = 157.2,
                theta_step = .1
            )
        assert not open_shape.is_closed()
        assert closed_shape.is_closed()
