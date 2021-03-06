from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
	LOGIN_URL = (By.CSS_SELECTOR, "#login_link_inc")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	LOGIN_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
	EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
	PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
class ProductPageLocators():
	BUTTON_ADD = (By.CSS_SELECTOR, "#add_to_basket_form > button")
	BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
	BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
	BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
	BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_URL = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_BUTTON =(By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
	MESSAGE_NONE_BUSKET = (By.CSS_SELECTOR, "#content_inner > p")
	BASKET_PRODUCT = (By.CSS_SELECTOR, "#id_form-0-quantity")

