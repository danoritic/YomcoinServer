from typing import Optional
from pydantic import BaseModel

class SignUpSchema(BaseModel):
    email:str
    password:str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    PhoneNumber: Optional[str] = None
    brithday: Optional[str] = None
    gender: Optional[str] = None
    deviceID: Optional[str] = None
    
    
    class Config:
        schema_extra={
            'example':{
                'email':'sampleMail@gmail.com',
                'password':'samplePassword1234',
                
            }
        }
class LoginSchema(BaseModel):
    email:str
    password:str
    deviceID:str

    class Config:
        schema_extra={
            'example':{
                'email':'sampleMail@gmail.com',
                'password':'samplePassword1234',
                
            }
        }
class resetPasswordSchema(BaseModel):
    oldPassword:str
    newPassword:str
class forgotPasswordSchema(BaseModel):
    email:str

class LogoutSchema(BaseModel):
    email:str
    
    

class dataSubscribeModelSchema(BaseModel):
    MobileNetwork: str
    DataPlan: str
    MobileNumber: str



class cableNumberVerificationModelSchema(BaseModel):
    CableTV: str
    SmartCardNo: str
class cablePurchaseModelSchema(BaseModel):
    CableTV:str
    SmartCardNo:str
    Package:str
    


class userFieldModelSchema(BaseModel):
    email:str
    

class getCoinEstimateModelSchema(BaseModel):
    fixed:str
    currency_from:str
    currency_to:str
    amount:str
class getCurrencyPairModelSchema(BaseModel):
    fixed:str
    symbol:str
class getCurrencyPairModelSchema(BaseModel):
    fixed:str
    currency_from:str
    currency_to: str
class createCryptoAddressModelSchema(BaseModel):
    cryptoTokenName:str
class fetchCryptodetailsModelSchema(BaseModel):
    email:str
class getAddressModelSchema(BaseModel):
    email:str
    cryptoTokenName:str
class getAddressBalanceModelSchema(BaseModel):
    address:str
    cryptoTokenName:str

class addCryptodetailsModelSchema(BaseModel):
    email:str
    walletDetail:str
    walletBlockchain:str
    address:str
class createCryptoWalletModelSchema(BaseModel):
    name:str
    address:str
    cryptoTokenName:str



class electricBillPurchaseModelSchema(BaseModel):
    ElectricCompany:str
    MeterType:str
    Amount:str
    PhoneNo:str
class electricMeterNumberVerificationModelSchema(BaseModel):
    ElectricCompany:str
    MeterNo:str




class AirtimePurchaseModelSchema(BaseModel):
    MobileNetwork:str
    Amount:str
    MobileNumber:str



