# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : demo
# @File       : appium_demo.py
# @Time       : 2021/9/3 19:38
import os

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


Optional = {
  "platformName": "Android",
  "platformVersion": "6.0.1",
  "deviceName": "网易模拟器",
  "automationName": "Appium",
  "browserName": "Browser",
  "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Optional)

driver.implicitly_wait(20)
driver.get("https://m.baidu.com")
driver.find_element(By.ID, "index-kw").click()
driver.find_element(By.ID, "index-kw").send_keys("appium")

search_locator = (By.ID, "index-bn")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
driver.find_element(*search_locator).click()



driver.quit()