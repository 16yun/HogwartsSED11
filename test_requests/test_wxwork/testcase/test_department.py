from test_requests.test_wxwork.api import department
from test_requests.test_wxwork.api.department import Department


class TestDepartment:

    @classmethod
    def setup_class(cls):
        cls.department=Department()

    def test_creat(self):

        r=self.department.create(name="test1",parentid=1)

        assert r['errcode']==0


    def test_update(self):
        r=self.department.update(id=2,name_en="RDGZ")

        assert r['errcode']==0


    def test_delete(self):

        r=self.department.delete(id=3)

        assert r['errcode']==0


    def test_list(self):
        r=self.department.list()

        assert r["errcode"] == 0