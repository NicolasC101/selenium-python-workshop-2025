from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class MercadoSearch(BasePage):
    IPHONE_MSG = (By.CLASS_NAME, "poly-component__title")

    def isElementPresent(self, expectedSearch):
        try:
            self.find_element(self.IPHONE_MSG)
            return True
        except NoSuchElementException:
            return False
        
    def get_search_results(self):
        return self.driver.find_elements(*self.IPHONE_MSG)

    def verify_results_contain_iphone(self):
        results = self.get_search_results()
        for result in results:
            if "iPhone" in result.text:
                return True
        return False
    