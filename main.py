from pyscript import display, document

prices = {
    "chicken pops": 60,
    "cheese sticks": 40,
    "spam musubi": 60,
    "mango float": 20,
    "blueberry": 20,
    "magnum": 25,
}

def Order(event):

     subtotal = 0
     receipt_lines = []

     for food_id, price in price.items():
        checkbox = document.getElementById(food_id)
     if chackbox.checked:
        label_text = document.querySelector(f'label[for="{food_id}"]').innerText
        receipt_lines.appened(f"{label_text} - {price}pesos")
        subtotal += price

    vat = subtotal * 0.12
    total = subtotal + vat

    receipt_html = "<br>".join(receipt_lines) if receipt_lines else "No items chosen"

    display(receipt_html, target="receipt", append=False) 
    display(f"Subtotal: {subtotal:.2f} pesos", target="Subtotal", append=False)
    display(f"VATl: {vat:.2f}", target="VAT", append=False)
    display(f"Total Amount: {total:.2f} pesos", target="Total Amount", append=False)



   