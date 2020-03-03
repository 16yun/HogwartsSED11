import logging

from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class SearchPage(BasePage):

    def search(self,key : str):


        #self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")

        self.find(By.ID,"search_input_text").send_keys(key)
        self.find(By.ID,"name").click()

        return self

    #todo 获取价格
    def get_price(self):

        return float(self.find(By.ID, "current_price").text)

    #todo 点击取消退出搜索页
    def cancel_search(self):

        self.find(By.XPATH,"//*[@text='取消']").click()

        return self

    #todo 切换顶部标签
    def switch_label(self,value):
        self.find(By.XPATH,"//*[contains(@resource-id, 'title_container')]//*[@text='%s']"%value).click()

        return self

    # todo 通过股票号获取股票价格
    def get_stockCode_price(self,stockCode):
        # "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]"

        stockPrice=float(self.find(By.XPATH,"//*[@text='%s']/../../..//*[contains(@resource-id,'current_price')]"%stockCode).text)
        logging.info(stockPrice)

        return stockPrice
    # todo 通过股票号，添加自选
    def select_stockCode_stock(self,stockCode):
        #"//*[@text='TSLA']/../../..//*[contains(@resource-id,'follow_btn')]"
        stock=self.find(By.XPATH,"//*[@text='%s']/../../..//*[contains(@resource-id,'follow_btn')]"%stockCode)
        stock.click()

        return self

    #todo 取消已选择的股票
    def un_select_stock(self,stockCode):

        stock = self.find(By.XPATH, "//*[@text='%s']/../../..//*[contains(@resource-id,'followed_btn')]" % stockCode)
        stock.click()

        return self








