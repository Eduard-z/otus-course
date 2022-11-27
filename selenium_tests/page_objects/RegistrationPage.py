from selenium.webdriver.common.by import By
from .BasePage import BasePage


class RegistrationPage(BasePage):
    ACTION_ITEMS_COLUMN = (By.CSS_SELECTOR, "aside > div.list-group")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#content form[action]")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='firstname']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='lastname']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    TELEPHONE_FIELD = (By.CSS_SELECTOR, "input[name='telephone']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "input[name='confirm']")
    NEWSLETTER_RADIO_YES = (By.CSS_SELECTOR, "[value='1'][name='newsletter']")
    NEWSLETTER_RADIO_NO = (By.CSS_SELECTOR, "[value='0'][name='newsletter']")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, "[type='checkbox'][name='agree']")
    PRIVACY_POLICY_LINK = (By.LINK_TEXT, "Privacy Policy")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[value='Continue']")

    path = "/index.php?route=account/register"
    page_title = "Register Account"

    def open_registration_page(self):
        self.browser.get(url=self.browser.url + self.path)

    def check_registration_page_title(self, title=page_title):
        self._verify_page_title(title)

    def wait_until_registration_form_is_displayed(self):
        self._verify_element_presence(self.REGISTRATION_FORM)

    def find_action_items_column(self):
        self._verify_element_presence(self.ACTION_ITEMS_COLUMN)

    def populate_registration_fieldset(self, user_registration_dataset: dict):
        self._input_field_value(self.FIRST_NAME_FIELD, user_registration_dataset["first_name"])
        self._input_field_value(self.LAST_NAME_FIELD, user_registration_dataset["last_name"])
        self._input_field_value(self.EMAIL_FIELD, user_registration_dataset["email_address"])
        self._input_field_value(self.TELEPHONE_FIELD, user_registration_dataset["telephone"])
        self._input_field_value(self.PASSWORD_FIELD, user_registration_dataset["password"])
        self._input_field_value(
            self.PASSWORD_CONFIRM_FIELD, user_registration_dataset["confirm_pass"])

    def tick_privacy_policy_checkbox(self):
        self._click(self.PRIVACY_POLICY_CHECKBOX)

    def click_privacy_policy_link(self):
        self._click(self.PRIVACY_POLICY_LINK)

    def select_newsletter_radio_yes(self):
        self._click(self.NEWSLETTER_RADIO_YES)

    def click_continue_button(self):
        self._click(self.CONTINUE_BUTTON)
