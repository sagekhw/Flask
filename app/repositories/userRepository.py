from app.config.sql_db.orm.crud import *
from app.config.sql_db.orm.read import *
from app.config.sql_db.orm.insert import *
from app.config.sql_db.orm.update import *
from app.config.ReplacementConfig import *
from app.entities.user import *
from datetime import *

class userRepository(user):
    def __init__(self):
        pass

    ################################################### SELECT ###################################################
  
    def countByIdSql(self,id):
        query = (
            f"SELECT count(*) as count FROM {STR.SMART_INDIVIDUAL} WHERE {STR.IN_ID} = '{id}'"
            )
        return query
    
    def countByEmailSql(self,email):
        query = (
            f"SELECT count(*) as count FROM {STR.SMART_INDIVIDUAL} WHERE {STR.IN_EMAIL} = '{email}'"
            )
        return query
    
    def findByEmailSql(self,email):
        query = (
            f"SELECT * FROM {STR.USER} WHERE {STR.EMAIL} = '{email}'"
            )
        return query
   
    ################################################### INSERT ###################################################
    def saveAuthSql(self,user):
        query = (
            f"INSERT INTO {STR.USER} " +
            f" ({STR.EMAIL},{STR.PASSWORD},{STR.ROLE}) " + 
            f"VALUES ('{user.email}','{user.password}','{user.role}')"
            )
        return query

    def saveSql(self,user):
        query = (
            f"INSERT INTO {STR.SMART_INDIVIDUAL} ( " +
            f"{STR.IN_ID},{STR.IN_PW},{STR.IN_NAME},{STR.IN_TEL} " +
            f",{STR.IN_TEL2},{STR.IN_EMAIL},{STR.IN_IP} " +
            f",{STR.IN_MDATE},{STR.IN_RDATE},{STR.IN_LDATE} " +
            f",{STR.IN_PW_RDATE},{STR.M_OPT_DATE},{STR.IN_ODATE} " +
            f",{STR.IN_ZONECODE},{STR.IN_ADDRESS_DORO} " +
            f",{STR.IN_CANCEL_BANK},{STR.IN_CANCEL_BANK_NAME},{STR.IN_CANCEL_BANK_ACCOUNT} " +
            f",{STR.FB_ENCID},{STR.KO_ENCID},{STR.NV_ENCID} " +
            f",{STR.IN_MGSUID_OLD} " +
            f") " +
            f"VALUES ( " +
            f"'{user.in_id}',password('"+user.in_pw+"'),'"+f"{user.in_name}','{user.in_tel}' " +
            f",'{user.in_tel2}','{user.in_email}','{user.in_ip}' " +
            f",now(),now(),now() " +
            f",now(),now(),'{user.in_odate}' " +
            f",'{user.in_zonecode}','{user.in_address_doro}' " +
            f",'{user.in_cancel_bank}','{user.in_cancel_bank_name}','{user.in_cancel_bank_account}' " +
            f",'{user.fb_encid}','{user.ko_encid}','{user.nv_encid}' " +
            f",'{user.in_mgsuid_old}' " +
            f" )"
            )
        return query

    ################################################### UPDATE ###################################################
 
    ################################################### DELETE ###################################################

    ################################################### FUNCTION ###################################################
    # def countById(self,id):
    #     try:
    #         print("---------------------------------------")
    #         server,db_connect = crud.init_db(self)
    #         cur = db_connect.cursor()

    #         cur.execute(MariadbSTR.START_TRANSACTION)
    #         query = self.countByIdSql(id)
    #         cur.execute(query)
    #         rv = cur.fetchall()
    #         # print(rv)
            
    #     except Exception as e:
    #         print(e)
    #         db_connect.rollback()
    #         return f"{e}"
    #     else:
    #         cur.close()
    #         db_connect.commit()
    #         return rv
    #     finally:
    #         db_connect.close()
    #         server.close()

    # def countByEmail(self,email):
    #     try:
    #         print("---------------------------------------")
    #         server,db_connect = crud.init_db(self)
    #         cur = db_connect.cursor()

    #         cur.execute(MariadbSTR.START_TRANSACTION)
    #         query = self.countByEmailSql(email)
    #         cur.execute(query)
    #         rv = cur.fetchall()
    #         # print(rv)
            
    #     except Exception as e:
    #         print(e)
    #         db_connect.rollback()
    #         return f"{e}"
    #     else:
    #         cur.close()
    #         db_connect.commit()
    #         return rv
    #     finally:
    #         db_connect.close()
    #         server.close()
    def findByEmail(self,email):
        try:
            print("---------------------------------------")
            # server,db_connect = crud.init_db(self)
            db_connect = crud.db_mariadb_init(self)
            cur = db_connect.cursor()

            cur.execute(MariadbSTR.START_TRANSACTION)
            query = self.findByEmailSql(email)
            # print(query)
            cur.execute(query)
            rv = cur.fetchall()
            

        except Exception as e:
            print(e)
            db_connect.rollback()
            return f"{e}"
        else:
            cur.close()
            # db_connect.rollback()
            db_connect.commit()
            return rv
        finally:
            db_connect.close()
            # server.close()

    def saveAuth(self,user):
        try:
            print("---------------------------------------")
            # server,db_connect = crud.init_db(self)
            db_connect = crud.db_mariadb_init(self)
            cur = db_connect.cursor()

            cur.execute(MariadbSTR.START_TRANSACTION)
            query = self.saveAuthSql(user)
            # print(query)
            cur.execute(query)
            rv = cur.fetchall()
            

        except Exception as e:
            print(e)
            db_connect.rollback()
            return f"{e}"
        else:
            cur.close()
            # db_connect.rollback()
            db_connect.commit()
            return rv
        finally:
            db_connect.close()
            # server.close()

    # def save(self,user):
    #     try:
    #         print("---------------------------------------")
    #         server,db_connect = crud.init_db(self)
    #         cur = db_connect.cursor()

    #         cur.execute(MariadbSTR.START_TRANSACTION)
    #         query = self.saveSql(user)
    #         print(query)
    #         cur.execute(query)
    #         rv = cur.fetchall()
            

    #     except Exception as e:
    #         print(e)
    #         db_connect.rollback()
    #         return f"{e}"
    #     else:
    #         cur.close()
    #         # db_connect.rollback()
    #         db_connect.commit()
    #         return rv
    #     finally:
    #         db_connect.close()
    #         server.close()

    

































































    ################################################### TEST ###################################################
    def test_register_user(self,user_email):
        query = (
            f"INSERT INTO user " +
            f"(email)" +
            f"VALUES ('{user_email}') "
            )
        print(query)    
        # return "updateCompanySql"
        return crud.InsertBySQL(self,query)

    def test_select_user(self,user_email):
        query = (
            f"SELECT * FROM user"
        )
        print(query)
        return crud.findBySQL(self,query)

        
    def test_joinCompany(self,user_email,company_id):
        query = (
            f"UPDATE user " +
            f"SET  company_id = '{company_id}' " +
            f"WHERE  email = '{user_email}'" 
            )
        print(query)
        return  crud.UpdateBySQL(self,query)

    def test_findUserAll(self):
        query = (
            f"SELECT * FROM user"
        )
        print(query)
        return crud.findBySQL(self,query)