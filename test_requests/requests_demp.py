from pprint import pprint

import requests

secret='c1LpUxHNsq2Om1rc9FfVlET0fBrgy_Zp4PCspWUd4Z4'
corpid='wwe615731600f622f1'
url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'

def test_get_access_token():

    r= requests.get(url=url,
                    params={"corpid":corpid,"corpsecret":secret})

    print(r.json())

def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    pprint(r)

    print(r.status_code)
    print(r.json())
    assert r.status_code == 200

def test_get():
    r = requests.get(
        "https://httpbin.testing-studio.com/get",
        params={
            "a": 1,
            "b": 2,
            "c": "cccc"
        })
    print(r.json())
    assert r.status_code == 200

    
def test_post():
    r = requests.post(
        "https://httpbin.testing-studio.com/post",
        params={
            "a": 1,
            "b": 2,
            "c": "cccc"
        },
        data={
            "a": 11,
            "b": 22,
            "c": "cccccccc"
        },
        headers={"h": "header demo"},
        proxies=proxies,
        verify=False
    )
    print(r.json())
    assert r.status_code == 200
    assert r.json()["headers"]["H"] == "header demo"


def test_upload():
    # todo: upload fix

    r = requests.post(
        "https://httpbin.testing-studio.com/post",
        files={"file": open("__init__.py", 'rb')},
        proxies=proxies,
        verify=False
    )
    print(r.json())
    assert r.status_code == 200
