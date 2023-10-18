from selenium import webdriver
# from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import ait

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-notifications')
options.add_argument("--guest")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('https://demo.automationtesting.in/Dynamic.html')
driver.maximize_window()
driver.implicitly_wait(3)

actions = ActionChains(driver=driver)

def mouse_hover():

    el1= driver.find_element(By.LINK_TEXT, 'SwitchTo')
    actions.move_to_element(to_element=el1).pause(1).perform()
    el2= driver.find_element(By.LINK_TEXT, 'Alerts')
    actions.move_to_element(to_element=el2).perform()

def drag_and_drop():

    driver.get("https://demoqa.com/droppable")
    el1 = driver.find_element(By.ID, 'draggable')
    el2 = driver.find_element(By.ID, 'droppable')
    actions.drag_and_drop(source=el1, target=el2).perform()

def resize():

    driver.get("https://demoqa.com/resizable")
    resize = driver.find_element(By.XPATH, "//div[@id='resizableBoxWithRestriction']//span")
    actions.drag_and_drop_by_offset(source=resize, xoffset=200, yoffset=100).perform()

def multiselect():

    driver.get("https://demo.automationtesting.in/Selectable.html")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Serialize").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(locator=(By.ID,"feedback"), text_="You've selected: None:"))
    items = driver.find_elements(By.XPATH, "//ul[@class='SerializeFunc']//li")
    actions.key_down(Keys.CONTROL).click(on_element=items[1]).click(on_element=items[3]).click(on_element=items[5]).key_up(Keys.CONTROL).click(on_element=items[5]).perform()

resize()
sleep(2)
driver.quit()