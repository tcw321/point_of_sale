import pytest
from point_of_sale import *

def test_valid_input():
    on_barcode("12345\n")
    assert last_text_displayed() == "$10.50"

