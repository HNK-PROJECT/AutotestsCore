from .core_project import CoreProject
from .tim_project import  TimProject
from .distr_project import DistributorProject
from .jeans_project import JeansProject
import allure

# pytest --browser_name=firefox --alluredir allure_results -v --tb=line  test_page.py
# C:\Users\Kim\Desktop\Autotests> allure serve allure_results

#  blocker critical normal minorcd

corelink = 'https://demo.core.heineken.com/CAWA/signin'
distrlink = 'https://demo.core.heineken.com/JDWA/login'




@allure.feature('Authorization distr')
@allure.story('Авторизация в системе дистрибьютора')
@allure.severity('blocker')
def test_authorization_distr(browser):
    distr_case = DistributorProject(browser, distrlink)
    distr_case.open()
    distr_case.distr_authorization()