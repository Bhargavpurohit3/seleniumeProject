import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


def test_action_chain_keybord():

    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search = driver.find_element(By.ID,"APjFqb")

    act = ActionChains(driver=driver)
    (act.key_down(Keys.SHIFT)
     .send_keys_to_element(search,"bhargav")
     .key_up(Keys.SHIFT).perform()
     )
    time.sleep(2)

    submit = driver.find_element(By.CLASS_NAME,"gNO89b")
    submit.click()

    #robot captcha pop up
