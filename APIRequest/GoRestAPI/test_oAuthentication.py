import json
import requests
import jsonpath
def test_oauth_api():
    API_URL='http://thetestingworldapi.com/api/StDetails/1104'
    resp=requests.get(API_URL)
    print(resp.text)
