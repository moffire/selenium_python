from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.Group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.driver.quit()