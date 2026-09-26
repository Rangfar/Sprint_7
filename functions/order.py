import allure
import requests
import time
from constants import Constants
from functions.base import generate_random_string, generate_random_phone

class Order:
    @allure.step('Отправка запроса на получение списка заказов')
    def get_order_list(self):
        self.order_list_response = requests.get(Constants.ORDER_URL)

    @allure.step('Создание заказа с валидными значениями')
    def create_order_with_valid_random_data(self, color):
        first_name = generate_random_string(6)
        last_name = generate_random_string(6)
        address = generate_random_string(10)
        metro_station = 4
        phone = generate_random_phone()
        rent_time = 5
        delivery_date = '2027-06-06'
        comment = generate_random_string(20)

        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }
        self.send_create_order_request(payload)

    @allure.step('Отправка запроса на создание заказа')
    def send_create_order_request(self, payload):
        self.create_response = requests.post(Constants.ORDER_URL, json = payload)
        if self.create_response.status_code == 201:
            self.track = self.create_response.json()["track"]

    #относится к дополнительному заданию
    @allure.step('Получение id заказа')
    def get_order_id(self):
        response = self.wait_for_order(self.track)
        return response.json()["order"]["id"]

    @allure.step('Отправление запроса на поиск заказа по трек номеру')
    def get_order_data(self, track):
        return requests.get(Constants.FIND_ORDER_URL.format(track))

    @allure.step('Отправление неполного запроса на поиск заказа')
    def get_order_data_without_track(self):
        return requests.get(Constants.FIND_ORDER_URL_NON_TRACK)

    @allure.step('Отправление запроса на принятие заказа')
    def send_accept_order_request(self, courier_id, order_id):
        response = requests.put(Constants.ACCEPT_ORDER_URL.format(order_id, courier_id))
        return response

    @allure.step('Отправление неполного запроса на принятие заказа')
    def send_accept_order_request_without_courier_id(self, order_id):
        response =  requests.put(Constants.ACCEPT_ORDER_URL_NON_COURIER_ID.format(order_id))
        return response

    @allure.step('Отправление запроса на отмену заказа')
    def cancel_order(self):
        requests.put(Constants.CANCEL_ORDER_URL.format(self.track))

    @allure.step('Ожидание завершения процесса создания заказа')
    def wait_for_order(self, track, timeout=3):
        start_time = time.time()
        while time.time() - start_time < timeout:
            response = self.get_order_data(track)
            if response.status_code == 200:
                return response
            time.sleep(0.5)
            