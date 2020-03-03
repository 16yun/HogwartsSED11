from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage
from test_appium.page.search import SearchPage


class MarketPage(BasePage):

    def goto_search(self):

        self.find(By.ID, "action_search").click()

        return SearchPage(self._driver)