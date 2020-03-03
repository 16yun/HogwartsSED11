from appium.webdriver.webdriver import WebDriver
import logging

from selenium.webdriver.common.by import By




class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver

    _black_list = [
        (By.ID, 'tv_agree'),
        (By.XPATH, '//*[@text="下次再说"]'),
        (By.XPATH, '//*[@text="确定"]'),
        (By.ID,'tv_left')
    ]

    _error_max = 10
    _error_count = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # todo 查找单个元素
    def find(self, locator, value: str = None):

        logging.info(locator)
        logging.info(value)

        try:
            # 查询元素
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator,value)
            # 清空错误计数
            self._error_count = 0

            return element

        except Exception as e:

            if self._error_count > self._error_max:
                logging.warning("查询错误数>10次")

                raise e

            # 增加一次异常错误
            self._error_count += 1

            for element in self._black_list:
                logging.info(element)


                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()

                    return self.find(locator, value)

            logging.warning("黑名单中未找到元素")

            raise e


    def find_by_elements(self,locator,value):
        logging.info(locator)
        logging.info(value)

        try:
            # 查询元素
            elements = self._driver.find_elements(*locator) if isinstance(locator, tuple) else self._driver.find_elements(
                locator, value)
            # 清空错误计数
            self._error_count = 0

            return elements

        except Exception as e:

            if self._error_count > self._error_max:
                logging.warning("查询错误数>10次")

                raise e

            # 增加一次异常错误
            self._error_count += 1

            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()

                    return self.find_elements(locator, value)

                raise e
            logging.warning("黑名单中未找到元素")

            raise e

    def get_toast(self):
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").text

    def text(self,key):
        return (By.XPATH,"//*[@text='%s']" % key)

    def find_by_text(self,key):
        return self.find(self.text(key))



    def find_click(self, locator):

        return self.find(locator).click()
