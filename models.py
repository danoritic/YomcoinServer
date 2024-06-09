import datetime
from typing import Optional
from pydantic import BaseModel

class SignUpSchema(BaseModel):
    email:str
    password:str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    PhoneNumber: Optional[str] = None
    birthday: Optional[str] = None
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
    email:str
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

class transactionStoreModel(BaseModel):
    userEmail:str
    transactionDetails:str
    userId:str
    serviceType:str
    date:str
class transactionGetModel(BaseModel):
    startDate:str|None
    endDate:str|None
    userId:str


# transactionStoreModel

class userFieldModelSchema(BaseModel):
    email:str
    

class getCoinEstimateModelSchema(BaseModel):
    fixed:str
    currency_from:str
    currency_to:str
    amount:str
# class getAllCoinEstimate(BaseModel):
#     fixed:str
#     currency_from:str
#     currency_to:str
#     amount:str

class getCurrencyPairModelSchema(BaseModel):
    fixed:str|None
    symbol:str
class getingCompanyAddressModel(BaseModel):
    userId:str

class sendCoinModel(BaseModel):
    fixed: str
    currency_from:str
    currency_to:str
    amount:str
    address_to:str
    extra_id_to:str
    user_refund_address:str
    user_refund_extra_id:str

# getingCompanyAddressModel
class getCurrencyRangeModelSchema(BaseModel):
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

class verifyAndCredit(BaseModel):
    userEmail:str
    userID:str
    amount:str

class debitModel(BaseModel):
    # {"Content-Type": "application/json"}
    userID:str
    amount:str
class AmountModel(BaseModel):
    # {"Content-Type": "application/json"}
    userID:str

class getTokenModel(BaseModel):
    userID:str

class orderGiftcardModel(BaseModel):
    token:str
    userID:str
    userEmail:str
    productId:str
    quantity:str
    unitPrice:str
    senderName:str
    phoneCountryCode:str|None
    phoneNumber:str
    
class getGiftcardRedemptionCodeModel(BaseModel):
    token:str
    transactionId:str
    
class getGiftcardsAvailableModel(BaseModel):
    token:str
    page:str
    productName:str
    countryCode:str



# ?size=10&page=1&productName=Amazon&countryCode=US& =true&includeFixed=true"

# AmountModel orderGiftcardModel

class electricBillPurchaseModelSchema(BaseModel):
    ElectricCompany:str
    MeterType:str
    MeterNo:str
    Amount:str
    PhoneNo:str
class electricMeterNumberVerificationModelSchema(BaseModel):
    ElectricCompany:str
    MeterNo:str




class AirtimePurchaseModelSchema(BaseModel):
    MobileNetwork:str
    Amount:str
    MobileNumber:str



class createCardBINModelSchema(BaseModel):
    cardBIN:str
    
