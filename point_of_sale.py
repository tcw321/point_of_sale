
amount = "$10.50"

def on_barcode(barcode):
    global amount
    if barcode == "":
        amount = "invalid"

def last_text_displayed():
    return amount