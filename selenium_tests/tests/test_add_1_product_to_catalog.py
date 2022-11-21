import pytest
import allure

from selenium_tests.page_objects.AdminPage import AdminPage
from selenium_tests.page_objects.admin_menu_pages.AddProductPage import AddProductPage
from selenium_tests.page_objects.admin_menu_pages.CatalogProductsPage import CatalogProductsPage
from .test_login_as_admin import test_login_as_admin as login_as_admin


@allure.feature("Add a product")
@allure.story("Add new product to Products List")
@allure.title("Add 1 new product to Products List")
@pytest.mark.parametrize("test_product_name, description, meta_tag, model",
                         [("Huawei P40", "smartphone", "Huawei", "P40 Pro 5G")])
def test_add_1_product_to_catalog(browser, test_product_name, description, meta_tag, model):
    with allure.step("Pre-condition: Login as admin"):
        login_as_admin(browser=browser)

    with allure.step("Open 'Add Product' page"):
        admin_page = AdminPage(browser=browser)
        admin_page.check_admin_page_title()
        admin_page.wait_until_menu_is_displayed()
        admin_page.open_products_list()

        catalog_products_page = CatalogProductsPage(browser=browser)
        catalog_products_page.check_products_page_title()
        catalog_products_page.click_add_new_button()

    with allure.step("Populate new product form"):
        add_product_page = AddProductPage(browser=browser)
        add_product_page.wait_until_add_product_form_is_displayed()
        add_product_page.input_product_name(test_product_name)
        add_product_page.input_description(description)
        add_product_page.input_meta_tag_title(meta_tag)

        add_product_page.switch_to_another_tab("Data")
        add_product_page.input_model(model)

    with allure.step(f"Verify product {test_product_name} created"):
        add_product_page.click_save_button()
        CatalogProductsPage(browser=browser).check_success_alert_displayed()
