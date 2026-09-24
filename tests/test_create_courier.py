import allure

@allure.suite('Проверка создания нового курьера')
class TestCreateCourier:

    @allure.title('Позитивная проверка с валидными данными')
    def test_create_valid_courier(self, courier):
        courier.register_new_random_courier()
        assert courier.response.status_code == 201
        assert courier.response.json() == {"ok": True}

    @allure.title('Негативная проверка с использованием данных уже существующего курьера')
    def test_create_two_similar_courier(self, courier):
        courier.register_new_random_courier()
        courier.register_new_hand_mode_courier(courier.login, courier.password, courier.first_name)
        assert courier.response.status_code == 409
        assert courier.response.json() == {"message": "Этот логин уже используется"}

    @allure.title('Негативная проверка с использованием только пароля и имени')
    def test_create_courier_without_login(self, courier):
        courier.register_new_random_courier_without_login()
        assert courier.response.status_code == 400
        assert courier.response.json() == {"message": "Недостаточно данных для создания учетной записи"}

    @allure.title('Негативная проверка с использованием только логина и имени')
    def test_create_courier_without_password(self, courier):
        courier.register_new_random_courier_without_password()
        assert courier.response.status_code == 400
        assert courier.response.json() == {"message": "Недостаточно данных для создания учетной записи"}

    @allure.title('Негативная проверка с использованием только логина и пароля')
    def test_create_courier_without_surname(self, courier):
        courier.register_new_random_courier_without_name()
        assert courier.response.status_code == 400
        assert courier.response.json() == {"message": "Недостаточно данных для создания учетной записи"}
