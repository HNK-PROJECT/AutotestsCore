import time
import allure
from .base_page import BasePage
from .locators import DistributorLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType


class DistributorProject(BasePage):

    def distr_authorization(self):
        auth = self.browser.find_element(*DistributorLocators.LOGIN)
        auth.send_keys('nurtestdistr')
        auth = self.browser.find_element(*DistributorLocators.PASSWORD)
        auth.send_keys('Demo!1234')
        auth = self.browser.find_element(*DistributorLocators.ENTER)
        auth.click()
        time.sleep(3)

    def distr_orders(self):
        orders = self.browser.find_element(*DistributorLocators.ORDERS)
        orders.click()
        time.sleep(3)

    def distr_orders_excel(self):
        excel = self.browser.find_element(*DistributorLocators.ORDERSEXCEL)
        excel.click()
        time.sleep(3)