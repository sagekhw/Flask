from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.entities.user import *
from app.services.userService import *
from app.config.ReplacementConfig import *
from datetime import *


user_API = Blueprint('UserController', __name__, url_prefix='/user')

userService = userService()


@user_API.route("/test", methods=["POST","GET"])
def test():
    return "hello"


################################################### TEST ###################################################
