from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddGroup:
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_add_group(self):
    self.driver.get("http://localhost/addressbook/index.php")
    self.driver.set_window_size(911, 692)
    self.driver.find_element(By.NAME, "user").send_keys("admin")
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys("secret")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    self.driver.find_element(By.LINK_TEXT, "groups").click()
    self.driver.find_element(By.NAME, "new").click()
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys("test_group")
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys("header")
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys("footer")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "home").click()
  
