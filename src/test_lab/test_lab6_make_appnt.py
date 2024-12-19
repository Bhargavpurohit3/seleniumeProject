from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_chrome_confirm_url():
    driver = webdriver.Chrome()   #choose the which browser you want to use
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    #1-Find Element Anchor Tag
    #2-we need to find the unoque element id it can be id  or name or anythig

    make_apointment_element = driver.find_element(By.ID,value="btn-make-appointment")

    #3.by click
    make_apointment_element.click()
    #4 login details

    login_user_name = driver.find_element(By.ID,value="txt-username")
    login_user_name.send_keys("John Doe")

    login_password = driver.find_element(By.ID,value="txt-password")
    login_password.send_keys("ThisIsNotAPassword")

    submit = driver.find_element(By.ID,value="btn-login")
    time.sleep(3)
    submit.click()

    #c. confirm url
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(10)

    driver.quit()