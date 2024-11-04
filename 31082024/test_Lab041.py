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
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(2)
    div = driver.find_element(By.XPATH,"//div[@class='jackPart']")


    # scroll to view to DIV

    driver.execute_script("arguments[0].scrollIntoView(true);", div)
    time.sleep(2)

    pizza = driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")
    pizza.send_keys("Farmhouse")

    # pizza = driver.find_element(By.ID, "pizza")
    # pizza.send_keys("Farmhouse")

    time.sleep(6)
    driver.close()