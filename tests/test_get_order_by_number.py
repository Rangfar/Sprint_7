#дополнительное задание 3
import allure
from data import TextErrorFoundByNumber

@allure.suite('Проверка получения заказа по его номеру')
class TestGetOrderByNumber:
    @allure.title('Позитивная проверка с использованием существующих данных')
    def test_get_order_data_with_existing_track(self, order):
        order.create_order_with_valid_random_data([])
        response = order.get_order_data(order.track)
        assert response.status_code == 200
        assert isinstance(response.json()["order"], dict)

    @allure.title('Негативная проверка без использования трек номера')
    def test_get_order_data_witout_track(self, order):
        order.create_order_with_valid_random_data([])
        response = order.get_order_data_without_track()
        assert response.status_code == 400
        assert response.json()["message"] == TextErrorFoundByNumber.TEXT_RESPONSE_NOT_ENOUGH_DATA

    @allure.title('Негативная проверка с несуществующим трек номером')
    def test_get_order_data_non_existing_track(self, order):
        order.create_order_with_valid_random_data([])
        track = 999999999
        response = order.get_order_data(track)
        assert response.status_code == 404
        assert response.json()["message"] == TextErrorFoundByNumber.TEXT_RESPONSE_ORDER_NOT_FOUND