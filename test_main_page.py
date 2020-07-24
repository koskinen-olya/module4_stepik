from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com"
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page() 
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()   

#Проверяем, что с главной страницы можно перейти на страницу входа/регистрации
def test_guest_should_see_login_link(browser):
	link = "http://selenium1py.pythonanywhere.com"
	page = MainPage(browser, link)
	page.open()
	page.should_be_login_link()

#Проверяем, что с главной страницы можно перейти в корзину
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com"
	page = MainPage(browser, link)
	page.open()
	page.go_to_basket()
	page2 = BasketPage(browser, browser.current_url)
	page2.product_basket()
	page2.message_basket()


