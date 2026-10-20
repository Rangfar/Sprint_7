import pytest
from functions.courier import Courier
from functions.order import Order

@pytest.fixture
def courier():
    courier = Courier()
    yield courier

    if courier.response.status_code == 201:
        courier.login_courier({'login': courier.login, 'password': courier.password})
        courier.set_courier_id()
        courier.delete_courier(courier.courier_id)

@pytest.fixture
def order():
    order = Order()
    yield order

    if hasattr(order, 'track'):
        order.cancel_order()

@pytest.fixture
def prepare_order(courier, order):
    courier.register_new_random_courier()
    courier.login_courier(courier.payload)
    order.create_order_with_valid_random_data([])
    return courier, order

@pytest.fixture
def prepare_courier(courier):
    courier.register_new_random_courier()
    return courier