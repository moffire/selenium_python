from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    driver = webdriver.Chrome()

    def __init__(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")

    def login(self, username, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

    def logout(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "logout").click()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
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

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def destroy(self):
        self.driver.quit()