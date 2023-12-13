import requests
import json
import jsonpath
url="https://reqres.in/api/users?page=2"
resp=requests.get(url)
json_resp=json.loads(resp.text)
# print(resp.headers)
# print(resp.headers['Content-Type'])
# print(resp.cookies)
# print(resp.encoding)
# print(resp.elapsed)
# jsonpath=jsonpath.jsonpath(json_resp,'total_pages')
print(jsonpath)
for i in range(0,3):
    fname=jsonpath.jsonpath(json_resp,'data['+str(i)+'].first_name')
    print((fname[0]))