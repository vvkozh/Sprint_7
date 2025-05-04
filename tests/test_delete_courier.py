import requests
import generators
import allure
from curls import Url
from data import Response

class TestDeleteCourier:
    @allure.title('Тест удаления курьера')
    def test_delete_courier(self, create_courier):
        id_courier = create_courier
        response = requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER_URL}{id_courier['id']}')
        assert response.status_code == 200
        assert response.json() == Response.RESPONSE_SUCCESS

    @allure.title('Тест удаления курьера без id')
    def test_delete_courier_without_id(self):
        response = requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER_URL}')
        assert response.status_code == 400
        assert response.json() == Response.RESPONSE_DELETE_WITHOUT_ID

    @allure.title('Тест удаления курьера с несуществующим id')
    def test_delete_courier_invalid_id(self):
        id_courier = generators.generate_id_courier()
        response = requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER_URL}{id_courier['id']}')
        assert response.status_code == 404
        assert response.json() == Response.RESPONSE_DELETE_INVALID_ID