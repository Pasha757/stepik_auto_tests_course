from .pages.product_page import MainPage
import pytest

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="Product name is not correct")),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#def test_guest_can_add_product_to_basket(browser):
#    page = MainPage(browser, link)
#    page.open()
#    product_name, product_price = page.add_to_basket()
#    #page.solve_quiz_and_get_code()
#    page.is_product_name_correct(product_name)
#    page.is_product_price_correct(product_price)

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    product_name, product_price = page.add_to_basket()
    #page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)
    page.open()
    #page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    product_name, product_price = page.add_to_basket()
    #page.solve_quiz_and_get_code()
    page.success_message_should_disappear()
