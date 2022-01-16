from selenium_tests.page_objects.RegistrationPage import RegistrationPage
from selenium_tests.page_objects.UserAccountCreatedPage import UserAccountCreatedPage
import pytest


@pytest.mark.parametrize("user_registration_data",
                         [{"first_name": "first name test1", "last_name": "last name test1",
                           "email_address": "email@test14.ru", "telephone": "1111111",
                           "password": "password_test1", "confirm_pass": "password_test1"}
                          ])
def test_register_new_user(browser, user_registration_data):
    registration_page = RegistrationPage(browser=browser)
    registration_page.open_registration_page()
    registration_page.wait_until_page_title_is_displayed("Register Account")

    # email_address value should be unique
    registration_page.populate_registration_fieldset(user_registration_data)
    registration_page.tick_privacy_policy_checkbox()
    registration_page.click_continue_button()
    UserAccountCreatedPage(browser=browser).check_success_message()
