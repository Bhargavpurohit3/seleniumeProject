import time
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
import allure_result


@allure.description("negetive test cases")

def test_neg_test_login():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    login_vwo = driver.find_element(By.ID,value="login-username")
    login_vwo.send_keys("abc@gmail.com")

    pass_vwo  = driver.find_element(By.ID,value="login-password")
    pass_vwo.send_keys("bhargv")

    submit_vwo = driver.find_element(By.ID,value="js-login-btn")
    submit_vwo.click()

    time.sleep(3)

    error_msg_login_vwo = driver.find_element(By.ID,value="js-notification-box-msg")
    assert error_msg_login_vwo.text == "Your email, password, IP address or location did not match"

    driver.close()