import time
from selenium import webdriver
driver = webdriver.Chrome("c:\\temp\\chromedriver.exe")
driver.get('http://192.168.99.100:5000')
driver.maximize_window()
txt2print=driver.find_element_by_css_selector("body").text
print(txt2print)

