
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


@allure.feature('Authorization core')
@allure.story('Авторизация на основной странице сервиса core')
@allure.severity('blocker')
def test_authorization_core(browser):
    core_case = CoreProject(browser, corelink)
    core_case.open()
    core_case.core_authorization()


@allure.feature('Create User')
@allure.story('Создаём тестового пользователя')
@allure.severity('critical')
def test_create_user(browser):
    core_case = CoreProject(browser, corelink)
    core_case.open()
    core_case.core_authorization()
    core_case.choose_core_project()
    core_case.choose_company_menu()
    core_case.do_create_user()


@allure.feature('Delete User')
@allure.story('Удаляем созданные тестовые данные')
@allure.severity('normal')
def test_delete_user(browser):
    core_case = CoreProject(browser, corelink)
    core_case.open()
    core_case.core_authorization()
    core_case.choose_core_project()
    core_case.choose_company_menu()
    core_case.do_delete_user()


@allure.feature('Open jeans project')
@allure.story('Открытие Jeans Web Admin')
@allure.severity('blocker')
def test_open_jeans(browser):
    jeans_case = JeansProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_jeans()


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



@allure.feature('Open promo module')
@allure.story('Открытие экрана работы с промоакциями')
@allure.severity('blocker')
def test_promo_open(browser):
    jeans_case = JeansProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_jeans()
    jeans_case.go_to_promo()


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


@allure.feature('Open visit module')
@allure.story('Открытие модуль Маршрутизации')
@allure.severity('blocker')
def test_go_to_visit(browser):
    jeans_case = JeansProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_jeans()
    jeans_case.go_to_visit_module()


@allure.feature('Go to bind visit')
@allure.story('Планирование визитов')
@allure.severity('blocker')
def test_bind_visit(browser):
    jeans_case = JeansProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_jeans()
    jeans_case.go_to_visit_module()
    jeans_case.do_bind_visit()


@allure.feature('Open Tim')
@allure.story('Открытие проекта TIM')
@allure.severity('blocker')
def test_go_to_tim(browser):
    jeans_case = TimProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_tim()


@allure.feature('Create contract')
@allure.story('Создание нового контракта')
@allure.severity('blocker')
def test_create_contract(browser):
    jeans_case = TimProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_tim()
    jeans_case.create_contract()


@allure.feature('Change status contract')
@allure.story('Изменение статуса чернового  контракта')
@allure.severity('blocker')
def test_change_status_contract(browser):
    jeans_case = TimProject(browser, corelink)
    case_core = CoreProject(browser, corelink)
    jeans_case.open()
    case_core.core_authorization()
    jeans_case.go_to_tim()
    jeans_case.change_status_contract()
