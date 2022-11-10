from selenium import webdriver
import pytest

from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.checkout import CheckOut

from pageobjects.homepage import HomePage
from utilities.baseclass import baseClass


class TestOne(baseClass):

        def test_e2e(self):
                log = self.getlogger()
                hompage=HomePage(self.driver)
                self.driver.implicitly_wait(5)
                checkout=hompage.shopItems()
                log.info("getting all card items")
                items = checkout.getCardTitles()
                i =-1
                for item in items:
                        i = i+1
                        productname=item.text
                        if productname == "Blackberry":
                                checkout.getItems().click()
                checkout.checkOutitem().click()
                confirmout=checkout.proceed()
                log.info("Entering country name")
                confirmout.checkOutPage().send_keys("ind")
                self.verifyLinkPresence("India")
                self.driver.find_element(By.LINK_TEXT, "India").click()
                self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
                self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
                sucess = self.driver.find_element(By.CLASS_NAME, "alert-success").text
                log.info("text received from application is"+sucess)
                assert "Success! Thank you! " in sucess