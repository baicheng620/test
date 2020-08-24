from selenium import webdriver
import pytest
from time import sleep

driver = webdriver.Chrome()
driver.get("http://192.168.0.112:8899")
driver.maximize_window()


#登录
sleep(2)
driver.find_element_by_id("userName").clear()
driver.find_element_by_id("userName").send_keys("008")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")

driver.find_element_by_css_selector(".ant-btn").click()

sleep(5)
