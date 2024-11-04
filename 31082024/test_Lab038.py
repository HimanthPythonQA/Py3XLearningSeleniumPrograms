import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_dragdrop():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    driver.maximize_window()

    actions = ActionChains(driver)
    from_element = driver.find_element(By.XPATH,"//div[@id='column-a']")
    to_element = driver.find_element(By.XPATH,"//div[@id='column-b']")

    actions.click_and_hold(from_element).move_to_element(to_element).release(to_element).perform()
    #actions.drag_and_drop(from_element,to_element)/ sometimes give error with firefox and other drivers


    time.sleep(8)
    driver.close()