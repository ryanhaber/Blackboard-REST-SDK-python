# supporting docs
# https://community.blackboard.com/external/4251
# Ryan Haber

import requests
import time
import json



def getAccessToken():
    # token request URL
    # you must replace YOUR_ENCODED_ASSERTION_HEADER, YOUR_ENCODED_ASSERTION_PAYLOAD, and YOUR_ENCODED_ASSERTION-SIGNATURE
    # See "Authorize and Authenticate in Blackboard Collaborate" https://community.blackboard.com/docs/DOC-3115 for more details
    url = 'https://xx-csa.bbcollab.com/token?grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=YOUR_ENCODED_ASSERTION_HEADER.YOUR_ENCODED_ASSERTION_PAYLOAD.YOUR_ENCODED_ASSERTION-SIGNATURE'
    
    # don't think timezone conversion is an issue
    expiry = int(round(time.time() * 1000)) + 270000
    
    # base headers and payload
    headers = { "content-Type": "application/x-www-form-urlencoded" }

    # request access token
    response = requests.request("POST", url, headers=headers)

    responsebody = json.loads(response.text)
    return responsebody["access_token"]






# use access_token to make API request
token = getAccessToken()
auth = "Bearer " + token

method = "GET"

baseurl = "https://xx-csa.bbcollab.com/"
url = baseurl + "users"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': auth,
    'cache-control': "no-cache",
    }

# body for creating a user
# body = {
#     "lastName": "Ug",
#     "firstName": "ly",
#     "displayName": "Yomama so",
#     "extId": "derp",
#     "email": "derp@geniusleague.com"
# }

# body for creating a session - note the way startTime is done
# body = {
#     "startTime":"2017-12-14T11:33:44.123Z",
#     "allowInSessionInvitees": 'true',
#     "guestRole": "presenter",
#     "openChair": 'true',
#     "sessionExitUrl": "string",
#     "mustBeSupervised": 'false',
#     "noEndDate": 'true',
#     "description": "Another Room",
#     "canPostMessage": 'true',
#     "participantCanUseTools": 'true',
#     "courseRoomEnabled": 'true',
#     "canAnnotateWhiteboard": 'true',
#     "canDownloadRecording": 'true',
#     "canShareVideo": 'true',
#     "name": "Collab API Demo Room",
#     "raiseHandOnEnter": 'false',
#     "allowGuest": 'true',
#     "showProfile": 'true',
#     "canShareAudio": 'true'      
# }



# convert payload body from Python object to JSON
payload = json.dumps(body)

# make request
response = requests.request(method, url, data=payload, headers=headers)

# output response
print("\nResponse: \n", response.text)