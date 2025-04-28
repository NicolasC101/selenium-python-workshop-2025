from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class IntuLogin(BasePage):
    USER_NAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "logibtn")
    ERROR_MSG = (By.CLASS_NAME, "alert alert-danger")

    def login(self, username, password):
        self.enter_text(self.USER_NAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)

    def isElementPresent(self):
        try:
            self.find_element(self.ERROR_MSG)
            return True
        except NoSuchElementException:
            return False
    