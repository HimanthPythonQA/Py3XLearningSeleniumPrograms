import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options


@pytest.mark.positive

def test_mini_project_4():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    #make_appointment_btn = driver.find_element(By.XPATH,"//a[text()='Make Appointment' and contains(@id,'btn-make-appointment')]")
    make_appointment_btn = driver.find_element(By.CSS_SELECTOR,"#btn-make-appointment")

    make_appointment_btn.click()


    time.sleep(4)
    driver.quit()