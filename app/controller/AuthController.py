from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.decorators.auth_jwt_decorator import *
from app.entities.user import *
from app.services.userService import *
from app.config.ReplacementConfig import *
import bcrypt
import datetime

auth_API = Blueprint('AuthController', __name__, url_prefix='/auth')

user_service = userService()

@auth_API.route("/user/register", methods=["POST"])
def user_register():
    req = request.get_json()
    return register(req,JWT.ROLE_USER)

@auth_API.route("/admin/register", methods=["POST"])
def admin_register():
    req = request.get_json()
    return register(req,JWT.ROLE_ADMIN)

@auth_API.route('/login', methods=['POST'])
def login():
    try:
        req = request.get_json()
        user = user_login_init(req)
        return user_service.login_check(user)
    except Exception as e:
        print(e)
        return f"{e}"

@auth_API.route("/protected", methods=["GET"])
@role_user_admin()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@auth_API.route("/admin", methods=["GET"])    
@role_admin()  
def admin_test():
    current_user = get_jwt_identity()    
    return jsonify(logged_in_as=current_user), 200

@auth_API.route("/user", methods=["GET"])
@role_user()   
def user_test():
    current_user = get_jwt_identity()  
    return jsonify(logged_in_as=current_user), 200

@auth_API.route("/test1", methods=["GET"])
@jwt_required()                         # jwt check
@role(JWT.CLAIMS_ROLE,JWT.ROLE_USER)    # role : role check
def user_test1():
    current_user = get_jwt_identity()  
    return jsonify(logged_in_as=current_user), 200


################################################### FUNCTION ###################################################
def register(req,role):
    try:
        user = user_register_init(req,role)
        return user_service.user_register(user)
    except Exception as e:
        print(e)
        return f"{e}"

################################################### TEST ###################################################


    