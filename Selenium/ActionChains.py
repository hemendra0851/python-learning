from selenium.webdriver.common.action_chains import ActionChains

menu = driver.find_element_by_id(“menu”)

submenu = driver.find_element_by_id(“submenu1”)

ActionChains(driver)

.move_to_element(menu)

.click(submenu)

.perform()
