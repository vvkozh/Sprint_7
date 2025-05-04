import requests
import generators
import allure
from curls import Url
from data import Response


class TestCreateCourier:
    @allure.title('Тест создания курьера')
    def test_create_courier(self):
        payload = generators.generate_courier_body()
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', data = payload)
        assert response.status_code == 201
        assert response.json() == Response.RESPONSE_SUCCESS

    @allure.title('Тест создания курьера с повторяющимся логином')
    def test_create_identical_courier(self):
        payload = generators.generate_courier_body()
        requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', data = payload)
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', data = payload)
        assert response.status_code == 409
        assert response.json() == Response.RESPONSE_DUPLICATE_LOGIN

    @allure.title('Тест создания курьера без логина')
    def test_create_courier_without_login(self):
        payload = {'password': generators.generate_password(),
                   'first_name': generators.generate_first_name()}
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', data = payload)
        assert response.status_code == 400
        assert response.json() == Response.RESPONSE_FAILED_CREATE_COURIER

    @allure.title('Тест создания курьера без пароля')
    def test_create_courier_without_password(self):
        payload = {'login': generators.generate_login(),
                   'first_name': generators.generate_first_name()}
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', data = payload)
        assert response.status_code == 400
        assert response.json() == Response.RESPONSE_FAILED_CREATE_COURIER

