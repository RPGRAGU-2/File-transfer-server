from functools import wraps
from flask import redirect, url_for, session

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("authenticated"):
            return redirect(url_for("auth.login"))
        return func(*args, **kwargs)
    return wrapper
