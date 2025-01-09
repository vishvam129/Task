# cart.py: Add a function add_to_cart(item, quantity).
cart = {}
products = {"Milk":33,"Bread":50,"Tiktoc":20,"Kitkat":10,"ice":30,"Mouse":799,"Watch":2900}
def add_to_cart(item,quantity):
    if item in products:
        cart[item] = quantity * products[item]
    else:
        raise Exception("Enter available product")