import itertools
import collections
from typing import Tuple, List, Union
from numbers import Number

def _get_products_of_inputs(*args) -> Tuple[Number]:
        """Return a list of tuples that contains all of the input arguments"""
        list_of_lists = [_set_int_to_list(el) for el in args]
        product = list(itertools.product(*list_of_lists))
        return product

def _validate_only_one_iterable(*args) -> bool:
    """Return validation check that only one argument passed to create_range is an iterable"""
    inputs = collections.Counter([isinstance(el, collections.abc.Iterable) for el in args])
    if inputs[True] > 1:
        raise ValueError("More than one input variable was varied. Please only pass one list of varying inputs and try again.")

def _set_int_to_list(input_val: Union[Number, List[Number]]) -> List[Number]:
    """Return list of numbers from given input parameter"""
    if isinstance(input_val, Number):
        input_val = [input_val]
    return input_val