import time

from selenium.webdriver.common.by import By

from testproject.Base import Base


class Test_One(Base):
    num = ""

    def test_login(self):
        self.Driver.find_element(By.XPATH, "//input[@type='email']").send_keys("gaurav.sachdeva1@team.cliffex.com")
        self.Driver.find_element(By.ID, "identifierNext").click()
        time.sleep(7)
        self.Driver.find_element(By.XPATH, "//input[@type= 'password']").send_keys("Gauravcliffex@1234")
        self.Driver.find_element(By.ID, "passwordNext").click()
        time.sleep(5)

        List = self.Driver.find_elements(By.CSS_SELECTOR, "div[class='yW'] span")
        for Lists in List:
            if Lists.text == "intellispine.csc":
                Lists.click()
                break
        time.sleep(2)

        A = self.Driver.find_element(By.XPATH, "(//div[@class='a3s aiL ']/h1)[1]").text
        need = A.split()
        self.num = need[3]

