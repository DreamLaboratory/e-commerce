def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()  # TTL = Time to Live
    return cart
