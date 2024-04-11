from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/l/target-circle/-/N-pzno9')
sleep(3)
# #step cases
# #Find the logo



expected = 6
deals = driver.find_elements(By.XPATH, '//div[@data-component-id="WEB-397697"] //a[@data-test="@web/slingshot-components/CellsComponent/Link"]')
numbers = int(len(deals))
print(numbers)
assert expected == numbers
print(f'Expected deals {expected}, got {numbers}')
sleep(3)



















#
# driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# print("Test case - passed. Logo has been found")
# #Find email field # selector #ap_email
# driver.find_element(By.XPATH, "//input[@type='email']")
# print("Test case by the type - email - passed. Email field has been found")
# driver.find_element(By.XPATH, "//input[@id='ap_email']")
# print("Test case by ID - ap_email - passed. Email field has been found")
# #Find Cintinue button #
# driver.find_element(By.XPATH, "//input[@id='continue']")
# print("Test case Continue button - by id - passed.")
# driver.find_element(By.XPATH, "//input[@class='a-button-input']")
# print("Test case Continue button - by class - passed.")
# driver.find_element(By.XPATH, "//*[contains(@class, 'a-button-input')]")
# print("Test case Continue button - by contains - passed.")
# driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
# print("Test case Privacy Notice - by Text - passed.")
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# print("Test case <Need help?> - by tag span and the attribute class - passed.")
# driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
# print("Test case <Forgot your password?> - by tag id - passed.")
# driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link' and contains(@href, 'account-issues')]")
# print("Test case <Other issues with Sign-In> - by id - passed.")
# driver.find_element(By.ID, 'createAccountSubmit')
# print("Test case <Create your Amazon account> - by id - passed.")
# driver.find_element(By.XPATH,"//a[@id='createAccountSubmit' and contains(@href, 'ap')]")
# print("Test case <Create your Amazon account> - by id and contains (portion) - passed.")