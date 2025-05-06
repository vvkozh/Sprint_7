import pytest
import requests
import generators
import allure
from curls import Url
from data import Response

class TestAcceptOrder:
    @allure.title('Тест принятия заказа')
    def test_accept_order(self, create_courier, create_order):
        id_courier = create_courier
        id_order = create_order['id_order']
        with allure.step('Принятие заказа'):
            response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}{id_order['order']['id']}?courierId={id_courier['id']}')
        assert response.status_code == 200
        assert response.json() == Response.RESPONSE_SUCCESS

    @allure.title('Тест принятия заказа без ID курьера')
    def test_accept_order_without_id_courier(self, create_order):
        id_order = create_order['id_order']
        with allure.step('Принятие заказа без ID курьера'):
            response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}{id_order['order']['id']}?courierId=')
        assert response.status_code == 400
        assert response.json() == Response.RESPONSE_NOT_ID

    @allure.title('Тест принятия заказа без ID заказа')
    def test_accept_order_without_id_order(self, create_courier):
        id_courier = create_courier
        with allure.step('Принятие заказа без ID заказа'):
            response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}?courierId={id_courier['id']}')
        assert response.status_code == 400
        assert response.json() == Response.RESPONSE_NOT_ID

    @allure.title('Тест принятия заказа с несуществующим ID курьера')
    def test_accept_order_invalid_id_courier(self, create_order):
        id_courier = generators.generate_id_courier()
        id_order = create_order['id_order']
        with allure.step('Принятие заказа с несуществующим ID курьера'):
            response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}{id_order['order']['id']}?courierId={id_courier['id']}')
        assert response.status_code == 404
        assert response.json() == Response.RESPONSE_INVALID_ID_COURIER

    @allure.title('Тест принятия заказа с несуществующим ID заказа')
    def test_accept_order_invalid_id_order(self, create_courier):
        id_courier = create_courier
        id_order = generators.generate_id_order()
        with allure.step('Принятие заказа с несуществующим ID заказа'):
            response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}{id_order['order']['id']}?courierId={id_courier['id']}')
        assert response.status_code == 404
        assert response.json() == Response.RESPONSE_INVALID_ID_ORDER