import requests
import allure
import generators
import pytest
from curls import Url
from data import Response

class TestLoginCourier:
    @allure.title('Тест авторизации курьера в системе')
    def test_login_courier(self, create_courier):
        data_courier = create_courier['data_login']
        with allure.step('Авторизация курьера'):
            response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data = data_courier)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Тест авторизации курьера в систему без логина')
    def test_login_without_login(self, create_courier):
        data_courier = create_courier['data_login']
        payload = {'password': data_courier['password']}
        with allure.step('Авторизация курьера без логина'):
            response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data = payload)
        assert response.status_code == 400
        assert response.json() == Response.RESPONSE_LOGIN_WITHOUT_LOGIN

    @allure.title('Тест авторизации курьера в систему с неверными данными')
    @pytest.mark.parametrize('login, password, name_test', [[generators.generate_login(), 'correct_password', 'Авторизация с несуществующим пользователем'],
                                                            ['correct_login', generators.generate_password(), 'Авторизация с неправильным паролем']])
    def test_login_invalid_data(self, create_courier, login, password, name_test):
        data_courier = create_courier['data_login']
        payload = {'login': login if login != 'correct_login' else data_courier['login'],
                   'password': password if password != 'correct_password' else data_courier['password']}
        with allure.step(name_test):
            response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data = payload)
        assert response.status_code == 404
        assert response.json() == Response.RESPONSE_LOGIN_WITH_INVALID_DATA
