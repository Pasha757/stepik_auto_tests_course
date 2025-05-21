from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    def view_basket(self):
        view_basket_button = self.browser.find_element(*MainPageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()
    def is_product_name_in_basket_correct(self):
        assert MainPageLocators.PRODUCT_NAME.text ==  MainPageLocators.PRODUCT_NAME_BASKET.text, "Product name in basket is not correct"
    def is_product_price_in_basket_correct(self):
        assert MainPageLocators.PRODUCT_PRICE.text ==  MainPageLocators.PRODUCT_PRICE_BASKET.text, "Product price in basket is not correct"
    

