#дополнительное задание 1
import allure
import requests
from constants import Constants
from functions.courier import Courier
from functions.base import generate_random_number

@allure.suite('Проверка функции удаления курьера')
class TestDeleteCourier:
    @allure.title('Позитивная проверка удаления существующего курьера')
    def test_delete_existing_courier(self):
        courier = Courier()
        courier.register_new_random_courier()
        data = {'login': courier.login, 'password': courier.password}
        courier.login_courier(data)
        courier.delete_courier()
        assert courier.delete_response.status_code == 200
        assert courier.delete_response.json() == {"ok": True}

    @allure.title('Негативная проверка удаления без указания id')
    def test_delete_courier_without_id(self):
        delete_response = requests.delete(Constants.DELETE_COURIER_URL.format(''))
        assert delete_response.status_code == 400
        assert delete_response.json() == {"message":  "Недостаточно данных для удаления курьера"}

    @allure.title('Негативная проверка удаления с указанием несуществующего id')
    def test_delete_courier_with_non_existing_id(self):
        id = generate_random_number(1, 100)
        delete_response = requests.delete(Constants.DELETE_COURIER_URL.format(id))
        assert delete_response.status_code == 404
        assert delete_response.json() == {"message": "Курьера с таким id нет"}