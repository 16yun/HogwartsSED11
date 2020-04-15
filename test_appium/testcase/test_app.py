from test_appium.page.app import App


class TestThreadApp:

    def setup(self):
        devices=['emulator-5554','emulator-5556','emulator-5558']
        # for i in devices:
        #     self.main = App().thread_start(i).main()
        # self.main = App().thread_start(devices[1]).main()
        for i in devices:
            self.main=App.thread_start(i).main()


    def test_search(self):

        assert self.main.goto_seach().search("阿里巴巴").get_price()>100

    def teardown(self):

        App.kill_appium(self)