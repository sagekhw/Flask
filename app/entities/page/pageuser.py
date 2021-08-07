from app.config.sql_db.orm.crud import crud
from app.config.sql_db.orm.read import *
from app.config.ReplacementConfig import *

class pageuser(crud):
    
    def __init__(self
                ,member_email=None
                ,member_password=None
                ):
        self.table_name = self.__class__.__name__
        self.member_email = member_email
        self.member_password = member_password
       

    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

def user_All_init(req):
    return pageuser(
                member_email=req[PAGE.MEMBER_EMAIL]
                ,member_password=req[PAGE.MEMBER_PASSWORD]
                )
def user_email_password_init(req):
    return pageuser(
                member_email=req[PAGE.MEMBER_EMAIL]
                ,member_password=req[PAGE.MEMBER_PASSWORD]
                )
