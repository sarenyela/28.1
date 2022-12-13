from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
import time
import pytest
import os
import config

# Тест 1: Регистрации с паролем короче 8 символов




@pytest.fixture(scope="module")
def test_auth_001():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('Qaz123')
    #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Длина пароля должна быть не менее 8 символов'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('Qaz123')
    #WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Длина пароля должна быть не менее 8 символов'))).click()
    yield
    driver.quit()

# Тест 2: Регистрация с несоответствующим условиям сайта именем и фамилией


@pytest.fixture(scope="module")
def test_auth_002():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(By.name, "firstName")).send_keys('Ambrorich0')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(By.name, "lastName")).send_keys('Ambrorich0')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))).click()
    yield
    driver.quit()

# Тест 3: Ввести в поле "Подтверждение пароля" не корректный пароль


@pytest.fixture(scope="module")
def test_auth_003():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('positive_pass')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('positive_pass')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Пароли не совпадают'))).click()
    yield
    driver.quit()

# Тест 4: Регистрация с паролем, в котором нет заглавных букв


@pytest.fixture(scope="module")
def test_auth_004():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('negative_pass')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Пароль должен содержать хотя бы одну заглавную букву'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('negative_pass')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Пароль должен содержать хотя бы одну заглавную букву'))).click()
    yield
    driver.quit()

# Тест 5: Регистрация с некорректно введенным e-mail


@pytest.fixture(scope="module")
def test_auth_005():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('negative_email')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'))).click()
    yield
    driver.quit()

# Тест 6: Регистрация с некорректно введенным телефоном


@pytest.fixture(scope="module")
def test_auth_006():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('810199')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'))).click()
    yield
    driver.quit()

# Тест 7: Регистрация с полностью корректными данными


@pytest.fixture(scope="module")
def test_auth_007():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "firstName"))).send_keys('Имя')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "lastName"))).send_keys('Фамилия')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('real_email')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('positive_pass')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('positive_pass')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "register"))).click()
    yield
    driver.quit()

# Тест 8: Авторизация с несуществующей учетной записью


@pytest.fixture(scope="module")
def test_auth_008():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('AmoMordor@mail.ru')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('Zaq123321qaz')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.text, "Неверный логин или пароль")))
    yield
    driver.quit()

# Тест 9: Авторизация через e-mail


@pytest.fixture(scope="module")
def test_auth_009():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('real_email')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('positive_pass')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=cfd5bad0-08de-4e47-9a65-e8c0e4ee70a5&client_id=account_b2c#/')
    yield
    driver.quit()

# Тест 10: Привязка телефона к личному кабинету


@pytest.fixture(scope="module")
def test_auth_010():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "phone_action"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.text, "rt-code"))).send_keys('positive_pass')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "new_PHONE"))).send_keys('+79000010101')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "new_address_submit"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.text, "rt-code")).send_keys('positive_pass'))
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "submit"))).click()
    yield
    driver.quit()

# Тест 11: Смена пароля через личный кабинет


@pytest.fixture(scope="module")
def test_auth_011():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password_change"))).click()
    # driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password_change"))).send_keys('positive_pass')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "new_password"))).send_keys('positive_pass'+'RT')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "confirm_password"))).send_keys('positive_pass'+'RT')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password_save"))).click()
    yield
    driver.quit()

# Тест 12: Авторизация через телефон


@pytest.fixture(scope="module")
def test_auth_012():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('positive_email')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('positive_pass')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    yield
    driver.quit()

# Тест 13: Авторизация через социальную сеть


@pytest.fixture(scope="module")
def test_auth_013():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "oidc_google"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "view_container"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "page-right")))
    yield
    driver.quit()

# Тест 14: Восстановление пароля при помощи e-mail


@pytest.fixture(scope="module")
def test_auth_014():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('real_email')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "forgot_password"))).click()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=yO70VJtgeUI')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('real_email')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "captcha"))).send_keys('*******')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "reset"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "page-right"/div[1]/div[1]/div[1]/form[1]/div[1]/label[2]/span[1]/span[2]))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.label_class, "rt-btn"))).click()
    #открываем письмо со ссылкой для восстановления пароля и нажимаем кнопку "Восстановить"
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=og1zRJVat3M')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-new"))).send_keys('****************')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('****************')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-reset-pass"))).click()
    yield
    driver.quit()

# Тест 15: Восстановление пароля при помощи телефона


@pytest.fixture(scope="module")
def test_auth_p015():
    driver = webdriver.Chrome(r'C:\Program Files\Python310\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('base_url+/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=M_iHZqpajBw')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('positive_phone')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "forgot_password"))).click()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=og1zRJVat3M')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('positive_phone')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "captcha"))).send_keys('*******')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "reset"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "page-right"/div[1]/div[1]/div[1]/form[1]/div[1]/label[1]/span[1]/span[3]/span[1]))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.label_class, "rt-btn"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "rt-code-0"))).send_keys('******')
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=og1zRJVat3M')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-new"))).send_keys('****************')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('****************')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-reset-pass"))).click()
    yield
    driver.quit()
