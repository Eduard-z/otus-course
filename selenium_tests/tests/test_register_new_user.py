from selenium_tests.page_objects.RegistrationPage import RegistrationPage
from selenium_tests.page_objects.UserAccountCreatedPage import UserAccountCreatedPage
import pytest


@pytest.mark.parametrize("first_name, last_name, email_address, phone, password, confirm_pass",
                         [("first name test1", "last name test1", "email@test12.ru",
                           "1111111", "password_test1", "password_test1")
                          ])
def test_register_new_user(browser, first_name, last_name, email_address,
                           phone, password, confirm_pass):
    registration_page = RegistrationPage(browser=browser)
    registration_page.open_registration_page()
    registration_page.wait_until_page_title_is_displayed("Register Account")

    # email value should be unique
    registration_page.populate_registration_fieldset(
        first_name, last_name, email_address, phone, password, confirm_pass)
    registration_page.tick_privacy_policy_checkbox()
    registration_page.click_continue_button()
    UserAccountCreatedPage(browser=browser).check_success_message()
