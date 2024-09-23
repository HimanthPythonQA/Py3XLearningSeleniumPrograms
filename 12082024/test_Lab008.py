import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options


@pytest.mark.positive
@allure.title("VWO Invalid Login page-test_mini_project_2")
@allure.description("verify with invalid email,password. Error message pops up")
def test_mini_project_2():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url == "https://app.vwo.com/#/login"

    # ID-->Name-->classname-->link/partial(works with anchor<)-->tagname-->CSS Selector-->xpath
    # find the Email-password and enter the invalid details
    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    #email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element = driver.find_element(By.NAME, "username")
    email_web_element.send_keys("wbabblu85@gmail.com")

   #< input
   # type = "password"
   #class ="text-input W(100%)"
   # name="password"
   # id="login-password"
   # data-qa="jobodapuxe"


    password_web_element = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    password_web_element.send_keys("prihim@123")

    # <button
    # type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica"
    # fdprocessedid="10giac">
    # <span class="icon loader hidden"
    # data-qa="zuyezasugu">
    # </span>
    # <span data-qa="ezazsuguuy">Sign in</span>
    # </button>

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    time.sleep(4)

    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match</div>

    error_message_web_element = driver.find_element(By.ID,"js-notification-box-msg")
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
    driver.quit()
