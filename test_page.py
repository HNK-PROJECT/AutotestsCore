from .core_project import CoreProject
from .jeans_project import JeansProject
from .tim_project import TimProject
import allure

# pytest --browser_name=firefox --alluredir allure_results -v --tb=line  test_page.py
# C:\Users\Kim\Desktop\Autotests> allure serve allure_results


corelink = 'https://demo.core.heineken.com/CAWA/signin'
distrlink = 'https://demo.core.heineken.com/JDWA/login'

            #'https://jeans.heineken.com/distradmin/login'






@allure.feature('Create sale point')
@allure.story('Создание торговой точки')
@allure.severity('blocker')
def test_create_sp(browser):
    jeans_case = JeansProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_jeans()
    jeans_case.go_to_sp_module()
    jeans_case.create_sp()
    jeans_case.find_sp()




@allure.feature('Create promo discount')
@allure.story('Создание промоакции')
@allure.severity('blocker')
def test_create_promo(browser):
    jeans_case = JeansProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_jeans()
    jeans_case.go_to_promo()
    jeans_case.do_create_promo()





