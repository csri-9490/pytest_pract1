import requests

# r = requests.get('https://github.com/login',verify=True,auth=('srikanthchelukala@gmail.com', 'Shivaya9@34'))
# print(r)
url="https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files={'file':open('C:\\Users\\srika\\OneDrive\\Desktop\\j1.jpg','rb')}
r1=requests.post(url,files=files)
print(r1.status_code)
print(r1.text)