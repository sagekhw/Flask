
import json

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
    json_data = json.load(json_file)


class FlaskConfig():
    JWT_SECRET_KEY = json_data['production']['SERVER']['JWT_SECRET_KEY']
    JWT_ALGORITHM = json_data['production']['SERVER']['JWT_ALGORITHM']
    JWT_ACCESS_TOKEN_EXPIRES = json_data['production']['SERVER']['JWT_ACCESS_TOKEN_EXPIRES']
    HOST = json_data['production']['SERVER']['HOST']
    PORT = json_data['production']['SERVER']['PORT']

class JWT():
    ROLE_USER   =   json_data['production']['SERVER']['JWT_ROLE']['USER']
    ROLE_ADMIN  =   json_data['production']['SERVER']['JWT_ROLE']['ADMIN']
    CLAIMS_ROLE =   json_data['production']['SERVER']['JWT_ROLE']['CLAIMS_ROLE']