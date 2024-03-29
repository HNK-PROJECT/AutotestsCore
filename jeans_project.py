import time
import allure
from .base_page import BasePage
from .locators import JeansLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from allure_commons.types import AttachmentType


class JeansProject(BasePage):

    def go_to_jeans(self):
        jeans = self.browser.find_element(*JeansLocators.BUTTONJEANS)
        jeans.click()
        time.sleep(2)

    def go_to_sp_module(self):
        time.sleep(3)
        btnsp = self.browser.find_element(*JeansLocators.SP)
        btnsp = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.flaticon-shopping13'))
        )
        btnsp.click()
        time.sleep(3)

    def create_sp(self):
        time.sleep(3)
        createsp = self.browser.find_element(*JeansLocators.CREATESP)
        createsp.click()
        statussp = self.browser.find_element(*JeansLocators.STATUSSPCLICK)
        statussp.click()
        time.sleep(1)
        status_sp_choose = self.browser.find_element(*JeansLocators.STATUSSPCHOOSE)
        status_sp_choose.click()
        namesp = self.browser.find_element(*JeansLocators.NAMESP)
        namesp.send_keys("AutomateCreatedSalePoint55")
        channel = self.browser.find_element(*JeansLocators.CHANNELCLICK)
        channel.click()
        channel = self.browser.find_element(*JeansLocators.CHANNELCHOOSE)
        for option in channel.find_elements_by_tag_name('div'):
            if option.text == 'АЗС':
                option.click()
                break
        adres = self.browser.find_element(*JeansLocators.ADRES)
        adres.send_keys("AutomateAdresInput")
        territory = self.browser.find_element(*JeansLocators.TERRITORYCLICK)
        territory.click()
        territory = self.browser.find_element(*JeansLocators.TERRITORYCHOOSE)
        for option in territory.find_elements_by_tag_name('div'):
            if option.text == '1234':
                option.click()
                break
        region = self.browser.find_element(*JeansLocators.REGIONCLICK)
        region.click()
        region = self.browser.find_element(*JeansLocators.REGIONCHOOSE)
        for option in region.find_elements_by_tag_name('div'):
            if option.text == 'Eastern Siberia Region':
                option.click()
                break
        city = self.browser.find_element(*JeansLocators.CITY)
        city.click()
        city = self.browser.find_element(*JeansLocators.CITYCHOSE)
        time.sleep(1)
        for option in city.find_elements_by_tag_name('div'):
            if option.text == 'Baikalsk':
                option.click()
                break
        distr = self.browser.find_element(*JeansLocators.DISTRCLICK)
        distr.click()
        distr_choose = self.browser.find_element(*JeansLocators.DISTRCHOOSE)
        for option in distr_choose.find_elements_by_tag_name('div'):
            if option.text == 'Nurtestdistr':
                option.click()
                break
        warehouse = self.browser.find_element(*JeansLocators.WAREHOUSE)
        warehouse.click()
        warehouse = self.browser.find_element(*JeansLocators.WAREHOUSECHOOSE)
        time.sleep(1)
        for option in warehouse.find_elements_by_tag_name('div'):
            if option.text == '1234':
                option.click()
                break
        salearea = self.browser.find_element(*JeansLocators.SALESAREA)
        salearea.click()
        for option in salearea.find_elements_by_tag_name('div'):
            if option.text == '<25':
                option.click()
                break
        with allure.step('Фиксируем результат ввода полей скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)
        time.sleep(3)
        btn_save_sp = self.browser.find_element(*JeansLocators.SAVESP)
        btn_save_sp.click()
        time.sleep(1)
        with allure.step('Фиксируем сохранение'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)
        time.sleep(15)

    def find_sp(self):
        find = self.browser.find_element(*JeansLocators.FIND)
        find.send_keys("AutomateCreatedSalePoint55")
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.Table-row:nth-child(2) > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > i:nth-child(1)'))
        )
        time.sleep(2)
        with allure.step('Фиксируем результат поиска скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)

    def delete_sp(self):
        edit = self.browser.find_element(*JeansLocators.EDITSP)
        edit.click()
        delete = self.browser.find_element(*JeansLocators.STATUSSPCLICK)
        delete.click()
        delete = self.browser.find_element(*JeansLocators.STATUSSPCHOOSE)
        for option in delete.find_elements_by_tag_name('div'):
            if option.text == 'Удалена':
                option.click()
                break
        time.sleep(2)
        btn_save_sp = self.browser.find_element(*JeansLocators.SAVESP)
        btn_save_sp.click()
        time.sleep(10)
        filtersp = self.browser.find_element(*JeansLocators.CHANGEFILTERSP)
        filtersp.click()
        filtersp = self.browser.find_element(*JeansLocators.CHOOSESPFILTER)
        for option in filtersp.find_elements_by_tag_name('div'):
            if option.text == 'Удалена':
                option.click()
                break
        time.sleep(3)
        with allure.step('Фиксируем результат отображение удаленной тт скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)

    def go_to_promo(self):
        skumodule = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.flaticon-shopping13'))
        )
        skumodule = self.browser.find_element(*JeansLocators.SKUASSORT)
        skumodule.click()
        submenu = self.browser.find_element(*JeansLocators.SUBMENU)
        submenu.click()
        time.sleep(3)

    def do_create_promo(self):
        create_promo = self.browser.find_element(*JeansLocators.CREATEPROMO)
        create_promo.click()
        namepromo = self.browser.find_element(*JeansLocators.NAMEPROMO)
        namepromo.send_keys("AutomateCreatePromo")
        terms = self.browser.find_element(*JeansLocators.TERMSPROMO)
        terms.send_keys("Terms")
        datefrom = self.browser.find_element(*JeansLocators.DATEFROMPROMO)
        datefrom.click()
        datefrom.click()
        datefrom.send_keys("01/07/2021")
        discount = self.browser.find_element(*JeansLocators.DISCOUNT1)
        discount.click()
        discount = self.browser.find_element(*JeansLocators.DISCOUNT2)
        for option in discount.find_elements(By.TAG_NAME, 'div'):
            if option.text == 'Фикс. цена':
                option.click()
                break
        autoin = self.browser.find_element(*JeansLocators.AUTOIN)
        autoin.send_keys("37")
        sku = self.browser.find_element(*JeansLocators.SKUPROMO)
        sku.click()
        save = self.browser.find_element(*JeansLocators.SAVEPROMO)
        save.click()
        time.sleep(10)
        with allure.step('Фиксируем результат создания промо скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)

    def go_to_visit_module(self):
        visit = self.browser.find_element(*JeansLocators.VISIT)
        visit.click()
        time.sleep(4)

    def do_bind_visit(self):
        datefrom = self.browser.find_element(*JeansLocators.DATEFROMVISIT1)
        datefrom.click()
        datefrom = self.browser.find_element(*JeansLocators.DATEFROMVISIT2)
        datefrom.clear()
        datefrom.send_keys("01/07/2021")
        dateto = self.browser.find_element(*JeansLocators.DATETOVISIT1)
        dateto.click()
        dateto = self.browser.find_element(*JeansLocators.DATETOVISIT2)
        dateto.clear()
        dateto.send_keys("07/07/2021")
        dateto.click()
        visitbind = self.browser.find_element(*JeansLocators.VISITBIND)
        visitbind.click()
        action = ActionChains(self.browser)
        action.double_click(on_element=visitbind)
        action.perform()
        save = self.browser.find_element(*JeansLocators.SAVEVISIT)
        save.click()
        time.sleep(5)
        with allure.step('Фиксируем результат создания промо скриншотом'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)

    def go_to_tasks(self):
        task_page = self.browser.find_element(*JeansLocators.OPEN_TASK)
        task_page.click()
        time.sleep(3)
        with allure.step('Фиксируем результат списка задач'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)
        time.sleep(3)

    def mass_create_task(self):
        mass_task = self.browser.find_element(*JeansLocators.MASS_CREATE_TASK)
        mass_task.click()
        time.sleep(1)
        mass_task_input = self.browser.find_element(*JeansLocators.MASSTASK_TYPE_CLICK)
        mass_task_input.click()
        time.sleep(1)
        mass_task_input = self.browser.find_element(*JeansLocators.MASSTASK_TYPE_CHOOSE)
        mass_task_input.click()
        time.sleep(1)
        mass_task_input = self.browser.find_element(*JeansLocators.MASSTASK_DATE)
        mass_task_input.send_keys("01/01/2022")
        mass_task_input.click()
        mass_task_input = self.browser.find_element(*JeansLocators.MASSTASK_DESCRIPTION)
        mass_task_input.send_keys("Автоматически созданная задача. By PyTest")
        mass_task_input = self.browser.find_element(*JeansLocators.MASSTASK_SAVE)
        mass_task_input.click()
        time.sleep(3)
        with allure.step('Фиксируем результат создания задач'):
            allure.attach(self.browser.get_screenshot_as_png(), name='Scr_User', attachment_type=AttachmentType.PNG)
        time.sleep(3)




