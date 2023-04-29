

import requests
import json
import time
import allure
import pytest

@allure.severity(allure.severity_level.NORMAL)
 

def enrollment1(): 
    # api-endpoint
    URL = "firstapilink"
    
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {
    "grant_type":"",
    "scope":"",
    }
      
    r = requests.post(URL,json=PARAMS)
    
    #If second API need Bearer token to use 
    x = r.content
    y = json.loads(x)
    Bearers = y["access_token"]
    
    EnrollmentURL = "youcanwriteyourapitohere"
    
    
    EnrollmentParameter = {
    "cardNumber": "<card_number>",
    "expiryMonth": "<expiry_month>",
    "expiryYear": "<expiry_year>",
    "cvv": "<cvv>",
    "firstName": "<first_name>",
    "lastName": "<last_name>",
    "email": "<email>",
    "phone": "<phone>"
    }
    
    
    hed = {'Authorization': 'Bearer ' + Bearers}
    d = requests.post(EnrollmentURL, json=EnrollmentParameter, headers=hed)
    
    responseofServ= d.status_code
    xb = d.content
    print(responseofServ)
    if responseofServ == 200:
       print("Enrollment Successfully Done")
       print(xb)
       return True
    else:
       print("Enrollment failed") 
       print(xb)
       return False
     

def test_answer():
    assert enrollment1() == True
