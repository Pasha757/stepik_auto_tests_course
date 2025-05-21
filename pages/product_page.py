from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def add_to_basket(self):
        product_name = self.browser.find_element(*MainPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*MainPageLocators.PRODUCT_PRICE).text
        add_to_basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        return product_name, product_price

    def view_basket(self):
        view_basket_button = self.browser.find_element(*MainPageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()
        time.sleep(5)

    def is_product_name_in_basket_correct(self, product_name):
        product_name_basket = self.browser.find_element(*MainPageLocators.PRODUCT_NAME_BASKET).text
        assert product_name == product_name_basket, f"Product name in basket is not correct: {product_name} != {product_name_basket}"

    def is_product_price_in_basket_correct(self, product_price):
        product_price_basket = self.browser.find_element(*MainPageLocators.PRODUCT_PRICE_BASKET).text
        assert product_price == product_price_basket, f"Product price in basket is not correct: {product_price} != {product_price_basket}"

    

