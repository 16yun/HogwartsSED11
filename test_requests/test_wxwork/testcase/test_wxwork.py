import json

from test_requests.test_wxwork.api.wxwork import Wxwork


class TestWxwork:


    @classmethod
    def setup_class(cls):
        cls.token=Wxwork.get_token()


    def test_get_access_token(self):
        r = Wxwork.get_access_token(Wxwork.secret)

        assert r["errcode"] ==0

