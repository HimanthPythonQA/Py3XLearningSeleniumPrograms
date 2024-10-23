import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_031_actions():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))
    driver.find_element(By.XPATH,"//span[@data-cy='closeModal']").click()

    time.sleep(3)

    fromCity = driver.find_element(By.ID,"fromCity")

    actions = ActionChains(driver)
    (actions.move_to_element(fromCity).click().send_keys("Mumbai").key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform())

    time.sleep(9)
    driver.close()