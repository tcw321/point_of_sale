
class Display:

    def setText(self, text):
        self.text = text

    def text(self):
        return self.text

class SalesSystem:
    def __init__(self, pricesByBarcode, display):
        self.pricesByBarcode = pricesByBarcode
        self.display2 = display

    def on_barcode(self, barcode, pricesByBarcode={}):
        global display
        if barcode != "" and barcode[-1] != "\n":
            display = "invalid"
        else:
            try:
                barcode_value = int(barcode)
                try:
                    display = self.pricesByBarcode[str(barcode_value)]
                except:
                    display = "No price found"
            except:
                display = "invalid"

    def display(self):
        return display

