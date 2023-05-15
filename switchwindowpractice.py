from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Obj = Service('C:\\Users\\DELL\\Desktop\\Driver\\chromedriver.exe')
Driver = webdriver.Chrome(service=Obj)
Driver.maximize_window()
Driver.get('https://rahulshettyacademy.com/AutomationPractice/')
Driver.implicitly_wait(5)
Driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

Driver.switch_to.frame('iframe-name')
Driver.find_element(By.LINK_TEXT, 'Courses').click()
