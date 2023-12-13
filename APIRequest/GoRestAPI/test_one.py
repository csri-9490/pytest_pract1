import requests


def test_auth():

    r = requests.get('https://api.github.com/user', auth=('srikanthchelukala@gmail.com', 'Shivaya9@'))

    print(r.text)