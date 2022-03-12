import pytest
from point_of_sale import *

@pytest.fixture
def pricesByBarcode():
    return {"12345": "$10.50", "54321": "$8.64"}

@pytest.fixture
def my_display():
    return Display();

@pytest.fixture
def my_point_of_sale(pricesByBarcode, my_display):
    return SalesSystem(pricesByBarcode, my_display)

def test_purchase_one_item(my_point_of_sale, pricesByBarcode, my_display):
    my_point_of_sale.on_barcode("12345\n")
    my_point_of_sale.total()
    assert my_display.displayText() == "Total: $10.50"

def test_purchase_another_one_item(my_point_of_sale, pricesByBarcode, my_display):
    my_point_of_sale.on_barcode("54321\n")
    my_point_of_sale.total()
    assert my_display.displayText() == "Total: $8.64"