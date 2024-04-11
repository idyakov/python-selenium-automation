from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main circle page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

@when("The page is opened verify the benefits")
def target_benefits_verification(context):
    expected = 6
    deals = context.driver.find_elements(By.XPATH,'//div[@data-component-id="WEB-397697"] //a[@data-test="@web/slingshot-components/CellsComponent/Link"]')
    numbers = int(len(deals))
    assert expected == numbers
    print(f'Expected deals {expected}, got {numbers}. Gongrats! Go and take your cookies from the table.')
    sleep(3)


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
    sleep(8)
    context.driver.find_element(By.XPATH, "//div[@class='ReactModal__Content ReactModal__Content--after-open styles__StyledReactModal-sc-10966vp-0 cfemXU']//button[text()='Add to cart']").click()
    sleep(8)
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
    sleep(5)
@then("Check the input data on the page")
def target_button_pressed(context):
    item = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='cartItem-title']").text
    print(f'Here is your item - {item}. Go ahead, American boy, wear it and meet a winter time.')
    sleep(3)
    text1 = context.driver.find_element(By.CSS_SELECTOR, "div[class='styles__StyledHeading-sc-1ge2jts-1 bmsjWz']").text
    print(f'The price is {text1} including the taxes and the shipping')
    sleep(10)

@given('Open Target online help ui page')
def open_target_help_page(context):
    context.driver.get('https://help.target.com/help')
@when("Verify UI elements")
def open_target_help_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "h2[class='custom-h2']")
    print("Target help header - passed")
    context.driver.find_element(By.ID, 'j_id0:j_id2:j_id32:name')
    print("Target search panel - passed")
    context.driver.find_element(By.CSS_SELECTOR, "input[class='btn-sm search-btn']")
    print("Target search loop icon - passed")
    context.driver.find_element(By.CSS_SELECTOR, "div[class='container clearfix']")
    print("Target action steps to do - passed")
    context.driver.find_element(By.CSS_SELECTOR, "div[class='salesforceBox txtAC bigbox1']")
    print("Target Manage my lines - passed")
    context.driver.find_element(By.CSS_SELECTOR, "div[class='grid_4 boxSmallr txtAC bigbox2']")
    print("Target Contact us - passed")
    context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']")
    print("Target Browse all help pages - passed")
    sleep(5)
