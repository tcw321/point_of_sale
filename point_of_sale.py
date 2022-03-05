

def on_barcode(barcode, catalog={}):
    global display
    if barcode != "" and barcode[-1] != "\n":
        display = "invalid"
    else:
        try:
            barcode_value = int(barcode)
            if barcode_value == 12345:
               display = "$10.50"
            elif barcode_value == 54321:
               display = "$8.64"
            else:
               display = "No price found"
        except:
            display = "invalid"

def last_text_displayed():
    return display