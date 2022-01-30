import pytest
from point_of_sale import *

def test_valid_input():
    on_barcode("12345\n")
    assert last_text_displayed() == "$10.50"

def test_invalid_input_blank_string():
    on_barcode("")
    assert last_text_displayed() == "invalid"
