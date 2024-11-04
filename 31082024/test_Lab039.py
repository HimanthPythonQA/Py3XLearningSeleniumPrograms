import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_shadowdom():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    driver.maximize_window()
    div = driver.find_element(By.XPATH,"//div[@class='jackPart']")

    # scroll to view to div
    # Handle the shadow dom
    # click on pizza

    pizza = driver.find_element(By.ID,"pizza")
    pizza.send_keys("Farmhouse")




    time.sleep(6)
    driver.close()