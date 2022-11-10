from selenium.webdriver.common.by import By

from pageobjects.checkout import CheckOut


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    password = (By.NAME, "email")
    sumbit = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    radio = (By.CSS_SELECTOR, "#inlineRadio1")
    suceess = (By.XPATH, "//input[@class='btn btn-success']")
    message = (By.CLASS_NAME, "alert")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckOut(self.driver)
        return checkout

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.sumbit)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getRadio(self):
        return self.driver.find_element(*HomePage.radio)

    def getSucess(self):
        return self.driver.find_element(*HomePage.suceess)

    def getMessaged(self):
        return self.driver.find_element(*HomePage.message)