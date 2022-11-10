from selenium.webdriver.common.by import By

from pageobjects.confirmpage import ConfirmPage


class CheckOut:
    def __init__(self,driver):
        self.driver=driver

    cardTitle=(By.XPATH, "//div[@class='card h-100']")
    submit=(By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkot=(By.XPATH, "//button[@class='btn btn-success']")
    def getCardTitles(self):
        return self.driver.find_elements(*CheckOut.cardTitle)

    item=(By.CSS_SELECTOR, ".btn-info")
    def getItems(self):
        return self.driver.find_element(*CheckOut.item)

    def checkOutitem(self):
        return self.driver.find_element(*CheckOut.submit)

    def proceed(self):
        self.driver.find_element(*CheckOut.checkot).click()
        confirmout = ConfirmPage(self.driver)
        return confirmout