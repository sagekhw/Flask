import pymysql
import json
from sshtunnel import SSHTunnelForwarder

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
     json_data = json.load(json_file)
    
    
mariadb_conns = []
def db_mariadb_init():
    con = pymysql.connect(
        host=json_data['production']['DATABASES']['MARIADB']['HOST']        ,
        port=json_data['production']['DATABASES']['MARIADB']['PORT']        , 
        user=json_data['production']['DATABASES']['MARIADB']['USER']        , 
        passwd=json_data['production']['DATABASES']['MARIADB']['PASSWORD']  , 
        db=json_data['production']['DATABASES']['MARIADB']['NAME']          ,
        charset='utf8'                                                      ,
        cursorclass=pymysql.cursors.DictCursor                              ,
        autocommit=False
    )

    mariadb_conns.append(con)

    return mariadb_conns.pop()



# sql_hostname = json_data['production']['DATABASES']['MYSQL']['HOST']
# sql_username = json_data['production']['DATABASES']['MYSQL']['USER']
# sql_password = json_data['production']['DATABASES']['MYSQL']['PASSWORD']
# sql_main_database = json_data['production']['DATABASES']['MYSQL']['NAME']
# sql_port = json_data['production']['DATABASES']['MYSQL']['PORT']
# ssh_host = json_data['production']['REMOTE_SERVER_SSH']['HOST']
# ssh_user = json_data['production']['REMOTE_SERVER_SSH']['USER']
# ssh_port = json_data['production']['REMOTE_SERVER_SSH']['PORT']
# ssh_key = json_data['production']['REMOTE_SERVER_SSH']['KEY'] 

# conns = []
# ssh_conns = []
# default_cursor = pymysql.cursors.DictCursor
# def db_init():
#     server = SSHTunnelForwarder(
#              (ssh_host, ssh_port),
#              ssh_password="1234",
#              ssh_username=ssh_user,
#              remote_bind_address=(sql_hostname, sql_port))
#     server.start()
#     conn = pymysql.connect(
#         host='127.0.0.1'            , 
#         user=sql_username           ,
#         passwd=sql_password         , 
#         db=sql_main_database        ,
#         port=server.local_bind_port ,
#         charset='utf8'                                                      ,
#         cursorclass=pymysql.cursors.DictCursor                              ,
#         autocommit=False
#     )
#     ssh_conns.append(server)
#     conns.append(conn)
    

#     return ssh_conns.pop(),conns.pop()
