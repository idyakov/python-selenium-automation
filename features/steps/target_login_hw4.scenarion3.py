from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

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
