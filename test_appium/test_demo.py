import logging

# import uiautomator2 as u2

# d=u2.connect('2ae7055e') #如果设备和PC电脑在同一局域网的话，还可以是你的设备IP地址。
#
# print(d.info)
import yaml


def demo(value):

    print("//*[contains(@resource-id, 'title_container')]//*[@text='%s']"%value)

def test_demo():


    demo('ssssss')

def test_01():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # for c in range(len(m)):
    #
    #     col =[row[c] for row in m]
    # a = [1, 2, 3]
    # b = [4, 5, 6]
    # print(list(zip(a,b)))
    #     print(col)
    # print(list(i) for i in zip(*m))
    # name = "老男孩"
    # l = reversed(name)
    #字符串切片
    # l = name[::-1]

    # print(l)

    a, b = 0, 1
    for i in range(10):
        print(b)
        a, b = b, a + b
    lst = [0, 1]
    for i in range(10):
        lst.append(lst[-1] + lst[-2])
    print(lst)


def num():

    return [lambda x,i=i:i*x for i in range(4)]

def test_num():

    print([m(2) for m in num()])










def get_devices_caps(devicesName):

    path="E:\\PycharmProjects\\HogwartsSED11\\test_appium\\page\\caps.yaml"

    with open(path,"r",encoding="utf-8") as f:

        devices_caps: list[dict]  = yaml.safe_load(f)
        # print(devices_caps)
        for devices in devices_caps:
            logging.info(devices)
            if devicesName in devices['desc']:
                udid=devices['desired_caps']['udid']
                caps=devices['desired_caps']
                port=devices['port']

                #todo 开启服务
                # self.start_appium(port=devices['port'],udid=udid)
                return (caps,port)


def test_caps():

    caps,port=get_devices_caps('emulator-5558')
    print(caps)
    print(port)
