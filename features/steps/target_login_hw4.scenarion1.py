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

##