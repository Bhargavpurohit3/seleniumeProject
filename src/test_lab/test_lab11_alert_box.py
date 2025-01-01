import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.description("where_we_are_testing_the_javascript_alert_button")
@allure.title("alert_checking")

def test_js_alert() :

    driver_alert = webdriver.Chrome()
    driver_alert.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver_alert.maximize_window()

    js_alert1 = driver_alert.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    js_alert1.click()

    WebDriverWait(driver=driver_alert, timeout=5).until(EC.alert_is_present())

    alert = driver_alert.switch_to.alert
    alert.accept()

    result = driver_alert.find_element(By.ID, "result").text
    assert result == "You successfully clicked an alert"

    driver_alert.maximize_window()
    driver_alert.quit()


@allure.title("js-alert the confirm button")
@allure.description("accepting the js buttom")
def test_js_alert_confirm_pos():

    driver_alert_cnf = webdriver.Chrome()
    driver_alert_cnf.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver_alert_cnf.maximize_window()

    js_alert1 = driver_alert_cnf.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    js_alert1.click()

    WebDriverWait(driver=driver_alert_cnf, timeout=5).until(EC.alert_is_present())

    alert = driver_alert_cnf.switch_to.alert
    alert.accept()

    result = driver_alert_cnf.find_element(By.ID, "result").text
    assert result == "You clicked: Ok"

    driver_alert_cnf.maximize_window()
    driver_alert_cnf.quit()
@allure.title("js alert neg")
@allure.description("js dismiss the js allert")
def test_js_alert_confirm_neg():

    driver_alert_cnf_n = webdriver.Chrome()
    driver_alert_cnf_n.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver_alert_cnf_n.maximize_window()

    js_alert1 = driver_alert_cnf_n.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    js_alert1.click()

    WebDriverWait(driver=driver_alert_cnf_n, timeout=5).until(EC.alert_is_present())

    alert = driver_alert_cnf_n.switch_to.alert
    alert.dismiss()

    result = driver_alert_cnf_n.find_element(By.ID, "result").text
    assert result == "You clicked: Cancel"

    driver_alert_cnf_n.maximize_window()
    driver_alert_cnf_n.quit()

@allure.title("js_alert_promt_accep")
@allure.description("accept and give the value to js allert")

def test_js_alert_promt_pos():

    driver_alertpromt = webdriver.Chrome()
    driver_alertpromt.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver_alertpromt.maximize_window()

    js_alert1 = driver_alertpromt.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    js_alert1.click()

    WebDriverWait(driver=driver_alertpromt, timeout=5).until(EC.alert_is_present())

    alert = driver_alertpromt.switch_to.alert
    alert.send_keys("bhargav")
    alert.accept()

    result = driver_alertpromt.find_element(By.ID, "result").text
    assert result == "You entered: bhargav"

    driver_alertpromt.maximize_window()
    driver_alertpromt.quit()

@allure.title("js-aert-promt-decline")
@allure.description("js-alert-dismiss-button")
def test_js_alert_promt_neg():

    driver_alertpromt = webdriver.Chrome()
    driver_alertpromt.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver_alertpromt.maximize_window()

    js_alert1 = driver_alertpromt.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    js_alert1.click()

    WebDriverWait(driver=driver_alertpromt, timeout=5).until(EC.alert_is_present())

    alert = driver_alertpromt.switch_to.alert
    #alert.send_keys("bhargav")
    alert.dismiss()

    result = driver_alertpromt.find_element(By.ID, "result").text
    assert result == "You entered: null"

    driver_alertpromt.maximize_window()
    driver_alertpromt.quit()




