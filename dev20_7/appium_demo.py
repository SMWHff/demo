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
  "platformVersion": "6.0.1",
  "deviceName": "网易模拟器",
  "automationName": "Appium",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".common.MainActivity",
  "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Optional)
driver.implicitly_wait(10)
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("阿里巴巴")
