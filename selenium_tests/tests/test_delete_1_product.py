import pytest
import allure

from selenium_tests.page_objects.AdminPage import AdminPage
from selenium_tests.page_objects.admin_menu_pages.CatalogProductsPage import CatalogProductsPage
from .test_login_as_admin import test_login_as_admin as login_as_admin
from .test_add_1_product import test_add_1_product as add_1_product


@allure.feature("Delete a product")
@allure.story("Delete a product from Products List")
@allure.title("Filter by name and Delete 1 product from Products List")
@pytest.mark.parametrize("test_product_name, description, meta_tag, model",
                         [("Huawei P40", "smartphone", "Huawei", "P40 Pro 5G")])
def test_delete_1_product(browser, test_product_name, description, meta_tag, model):
    login_as_admin(browser=browser)

    with allure.step("Open Products list"):
        admin_page = AdminPage(browser=browser)
        admin_page.wait_until_menu_is_displayed()
        admin_page.open_products_list()

    with allure.step(f"Search for {test_product_name} products"):
        catalog_product_page = CatalogProductsPage(browser=browser)
        catalog_product_page.filter_products_by_name(test_product_name)

    with allure.step("If no results create new product and search again"):
        if catalog_product_page.number_of_products_filtered_by_name(test_product_name) == 0:
            add_1_product(browser, test_product_name, description, meta_tag, model)
            catalog_product_page.filter_products_by_name(test_product_name)

    with allure.step(f"Delete {test_product_name} product"):
        catalog_product_page.select_first_product()

        admin_page.delete_product()
        CatalogProductsPage(browser=browser).check_success_alert_displayed()
