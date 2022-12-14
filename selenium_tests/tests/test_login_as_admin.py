import allure

from selenium_tests.page_objects.LoginAdminPage import LoginAdminPage
from selenium_tests.page_objects.AdminPage import AdminPage


@allure.feature("Authorization")
@allure.story("Login as Admin")
def test_login_as_admin(browser):
    with allure.step("Open Login page"):
        login_page = LoginAdminPage(browser=browser)
        login_page.open_login_page()
        login_page.check_login_page_title()
        login_page.wait_until_login_form_is_displayed()

    with allure.step("Input credentials and log in"):
        login_page.input_username()
        login_page.input_password()
        login_page.click_login_button()
        AdminPage(browser=browser).check_admin_page_title()
