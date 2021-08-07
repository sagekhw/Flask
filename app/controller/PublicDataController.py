# #-*- coding:utf-8 -*-

from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
from app.config.ReplacementConfig import *
from datetime import *
import urllib.parse
import urllib
import requests
from werkzeug.utils import secure_filename
import os

publicData_API = Blueprint('PublicDataController', __name__, url_prefix='/publicData')
with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
     json_data = json.load(json_file)

National_Parking_Lot_Information_URL = json_data['production']['DATA.GO.KR']['OPENAPI']['National_Parking_Lot_Information']['URL']
National_Parking_Lot_Information_ServiceKey = json_data['production']['DATA.GO.KR']['OPENAPI']['National_Parking_Lot_Information']['SERVICE_KEY']

@publicData_API.route("/test", methods=["POST","GET"])
def test():
    return "hello"

"""
전국주차장정보표준데이터
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15012896
"""
@publicData_API.route("/National_Parking_Lot_Information", methods=["POST","GET"])
def National_Parking_Lot_Information():
    url = National_Parking_Lot_Information_URL
    ServiceKey = National_Parking_Lot_Information_ServiceKey
    req = request.get_json()
    try:
        pageNumber = req['pageNo']
        pageNumberOfRows = req['numOfRows']
    except Exception as e:
        print(e)
        return "Please Check request Data"
    else:
        try:
            parameters = {
            "ServiceKey":ServiceKey
            ,"pageNo": pageNumber
            , "numOfRows": pageNumberOfRows
            ,"type":"json"
            } 
            response = requests.get(url, params = parameters)

        except Exception as e:
            print(e)
            return "Please check url or service key also check validity date."
        
        else:
            return response.text

        






    

# ################################################### TEST ###################################################
# # parameters = {
# #             "ServiceKey":ServiceKey
# #             ,"pageNo": pageNumber
# #             , "numOfRows": pageNumberOfRows
# #             ,"type":"json"
# #             # ,"prkplceNo":''
# #             # ,"prkplceNm":''
# #             # ,"prkplceSe":''
# #             # ,"prkplceType":''
# #             # ,"rdnmadr":''
# #             # ,"lnmadr":''
# #             # ,"prkcmprt":''
# #             # ,"feedingSe":''
# #             # ,"enforceSe":''
# #             # ,"operDay":''
# #             # ,"weekdayOperOpenHhmm":''
# #             # ,"weekdayOperColseHhmm":''
# #             # ,"satOperOperOpenHhmm":''
# #             # ,"satOperCloseHhmm":''
# #             # ,"holidayOperOpenHhmm":''
# #             # ,"holidayCloseOpenHhmm":''
# #             # ,"parkingchrgeInfo":''
# #             # ,"basicTime":''
# #             # ,"basicCharge":''
# #             # ,"addUnitTime":''
# #             # ,"addUnitCharge":''
# #             # ,"dayCmmtktAdjTime":''
# #             # ,"dayCmmtkt":''
# #             # ,"monthCmmtkt":''
# #             # ,"metpay":''
# #             # ,"spcmnt":''
# #             # ,"institutionNm":''
# #             # ,"phoneNumber":''
# #             # ,"latitude":''
# #             # ,"longitude":''
# #             # ,"referenceDate":''
# #             # ,"instt_code":''
# #             # ,"instt_nm":''
# #             } 
