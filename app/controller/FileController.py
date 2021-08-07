#-*- coding:utf-8 -*-

from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.ReplacementConfig import *
from datetime import *

from werkzeug.utils import secure_filename
import os

file_API = Blueprint('FileController', __name__, url_prefix='/file')

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
     json_data = json.load(json_file)

FPATH = json_data['production']['FILES']['PATH'] 


@file_API.route("/test", methods=["POST","GET"])
def test():
    return "hello"

#파일 업로드 처리
@file_API.route('/fileUpload', methods=['POST'])
@jwt_required()
def upload_file():
    current_user = get_jwt_identity()
    files = request.files
    try:
        for f in files.to_dict(flat=False)['files']:
            os.makedirs(FPATH+current_user+'/', exist_ok=True)
            # f.save(FPATH+current_user+'/'+secure_filename(f.filename)) #한글파일 처리 이슈
            f.save(FPATH+current_user+'/'+f.filename)
            print(f.filename)
        
        
    except Exception as e:
        print(e)
        return f"{e}"
    else:
        return "success"
    finally:
        pass


#파일 download 처리
@file_API.route('/fileDownload', methods=['POST'])
@jwt_required()
def download_file():
    req = request.get_json()
    sw=0
    files = os.listdir(FPATH)
    for x in files:
        if(x==req['file']):
            sw=1
    path = FPATH
    return send_file(path + req['file'],
				attachment_filename = req['file'],
				as_attachment=True)

@file_API.route('/test/<path:filename>', methods=['GET', 'POST'])
@jwt_required()
def download(filename):
    directory = FPATH
    return send_from_directory(directory, filename, as_attachment=True)



################################################### TEST ###################################################
