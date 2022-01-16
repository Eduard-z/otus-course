from .page_objects.RegistrationPage import RegistrationPage


def test_registration_page(browser):
    RegistrationPage(browser=browser).open_registration_page()

    RegistrationPage(browser=browser).wait_until_page_title_is_displayed("Register Account")
    RegistrationPage(browser=browser).find_action_items_column()
    RegistrationPage(browser=browser).find_personal_details_fieldset()
    RegistrationPage(browser=browser).find_privacy_policy_link()
    RegistrationPage(browser=browser).find_newsletter_radio_yes()
