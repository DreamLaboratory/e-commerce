def _cart_id(request):
    cart = request.session.session_key
    print("-0----", cart)
    if not cart:

        cart = request.session.create()
        print(cart)
    print("----c", cart)
    return cart
