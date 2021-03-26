from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddGroup:
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/index.php")

    def login(self, driver):
        driver.find_element(By.NAME, "user").clear().send_keys("admin")
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear().send_keys("secret")
        driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

    def open_groups_page(self, driver):
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, driver):
        # init group creation
        driver.find_element(By.NAME, "new").click()
        # fill group form
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys("test_group")
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").send_keys("header")
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").send_keys("footer")
        # submit group creation
        driver.find_element(By.NAME, "submit").click()

    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.open_groups_page(driver)
        self.create_group(driver)
        self.open_home_page(driver)

