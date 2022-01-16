from .page_objects.MainPage import MainPage


def test_main_page(browser):
    main_page = MainPage(browser=browser)
    main_page.open_main_page()

    main_page.find_navigation_bar()
    main_page.find_my_account_dropdown()
    main_page.find_search_field()
    main_page.find_cart_button()
    main_page.find_your_store_link()
    main_page.find_product_item_card()
