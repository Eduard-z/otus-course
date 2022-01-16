from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage
from selenium.common.exceptions import TimeoutException


class RegistrationPage(BasePage):
    ACTION_ITEMS_COLUMN = (By.CSS_SELECTOR, "aside > div.list-group")
    PERSONAL_DETAILS_FIELDSET = (By.CSS_SELECTOR, "fieldset#account")
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

    def open_registration_page(self):
        self.browser.get(url=self.browser.url + self.path)

    def wait_until_page_title_is_displayed(self, title):
        try:
            WebDriverWait(driver=self.browser, timeout=1).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError(f"Expected title = '{title}' but it is '{self.browser.title}'")

    def find_action_items_column(self):
        self._verify_element_presence(self.ACTION_ITEMS_COLUMN)

    def find_personal_details_fieldset(self):
        self._verify_element_presence(self.PERSONAL_DETAILS_FIELDSET)

    def populate_registration_fieldset(self, first_name, last_name, email_address,
                                       telephone, password, confirm_password):
        self._input_field_value(self.FIRST_NAME_FIELD, first_name)
        self._input_field_value(self.LAST_NAME_FIELD, last_name)
        self._input_field_value(self.EMAIL_FIELD, email_address)
        self._input_field_value(self.TELEPHONE_FIELD, telephone)
        self._input_field_value(self.PASSWORD_FIELD, password)
        self._input_field_value(self.PASSWORD_CONFIRM_FIELD, confirm_password)

    def tick_privacy_policy_checkbox(self):
        self.browser.find_element(*self.PRIVACY_POLICY_CHECKBOX).click()

    def find_privacy_policy_link(self):
        self._verify_element_presence(self.PRIVACY_POLICY_LINK)

    def find_newsletter_radio_yes(self):
        self._verify_element_presence(self.NEWSLETTER_RADIO_YES)

    def click_continue_button(self):
        self.browser.find_element(*self.CONTINUE_BUTTON).click()
