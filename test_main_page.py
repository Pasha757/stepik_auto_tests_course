from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_text_that_basket_is_empty()

@pytest.mark.login_guest
class TestLoginFromMainPage():
     def test_guest_should_see_login_link_on_product_page(self, browser):
         link = "http://selenium1py.pythonanywhere.com/en-gb/"
         page = MainPage(browser, link)
         page.open()
         page.should_be_login_link()

     def test_guest_can_go_to_login_page_from_product_page(self, browser):
         link = "http://selenium1py.pythonanywhere.com/en-gb/"
         page = MainPage(browser, link)
         page.open()
         page.go_to_login_page()

