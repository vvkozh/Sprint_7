import generators
import requests
import allure
from curls import Url
from data import Response

class TestGetOrderByTrack:
    @allure.title('Тест получения заказа по его номеру')
    def test_get_order_by_track(self, create_order):
        track = create_order['track_order']
        response = requests.get(f'{Url.BASE_URL}{Url.GET_ID_ORDER}{track['track']}')
        assert response.status_code == 200
        assert 'order' in response.json()

    @allure.title('Тест получения заказа без номера')
    def test_get_order_without_track(self):
        response = requests.get(f'{Url.BASE_URL}{Url.GET_ID_ORDER}')
        assert response.status_code == 400
        assert response.json() == Response.RESPONSE_WITHOUT_TRACK

    @allure.title('Тест получения заказа с несуществующим номером')
    def test_get_order_invalid_track(self):
        invalid_track = generators.generate_track_order()
        response = requests.get(f'{Url.BASE_URL}{Url.GET_ID_ORDER}{invalid_track}')
        assert response.status_code == 404
        assert response.json() == Response.RESPONSE_INVALID_TRACK