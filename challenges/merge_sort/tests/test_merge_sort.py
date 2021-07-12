from merge_sort import __version__
from merge_sort.merge_sort import merge_sort


def test_version():
    assert __version__ == '0.1.0'

def test_Reverse_sorted():
    assert merge_sort([20,18,12,8,5,-2])==[-2,5,8,12,18,20]

def test_few_uniques():
    assert merge_sort([5,12,7,5,5,7])==[5,5,5,7,7,12]

def test_nearly_sorted():
    assert merge_sort([2,3,5,7,13,11])==[2,3,5,7,11,13]