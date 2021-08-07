from functools import wraps
from flask_jwt_extended import ( verify_jwt_in_request, jwt_required,  get_jwt_identity, get_jwt)
from app.config.AppConfig import *



def role_admin():
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims[JWT.CLAIMS_ROLE] == JWT.ROLE_ADMIN:
                # print("ADMIN")
                return fn(*args, **kwargs)
            else:
                # print("NOT ADMIN")
                return jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper

def role_user():
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims[JWT.CLAIMS_ROLE] == JWT.ROLE_USER:
                # print("USER")
                return fn(*args, **kwargs)
            else:
                # print("NOT USER")
                return jsonify(msg="Users only!"), 403

        return decorator
    return wrapper

def role_user_admin():
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims[JWT.CLAIMS_ROLE] == JWT.ROLE_USER or claims[JWT.CLAIMS_ROLE] == JWT.ROLE_ADMIN:
                # print("role_user_admin")
                return fn(*args, **kwargs)
            else:
                # print("NOT role_user_admin")
                return jsonify(msg="Users and Admin only!"), 403

        return decorator
    return wrapper

def role(role_key,role_type):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims[role_key] == role_type:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="role only!"), 403

        return decorator
    return wrapper