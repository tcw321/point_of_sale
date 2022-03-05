import pytest
from point_of_sale import *

def test_valid_barcode_displays_valid_amount():
    on_barcode("12345\n")
    assert last_text_displayed() == "$10.50"

def test_second_valid_barcode_displays_valid_amount():
    on_barcode("54321\n")
    assert last_text_displayed() == "$8.64"