import pytest

from spyrograph.core._misc import (
    _set_int_to_list,
    _get_products_of_inputs,
    _validate_only_one_iterable,
    _validate_theta
)

def test_set_int_to_list():
    num_test = _set_int_to_list(1)
    list_test = _set_int_to_list([2])
    assert isinstance(num_test, list)
    assert isinstance(list_test, list)
    assert num_test[0] == 1
    assert list_test[0] == 2

def test_get_products_of_inputs():
    return_vals = _get_products_of_inputs(3, [1,2,3], 5)
    assert return_vals[0] == (3, 1, 5)
    assert return_vals[2] == (3, 3, 5)

def test_validate_only_one_iterable():
    with pytest.raises(ValueError):
        _validate_only_one_iterable(1,2,[1,2], [2,3])

def test_validate_theta_multiple_thetas_exception_raise():
    with pytest.raises(ValueError, match="Multiple definitions of theta were passed in as argument which is ambiguous - please define only one set of theta values."):
        _validate_theta(thetas=[1,2,3], theta_start=1, theta_stop=3, theta_step=.1)

def test_validate_theta_empty_list_exception_raise():
    with pytest.raises(ValueError, match="An empty list of thetas was passed in as argument."):
        _validate_theta(thetas=[], theta_start = None, theta_stop = None, theta_step = None)