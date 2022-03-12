
class Display:

    def __init__(self):
        self.text = ""

    def setText(self, text):
        self.text = text

    def displayText(self):
        return self.text

class SalesSystem:
    def __init__(self, pricesByBarcode, display):
        self.pricesByBarcode = pricesByBarcode
        self.display = display

    def on_barcode(self, barcode, pricesByBarcode={}):
        if barcode != "" and barcode[-1] != "\n":
            self.display.setText("invalid")
        else:
            try:
                barcode_value = int(barcode)
                try:
                    self.display.setText(self.pricesByBarcode[str(barcode_value)])
                except:
                    self.display.setText("No price found")
            except:
                self.display.setText("invalid")

    def total(self):
        self.display.setText("Total: " + self.display.displayText())
