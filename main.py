from pyscript import display, document


def SKU_generator(e):
    # Clear previous output
    document.getElementById("sku_output").innerHTML = ""

    # Get input values
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("quantity").value

    # Generate SKEW/SKU
    sku = (
        category[:3].upper()
        + "-"
        + product_name[:4].upper()
        + "-"
        + str(stock_qty)
    )

    # Display generated SKU/SKEW
    display("SKU: " + sku, target="sku_output")


def create_order(e):
    # Get menu items
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    # Calculate total by multiplying value by checked status (1 or 0)
    # Calculate subtotal, tax, and total

    subtotal = (
        float(prod1.value) * prod1.checked
        + float(prod2.value) * prod2.checked
        + float(prod3.value) * prod3.checked
        + float(prod4.value) * prod4.checked
        + float(prod5.value) * prod5.checked
    )

    # 12% VAT, no need for excise tax. too complicated
    tax_rate = 0.12
    tax = subtotal * tax_rate

    # Calculate total amount
    total = subtotal + tax

    # Create receipt
    receipt = f"""
    <h3> 𓏲⤷ ゛Receipt ⋆˚꩜｡ˎˊ˗</h3>

    <p>Subtotal: ₱{subtotal:.2f}</p>

    <p>VAT: ₱{tax:.2f}</p>

    <p><strong>Total Amount: ₱{total:.2f}</strong></p>
    """

    # Display receipt
    document.getElementById("show").innerHTML = receipt

    