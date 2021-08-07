#-*- coding:utf-8 -*-

from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.ReplacementConfig import *
from datetime import *
import urllib.parse
import urllib
import requests
from werkzeug.utils import secure_filename
import os

push_API = Blueprint('PushController', __name__, url_prefix='/push')
with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
     json_data = json.load(json_file)

GOOGLECLOUD_FIREBASE_CLOUD_MESSAGING_WEBAPIKEY  =   json_data['production']['GOOGLECLOUD']['FIREBASE']['CLOUD_MESSAGING']['WEBAPIKEY']
GOOGLECLOUD_FIREBASE_CLOUD_MESSAGING_TOKEN      =   json_data['production']['GOOGLECLOUD']['FIREBASE']['CLOUD_MESSAGING']['TOKEN']
GOOGLECLOUD_FIREBASE_CLOUD_MESSAGING_PROJECT_ID =   json_data['production']['GOOGLECLOUD']['FIREBASE']['CLOUD_MESSAGING']['PROJECT_ID']

PROJECT_ID = GOOGLECLOUD_FIREBASE_CLOUD_MESSAGING_PROJECT_ID
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/messages:send'
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']


@push_API.route('/getToken', methods=['GET'])
def getToken():
    access_token = _get_access_token()
    req = request.get_json()

    params = {
        "to": req.get('token'),
        "notification": {
            "title":"sagekhw title",
            "body":"sagekhe body",
            "click_action":"https://google.com"
        }
    }
    headersParam = {
        "Authorization":"key=  "+GOOGLECLOUD_FIREBASE_CLOUD_MESSAGING_WEBAPIKEY,
        "Content-Type":"application/json"
    }
    
    res = requests.post("https://fcm.googleapis.com/fcm/send",headers=headersParam, data=json.dumps(params))
    return res.text


def _get_access_token():

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
      'service-account.json', SCOPES)
    access_token_info = credentials.get_access_token()
    return access_token_info.access_token



        

################################################### TEST ###################################################
