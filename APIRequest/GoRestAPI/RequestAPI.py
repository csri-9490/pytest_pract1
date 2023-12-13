import requests
import random
import json
import string
base_url="https://gorest.co.in"

auth_token="Bearer 23f105391f1564af2b58e1a9ecf39841b15c1c6b0fd791dab7ef21dd43963f5a"
def generate_random_email():
    domain='automation.com'
    email_length=10
    random_string=''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email=random_string+"@"+domain
    return email
def get_request():
    url = base_url + '/public/v2/users'
    header={"Authorization":auth_token}
    resp=requests.get(url,headers=header)
    json_data1=resp.json()
    json_string1=json.dumps(resp.json(),indent=4)
    print('json GET response body',json_string1)

def post_request():
    url=base_url+'/public/v2/users'
    header={"Authorization":auth_token}
    data={"name":"zzccc Chelukala",
          "email":generate_random_email(),
          "gender":"male",
          "status":"active"}
    post_resp=requests.post(url,json=data,headers=header)
    json_data=post_resp.json()
    json_str=json.dumps(json_data,indent=4)
    print('json POST responce body',json_str)
    user_id=json_data["id"]
    assert post_resp.status_code==201
    return user_id
    # print(user_id)

def put_request(user_id):
    url = base_url + f'/public/v2/users/{user_id}'
    header = {"Authorization": auth_token}
    data = {"name": "rajeev reddy CH1",
            "email": generate_random_email(),
            "gender": "male",
            "status": "inactive"}
    put_resp=requests.put(url,json=data,headers=header)
    print(put_resp.status_code)

def delete_request(user_id):
    url = base_url + f'/public/v2/users/{user_id}'
    header = {"Authorization": auth_token}

    del_resp=requests.delete(url,headers=header)
    print(del_resp.status_code)
# get_request()
userid=post_request()
put_request(userid)
delete_request(userid)
# get_request()