import pytest
import allure

from selenium_tests.page_objects.LoginUserPage import LoginUserPage
from selenium_tests.page_objects.MainPage import MainPage
from selenium_tests.page_objects.RegistrationPage import RegistrationPage
from selenium_tests.page_objects.UserAccountCreatedPage import UserAccountCreatedPage
from selenium_tests.page_objects.UserAccountPage import UserAccountPage
from selenium_tests.page_objects.page_elements.OpencartHeaderElement import OpencartHeaderElement


# @pytest.mark.skip(reason="existing email_address")
@allure.feature("Register new user")
@allure.story("Create new user account")
@allure.title("Create new user account")
@pytest.mark.parametrize("user_registration_data",
                         [{"first_name": "first name test1", "last_name": "last name test1",
                           "email_address": "email@test31.ru", "telephone": "1111111",
                           "password": "password_test1", "confirm_pass": "password_test1"}
                          ])
def test_register_new_user(browser, user_registration_data):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Open Registration page"):
        header_element = OpencartHeaderElement(browser=browser)
        header_element.expand_my_account_dropdown()
        header_element.click_register_account()

        registration_page = RegistrationPage(browser=browser)
        registration_page.check_registration_page_title()
        registration_page.wait_until_registration_form_is_displayed()

    with allure.step("Populate user registration form"):
        # email_address value should be unique
        registration_page.populate_registration_fieldset(user_registration_data)
        registration_page.tick_privacy_policy_checkbox()

    with allure.step("Verify user created"):
        registration_page.click_continue_button()

        user_account_created_page = UserAccountCreatedPage(browser=browser)
        user_account_created_page.check_user_account_page_title()
        user_account_created_page.check_success_message()


@allure.feature("Register new user")
@allure.story("Create new user account")
@allure.title("Login with created user account")
@pytest.mark.parametrize("user_registration_data",
                         [{"first_name": "first name test1", "last_name": "last name test1",
                           "email_address": "email@test31.ru", "telephone": "1111111",
                           "password": "password_test1", "confirm_pass": "password_test1"}
                          ])
def test_login_as_user(browser, user_registration_data):
    with allure.step("Pre-condition: Ensure user is not logged in"):
        header_element = OpencartHeaderElement(browser=browser)
        if header_element.is_user_logged_in():
            header_element.expand_my_account_dropdown()
            header_element.click_logout()

    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Open User Account Login page"):
        header_element = OpencartHeaderElement(browser=browser)
        header_element.expand_my_account_dropdown()
        header_element.click_login_into_user_account()

        login_user_page = LoginUserPage(browser=browser)
        login_user_page.check_login_page_title()
        login_user_page.wait_until_login_form_is_displayed()

    with allure.step("Populate user login form"):
        login_user_page.input_email(user_registration_data["email_address"])
        login_user_page.input_password(user_registration_data["password"])

    with allure.step("Verify user logged in"):
        login_user_page.click_login_button()

        user_account_page = UserAccountPage(browser=browser)
        user_account_page.check_user_account_page_title()
        user_account_page.check_user_account_breadcrumb()
