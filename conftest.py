import pytest
import requests
from functions.courier import Courier
from functions.order import Order
from constants import Constants

@pytest.fixture
def courier():
    courier = Courier()
    yield courier

    if courier.response.status_code == 201:
        login_response = requests.post(Constants.LOGIN_COURIER_URL, data = {'login': courier.login, 'password': courier.password})
        courier_id = login_response.json()["id"]

        requests.delete(f'{Constants.COURIER_URL}/{courier_id}')

@pytest.fixture
def order():
    order = Order()
    yield order

    if hasattr(order, 'track'):
        requests.put(f'{Constants.CANCEL_ORDER_URL}{order.track}')

@pytest.fixture
def prepare_order(courier, order):
    courier.register_new_random_courier()
    courier.login_courier(courier.payload)
    order.create_order_with_valid_random_data([])
    return courier, order