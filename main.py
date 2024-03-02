
# main.py

import json
import time
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import requests
import uvicorn

import firebase_admin
from firebase_admin import credentials,auth
# from firebase_admin.auth

import pyrebase
# import pyrebase.


from models import AirtimePurchaseModelSchema, LogoutSchema, SignUpSchema,LoginSchema, addCryptodetailsModelSchema, cableNumberVerificationModelSchema, cablePurchaseModelSchema, createCryptoAddressModelSchema, createCryptoWalletModelSchema, dataSubscribeModelSchema, fetchCryptodetailsModelSchema, forgotPasswordSchema, getAddressBalanceModelSchema, getAddressModelSchema, getCoinEstimateModelSchema, getCurrencyPairModelSchema, resetPasswordSchema, userFieldModelSchema

from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request

from datetime import datetime
# from db import DatabaseHandler

from firebase_admin._user_mgt import UserRecord

from firebase_admin import firestore


from google.cloud.firestore_v1.base_query import FieldFilter
from google.cloud import firestore as queriableFirestore
# import google.cloud.firestore_v1.






import clubKonnect_Keys as ck

import SimpleSwap_Key as ss

import BlockCypher_Key as bc



app = FastAPI(title='Yomcoin Server')

# @app.get("/items/{item_id}")
# async def create_item(item_id: int):
#     return {"item_id": item_id }




if not firebase_admin._apps:
    cred = credentials.Certificate("credFromMain.json")
    firebase_admin.initialize_app(cred)
    
    # ,{"databaseURL":''}
db = firestore.client()

# db.collection('users').stream()



# database Module '''''''''''''''''''''''''''



class DatabaseHandler:
    
    def __init__(self,collectionName:any,collectionRef:Optional[any]=None):
        # document id will be user email for the user collections.
        # self.ref = db.reference('docPath')
        if collectionRef:
            self.collection_ref=collectionRef
        else:
            self.collection_ref = db.collection(collectionName)
        
        
        
        # db.collections.
        # ref.
    def createDoc(self,new_data:dict,doc_unique_name:str):        
        '''fresh from the pot'''
        doc_ref=self.collection_ref.document(doc_unique_name)
        
        doc_ref.set(new_data)
    def getDocList(self,filterDetail:list=[],orderDetail:list=[],limit: Optional[int] = None):
        # for the filterDetail param it is a list of list which should have the field 
        # the comparing sig
        query=self.collection_ref
        if len(filterDetail)!=0:
            for i in filterDetail:
                query=query.where(filter=FieldFilter(str(i[0],i[1],i[2])))
                
            
        if len(orderDetail)!=0:
            descendOrAscend=None
            if orderDetail[1]=='ascending':
                descendOrAscend =firestore.Query.DESCENDING
            else:
                descendOrAscend =firestore.Query.ASCENDING
            
            query=query.order_by("name", direction=descendOrAscend)
            
   
    
        if limit:
            query.limit(limit)
        
        docs = (
            query
            .stream()
        )
        result:list =[]

        for doc in docs:
            print(f"{doc.id} => {doc.to_dict()}")
            result.append(doc.to_dict())
                
        return result
    def getDocContent(self,doc_id:str):
        # Note: Use of CollectionRef stream() is prefered to get()
        doc_ref = self.collection_ref.document(doc_id)

        doc = doc_ref.get()
        result:dict={}
        if doc.exists:
            result=doc.to_dict()
        
            

        return result
    
    def updateDoc(self,update_data:dict,doc_id:str):
        
        doc_ref=self.collection_ref.document(doc_id)
        doc_ref.update(update_data)

    def deleteDoc(self,new_data:dict,document_id:str):
        doc_ref = self.collection_ref.document(document_id)
        doc_ref.delete()

    
        

# ''''''''''''''''''''''''''''''''''''''''

# https://yomcoin-dbd48-default-rtdb.firebaseio.com
# https://yomcoin-dbd48-default.firebaseio.com


