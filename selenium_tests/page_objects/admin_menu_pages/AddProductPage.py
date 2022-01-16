from selenium.webdriver.common.by import By
from ..BasePage import BasePage


class AddProductPage(BasePage):
    list_of_product_form_tabs = ['General', 'Data', 'Links', 'Attribute', 'Option',
                                 'Recurring', 'Discount', 'Special', 'Image',
                                 'Reward Points', 'SEO', 'Design']

    ADD_PRODUCT_FORM = (By.CLASS_NAME, "panel panel-default")
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "input[id='input-name1']")
    META_TAG_TITLE_FIELD = (By.CSS_SELECTOR, "input[id='input-meta-title1']")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "div[role='textbox']")
    MODEL_FIELD = (By.CSS_SELECTOR, "input[name='model']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")

    def wait_until_add_product_form_is_displayed(self):
        self._verify_element_presence(self.ADD_PRODUCT_FORM)

    def switch_to_another_tab(self, tab_name):
        self.browser.find_element(By.XPATH, f"//ul[contains(@class, 'nav-tabs')]"
                                            f"//a[text()='{tab_name}']").click()

    def input_product_name(self, product_name):
        product_name_field = self._verify_element_presence(self.PRODUCT_NAME_FIELD)
        product_name_field.click()
        product_name_field.clear()
        product_name_field.send_keys(product_name)

    def input_meta_tag_title(self, meta_tag_title):
        meta_tag_title_field = self._verify_element_presence(self.META_TAG_TITLE_FIELD)
        meta_tag_title_field.click()
        meta_tag_title_field.clear()
        meta_tag_title_field.send_keys(meta_tag_title)

    def input_description(self, description_text):
        description_field = self._verify_element_presence(self.DESCRIPTION_FIELD)
        description_field.click()
        description_field.clear()
        description_field.send_keys(description_text)

    def input_model(self, model_name):
        model_field = self._verify_element_presence(self.MODEL_FIELD)
        model_field.click()
        model_field.clear()
        model_field.send_keys(model_name)

    def click_save_button(self):
        self.browser.find_element(*self.SAVE_BUTTON).click()
