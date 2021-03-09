from quick_sort import __version__
from quick_sort.quick_sort import quick_sort, test_with_negative, testing_list


def test_version():
    assert __version__ == '0.1.0'


# ******************** HAPPY PATH ********************
def test_can_successfully_sort_an_unsorted_list():
    expected = [4, 8, 15, 16, 23]
    actual = quick_sort(testing_list)
    assert expected == testing_list

# ******************** EDGE CASE ********************
def test_can_successfully_sort_a_list_with_negative_nubmers():
    expected = [-16, 4, 8, 15, 23]
    actual = quick_sort(test_with_negative)
    assert expected == test_with_negative

# ******************** EXPECTED FAIL ********************
def test_will_fail_when_passed_letters():
    expected = "Error"
    actual = quick_sort(["a", "z", "g", "w", "y", "s", "t"])
    assert expected == actual