from selenium.webdriver.common.by import By


class MainPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1").text
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color").text
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn[href = '/en-gb/basket/']")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a").text
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".col-sm-2 .price_color").text
    

