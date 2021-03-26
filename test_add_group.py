from selenium import webdriver
from selenium.webdriver.common.by import By

from group import Group


class TestAddGroup:
    driver = webdriver.Firefox()

    def setUp(self):
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/index.php")

    def login(self, driver, username, password):
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

    def open_groups_page(self, driver):
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, driver, group):
        # init group creation
        driver.find_element(By.NAME, "new").click()
        # fill group form
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element(By.NAME, "submit").click()

    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username='admin', password='secret')
        self.open_groups_page(driver)
        self.create_group(driver, Group(name='new_group', header='header', footer='footer'))
        self.open_home_page(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username='admin', password='secret')
        self.open_groups_page(driver)
        self.create_group(driver, Group(name='', header='', footer=''))
        self.open_home_page(driver)