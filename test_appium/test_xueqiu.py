# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu():

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "yun"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["unicodeKeyboard"]=True
        caps["chromedriverExecutable"] = "E:/PycharmProjects/HogwartsSED11/venv/chromedriver.exe"

        self.driver: WebDriver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)
        try:
            self.driver.find_element(By.XPATH, "//*[@text='同意']").click()
        finally:
            pass

    def test_search(self):
        # el5 = driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el5.click()
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")

    def test_search_get_price(self):
        # 点击搜索
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").click()
        # 输入阿里巴巴
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        # 点击股票按钮
        # Xpath contains 模糊匹配查找resource-id中包含title_container关键字的元素
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@resource-id, 'title_container')]//*[@text='股票']").click()
        # 获取中国阿里巴巴股票价格
        # “../”获取元素父节点
        price = self.driver.find_element(MobileBy.XPATH,
                                         "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text
        assert float(price) < 219

    def test_add_stock(self):
        # 搜索股票特斯拉
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("特斯拉")
        self.driver.find_element(MobileBy.ID, "name").click()
        # 选择美国特斯拉股票加自选
        # Xpath contains 模糊匹配resoure-id包含follow_btn的元素
        TSLA_Stock = (By.XPATH, "//*[@text='TSLA']/../../..//*[contains(@resource-id,'follow_btn')]")
        self.driver.find_element(*TSLA_Stock).click()
        # 点击取消按钮回到首页
        self.driver.find_element(MobileBy.XPATH, "//*[@text='取消']").click()
        # 搜索股票特斯拉
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("特斯拉")
        self.driver.find_element(MobileBy.ID, "name").click()
        # 选择股票列表
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@resource-id, 'title_container')]//*[@text='股票']").click()
        # 获取信息

        text = self.driver.find_element(MobileBy.XPATH,
                                        "//*[@text='TSLA']/../../..//*[contains(@resource-id,'add_attention')]/android.widget.TextView"
                                        ).get_attribute('resource-id')
        print(text)
        # 断言followed_btn 包含在text字符串中
        assert 'followed_btn' in text

    def test_uiselector(self):
        # 滑动页面直到发现文本“5小时前”
        scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                           'new UiSelector().scrollable(true).instance(0))'
                                                           '.scrollIntoView('
                                                           'new UiSelector().text("5小时前").instance(0));')

        self.driver.find_element(*scroll_to_element).click();

    def test_appium_webview(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()

        #首次测试时用于分析上下文
        # for i in range(5):
        #     print(self.driver.contexts)
        #     sleep(0.5)
        # print(self.driver.page_source)
        # 坑1：webview上下文出现大概有3s的延迟, android 6.0默认支持，其他的需要打开webview调试开关
        # adb shell cat /proc/net/unix | grep  webview  获取webview 套接字

        #显示等待元素
        # WebDriverWait(self.driver,30).until(lambda x:len(self.driver.contexts) >3 )
        #切换到最后一个context
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.CSS_SELECTOR,".trade_home_xueying_SJY").click()

        # 首次测试是用于分析当前的窗口
        # for i in range(5):
        #     print(self.driver.window_handles)
        #     sleep(0.5)
        WebDriverWait(self.driver,30).until(lambda x : len(self.driver.window_handles)>3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #隐式等待当手机号输入框可以点击时再进行下一步
        WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'[placeholder="请输入手机号"]')))
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入手机号"]').send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入验证码"]').send_keys("555555")
        self.driver.find_element(By.CSS_SELECTOR,".open_form-submit_1Ms").click()

        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(By.ID,"action_bar_back").click()




    def test_add(self):
        assert 1 + 1 == 3

    def teardown(self):
        sleep(30)
        self.driver.quit()
