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
        response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}{id_order['order']['id']}?courierId={id_courier['id']}')
        assert response.status_code == 200
        assert response.json() == Response.RESPONSE_SUCCESS

    @allure.title('Тест принятия заказа без ID курьера или ID заказа')
    @pytest.mark.parametrize('without_id', ['Нет ID курьера', 'Нет ID заказа'])
    def test_accept_order_without_id(self, create_courier, create_order, without_id):
        id_courier = create_courier
        id_order = create_order['id_order']
        if without_id == 'Нет ID курьера':
            response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}{id_order['order']['id']}?courierId=')
        elif without_id == 'Нет ID заказа':
            response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}?courierId={id_courier['id']}')
        assert response.status_code == 400
        assert response.json() == Response.RESPONSE_NOT_ID

    @allure.title('Тест принятия заказа с несуществующим ID курьера или ID заказа')
    @pytest.mark.parametrize('invalid_id', ['Запрос с несуществующим номером заказа', 'Запрос с несуществующим номером курьера'])
    def test_accept_order_invalid_id(self, create_courier, create_order, invalid_id):
        if invalid_id == 'Запрос с несуществующим номером заказа':
            id_courier = create_courier
            id_order = generators.generate_id_order()
            wait_response = Response.RESPONSE_INVALID_ID[0]
        elif invalid_id == 'Запрос с несуществующим номером курьера':
            id_courier = generators.generate_id_courier()
            id_order = create_order['id_order']
            wait_response = Response.RESPONSE_INVALID_ID[1]
        response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}{id_order['order']['id']}?courierId={id_courier['id']}')
        assert response.status_code == 404
        assert response.json() == wait_response