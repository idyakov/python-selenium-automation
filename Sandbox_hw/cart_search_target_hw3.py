from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome browser:
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open target.com
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//div[@class='styles__CartIconDiv-sc-jff2tp-1 bECXM']").click()

text1 = driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']").text
print(f'The text {text1} shown in the page by class ')
sleep(2)
driver.quit()