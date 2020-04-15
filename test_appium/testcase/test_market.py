from time import sleep

from test_appium.page.app import App


class TestMarket():

    def setup(self):

        self.main=App().start().market()

    def test_get_price(self):

        assert self.main.goto_search().search('jd').switch_label('股票').get_price() >40


    def test_by_stockCode_price(self):

        assert self.main.goto_search().search('jd').switch_label('股票').get_stockCode_price('SZ000725')>1


    def test_add_select_stock(self):

        toast=self.main.goto_search().search('jd').switch_label('股票').select_stockCode_stock('SZ000725').get_toast()

        assert toast in '添加成功'

    def test_un_select_stock(self):

        toast=self.main.goto_search().search('jd').switch_label('股票').select_stockCode_stock('SZ000725').un_select_stock('SZ000725').get_toast()

        assert  '删除' in toast







