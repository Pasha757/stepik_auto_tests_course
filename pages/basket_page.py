from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
import time


class BasketPage(BasePage):
    def should_be_text_that_basket_is_empty(self):
        self.go_to_basket_page()
        basket_text = self.browser.find_element(*BasePageLocators.BASKET_EMPTY_TEXT).text
        assert "Your basket is empty" in  basket_text, "Your basket is not empty"
