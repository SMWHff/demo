# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : appium_demo.py
# @Time       : 2021/9/3 19:38

from appium import webdriver

Optional = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "雷电模拟器",
  "automationName": "Appium",
  "browserName": "Browser",
  "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Optional)
driver.implicitly_wait(10)
driver.get("https://m.baidu.com")



driver.quit()