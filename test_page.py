from .core_project import CoreProject
from .tim_project import  TimProject
from .distr_project import DistributorProject
from .jeans_project import JeansProject
import allure

# pytest --browser_name=firefox --alluredir allure_results -v --tb=line  test_page.py
# C:\Users\Kim\Desktop\Autotests> allure serve allure_results

#  blocker critical normal minorcd

corelink = 'https://core.heineken.com/CAWA/signin'
distrlink = 'https://jeans.heineken.com/distradmin/login'
    #'https://demo.core.heineken.com/JDWA/login'





@allure.feature('Authorization distr')
@allure.story('Авторизация в системе дистрибьютора')
@allure.severity('blocker')
def test_authorization_distr(browser):
    distr_case = DistributorProject(browser, distrlink)
    distr_case.open()
    distr_case.distr_authorization()


@allure.feature('Open distr orders')
@allure.story('Открываем модуль заказ')
@allure.severity('critical')
def test_open_orders_distr(browser):
    distr_case = DistributorProject(browser, distrlink)
    distr_case.open()
    distr_case.distr_authorization()
    distr_case.distr_orders()


@allure.feature('Dowload orders excel')
@allure.story('Выгрузка файла excel данных по заказам')
@allure.severity('normal')
def test_orders_excel_distr(browser):
    distr_case = DistributorProject(browser, distrlink)
    distr_case.open()
    distr_case.distr_authorization()
    distr_case.distr_orders()
    distr_case.distr_orders_excel()
