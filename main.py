"""
Author: Jason McMillan

Simple automated test to test working features of a website. I have not used selenium before and a lot of this was
experimentation to find what worked and the features of selenium. I further plan to expand my knowledge of automated
testing and selenium and add features down the road.

To Run:
Install chrome driver and replace PATH variable with path to chrome driver on machine
Download chrome driver at: https://sites.google.com/chromium.org/driver/
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import unittest


# TO RUN, DOWNLOAD CHROME DRIVER AND REPLACE PATH TO CHROME DRIVER ON USER MACHINE
PATH = "/Users/jasonmcmillan/chromedriver"

# Declare global variables
USER_NAME = "test.test.123@test"
PASSWORD = "test"


class ProductStore(unittest.TestCase):

    def setUp(self):
        self.s = Service(PATH)
        self.driver = webdriver.Chrome(service=self.s)
    # End of constructor

    def test_store_name(self):
        """
        Simple test to check store name and make sure test environment is working
        :return:
        """
        self.driver.get("https://www.demoblaze.com/")
        self.assertIn("STORE", self.driver.title)
    # End of test_store_name

    def test_signup(self):
        """
        Simple test to try and sign up a already existing user. Should use already existing username and password and
        give an alert saying that the user already exists. If test fails to input username or password, it will give
        different alert failing the test.
        For some reason I had a hard time getting this one to work properly.
        :return:
        """
        self.driver.get("https://www.demoblaze.com/")

        #Click Sign Up Button
        search = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "signin2")))
        self.driver.implicitly_wait(5)
        search.send_keys(Keys.RETURN)

        # Type in username
        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "sign-username")))
        username.send_keys(USER_NAME)

        # Type in password
        password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "sign-password")))
        password.send_keys(PASSWORD)

        # Click sign up
        signup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')))
        signup.click()

        alert = Alert(self.driver)

        self.assertEqual(alert.text, "This user already exist.")

        alert.accept()
    # End of test_signup()

    def test_login(self):
        """
        Tests login with already established username and password. Checks to make sure welcome element is present.
        Could scale this by using alternate emails and passwords to test further.
        :return:
        """
        self.driver.get("https://www.demoblaze.com/")

        search = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "login2")))
        search.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(10)

        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "loginusername")))
        username.send_keys(USER_NAME)

        password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "loginpassword")))
        password.send_keys(PASSWORD)

        signup = self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        signup.click()

        if self.driver.find_element(By.ID, "nameofuser"):
            assert True
        else:
            assert False
    # End of test_login()

    def test_add_item(self):
        """
        Tests to see if product can be added to cart. Can further scale this by not allowing to add product to cart
        unless signed in.
        :return:
        """
        self.driver.get("https://www.demoblaze.com/")

        search = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')))
        search.click()

        add_cart = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a')))

        add_cart.click()

        time.sleep(5)

        alert = Alert(self.driver)

        self.assertEqual(alert.text, "Product added")

        alert.accept()
    # End of test_add_item()

    def tearDown(self):
        """
        Close browser window
        :return:
        """
        self.driver.close()
    # End of tearDown()


if __name__ == '__main__':
    unittest.main()

