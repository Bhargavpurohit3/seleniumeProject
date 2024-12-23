import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_vwo_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    user_name = driver.find_element(By.XPATH, "//input[@id='login-username']")
    user_name.send_keys("abc@gmaul.com")

    password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("bhargva")

    submit = driver.find_element(By.ID, value='js-login-btn')
    submit.click()

    (WebDriverWait(driver=driver, timeout=5)
     .until(EC.visibility_of_element_located
     ((By.CLASS_NAME, "notification-box-description"))))

    error_msg = driver.find_element(By.CLASS_NAME, value="notification-box-description")
    assert error_msg.text == "Your email, password, IP address or location did not match"
    driver.quit()