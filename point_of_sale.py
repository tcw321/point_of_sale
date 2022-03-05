

class SalesSystem:
    def on_barcode(self, barcode, pricesByBarcode={}):
        global display
        if barcode != "" and barcode[-1] != "\n":
            display = "invalid"
        else:
            try:
                barcode_value = int(barcode)
                try:
                    display = pricesByBarcode[str(barcode_value)]
                except:
                    display = "No price found"
            except:
                display = "invalid"

def on_barcode(barcode, pricesByBarcode={}):
    global display
    if barcode != "" and barcode[-1] != "\n":
        display = "invalid"
    else:
        try:
            barcode_value = int(barcode)
            try:
               display = pricesByBarcode[str(barcode_value)]
            except:
               display = "No price found"
        except:
            display = "invalid"

def last_text_displayed():
    return display