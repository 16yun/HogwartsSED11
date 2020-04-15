import logging
from time import sleep

import yaml
from appium import webdriver
from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage
from test_appium.page.main import MainPage
from test_appium.page.market import MarketPage


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "yun"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["unicodeKeyboard"] = True
            # caps["noReset"] = True
            caps["chromedriverExecutable"] = "E:/PycharmProjects/HogwartsSED11/venv/chromedriver.exe"
            caps["udid"] = 'emulator-5556'
            self._driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
            self._driver.implicitly_wait(5)

        else:
            self._driver.start_activity(self._package, self._activity)

        return self



    def thread_start(self,devicesName):
        if self._driver is None:
            devices_caps,port =self.get_devices_caps(devicesName)
            self._driver=webdriver.Remote('http://127.0.0.1:%s/wd/hub'%port,devices_caps)
            self._driver.implicitly_wait(5)

        else:
            self._driver.start_activity(self._package, self._activity)

        return self



    def main(self) -> MainPage:

        return MainPage(self._driver)

    def market(self) -> MarketPage:

        self.find(By.XPATH, "//*[@text='行情']").click()

        return MarketPage(self._driver)

    def stop(self):

        self._driver.quit()



