

def on_barcode(barcode):
    global amount
    amount = "$10.50"
    if barcode == "" or barcode == "junk":
        amount = "invalid"

def last_text_displayed():
    return amount