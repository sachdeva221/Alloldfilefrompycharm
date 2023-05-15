from selenium.webdriver.common.by import By

from test_intelspine.Base import Base


class Test_Main(Base):
    def test_login(self):
        self.Driver.find_element(By.ID, "email").click()