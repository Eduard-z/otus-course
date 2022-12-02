from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ..BasePage import BasePage


class ProductCardElement(BasePage):
    PRODUCT_CARD = (By.CSS_SELECTOR, ".product-thumb")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption a")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".button-group button:nth-of-type(1)")

    @property
    def all_product_cards_elements(self) -> list[WebElement]:
        return self.browser.find_elements(*self.PRODUCT_CARD)

    @property
    def all_product_names_elements(self) -> list[WebElement]:
        return [i.find_element(*self.PRODUCT_NAME) for i in self.all_product_cards_elements]

    @property
    def all_product_names(self) -> list:
        return [i.text for i in self.all_product_names_elements]

    def compare_card_names_to_search_text(self, search_text: str) -> bool:
        search_keywords = search_text.lower().split()
        for name in (i.lower() for i in self.all_product_names):
            for word in search_keywords:
                if word not in name:
                    return False
            return True

    def click_add_to_cart_button(self, card_element: WebElement):
        self._click_child_element(card_element, self.ADD_TO_CART_BUTTON)

    def click_into_first_product_card(self):
        self._click(self.PRODUCT_NAME)
