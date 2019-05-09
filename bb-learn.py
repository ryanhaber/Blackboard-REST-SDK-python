# supporting docs
# https://community.blackboard.com/external/4251
# Ryan Haber
# DRAFT - do not circulate

### import requests
import requests
import json
import time
import base64

def getToken():
    
    # don't think timezone conversion is an issue
    expiry = int(round(time.time() * 1000)) + 270000
    
    url = "http://localhost:9876/learn/api/public/v1/oauth2/token"
    payload = {
        'grant_type': 'client_credentials'
    }
    credentials = b"dc460647-e357-44b8-9a31-9704603033ab:2nNAKmbmOPnHaiRONpd3S9VSwatIdmNF"
    encoded = base64.b64encode(credentials)
    encodedAuth = b"Basic " + encoded

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': encodedAuth
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("\n\nresponse: ", response)

    responsebody = json.loads(response.text)
    return responsebody

    # This works
    # curl -i -X POST -u "47db3140-53aa-4f0c-a1f5-e3b8689ce50e:wS9H88B2yFwSNaGYSPv4juZtXQ8pzAy2" localhost:9876/learn/api/public/v1/oauth2/token -d "grant_type=client_credentials"
    # So why doesn't the preceding?


# parse into py format
token = getToken()
print("token: ", token)

auth = "Bearer " + token['access_token']

method = "GET"

baseurl = "http://localhost:9876"
url = baseurl + "/learn/api/public/v1/courses/_6_1/crossListSet"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': auth,
    }


body = {
    "userName": "meganmason",
    "password": "meganmason",
    "name": {
        "given": "Megan",
        "family": "Mason",
    },
}

# body = {
#     "name": "Intro to Literature of the Classical Period",
#     "courseId": "LIT-301",
#     "description": "Read Homer, Virgil, Horace, Cicero, and more"
# }


payload = json.dumps(body)

response = requests.request(method, url, data=payload, headers=headers)

print("\nResponse: \n", response.text)