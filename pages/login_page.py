from base.base_page import BasePage
from config.links import Links

class LoginPage(BasePage):

    PAGE_URL = Links.LODGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")

    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
