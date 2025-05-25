from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def add_to_basket(self):
        product_name = self.browser.find_element(*MainPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*MainPageLocators.PRODUCT_PRICE).text
        add_to_basket_button = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        return product_name, product_price

    def is_product_name_correct(self, product_name):
        time.sleep(5)
        product_name_basket = self.browser.find_element(*MainPageLocators.PRODUCT_NAME_BASKET).text
        assert product_name == product_name_basket, f"Product name in basket is not correct: {product_name} != {product_name_basket}"

    def is_product_price_correct(self, product_price):
        time.sleep(5)
        product_price_basket = self.browser.find_element(*MainPageLocators.PRODUCT_PRICE_BASKET).text
        assert product_price == product_price_basket, f"Product price in basket is not correct: {product_price} != {product_price_basket}"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE), \
           "Success message is present, but should disappear"
