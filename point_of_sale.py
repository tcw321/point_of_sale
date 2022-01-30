

def on_barcode(barcode):
    global amount
    if barcode != "" and barcode[-1] != "\n":
        amount = "invalid"
    else:
        try:
            int(barcode)
            amount = "$10.50"
        except:
            amount = "invalid"

def last_text_displayed():
    return amount