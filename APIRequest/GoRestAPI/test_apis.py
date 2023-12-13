import requests
import json
import jsonpath
def test_pyld():

    payload={'page':2}
    resp=requests.get("https://reqres.in/api/users",params=payload)
    print('cookies',resp.cookies)