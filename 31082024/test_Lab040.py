import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_javascript():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    #java script executor
    button = driver.find_element(By.XPATH,"//button[@onclick='addElement()']")
    # button.click()


    # using javascript code to click on this button
    js_ex = driver.execute_script
    js_ex("arguments[0].click",button)
    js_ex("arguments[0].scrollIntoView(true);", div)

    time.sleep(6)
    driver.close()