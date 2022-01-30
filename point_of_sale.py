

def on_barcode(barcode):
    global amount
    if barcode != "" and barcode[-1] == " ":
        amount = "invalid"
    else:
        try:
            int(barcode)
            amount = "$10.50"
        except:
            amount = "invalid"

def last_text_displayed():
    return amount