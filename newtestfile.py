from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\\Users\\DELL\\Desktop\\Driver\\chromedriver.exe")
Driver = webdriver.Chrome(service=serv)
Driver.maximize_window()
Driver.implicitly_wait(5)
Driver.get("https://rahulshettyacademy.com/angularpractice/shop")

product_lists = Driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
for product_list in product_lists:
    print(product_list.find_element(By.XPATH, 'div[1]/h4').text)
    names = product_list.find_elements(By.XPATH, 'div[1]/h4')
    for name in names:
        if name.text == 'Blackberry':
            product_list.find_element(By.XPATH, 'div[2]/button').click()