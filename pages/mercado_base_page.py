from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MercadoBase(BasePage):
    SEARCH_BAR = (By.ID, "cb1-edit")
    SEARCH_BTN = (By.CLASS_NAME, "nav-search-btn")

    def search(self, busqueda):
        self.enter_text(self.SEARCH_BAR, busqueda)
        self.click(self.SEARCH_BTN)