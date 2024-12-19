import time

from selenium import webdriver


def test_chrome_confirm_url():
    driver = webdriver.Chrome()   #choose the which browser you want to use
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(2)
    driver.quit()


def test_edge_confirm_url():
    driver = webdriver.Edge()   #choose the which browser you want to use
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(2)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

    driver.quit()