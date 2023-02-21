def cart_id(request)->str:
    session_key = request.session.session_key
    if session_key is None:
        session_key = request.session.create()
    return session_key
