import time
import allure
from .base_page import BasePage
from .locators import DistributorLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType


class DistributorProject(BasePage):

    def distr_authorization(self):
        auth = self.browser.find_element(*DistributorLocators.LOGIN)
        auth.send_keys('123')
        auth = self.browser.find_element(*DistributorLocators.PASSWORD)
        auth.send_keys('123')
        auth = self.browser.find_element(*DistributorLocators.ENTER)
        auth.click()
        self.browser.find_element(By.CSS_SELECTOR, '.buttonSave')
        with allure.step('Фиксируем результат скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)

    def distr_orders(self):
        orders = self.browser.find_element(*DistributorLocators.ORDERS)
        orders.click()
        self.browser.find_element(By.CSS_SELECTOR, '.getExcel')
        with allure.step('Фиксируем результат скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)
        time.sleep(3)

    def distr_orders_excel(self):
        excel = self.browser.find_element(*DistributorLocators.ORDERSEXCEL)
        excel.click()
        time.sleep(3)
        with allure.step('Фиксируем результат скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)
