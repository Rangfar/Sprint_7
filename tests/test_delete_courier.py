#дополнительное задание 1
import allure
from functions.courier import Courier
from functions.base import generate_random_number
from data import TextErrorDeleteCourier

@allure.suite('Проверка функции удаления курьера')
class TestDeleteCourier:
    @allure.title('Позитивная проверка удаления существующего курьера')
    def test_delete_existing_courier(self):
        courier = Courier()
        courier.register_new_random_courier()
        login_payload = {'login': courier.login, 'password': courier.password}
        courier.login_courier(login_payload)
        courier.set_courier_id()
        courier.delete_courier(courier.courier_id)
        assert courier.delete_response.status_code == 200
        assert courier.delete_response.json() == {"ok": True}

    @allure.title('Негативная проверка удаления без указания id')
    def test_delete_courier_without_id(self):
        courier = Courier()
        courier.delete_courier('')
        assert courier.delete_response.status_code == 404
        assert courier.delete_response.json()["message"] == TextErrorDeleteCourier.TEXT_RESPONSE_NOT_ENOUGH_ID

    @allure.title('Негативная проверка удаления с указанием несуществующего id')
    def test_delete_courier_with_non_existing_id(self):
        courier = Courier()
        id = -generate_random_number(1, 100)
        courier.delete_courier(id)
        assert courier.delete_response.status_code == 404
        assert courier.delete_response.json()["message"] == TextErrorDeleteCourier.TEXT_RESPONSE_COURIER_NOT_FOUND