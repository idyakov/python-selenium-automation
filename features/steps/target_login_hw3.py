from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when("Target cart button pressed")
def target_button_pressed(context):
    context.driver.find_element(By.XPATH, "//div[@class='styles__CartIconDiv-sc-jff2tp-1 bECXM']").click()
    sleep(2)


@then("Verify the cart is empty shown")
def verify_cart_is_empty(context):
    expected = 'Your cart is empty'
    text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']").text
    assert expected == text, f'Expected text {expected}, got {text}'
    print("the verification of the element in the code has been successful.")
    sleep(3)

@given('Open Target main page for signin functionality')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')

@when("Target Signin button pressed")
def target_signin_button_pressed(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

@then("Verify Sign In form opened")
def verify_signin_form_opened(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'StyledHeading')]").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'
# Make sure login button is shown
    print(f'The text "{actual}" shown in the page')
    print("The test cases follow the principles of BDD and work correctly")
    sleep(3)