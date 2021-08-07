from .insert import insert
from .read import read
from .update import update
from app.config.sql_db.db import *
import pymysql

class crud(insert,read,update):
    def __init__(self):
        pass

    def db_mariadb_init(self):
        return db_mariadb_init()
    
    def init_db(self):
        return db_init()
    


    