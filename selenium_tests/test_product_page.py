from .page_objects.ProductPage import ProductPage


def test_product_page(browser):
    product_page = ProductPage(browser=browser)
    product_page.open_product_page()

    product_page.find_add_to_cart_button()
    product_page.find_breadcrumb_item()
    product_page.find_product_image_additional()
    product_page.find_product_info_active_tab()
    product_page.find_add_to_wishlist_button()
    product_page.find_qty_field()
