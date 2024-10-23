import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_032_actions():
    driver = webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()

    source = driver.find_element(By.XPATH,"//div[@data-testid='search-source-code']")
    actions = ActionChains(driver)
    actions.move_to_element(source).click().send_keys("BLR").perform()

    time.sleep(5)
    driver.quit()