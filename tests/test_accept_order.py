#дополнительное задание 2
import allure
from data import TextErrorAcceptOrder

@allure.suite('Проверка принятия заказа')
class TestAcceptOrder:
    @allure.title('Позитивная проверка с использованием существующих данных')
    def test_accept_existing_order(self, prepare_order):
        courier, order = prepare_order
        courier_id = courier.login_response.json()["id"]
        order_id = order.get_order_id()
        response = order.send_accept_order_request(courier_id, order_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Негативная проверка без использования id курьера')
    def test_accept_order_without_courier_id(self, prepare_order):
        courier, order = prepare_order
        order_id = order.get_order_id()
        response = order.send_accept_order_request_without_courier_id(order_id)
        assert response.status_code == 400
        assert response.json()["message"] == TextErrorAcceptOrder.TEXT_RESPONSE_ACCEPR_ORDER_WITHOUT_ID

    @allure.title('Негативная проверка с неверным/несуществующим id курьера')
    def test_accept_order_with_incorrect_courier_id(self, prepare_order):
        courier, order = prepare_order
        courier_id = -courier.login_response.json()["id"]
        order_id = order.get_order_id()
        response = order.send_accept_order_request(courier_id, order_id)
        assert response.status_code == 404
        assert response.json()["message"] == TextErrorAcceptOrder.TEXT_RESPONSE_COURIER_NOT_FOUND

    @allure.title('Негативная проверка без использования id заказа')
    def test_accept_order_without_order_id(self, prepare_order):
        courier, order = prepare_order
        courier_id = courier.login_response.json()["id"]
        order_id = ''
        response = order.send_accept_order_request(courier_id, order_id)
        assert response.status_code == 404
        assert response.json()["message"] == TextErrorAcceptOrder.TEXT_RESPONSE_DATA_NOT_FOUND

    @allure.title('Негативная проверка с неверным/несуществующим id заказа')
    def test_accept_order_with_incorrect_order_id(self, prepare_order):
        courier, order = prepare_order
        courier_id = courier.login_response.json()["id"]
        order_id = -order.get_order_id()
        response = order.send_accept_order_request(courier_id, order_id)
        assert response.status_code == 404
        assert response.json()["message"] == TextErrorAcceptOrder.TEXT_RESPONSE_ORDER_NOT_FOUND
