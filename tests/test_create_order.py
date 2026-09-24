import pytest
import allure

@allure.suite('Проверка создания заказа')
class TestCreateOrder:
    @allure.title('Позитивная проверка с вариантом цвета {color}')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_different_colors(self, order, color):
        order.create_order_with_valid_random_data(color)
        assert order.create_response.status_code == 201
        assert order.create_response.json() == {"track": order.track}