# firebaseConfig = {
#     "apiKey": "AIzaSyCoNMwdUjdo_p1VUd2LYH6YaR7KflmkAgY",
#   "authDomain": "yomcoinserver.firebaseapp.com",
#   "projectId": "yomcoinserver",
#   "storageBucket": "yomcoinserver.appspot.com",
#   "messagingSenderId": "562071143831",
#   "appId": "1:562071143831:web:5857d5c1ff7ba9a8ec70d2",
#   "measurementId": "G-E5K0RHJMQY",
#   "databaseURL":''
# }

firebaseConfig = {
  "apiKey": "AIzaSyBUiMfg3XecwfkQPOPXfXpEULaU1BPKUGg",
  "authDomain": "yomcoin-75160.firebaseapp.com",
  "projectId": "yomcoin-75160",
  "storageBucket": "yomcoin-75160.appspot.com",
  "messagingSenderId": "146612941001",
  "appId": "1:146612941001:web:c154afa7a733bc5e60dd18",
  "measurementId": "G-4YK6VB7S41",
   "databaseURL":''
}


# {
#   "apiKey": "AIzaSyBxZfh3AVORHxYwAKWDfWRoZ9Ygfj4OlU0",
#   "authDomain": "yomcoin-dbd48.firebaseapp.com",
#   "projectId": "yomcoin-dbd48",
#   "storageBucket": "yomcoin-dbd48.appspot.com",
#   "messagingSenderId": "224590385789",
#   "appId": "1:224590385789:web:da368763bbb2c905e29714",
#   "measurementId": "G-T74B1C57GV",
#   "databaseURL":''
  
# }




firebase=pyrebase.initialize_app(firebaseConfig)

# Sign up ****************************************************************************
@app.post("/signup")
async def create_an_account(userData:SignUpSchema):
    
    email=userData.email
    password=userData.password
    firstName=userData.firstName
    lastName=userData.lastName
    PhoneNumber=userData.PhoneNumber
    birthday=userData.brithday
    gender=userData.gender
    deviceID=userData.deviceID
    
    
    try:
        # database situation ********************************
        userdb=DatabaseHandler(collectionName='users')
        print('userdb created')
        otherUserData={
            "isAdmin":False,
            "birthday":birthday,
            'account_level':0,
            "phoneNumber":PhoneNumber,
            'email':email,
            "firstName":firstName,
            "lastName":lastName,
            'deviceID':deviceID,
            "gender":gender,
            'islogedin':False,
            'cryptoDetails':[],
            "created_at": str(datetime.now()),
            "Updated_at": datetime.now().__str__(),
            'amount':0
            
            
        }
        
        # database situation ended **************************
        user:UserRecord =auth.create_user(email=email,password=password)
        # auth.
        
        print('auth.create_user done')
        
        print(f'user is of type {type(user)},and can be dictified into')
        otherUserData["Unique_ID"]= user.uid
    
        userdb.createDoc(otherUserData,email)
        # userdb.
        print('userdb.createDoc done')
        outputData={
            "Name": f"{firstName} {lastName}",
            "Unique_ID": user.uid,
            "Phone": PhoneNumber,
            "profile_pix": "",
            "Gender": gender,
            "Device_ID": deviceID,
            "Email": email,
            "Fb_UID": "343753e0-9dee-1db8-9906-490dbd0a707d",
            "account_level":0,
            'isAdmin':False,
            
            "created_at": datetime.now().__str__(),
            "Updated_at": datetime.now().__str__()
        }
        outputData.update(user._data)
        
        return JSONResponse(content={
    "status": True,
    "data": outputData,
    "message": "User registered succesfully"
},status_code=200)
    except auth.EmailAlreadyExistsError:
        raise HTTPException(status_code=400,detail='Email already exists')

# Sign up ended ****************************************************************************




