from .pages.product_page import MainPage

def test_guest_can_add_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    product_name, product_price = page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.view_basket()
    page.is_product_name_in_basket_correct(product_name)
    page.is_product_price_in_basket_correct(product_price)

