import time
import allure
from .base_page import BasePage
from .locators import TimLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType


class TimProject(BasePage):
    def go_to_tim(self):
        tim = self.browser.find_element(*TimLocators.BUTTONTIM)
        tim.click()
        time.sleep(4)
        with allure.step('Фиксируем  контракты'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)


    def create_contract(self):
        createcontract = self.browser.find_element(*TimLocators.CREATECONTRACT)
        createcontract.click()
        distr = self.browser.find_element(*TimLocators.DISTRTIM1)
        distr.click()
        distr = self.browser.find_element(*TimLocators.DISTRTIM2)
        for option in distr.find_elements(By.TAG_NAME, 'div'):
            if option.text == 'Nurtestdistr':
                option.click()
                break
        datefrom = self.browser.find_element(*TimLocators.DATEFROMCONTRACT)
        datefrom.click()
        datefrom.click()
        datefrom.send_keys("01-05-2021")
        dateto = self.browser.find_element(*TimLocators.DATETOCONTRACT)
        dateto.click()
        dateto.click()
        dateto.send_keys("01-09-2021")
        discountvalue = self.browser.find_element(*TimLocators.DISCOUNTVALUECONTRACT)
        discountvalue.send_keys("50")
        terms = self.browser.find_element(*TimLocators.TERMCONTRACT1)
        terms.click()
        terms.click()
        terms = self.browser.find_element(*TimLocators.TERMCONTRACT2)
        terms.send_keys("2")
        sale = self.browser.find_element(*TimLocators.SALECOTRACT1)
        sale.click()
        sale = self.browser.find_elements(*TimLocators.SALECOTRACT2)
        for element in sale:
            element.clear()
            element.send_keys("500")
        save = self.browser.find_element(*TimLocators.SAVECONTRACT)
        save.click()
        time.sleep(4)
        with allure.step('Фиксируем результат создания контракта скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)


    def change_status_contract(self):
        findcontract = self.browser.find_element(*TimLocators.CONTRACTMODULE)
        findcontract.click()
        time.sleep(5)
        draftlist = self.browser.find_element(*TimLocators.DRAFTLIST)
        draftlist.click()
        with allure.step('Фиксируем  статусы скриншотом скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)
        movecontract = self.browser.find_elements(*TimLocators.DRAFTMOVE)
        for element in movecontract:
            time.sleep(3)
            element.click()
            time.sleep(5)
            element = self.browser.find_element(By.CSS_SELECTOR, '#maine > div.modal.ng-isolate-scope.in > div > div > div > div.info-part > textarea')
            element.send_keys("123")
            time.sleep(5)
            element = self.browser.find_element(By.CSS_SELECTOR, '#maine > div.modal.ng-isolate-scope.in > div > div > div > div.info-part > button')
            element.click()
        time.sleep(4)
        with allure.step('Фиксируем результат смены статуса скриншотом скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)


