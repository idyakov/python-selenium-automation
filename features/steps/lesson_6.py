from selenium.webdriver.common.by import By
from behave import then, given, when
from time import sleep

SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, 'div[data-test="cartItem-title"]')
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_POP_UP = (By.XPATH, "//div[@class='ReactModal__Content ReactModal__Content--after-open styles__StyledReactModal-sc-10966vp-0 cfemXU']//button[text()='Add to cart']")
VIEW_CART_AND_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a[href="/cart"]')

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    # context.app.main_page.open_main()


@when("Search for {item}")
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)
    # context.app.header.search_product(item)



@when("Click add to cart")
def step_impl(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(5)
    context.driver.find_element(*ADD_TO_CART_BTN_POP_UP).click()
    sleep(6)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*VIEW_CART_AND_CHECKOUT_BTN).click()
    sleep(6)


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    assert expected_item in actual_text.lower(), f'Error! Text {expected_item} not in {actual_text}'
   # context.app.search_result_page.verify_search_results(expected_item)



@then('Verify that product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(4)
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    #
    # all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]
    top_products = context.driver.find_elements(*LISTINGS)[:4]  # list of the web elements
    #     for product in all_products:
    #         title = product.find_element(*PRODUCT_TITLE).text
    #         assert title, 'Product title not shown'
    #         product.find_element(*PRODUCT_IMG)

    for product in top_products:
        title = context.driver.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title != '', 'Product title not shown'
        product.find_element(*PRODUCT_IMG)
