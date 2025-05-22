from selenium.webdriver.common.by import By


class MainPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alert-safe strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, "div.alert-safe strong:nth-of-type(3)")
    

