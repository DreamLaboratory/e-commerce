def _cart_id(request) -> str:
    cart = request.session.session_key
    print(cart)
    print(type(cart))
    if not cart:
        cart = request.session.create()  # TTL= Time to Live
    return cart