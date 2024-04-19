from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target online help ui page')
def open_target_help_page(context):
    context.driver.get('https://help.target.com/help')
@when("Verify UI elements")
def open_target_help_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "h2[class='custom-h2']") #Target help header
    context.driver.find_element(By.ID, 'j_id0:j_id2:j_id32:name') #"Target search panel
    context.driver.find_element(By.CSS_SELECTOR, "input[class='btn-sm search-btn']") #Target search loop icon
    context.driver.find_element(By.CSS_SELECTOR, "div[class='container clearfix']") #Target action steps to do
    context.driver.find_element(By.CSS_SELECTOR, "div[class='salesforceBox txtAC bigbox1']") #Target Manage my lines
    context.driver.find_element(By.CSS_SELECTOR, "div[class='grid_4 boxSmallr txtAC bigbox2']") #Target Contact us
    context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']") #Target Browse all help pages - passed
    sleep(5)