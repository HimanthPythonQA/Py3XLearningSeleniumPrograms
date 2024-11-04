import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    button = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    button.click()


    wait = WebDriverWait(driver,10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("himanth")
    alert.accept()
    #alert.dismiss()

    time.sleep(3)
    result = driver.find_element(By.XPATH,"//p[@id='result']")
    print(result.text)
    assert "himanth" in result.text







    time.sleep(8)
    driver.close()