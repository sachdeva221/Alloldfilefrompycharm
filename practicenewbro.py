from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def test_login():
    obj = Service('C:\\Users\\DELL\\Desktop\\driverfirefox\\geckodriver.exe')
    driver = webdriver.Firefox(service=obj)

    driver.get("https://www.youtube.com")



