from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import ait

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-notifications')
options.add_argument("--guest")
options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=options)
driver.get('https://demo.automationtesting.in/Register.html')
driver.maximize_window()
driver.implicitly_wait(10)
driver.save_screenshot('1.png')

driver.find_element(By.XPATH, "//input[@ng-model='FirstName']").send_keys('Test')
driver.find_element(By.XPATH, "//input[@ng-model='LastName']").send_keys('User')
driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys('City Name')
driver.find_element(By.XPATH, "//input[@ng-model='EmailAdress']").send_keys('testuser@example.com')
driver.find_element(By.XPATH, "//input[@ng-model='Phone']").send_keys('1234567891')
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.XPATH, "//input[@value='Cricket']").click()
driver.find_element(By.XPATH, "//input[@value='Movies']").click()

driver.find_element(By.ID, "msdd").click()
WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='msdd']/following-sibling::div")))
driver.find_element(By.XPATH, "//li/a[text()='Arabic']").click()

actions = ActionChains(driver=driver)
actions.move_to_element(driver.find_element(By.XPATH, "//div[@id='msdd']/following-sibling::div")).perform()
actions.scroll_to_element(driver.find_element(By.XPATH, "//li/a[text()='Hindi']")).perform()
actions.pause(1).move_to_element(driver.find_element(By.XPATH, "//li/a[text()='Hindi']")).click().perform()
actions.move_by_offset(xoffset=100, yoffset=100).click().perform()

skills = Select(driver.find_element(By.ID, 'Skills'))
skills.select_by_value('APIs')

country = Select(driver.find_element(By.ID, 'country'))
country.select_by_value('India')

actions.move_to_element(driver.find_element(By.ID, 'imagesrc')).click().perform()
sleep(0.5)
ait.write(r"C:\Users\sheme\.emulator_console_auth_token")
sleep(0.5)
ait.press('enter')
driver.save_screenshot('2.png')
sleep(1)
ait.press('esc')
# driver.refresh()
# driver.quit()