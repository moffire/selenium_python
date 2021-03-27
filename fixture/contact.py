from selenium.webdriver.common.by import By

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        # init contact creation
        driver.find_element(By.LINK_TEXT, "add new").click()
        # fill contact form
        driver.find_element(By.NAME, "firstname").click()
        self.app.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.app.driver.find_element(By.NAME, "lastname").click()
        self.app.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.app.driver.find_element(By.NAME, "nickname").click()
        self.app.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        # submit group creation
        self.app.driver.find_element(By.NAME, "submit").click()