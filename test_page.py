from .core_project import CoreProject
from .jeans_project import JeansProject
from .tim_project import TimProject
from .distr_project import DistributorProject
import allure

# pytest --browser_name=firefox --alluredir allure_results -v --tb=line  test_page.py
# C:\Users\Kim\Desktop\Autotests> allure serve allure_results


corelink = '123'
distrlink = '123'



@allure.feature('Create mass tasks')
@allure.story('Выполняем массовое создание задач')
@allure.severity('critical')
def test_create_task(browser):
    jeans_case = JeansProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_jeans()
    jeans_case.go_to_sp_module()
    jeans_case.go_to_tasks()
    jeans_case.mass_create_task()
