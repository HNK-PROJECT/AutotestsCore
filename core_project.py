import time
import allure
from .base_page import BasePage
from .locators import CoreLocators
from .locators import MainMenuLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType


class CoreProject(BasePage):

    def core_authorization(self):
        login = self.browser.find_element(*MainMenuLocators.LOGIN)
        login.send_keys('nursrm')
        login = self.browser.find_element(*MainMenuLocators.PASSWORD)
        login.send_keys('Demo!1234')
        login = self.browser.find_element(*MainMenuLocators.ENTER)
        login.click()
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.item:nth-child(3) > app-card:nth-child(1) > div:nth-child(1)'))
        )

    def choose_core_project(self):
        go_to_core = self.browser.find_element(*CoreLocators.BUTTONCORE)
        go_to_core.click()
        time.sleep(3)

    def choose_company_menu(self):
        go_to_company = self.browser.find_element(*CoreLocators.COMPANYBUTTON)
        for option in go_to_company.find_elements(By.TAG_NAME, 'div'):
            if option.text == 'Компания':
                option.click()
                break
        time.sleep(3)

    def do_create_user(self):
        click_create_user = self.browser.find_element(*CoreLocators.CREATEUSER)
        click_create_user.click()
        time.sleep(3)
        cin_name = self.browser.find_element(*CoreLocators.INNAME)
        cin_name.send_keys("Automate")
        cin_second_name = self.browser.find_element(*CoreLocators.INSECONDNAME)
        cin_second_name.send_keys("Test")
        cin_third_name = self.browser.find_element(*CoreLocators.INTHIRDNAME)
        cin_third_name.send_keys("User")
        cin_mail = self.browser.find_element(*CoreLocators.INMAIL)
        cin_mail.send_keys("123@123.123")
        click_role = self.browser.find_element(*CoreLocators.ROLE1)
        click_role.click()
        choose_role = self.browser.find_element(*CoreLocators.ROLE2)
        for option in choose_role.find_elements(By.TAG_NAME, 'div'):
            if option.text == 'SR':
                option.click()
                break
        click_distr = self.browser.find_element(*CoreLocators.DISTR1)
        click_distr.click()
        choose_distr = self.browser.find_element(*CoreLocators.DISTR2)
        for option in choose_distr.find_elements(By.TAG_NAME, 'div'):
            if option.text == 'Nurtestdistr':
                option.click()
                break
        cin_login = self.browser.find_element(*CoreLocators.LOGIN)
        cin_login.send_keys("autouser01")
        cin_pass = self.browser.find_element(*CoreLocators.PASS)
        cin_pass.send_keys("Demo!1234")
        cin_repass = self.browser.find_element(*CoreLocators.REPASS)
        cin_repass.send_keys("Demo!1234")
        scroll = self.browser.find_element(*CoreLocators.SCROLL)
        scroll.click()
        action = ActionChains(self.browser)
        action.send_keys(Keys.PAGE_DOWN).perform()
        click_channel = self.browser.find_element(*CoreLocators.CHANNEL)
        click_channel.click()
        click_parent = self.browser.find_element(*CoreLocators.PARENT1)
        click_parent.click()
        choose_parent = self.browser.find_element(*CoreLocators.PARENT2)
        for option in choose_parent.find_elements(By.TAG_NAME, 'div'):
            if option.text == 'SRM_1 Тестовый1 Пользователь11 [SRM]':
                option.click()
                break
        finish_create = self.browser.find_element(*CoreLocators.CREATE)
        finish_create.click()
        time.sleep(3)
        with allure.step('Фиксируем результат скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)

    def do_delete_user(self):
        time.sleep(3)
        edit_user = self.browser.find_element(*CoreLocators.EDIT)
        edit_user.click()
        delete_user = self.browser.find_element(*CoreLocators.DELETE)
        delete_user.click()
        delete_agree = self.browser.find_element(*CoreLocators.AGREE)
        delete_agree.click()
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.notify:nth-child(2)'))
        )
        with allure.step('Фиксируем результат скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)



