from ecommerce import cart
total = 0
def bill():
    for i in cart.cart:
        print(f"{i}       :-  {cart.cart[i]}")
    global total
    total = sum(cart.cart.values())
bill()