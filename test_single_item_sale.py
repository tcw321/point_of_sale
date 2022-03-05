import pytest
from point_of_sale import *

@pytest.fixture
def pricesByBarcode():
    return {"12345": "$10.50", "54321": "$8.64"}

@pytest.fixture
def my_point_of_sale(pricesByBarcode):
    return SalesSystem(pricesByBarcode)

def test_valid_barcode_displays_valid_amount(pricesByBarcode):
    on_barcode("12345\n", pricesByBarcode)
    assert last_text_displayed() == "$10.50"

def test_second_valid_barcode_displays_valid_amount(pricesByBarcode):
    on_barcode("54321\n", pricesByBarcode)
    assert last_text_displayed() == "$8.64"

def test_valid_barcode_with_no_price():
    on_barcode("9999\n")
    assert last_text_displayed() == "No price found"