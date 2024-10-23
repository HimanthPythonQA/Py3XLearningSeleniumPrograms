import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_028_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")
    #first_name.send_keys("thetestingacademy")
    # for entering capital letters e.g---> THETESTINGACADEMY
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"thetestingacademy").key_up(Keys.SHIFT).perform()




    time.sleep(6)
    driver.close()