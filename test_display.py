import pytest
from point_of_sale import *

def test_display_of_two_trailing_zeroes():
    display = Display()
    display.setTotal(2)
    assert display.view() == "Total: $2.00"

def test_display_of_single_trailing_zero():
    display = Display()
    display.setTotal(2.2)
    assert display.view() == "Total: $2.20"