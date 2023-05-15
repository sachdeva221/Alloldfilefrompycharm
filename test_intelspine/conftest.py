import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    ser = Service("C:\\Users\\DELL\\Desktop\\Driver\\chromedriver.exe")
    Driver = webdriver.Chrome(service=ser)
    Driver.get("https://mail.google.com")
    Driver.maximize_window()
    request.cls.Driver = Driver
    yield
    Driver.close()
