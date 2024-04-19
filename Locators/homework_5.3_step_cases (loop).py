from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
#wait = WebDriverWait(driver, timeout=15)
#implicit
driver.implicitly_wait(4) #up to 4 sec
# explicit
#driver.wait = WebDriverWait(driver, timeout=10)
driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCarWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")

#Scenarion_1
expected = 6
deals = driver.find_elements(By.XPATH,'//div[@data-component-id="WEB-397697"] //a[@data-test="@web/slingshot-components/CellsComponent/Link"]')
numbers = int(len(deals))
assert expected == numbers
print(f'Expected deals {expected}, got {numbers}. Gongrats! ')
# sleep(3)


#Scenarion_2
driver.get('https://www.target.com/')

driver.find_element(By.ID, 'search').send_keys('car')  # item search

driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Press the loop
sleep(5) # I left sleep function here, because without it, it's failed, even if I do implicit wait. I think the Target has this issue.
driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor15280655']").click()  # press the button add to cart
sleep(8) # Same, I left sleep function here, because without it, it's failed, even if I do implicit wait. I think the Target has this issue.
driver.find_element(By.XPATH, "//div[@class='styles__ThreeUpButtonWrapper-sc-11rka0i-0 gfFifD']//button[text()='Add to cart']").click()
#sleep(8)

driver.find_element(By.XPATH, "//div[@class='h-margin-t-default']//button[text()='Decline coverage']").click() #click Decline coverage
#sleep(5)
driver.find_element(By.CSS_SELECTOR, "div[class='styles__CartIconDiv-sc-jff2tp-1 bECXM']").click()
#sleep(5)
text1 = driver.find_element(By.CSS_SELECTOR, "div[class='styles__StyledHeading-sc-1ge2jts-1 bmsjWz']").text
print(f'The price is {text1} including the taxes and the shipping')
#sleep(7)


#Scenarion_3
driver.get('https://help.target.com/help')

driver.find_element(By.CSS_SELECTOR, "h2[class='custom-h2']") #Test Target help header
driver.find_element(By.ID, 'j_id0:j_id2:j_id32:name') #Test Target search panel
driver.find_element(By.CSS_SELECTOR, "input[class='btn-sm search-btn']") #Test Target search loop icon
driver.find_element(By.CSS_SELECTOR, "div[class='container clearfix']") #Test Target action steps to do
driver.find_element(By.CSS_SELECTOR, "div[class='salesforceBox txtAC bigbox1']") #Test Target Manage my lines
driver.find_element(By.CSS_SELECTOR, "div[class='grid_4 boxSmallr txtAC bigbox2']") #Test Target Contact us
driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']") #Test Target Browse all help pages
print("All buttons of the Target pages - passed, within Implicit wait option")
sleep(5)
