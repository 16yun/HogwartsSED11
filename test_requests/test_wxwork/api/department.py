import logging

import requests

from test_requests.test_wxwork.api.wxwork import Wxwork


class Department(Wxwork):


    secret ='c1LpUxHNsq2Om1rc9FfVlET0fBrgy_Zp4PCspWUd4Z4'

    def create(self,name,parentid,**kwargs):

        url='https://qyapi.weixin.qq.com/cgi-bin/department/create'
        data={"name":name,"parentid":parentid}

        data.update(kwargs)
        logging.info(data)
        r = requests.post(
            url,
            params={'access_token':self.get_token(self.secret)},
            json=data
        )

        self.format(r)
        logging.info(r)

        return r.json()


    def update(self,id,**kwargs):

        url="https://qyapi.weixin.qq.com/cgi-bin/department/update"

        data={"id":id}
        data.update(kwargs)

        r=requests.post(url=url,
                    params={'access_token':self.get_token(self.secret)},
                        json=data)

        self.format(r)

        return r.json()


    def delete(self,id):
        url="https://qyapi.weixin.qq.com/cgi-bin/department/delete"

        r=requests.get(url=url,
                       params={"access_token":self.get_token(self.secret),"id":id})

        self.format(r)
        return r.json()

    def list(self,**kwargs):

        data={"access_token":self.get_token(self.secret)}

        data.update(kwargs)

        url='https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r=requests.get(url,
                       params=data)

        self.format(r)
        logging.info(r)

        return r.json()
