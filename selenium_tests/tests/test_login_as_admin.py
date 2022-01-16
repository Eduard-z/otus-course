from selenium_tests.page_objects.LoginPage import LoginPage
from selenium_tests.page_objects.AdminPage import AdminPage


def test_login_as_admin(browser):
    login_page = LoginPage(browser=browser)
    login_page.open_login_page()
    login_page.wait_until_login_form_is_displayed()

    login_page.input_username("user")
    login_page.input_password("bitnami")
    login_page.click_login_button()
    AdminPage(browser=browser).ensure_page_is_proper(page_header_text="Dashboard")
