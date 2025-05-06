import json
import requests
import pytest
import generators
import allure
from data import OrderData
from data import Response
from curls import Url

class TestCreateOrder:
    @allure.title('Тест создания заказа')
    @pytest.mark.parametrize('color_order', OrderData.COLOR)
    def test_create_order(self, color_order):
        payload = generators.generate_data_order()
        if len(color_order) > 0:
            payload['color'] = color_order
        payload_test = json.dumps(payload)
        with allure.step('Создание заказа'):
            response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', data = payload_test)
        assert response.status_code == 201
        assert Response.RESPONSE_CREATE_ORDER in response.json()