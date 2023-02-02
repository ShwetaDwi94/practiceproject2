"""This file demonstrates about browser commands"""

from selenium import webdriver
path = r"C:\Users\IRAHUL\PycharmProjects\practiceproject2\drivers\chromedriver.exe"
driver = webdriver.Chrome("path")

url = "https://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()

