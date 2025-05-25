from selenium.webdriver.common.by import By


class MainPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alert-safe strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, "div.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn[href='/en-gb/basket/']")
    BASKET_EMPTY_TEXT =  (By.CSS_SELECTOR, "#content_inner p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")
