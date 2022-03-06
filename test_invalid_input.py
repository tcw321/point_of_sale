import pytest
from point_of_sale import *

@pytest.fixture
def my_display():
    return Display();

@pytest.fixture
def my_point_of_sale(my_display):
    return SalesSystem({}, my_display)

def test_invalid_input_blank_string(my_point_of_sale):
    my_point_of_sale.on_barcode("")
    assert my_point_of_sale.last_text_displayed() == "invalid"

def test_input_non_number_characters(my_point_of_sale):
    my_point_of_sale.on_barcode("junk")
    assert my_point_of_sale.last_text_displayed() == "invalid"

def test_string_with_trailing_space_invalid_input(my_point_of_sale):
    my_point_of_sale.on_barcode("54321 ")
    assert my_point_of_sale.last_text_displayed() == "invalid"

def test_string_with_trailing_tab_invalid_input(my_point_of_sale):
    my_point_of_sale.on_barcode("34235\t")
    assert my_point_of_sale.last_text_displayed() == "invalid"
