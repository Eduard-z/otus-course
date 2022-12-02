from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button#button-cart")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, ".btn-group > button[data-original-title='Add to Wish List']")
    QTY_FIELD = (By.CSS_SELECTOR, "[name='quantity']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".btn-group ~ h1")
    FACEBOOK_IFRAME = (By.CSS_SELECTOR, "iframe[title='fb:like Facebook Social Plugin']")
    FACEBOOK_BUTTON = (By.CSS_SELECTOR, "#facebook button[title='Like']")
    TWITTER_BUTTON = (By.CSS_SELECTOR, "#widget a[href]")
    TWITTER_IFRAME = (By.CSS_SELECTOR, "iframe#twitter-widget-0")

    def click_add_to_cart_button(self):
        self._click(self.ADD_TO_CART_BUTTON)

    def click_add_to_wishlist_button(self):
        self._click(self.ADD_TO_WISHLIST_BUTTON)

    def find_qty_field(self):
        self._verify_element_presence(self.QTY_FIELD)

    @property
    def product_name(self) -> str:
        return self._verify_element_presence(self.PRODUCT_NAME).text

    def check_facebook_button_colour(self, button_colour: str):
        self._verify_iframe_button_colour(self.FACEBOOK_IFRAME, self.FACEBOOK_BUTTON, colour=button_colour)

    def check_twitter_button_colour(self, button_colour: str):
        self._verify_iframe_button_colour(self.TWITTER_IFRAME, self.TWITTER_BUTTON, colour=button_colour)

    def switch_to_main_browser_tab(self):
        self._switch_to_another_browser_tab("")

    def switch_to_new_browser_tab(self, stored_browser_tabs: list, opened_page_title: str):
        self._switch_to_another_browser_tab(self._get_new_window_name(stored_browser_tabs))
        self._verify_page_title(opened_page_title)

    @property
    def all_browser_windows(self) -> list:
        return self._get_browser_all_windows()

    def is_new_browser_tab_opened(self, stored_browser_tabs: list) -> bool:
        return self._verify_new_window_is_open(stored_browser_tabs)

    def click_facebook_like(self):
        self._click_social_net_widget(self.FACEBOOK_IFRAME, self.FACEBOOK_BUTTON)

    def click_twitter_tweet(self):
        self._click_social_net_widget(self.TWITTER_IFRAME, self.TWITTER_BUTTON)
