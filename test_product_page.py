from .pages.product_page import MainPage

def open_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    return page

def test_guest_can_add_product_to_basket(browser):
    page = open_main_page(browser)
    page.add_to_basket()
    page.solve_quiz_and_get_code()

def test_are_product_name_and_price_displayed_correctly_in_basket(browser)
    page = open_main_page(browser)
    page.view_basket()
    page.is_product_name_in_basket_correct()
    page.is_product_price_in_basket_correct()

