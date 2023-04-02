def test_set_int_to_list(self):
    """Test that setting int to list"""
    num_test = self.class_name._set_int_to_list(1)
    list_test = self.class_name._set_int_to_list([2])
    assert isinstance(num_test, list)
    assert isinstance(list_test, list)
    assert num_test[0] == 1
    assert list_test[0] == 2