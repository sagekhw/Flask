from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.sql_db.orm.crud import *
from app.config.AppConfig import *
from app.repositories.userRepository import *
from app.entities.user import *
from app.config.nosql_db.mongodbConfig import *
import bcrypt
from datetime import datetime
import simplejson as json

repo = userRepository()

class userService:
    def __init__(self):
        pass

    def user_register(self,user):
        if(user.role == JWT.ROLE_USER or user.role == JWT.ROLE_ADMIN):
            encrypted_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
            user.password = encrypted_password.decode("utf-8")
            result = repo.saveAuth(user)
            
            if not result:
                return jsonify(code=200, result="success")
            else:
                return jsonify(code=500,result=result )
        else:
        	return jsonify(code=500,result="Invalid Params!")

    def login_check(self,request_user):
        temp = repo.findByEmail(request_user.email)
        
        if(temp and len(temp) == 1):
            response_user = user_all_init(temp[0])
            if(bcrypt.checkpw(request_user.password.encode("utf-8"), response_user.password.encode("utf-8"))):

                additional_claims = {"role": f"{response_user.role}"}
                return jsonify(
                    code=200,
                    result = "success",
                    # 검증된 경우, access 토큰 반환
                    access_token = create_access_token( identity = response_user.email,
                                                        additional_claims=additional_claims,
                                                        expires_delta = timedelta(
                                                            minutes=FlaskConfig.JWT_ACCESS_TOKEN_EXPIRES)
                                                        )
                )	
            else:
                return jsonify(code=500, result="incorrect password")
            return jsonify(code=200, result="test")
        else:
            return jsonify(code=500, result="nothing or exception")
        
        # if(temp == "nothing" or temp == "False"):
        #     return jsonify(
        #         result = "Invalid Params!"
        #         )
        # else:
        #     input_role = temp[0]['role']
        #     if(not input_role):
        #         return "false"
            
        #     pw = temp[0]['password']
        #     if(not bcrypt.checkpw(user_password.encode("utf-8"), pw.encode("utf-8"))):
        #         return "false"

        #     additional_claims = {"role": f"{input_role}"}
        #     return jsonify(result = "success",
        #         # 검증된 경우, access 토큰 반환
        #         access_token = create_access_token(identity = user_email,
        #                                         additional_claims=additional_claims,
        #                                         expires_delta = False)
        #     )	









    def countById(self,id):
        try:
            temp = repo.countById(id)
        except Exception as e:
            print(e)
            return "False"
        else:
            if(not temp):
                return "nothing"
            else:
                return jsonify(
                        code = 200,
                        result = temp
                        )
        finally:
            pass
    
    def countByEmail(self,email):
        try:
            temp = repo.countByEmail(email)
        except Exception as e:
            print(e)
            return "false"
        else:
            if(not temp):
                return "nothing"
            else:
                return jsonify(
                        code = 200,
                        result = temp
                        )
        finally:
            pass
    
    # def save(self,req,userId):
    def save(self,req):
        try:
            print("hello")
            user = user_save_init(req)
            # user.in_id = userId
            temp = repo.save(user)
            
        except Exception as e:
            print(e)
            return "false"
        else:
            if(not temp):
                return "success"
            else:
                return jsonify(
                        code = 200,
                        result = temp
                        )
        finally:
            pass

    
    def combined_save(self,req):
        try:
            # here
            # user = user_save_init(req)
            # temp = repo.save(user)
            temp = "hello"
            
        except Exception as e:
            print(e)
            return "false"
        else:
            if(not temp):
                return "success"
            else:
                return jsonify(
                        code = 200,
                        result = temp
                        )
        finally:
            pass
 
    
    
