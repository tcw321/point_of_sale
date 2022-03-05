

class SalesSystem:
    pass

def on_barcode(barcode, catalog={}):
    global display
    if barcode != "" and barcode[-1] != "\n":
        display = "invalid"
    else:
        try:
            barcode_value = int(barcode)
            try:
               display = catalog[str(barcode_value)]
            except:
               display = "No price found"
        except:
            display = "invalid"

def last_text_displayed():
    return display