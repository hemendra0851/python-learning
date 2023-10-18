from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import robot
import time

driver = webdriver.Chrome()
driver.get("https://amazon.com")
driver.maximize_window()
# driver.
time.sleep(2)

try:
    driver.find_element_by_xpath("//div[@role='alertdialog']").click()
    driver.find_element_by_xpath("(//div[@role='alertdialog']//span)[2]//input").click()
    
except Exception:
    print("element not visible")
    
finally:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.invisibility_of_element_located((By.XPATH, "(//div[@role='alertdialog']//span)[2]//input")))

driver.find_element_by_id("twotabsearchtextbox").click()
driver.find_element_by_id("twotabsearchtextbox").send_keys('Shoes', Keys.ENTER)

element = wait.until(EC.title_contains('Shoes'))
print(driver.title)
assert driver.title == 'Amazon.com : Shoes'

driver.close()