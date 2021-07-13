from quick_sort import __version__
from quick_sort.quick_sort import quick_sort


def test_version():
    assert __version__ == '0.1.0'


def test_Reverse_sorted():
    assert quick_sort([20,18,12,8,5,-2],0,5)==[-2,5,8,12,18,20]

def test_few_uniques():
    assert quick_sort([5,12,7,5,5,7],0,5)==[5,5,5,7,7,12]

def test_nearly_sorted():
    assert quick_sort([2,3,5,7,13,11],0,5)==[2,3,5,7,11,13]