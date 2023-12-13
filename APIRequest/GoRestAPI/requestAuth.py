import requests

resp=requests.get("https://portal.digivante.com/auth/login",auth=('reddy.csri@gmail.com','Shivaya1@'))
print(resp.status_code)