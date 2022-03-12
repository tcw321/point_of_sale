
class Display:

    def __init__(self):
        self.text = ""

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def invalidState(self):
        self.text = "invalid"

    def notFoundState(self):
        self.text = "No price found"

    def setCurrentPrice(self, price):
        self.text = price

    def setTotal(self, totalPrice):
        self.text = totalPrice

class SalesSystem:
    def __init__(self, pricesByBarcode, display):
        self.pricesByBarcode = pricesByBarcode
        self.display = display
        self.item_prices = []

    def on_barcode(self, barcode, pricesByBarcode={}):
        if barcode != "" and barcode[-1] != "\n":
            self.display.invalidState()
        else:
            try:
                barcode_value = int(barcode)
                try:
                    self.item_prices.append(self.pricesByBarcode[str(barcode_value)])
                    self.display.setText(self.pricesByBarcode[str(barcode_value)])
                    self.display.setCurrentPrice(self.pricesByBarcode[str(barcode_value)])
                except:
                    self.display.notFoundState()
            except:
                self.display.invalidState()

    def total(self):
        if self.display.getText() == "":
            self.display.setText("No items scanned")
        elif self.display.getText() == "No price found":
            self.display.setText("No price found")
        else:
            sum = 0
            for x in self.item_prices:
                sum += x
            self.display.setTotal("Total: ${}".format(sum))
