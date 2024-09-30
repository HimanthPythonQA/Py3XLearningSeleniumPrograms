import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
@pytest.mark.positive
def test_katalon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    allure.attach(driver.get_screenshot_as_png(), name="step1_open_url", attachment_type=AttachmentType.PNG)

    make_appoin = driver.find_element(By.CSS_SELECTOR,"#btn-make-appointment")
    make_appoin.click()

    WebDriverWait(driver=driver, timeout=7).until(EC.url_contains("profile.php#login"))

    allure.attach(driver.get_screenshot_as_png(), name="step2_login_page", attachment_type=AttachmentType.PNG)

    username = driver.find_element(By.CSS_SELECTOR, "#txt-username")
    password = driver.find_element(By.CSS_SELECTOR, "#txt-password")
    username.send_keys("John Doe")
    password.send_keys("ThisIsNotAPassword")

    WebDriverWait(driver=driver,timeout=3).until(EC.element_to_be_clickable(((By.CSS_SELECTOR, "#btn-login"))))

    btn_login = driver.find_element(By.CSS_SELECTOR,"#btn-login")
    btn_login.click()

    allure.attach(driver.get_screenshot_as_png(), name="step3_login_click", attachment_type=AttachmentType.PNG)

    WebDriverWait(driver=driver, timeout=13).until(EC.url_contains("#appointment"))

    h2_element = driver.find_element(By.XPATH,"//h2[text()='Make Appointment']")
    allure.attach(driver.get_screenshot_as_png(),name="step4_verify_login_click", attachment_type=AttachmentType.PNG)
    assert h2_element.text == "Make Appointment"

    driver.quit()

