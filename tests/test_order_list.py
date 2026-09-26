import allure
from functions.order import Order

@allure.suite('Проверка получения списка заказов')
class TestOrderList:
    @allure.title('Позитивная проверка получение списка заказов без указания необязательных параметров')
    def test_getting_order_list(self):
        order = Order()
        order.get_order_list()
        assert order.order_list_response.status_code == 200
        assert isinstance(order.order_list_response.json()["orders"], list)