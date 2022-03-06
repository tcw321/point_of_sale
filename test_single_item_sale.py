import pytest
from point_of_sale import *

@pytest.fixture
def pricesByBarcode():
    return {"12345": "$10.50", "54321": "$8.64"}

@pytest.fixture
def my_point_of_sale(pricesByBarcode):
    display = Display();
    return SalesSystem(pricesByBarcode, display)

def test_valid_barcode_displays_valid_amount(my_point_of_sale, pricesByBarcode):
    for k in pricesByBarcode:
      my_point_of_sale.on_barcode(k+"\n")
      assert my_point_of_sale.last_text_displayed() == pricesByBarcode[k]

def test_valid_barcode_with_no_price(my_point_of_sale):
    my_point_of_sale.on_barcode("9999\n")
    assert my_point_of_sale.last_text_displayed() == "No price found"