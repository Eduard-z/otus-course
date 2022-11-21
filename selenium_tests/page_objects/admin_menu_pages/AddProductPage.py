from selenium.webdriver.common.by import By
from ..BasePage import BasePage


class AddProductPage(BasePage):
    list_of_product_form_tabs = ['General', 'Data', 'Links', 'Attribute', 'Option', 'Recurring',
                                 'Discount', 'Special', 'Image', 'Reward Points', 'SEO', 'Design']

    ADD_PRODUCT_FORM = (By.CLASS_NAME, "panel-body")
    FORM_TABS_ELEMENT = (By.XPATH, "//ul[contains(@class, 'nav-tabs')]")
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "input[id='input-name1']")
    META_TAG_TITLE_FIELD = (By.CSS_SELECTOR, "input[id='input-meta-title1']")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "div[role='textbox']")
    MODEL_FIELD = (By.CSS_SELECTOR, "input[name='model']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")

    def wait_until_add_product_form_is_displayed(self):
        self._verify_element_presence(self.ADD_PRODUCT_FORM)

    def switch_to_another_tab(self, tab_name: str):
        self._click_child_element(self.FORM_TABS_ELEMENT, (By.XPATH, f"//a[text()='{tab_name}']"))

    def input_product_name(self, product_name: str):
        self._input_field_value(self.PRODUCT_NAME_FIELD, product_name)

    def input_meta_tag_title(self, meta_tag_title: str):
        self._input_field_value(self.META_TAG_TITLE_FIELD, meta_tag_title)

    def input_description(self, description_text: str):
        self._input_field_value(self.DESCRIPTION_FIELD, description_text)

    def input_model(self, model_name: str):
        self._input_field_value(self.MODEL_FIELD, model_name)

    def click_save_button(self):
        self._click(self.SAVE_BUTTON)
