import allure

from allure_commons.types import Severity
from .page_objects.LoginPage import LoginPage


@allure.story("Elements validation")
@allure.title("Find elements on Login page")
@allure.severity(severity_level=Severity.MINOR)
def test_login_page(browser):
    login_page = LoginPage(browser=browser)
    login_page.open_login_page()

    login_page.wait_until_login_form_is_displayed()
    login_page.find_forgotten_password_link()
    login_page.find_link_to_opencart_site()