@app.post("/login")
async def create_access_token(userData:LoginSchema):
    print(-1)
    email=userData.email
    password=userData.password
    deviceID=userData.deviceID
    userdb:DatabaseHandler =DatabaseHandler(collectionName='users')
    
    # firebase.auth().
    userDetail= userdb.getDocContent(email)
    if not userDetail['islogedin']:
        user= firebase.auth().sign_in_with_email_and_password(email=email,password=password)
        userdb.updateDoc({'islogedin':True,
                        "Device_ID":deviceID},email)
    
        userDetail= userdb.getDocContent(email)
        
        # user['idToken']
        outputData={"status":True,"data":[
            {"Name":f"{userDetail['firstName']} {userDetail['lastName']}",
                "Unique_ID":userDetail['Unique_ID'],
                                        "Phone":userDetail["phoneNumber"],
                                        "token":user['idToken'],
                                        "Gender":userDetail["gender"],
                                        "Device_ID":"QP1A190711020",
                                        "Email":userDetail["email"],
                                        "birthday":userDetail["birthday"],
                                        'accountLevel':userDetail["account_level"]
                                        # "Fb_UID":"343753e0-9dee-1db8-9906-490dbd0a707d",
                                        }],
                "message":"Congrats, you're successfully logged in"
                
                }
        print(4)
        return JSONResponse(content=outputData,status_code=200)
    return JSONResponse(content={'status':False,"data":None,"message":'user already logged in'},status_code=300)
    
    
# Login Ended ****************************************************************************

# log out **************************************************
# To implement the auto log out scheme we have to check if the 
# device id matches the users db DeviceID per 20 sec in the background 
# and push the logout screen if it doesnt match
# 
@app.post("/logout")
async def logOut(userData:LogoutSchema):
    email=userData.email
    userdb:DatabaseHandler =DatabaseHandler(collectionName='users')
    userdb.updateDoc({'islogedin':False,
                        "Device_ID":None},email)
    return JSONResponse(content={'status':True,"data":None,
                                "message":'successfully logged out'},status_code=200)
    
# log out ended **************************************************

# resetting password *********************************************************
@app.post("/forgot_password")
async def forgotPassword(emaildetail:forgotPasswordSchema,):
    auth.get_user_by_email(emaildetail.email)
@app.post("/reset_password")
async def resetPassword(userData:resetPasswordSchema):
    pass
# resetting password *********************************************************

# end ponits for internet service *************************************
@app.post("/get_internet_data_plan")
async def getDataPlans(req:Request):
    # userData:resetPasswordSchema
    
    url=f'https://www.nellobytesystems.com/APIDatabundlePlansV2.asp?UserID={ck.UserID}'
    response:requests.Response =requests.get(url)

    
    return json.dumps(response.json())

@app.post("/subscribe_to_data_plan")
async def subscribe(req:Request,subscriptionDetail:dataSubscribeModelSchema):
    # userData:resetPasswordSchema
    # userID=ck.UserID
    
    url2=f'https://www.nellobytesystems.com/APIDatabundleV1.asp'
    param=subscriptionDetail.model_dump()
    param.update({'UserID': ck.UserID,
    'APIKey': ck.API_KEY})
    response:requests.Response =requests.get(url2,params=param)
    
    return json.dumps(response.json())
    
# end ponits for internet service ENDED**********************************************************

# end points for cable service *************************************************************************

@app.post("/get_available_cable_provider")
async def  getAvailableCableProvider():
    url='https://www.nellobytesystems.com/APICableTVPackagesV2.asp'
    response:requests.Response =requests.get(url)
    return json.dumps(response.json())
    
@app.post("/verify_cable_number")
async def verifyCableNumber(cableDetail:cableNumberVerificationModelSchema):
    # userData:resetPasswordSchema
    # userID=ck.UserID
    
    url2=f'https://www.nellobytesystems.com/APIVerifyCableTVV1.0.asp'
    param=cableDetail.model_dump()
    param.update({'UserID': ck.UserID,
    'APIKey': ck.API_KEY})
    response:requests.Response =requests.get(url2,params=param)
    
    return json.dumps(response.json())

