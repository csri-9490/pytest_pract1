import json

import requests
from requests.auth import HTTPBasicAuth


# https://api.github.com/user
resp=requests.get('https://api.github.com/user',auth=HTTPBasicAuth('srikanthchelukala@gmail.com','Shivaya9@'))
print(resp.status_code)
# json1=json.dumps(resp)
# json_resp=json.loads(resp)
print(resp.status_code)
