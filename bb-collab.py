# supporting docs
# https://community.blackboard.com/external/4251
# Ryan Haber
# DRAFT - do not circulate

### import requests
import requests
import jwt
import time
import json

def getToken():
    # token request URL
    url = 'https://xx-csa.bbcollab.com/token?grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJyeWFuLTc0RkQ5QkY5LTgxQTQtNEI4Mi04MTU2LUI4NzBDRjNGODI5RiIsInN1YiI6InJ5YW4tNzRGRDlCRjktODFBNC00QjgyLTgxNTYtQjg3MENGM0Y4MjlGIiwiZXhwIjoxNTA5MTUzNDcyMDAwfQ.OcGKh2eYZDFxhqSSeepFnmpxarTkc0t7qiWpR0GcjsM'
    
    # don't think timezone conversion is an issue
    expiry = int(round(time.time() * 1000)) + 270000
    
    # base headers and payload
    headers = { "content-Type": "application/x-www-form-urlencoded" }
    payload = { "sub": "ryan-74FD9BF9-81A4-4B82-8156-B870CF3F829F", "iss": "ryan-74FD9BF9-81A4-4B82-8156-B870CF3F829F", "exp": expiry}

    # encode
    encoded = jwt.encode(payload, '2A328B0B-7724-4ED9-A168-DECAB9F60F7B', algorithm='HS256')

    # request access token
    response = requests.request("POST", url, headers=headers, params=encoded)

    responsebody = json.loads(response.text)
    return responsebody["access_token"]


# parse into py format
token = getToken()

# use access_token to make request

auth = "Bearer " + token

method = "POST"

baseurl = "https://xx-csa.bbcollab.com/"
url = baseurl + "users"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': auth,
    'cache-control': "no-cache",
    'postman-token': "d9e338c3-6d4c-9aa5-08f7-2d17bb3d75a3"
    }

body = {
    "lastName": "Fu",
    "firstName": "bar",
    "displayName": "Smelly Belly",
    "extId": "smellybelly",
    "email": "smellybelly@geniusleague.com"
}
payload = json.dumps(body)

response = requests.request(method, url, data=payload, headers=headers)

print("\nResponse: \n", response.text)