@app.post("/buy_cable_plan")
async def buyCablePlan(cableDetail:cablePurchaseModelSchema):
    
    url2=f'https://www.nellobytesystems.com/APICableTVV1.asp'
    param=cableDetail.dict()
    param.update({'UserID': ck.UserID,
    'APIKey': ck.API_KEY})
    response:requests.Response =requests.get(url2,params=param)
    
    return json.dumps(response.json())

# end points for cable service ENDED *************************************************************************


# end points for Airtime  *************************************************************************

@app.post("/buy_airtime")
async def buyAirtime(cableDetail:AirtimePurchaseModelSchema):
    # userData:resetPasswordSchema
    # userID=ck.UserID
    
    url2=f'www.nellobytesystems.com/APIAirtimeV1.asp'
    param=cableDetail.dict()
    param.update({'UserID': ck.UserID,
    'APIKey': ck.API_KEY})
    response:requests.Response =requests.get(url2,params=param)
    
    return json.dumps(response.json())


# end points for Airtime ENDED *************************************************************************


# get user field ***********************************************
# Amount
@app.post("/get_user_balance")
async def getBalance(fieldGettingDetail:userFieldModelSchema):
    userdb:DatabaseHandler =DatabaseHandler(collectionName='users')
    userDetail= userdb.getDocContent(fieldGettingDetail.email)
    outPutData={"status":True,"data":{"id":"0",
                                "user_id":userDetail['UNIQUE_ID'],
                                "amount":userDetail['amount'],
                                "time":datetime.now().__str__()},
            "message":"amount fetched"}
    return  JSONResponse(content=outPutData,status_code=200)

@app.post("/get_user_cryptoDetail")
async def getCryptoDetail(fieldGettingDetail:userFieldModelSchema):
    userdb:DatabaseHandler =DatabaseHandler(collectionName='users')
    userDetail= userdb.getDocContent(fieldGettingDetail.email)
    outPutData={"status":True,"data":{"id":"0",
                                "user_id":userDetail['UNIQUE_ID'],
                                "amount":userDetail['cryptoDetail'],
                                "time":datetime.now().__str__()},
            "message":"amount fetched"}
    return  JSONResponse(content=outPutData,status_code=200)




# get user field ***********************************************

    




# end points for electricity bill *************************************************************************

@app.post("/get_available_electricity_bill_provider")
async def  getAvailableElectricityBillProvider():
    url='https://www.nellobytesystems.com/APIElectricityDiscosV1.asp'

    

    response:requests.Response =requests.get(url)
    return  json.dumps(response.json())

@app.post("/verify_electric_meter_number")
async def verifyElectricMeterNumber(cableDetail:cableNumberVerificationModelSchema):

    # &ElectricCompany=electric_company_code
    # &MeterNo=meter_no

 
    url2=f'https://www.nellobytesystems.com/APIVerifyElectricityV1.asp'
    param=cableDetail.dict()
    param.update({'UserID': ck.UserID,
    'APIKey': ck.API_KEY})
    response:requests.Response =requests.get(url2,params=param)
    
    return json.dumps(response.json())

@app.post("/buy_electricity")
async def buyElectricity(cableDetail:cableNumberVerificationModelSchema):
    url='https://www.nellobytesystems.com/APIElectricityV1.asp'

    
    param=cableDetail.dict()
    param.update({'UserID': ck.UserID,
    'APIKey': ck.API_KEY})
    response:requests.Response =requests.get(url,params=param)
    
    return json.dumps(response.json())

# end points for electricity bill ENDED *************************************************************************


# end points for send coin  *************************************************************************

@app.post("/get_coin_estimate")
async def  getCoinEstimate(detail:getCoinEstimateModelSchema):
    url="api.simpleswap.io/get_estimated"

    param=detail.dict()
    param.update({'api_key': ss.API_KEY,
    })

    response:requests.Response =requests.get(url)
    return  json.dumps(response.json())

