from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target online main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')
@when("Search for Russian hat")
def target_button_pressed(context):
    context.driver.find_element(By.ID, 'search').send_keys('russian hat')  # item search
    sleep(2)
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()  # prees the loop
    sleep(5)
    context.driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor88282075']").click()  # press the button add to cart
    sleep(5)
    context.driver.find_element(By.XPATH, "//div[@class='ReactModal__Content ReactModal__Content--after-open styles__StyledReactModal-sc-10966vp-0 cfemXU']//button[text()='Add to cart']").click()
    sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
    sleep(3)
@then("Check the input data on the page")
def target_button_pressed(context):
    item = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='cartItem-title']").text
    print(f'Here is your item - {item}. Go ahead, American boy, wear it and meet a winter time.')
    sleep(3)
    text1 = context.driver.find_element(By.CSS_SELECTOR, "div[class='styles__StyledHeading-sc-1ge2jts-1 bmsjWz']").text
    print(f'The price is {text1} including the taxes and the shipping')
    sleep(10)
##