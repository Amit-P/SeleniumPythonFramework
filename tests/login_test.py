import allure
import moment
from selenium import webdriver
import pytest
import sys
import os

import utils.utils
from utils.utils import URL, USERNAME, PASSWORD

sys.path.append(os.path.join(os.path.dirname(__file__), ".", ".."))
from pages.homePage import HomePage
from pages.loginPage import LoginPage

@pytest.mark.usefixtures("test_setup")
class TestLogin:


    def test_login(self):
        driver = self.driver
        driver.get(URL)
        login = LoginPage(driver)
        login.enter_username(USERNAME)
        login.enter_password(PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRMz"
        except AssertionError as error:
            print("Assert on error occurred")
            print(error)
            currTime = moment.now().strftime("%Y-%m-%d_%H-%M-%S")
            testName = utils.utils.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("D:/Automation/SeleniumPythonFramework/screenshots/"+screenshotName+".png")
            raise
        except:
            print("There was an exception")
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("I am inside finally block")

