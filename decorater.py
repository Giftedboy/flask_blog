from flask import redirect, request, url_for, session
from functools import wraps
import random

# 登陆限制装饰器

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('hahaha'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('manager.login'))
    return wrapper


# 已登陆认证
def already_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('hahaha'):
            return redirect(url_for('manager.index'))
        else:
            return func(*args, **kwargs)

    return wrapper
