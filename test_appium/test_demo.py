

import uiautomator2 as u2

# d=u2.connect('2ae7055e') #如果设备和PC电脑在同一局域网的话，还可以是你的设备IP地址。
#
# print(d.info)

def demo(value):

    print("//*[contains(@resource-id, 'title_container')]//*[@text='%s']"%value)

def test_demo():


    demo('ssssss')