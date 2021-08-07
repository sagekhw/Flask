from app.config.sql_db.orm.crud import crud
from app.config.sql_db.orm.read import *
from app.config.ReplacementConfig import *

class user(crud):
    
    def __init__(self
                ,user_id=None
                ,email=None
                ,password=None
                ,role=None
               
                ):
        self.table_name = self.__class__.__name__
        self.user_id = user_id
        self.email = email
        self.password = password
        self.role = role
        

    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

def user_all_init(req):
    return user(
                email      =req[STR.EMAIL]
                ,password   =req[STR.PASSWORD]
                ,role       =req[STR.ROLE]
                )

def user_register_init(req,req_role):
    return user(
                email       =req[STR.EMAIL]
                ,password   =req[STR.PASSWORD]
                ,role       =req_role
                )

def user_login_init(req):
    return user(
                email       =req[STR.EMAIL]
                ,password   =req[STR.PASSWORD]
                )

def check_request(req,option):
    try:
        if(option == 'auth_register'):
            req[STR.EMAIL]
            req[STR.PASSWORD]
            req[STR.ROLE]
        # elif:
        #     pass
        else:
            pass
    except Exception as e:
        print(e)
        return False
    else:
        return True
    finally:
        pass