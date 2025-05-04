import requests
import allure
from curls import Url

class TestGetListOrder:
    @allure.title('Тест получения списка заказов')
    def test_get_list_list_order(self):
        response = requests.get(f'{Url.BASE_URL}{Url.GET_LIST_ORDER}')
        assert response.status_code == 200
        assert 'orders' in response.json()
