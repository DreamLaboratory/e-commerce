def _cart_id(request):
    sess= request.session.session_key
    if not sess:
        sess = request.session.create()
    return sess