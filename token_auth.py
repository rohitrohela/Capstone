import http.client
import json
from auth import verify_decode_jwt
import os


def getUserCred(role):
    if role == "castingAssistant":
        return {
            "userName": os.getenv('USERNAME_CASTINGASSISTANT'),
            "password": os.getenv('PASSWORD_CASTINGASSISTANT')
        }
    if role == "castingDirector":
        return {
            "userName": os.getenv('USERNAME_CASTINGDIRECTOR'),
            "password": os.getenv('PASSWORD_CASTINGDIRECTOR')
        }
    if role == "executiveProducer":
        return {
            "userName": os.getenv('USERNAME_EXECUTIVEPRODUCER'),
            "password": os.getenv('PASSWORD_EXECUTIVEPRODUCER')
        }


def getRoleBasedToken(existingToken, role):
    if existingToken == "":
        userCred = getUserCred(role)
        return getToken(userCred["userName"], userCred["password"])

    try:
        verify_decode_jwt(existingToken)
    except Exception as e:
        userCred = getUserCred(role)
        existingToken = getToken(userCred["userName"], userCred["password"])
    finally:
        return existingToken


def getToken(userName, password):
    conn = http.client.HTTPSConnection("dev-hlhz1lj0edkt8z33.us.auth0.com")
    parameter = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'audience': 'CapestoneFinal',
        'grant_type': 'password',
        "username": userName,
        "password": password,
        "scope": "openid"
    }

    headers = {'content-type': "application/json"}
    conn.request("POST", "/oauth/token", str(parameter).replace("'", '"'), headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()
    return json.loads(data.decode("utf-8"))['access_token']
