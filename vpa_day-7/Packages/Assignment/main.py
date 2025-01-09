from ecommerce import cart,checkout
while True:
    print("Welcome to the Shopping ")
    print("1: purchase")
    print("2: see cart")
    print("3: Remove product from cart")
    print("4: go to Checkout")
    print("5: Payment ")
    
    user_input = int(input("Enter choise :- "))
    
    if (user_input == 1):
        print("available products is")
        for i in cart.products:
            print(f"{i}  --------->   {cart.products[i]}")
        item = input("Enter product and quantity with space (ex: Milk 2) ").split()
        cart.add_to_cart(item[0],int(item[1]))
    
    if(user_input == 2):
        print("-------------your_cart------------")
        for i in cart.cart:
            print(f"{i}       :-  {cart.cart[i]}")
        
    if(user_input == 3):
        item=input("Enter Product name to remove :- ")
        del cart.cart[item]
        print("-------------your_cart------------")
        for i in cart.cart:
            print(f"{i}       :-  {cart.cart[i]}")
        
    if(user_input == 4):
        print("-------------invoice------------")
        checkout.bill()
        print(f"Total Amount     :- {checkout.total}")
    if(user_input == 5):
        print("Payment methods ")
        print("1: cash ")
        print("2: card ")
        
        user_pay = int(input("Enter your choise :- "))
        
        if(user_pay == 1):
            print("Thanks for purchase")
            break
        if(user_pay == 2):
            print("Thanks for purchase")
            break
    