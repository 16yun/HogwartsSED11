import json

import requests

from test_requests.test_wxwork.api.base_api import BaseApi


class Wxwork(BaseApi):


    secret = 'c1LpUxHNsq2Om1rc9FfVlET0fBrgy_Zp4PCspWUd4Z4'
    corpid = 'wwe615731600f622f1'
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    token=dict()

    @classmethod
    def get_token(cls,secret=secret):

        if secret is None:
            return cls.token[secret]

        if secret not in cls.token.keys():
            r=cls.get_access_token(secret)
            cls.token[secret]=r["access_token"]

            return cls.token[secret]

    @classmethod
    def get_access_token(cls,secret):
        r= requests.get(url=cls.token_url,
                        params={"corpid":cls.corpid,"corpsecret":secret})

        # print(json.dumps(r.json(), indent=2))

        return r.json()


