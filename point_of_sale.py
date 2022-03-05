

def on_barcode(barcode):
    global amount
    if barcode != "" and barcode[-1] != "\n":
        amount = "invalid"
    else:
        try:
            barcode_value = int(barcode)
            if barcode_value == 12345:
               amount = "$10.50"
            elif barcode_value == 54321:
               amount = "$8.64"
            else:
               amount = "No price found"
        except:
            amount = "invalid"

def last_text_displayed():
    return amount