@app.post("/get_currrency_pair")
async def  getCurrrencyPair(detail:getCurrencyPairModelSchema):
    url="api.simpleswap.io/get_pairs"

    param=detail.dict()
    param.update({'api_key': ss.API_KEY,
    })

    response:requests.Response =requests.get(url)
    return  json.dumps(response.json())

@app.post("/get_range")
async def  getRange(detail:getCurrencyPairModelSchema):
    url="api.simpleswap.io/get_ranges"

    param=detail.dict()
    param.update({'api_key': ss.API_KEY,
    })

    response:requests.Response =requests.get(url)
    return  json.dumps(response.json())



# '/get_pairs', {
    #   'api_key': APIKey,
    #   'fixed': 'false',
    #   'symbol': currency,
    # createAddress


# end points for send coin  ENDED *************************************************************************



# end points for crypto wallet *************************************************************************
@app.post("/create_address")
async def  createAddress(detail:createCryptoAddressModelSchema):
    url=f"https://api.blockcypher.com/v1/{detail.cryptoTokenName}/main/addrs"
    # 'https://api.blockcypher.com/v1/ltc/main',

    # param=detail.dict()
    # param.update({'api_key': ss.API_KEY,
    # })

    response:requests.Response =requests.post(url)
    return  json.dumps(response.json())

@app.post("/fetch_crypto_details")
async def  fetchCryptoDetail(detail:fetchCryptodetailsModelSchema):
    userdb:DatabaseHandler =DatabaseHandler(collectionName='users')
    userDetail= userdb.getDocContent(detail.email)
    outPutData=[{
    "status": True,
    "data": userDetail['cryptoDetails'],
    "message": {
        "Name": "crypto",
        "message": "Data Successfully fetched"
    }}]
    return JSONResponse(content=outPutData,status_code=200)

@app.post("/add_crypto_details")
async def  addCryptoDetail(detail:addCryptodetailsModelSchema):
    userdb:DatabaseHandler =DatabaseHandler(collectionName='users')
    
    inputData=json.dumps({
        'email':detail.email,
        'address':detail.address,
        "detail":{
            'walletDetail':detail.walletDetail,
            'walletBlockchain':detail.walletBlockchain
            
        }
    })
    userdb.updateDoc({'cryptoDetails':queriableFirestore.ArrayUnion([inputData])})
    return JSONResponse(content={'status':True,
                                'data':[],
                                "message":'crypto detail added'},
                        status_code=200)

@app.post("/get_address")
async def  getAddress(detail:getAddressModelSchema):
    url=f"api.blockcypher.com/v1/${detail.cryptoTokenName}/main/wallets/{detail.email}"
    
    params={'token':bc.TOKEN}
    
    response:requests.Response =requests.get(url,params=params)
    return json.dumps(response.json())

@app.post("/get_address_balance")
async def  getAddressBalance(detail:getAddressBalanceModelSchema):
    url=f"https://api.blockcypher.com/v1/{detail.cryptoTokenName}/main/addrs/{detail.address}/balance"
    # String address, String blockchain
    params={'token':bc.TOKEN}
    
    response:requests.Response =requests.get(url)
    return json.dumps(response.json())

@app.post("/create_crypto_wallet")
async def  createCryptoWallet(detail:createCryptoWalletModelSchema):
    url=f"api.blockcypher.com/v1/${detail.cryptoTokenName}/main/wallets/{detail.email}"
    params=detail.dict()
    params.update({'token':bc.TOKEN})
    params.pop('cryptoTokenName')
    response:requests.Response =requests.post(url,params=params)
    return json.dumps(response.json())

# getAddress
# end points for crypto wallet  ENDED *************************************************************************



def validate_token(request:Request):
    headers=request.headers
    jwt=headers.get('authorization')
    user=auth.verify_id_token(jwt)
    return user.uid

@app.get("/")
async def do():
    return 12


if __name__=="__main__":
    uvicorn.run('main:app',reload=True)
    
