#seleniume practice
from selenium import webdriver
def test_task2():
  driver = webdriver.Chrome()
  driver.get("https://katalon-demo-cura.herokuapp.com/")
  page_src_code=driver.page_source
  assert "CURA Healthcare Service" in page_src_code
  driver.quit()