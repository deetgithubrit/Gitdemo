import pytest

from pageobjects.homepage import HomePage
from utilities.baseclass import baseClass


class TestHomePage(baseClass):

    def test_formSubmission(self,getData):
        homepage=HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getPassword().send_keys(getData["lastname"])
        homepage.getSubmit().click()
        self.selectOption(homepage.getGender(),getData["gender"])
        homepage.getRadio().click()
        homepage.getSucess().click()
        message = homepage.getMessaged().text

    @pytest.fixture(params=[{"firstname":"rahul","lastname":"shetty","gender":"Male"}])
    def getData(self,request):
        return request.param