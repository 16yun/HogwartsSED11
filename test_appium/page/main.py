from time import sleep

from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage

from test_appium.page.search import SearchPage


class MainPage(BasePage):

    def goto_seach(self):


        self.find(By.ID, "tv_search").click()

        return SearchPage(self._driver)



        return self








