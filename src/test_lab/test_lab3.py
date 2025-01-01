#seleniume practice parrallan briwser test cases

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''this is to persorm the option test in to the test cases like incognito mode or maximise or headless'''


def test_task2():
  chrome_option= Options()
  chrome_option.add_argument("--incognito")
  chrome_option.add_argument("--start-maximized ")

  driver = webdriver.Chrome(chrome_option)
  driver.get("https://katalon-demo-cura.herokuapp.com/")
  time.sleep(5)
  #assert True == False
  '''page_src_code=driver.page_source
  assert "CURA Healthcare Service" in page_src_code
  driver.quit()'''
