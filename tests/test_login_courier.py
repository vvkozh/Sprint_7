import requests
import allure
import generators
from curls import Url

class TestLoginCourier:
    @allure.title('Тест авторизации курьера в системе')
    def test_login_courier(self, create_courier):
        data_courier = create_courier['data_login']
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data = data_courier)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Тест авторизации курьера в систему без логина')
    def test_login_without_login(self, create_courier):
        data_courier = create_courier['data_login']
        payload = {'password': data_courier['password']}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data = payload)
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Тест авторизации курьера в систему с несуществующим логином')
    def test_login_another_login(self, create_courier):
        data_courier = create_courier['data_login']
        payload = {'login': generators.generate_login(),
                   'password': data_courier['password']}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data = payload)
        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Тест авторизации курьера в системе с неправильным паролем')
    def test_login_another_password(self, create_courier):
        data_courier = create_courier['data_login']
        payload = {'login': data_courier['login'],
                   'password': generators.generate_password()}
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data = payload)
        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}