from selenium_tests.page_objects.AdminPage import AdminPage
from selenium_tests.page_objects.admin_menu_pages.CatalogProductsPage import CatalogProductsPage
from .test_login_as_admin import test_login_as_admin as login_as_admin
from .test_add_1_product import test_add_1_product as add_1_product
import pytest


@pytest.mark.parametrize("test_product_name, description, meta_tag, model",
                         [("Huawei P40", "smartphone", "Huawei", "P40 Pro 5G")])
def test_delete_1_product(browser, test_product_name, description, meta_tag, model):
    login_as_admin(browser=browser)

    admin_page = AdminPage(browser=browser)
    admin_page.wait_until_menu_is_displayed()
    admin_page.open_products_list()

    catalog_product_page = CatalogProductsPage(browser=browser)
    catalog_product_page.filter_products_by_name(test_product_name)
    if catalog_product_page.number_of_products_filtered_by_name(test_product_name) == 0:
        add_1_product(browser, test_product_name, description, meta_tag, model)
        catalog_product_page.filter_products_by_name(test_product_name)
    catalog_product_page.select_first_product()

    admin_page.delete_product()
    CatalogProductsPage(browser=browser).check_success_alert_displayed()
