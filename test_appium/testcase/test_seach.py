from time import sleep

from test_appium.page.app import App



class TestSearch():

    def setup(self):

        self.main=App().start().main()

    def test_search(self):

        assert self.main.goto_seach().search("阿里巴巴").get_price()>200


    def teardown(self):

        sleep(10)
        App().stop()



