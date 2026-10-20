import allure
from functions.base import generate_random_string
from data import TextErrorLoginCourier

@allure.suite('Проверка авторизации курьера')
class TestLoginCourier:
    @allure.title('Позитивная проверка с использованием валидных данных')
    def test_login_courier_valid_data(self, prepare_courier):
        courier = prepare_courier
        data = {'login': courier.login, 'password': courier.password}
        courier.login_courier(data)
        assert courier.login_response.status_code == 200
        assert courier.login_response.json().keys() == {"id"}
        assert isinstance(courier.login_response.json()["id"], int)

    @allure.title('Негативная проверка с использованием только пароля')
    def test_login_courier_without_login(self, prepare_courier):
        courier = prepare_courier
        data = {'password': courier.password}
        courier.login_courier(data)
        assert courier.login_response.status_code == 400
        assert courier.login_response.json()["message"] == TextErrorLoginCourier.TEXT_RESPONSE_NOT_ENOUGH_DATA

    @allure.title('Негативная проверка с использованиеп только логина')
    def test_login_courier_without_password(self, prepare_courier):
        courier = prepare_courier
        data = {'login': courier.login}
        courier.login_courier(data)
        assert courier.login_response.status_code == 504
        assert courier.login_response.text == TextErrorLoginCourier.TEXT_RESPONSE_SERVICE_UNVAILABLE

    @allure.title('Негативная проверка с использоавнием несуществующего логина и существующего пароля')
    def test_login_courier_non_existent_login(self, prepare_courier):
        courier = prepare_courier
        new_login = generate_random_string(10)
        data = {'login': new_login, 'password': courier.password}
        courier.login_courier(data)
        assert courier.login_response.status_code == 404
        assert courier.login_response.json()["message"] == TextErrorLoginCourier.TEXT_RESPONSE_COURIER_NOT_FOUND

    @allure.title('Негативная проверка с использованием существующего логина и неверного пароля')
    def test_login_courier_non_existent_password(self, prepare_courier):
        courier = prepare_courier
        new_password = generate_random_string(10)
        data = {'login': courier.login, 'password': new_password}
        courier.login_courier(data)
        assert courier.login_response.status_code == 404
        assert courier.login_response.json()["message"] == TextErrorLoginCourier.TEXT_RESPONSE_COURIER_NOT_FOUND