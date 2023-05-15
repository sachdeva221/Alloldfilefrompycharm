import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


serv = Service("C:\\Users\\DELL\\Desktop\\Driver\\chromedriver.exe")
Driver = webdriver.Chrome(service=serv)
Driver.maximize_window()
Driver.implicitly_wait(5)
Driver.get("https://chat.openai.com/")
time.sleep(10)
Driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
time.sleep(10)
