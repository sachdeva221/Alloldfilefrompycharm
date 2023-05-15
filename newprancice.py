import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service('C:\\Users\\DELL\\Desktop\\Driver\\chromedriver.exe')
Driver = webdriver.Chrome(service=ser)
Driver.get('https://www.youtube.com')
Driver.maximize_window()
Driver.implicitly_wait(5)

time.sleep(10)
# Driver.find_element(By.ID, "search-input").click()
# Driver.find_element(By.NAME, 'search_query').send_keys("python basic")
# Driver.find_element(By.CSS_SELECTOR, 'button[class="style-scope ytd-searchbox"]').click()
Driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

