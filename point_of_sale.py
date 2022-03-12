
class Display:

    def __init__(self):
        self.text = ""

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

class SalesSystem:
    def __init__(self, pricesByBarcode, display):
        self.pricesByBarcode = pricesByBarcode
        self.display = display
        self.item_prices = []

    def on_barcode(self, barcode, pricesByBarcode={}):
        if barcode != "" and barcode[-1] != "\n":
            self.display.setText("invalid")
        else:
            try:
                barcode_value = int(barcode)
                try:
                    self.item_prices.append(self.pricesByBarcode[str(barcode_value)])
                    self.display.setText(self.pricesByBarcode[str(barcode_value)])
                except:
                    self.display.setText("No price found")
            except:
                self.display.setText("invalid")

    def total(self):
        if self.display.getText() == "":
            self.display.setText("No items scanned")
        elif self.display.getText() == "No price found":
            self.display.setText("No known item scanned")
        else:
            sum = 0
            for x in self.item_prices:
                sum += x
            self.display.setText("Total: ${}".format(sum))
