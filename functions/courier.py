import allure
import requests
from constants import Constants
from functions.base import generate_random_string

class Courier():
    @allure.step('Генерация случайных логина пароля и имени курьера')
    def genarate_new_random_courier_data(self):
        self.login = generate_random_string(10)
        self.password = generate_random_string(10)
        self.first_name = generate_random_string(10)

    @allure.step('Регистрация нового курьера с рандомно сгенерированными данными')
    def register_new_random_courier(self):
        self.genarate_new_random_courier_data()

        self.payload = {
                    "login": self.login,
                    "password": self.password,
                    "firstName": self.first_name
        }
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        self.send_create_request(self.payload)

    @allure.step('Отправка запроса на создание курьера')
    def send_create_request(self, payload):
        self.response = requests.post(Constants.COURIER_URL, data = payload)

    @allure.step('Установка полного набора данных нового курьера и отправка запроса')
    def register_new_hand_mode_courier(self, login, password, first_name):
        self.login = login
        self.password = password
        self.first_name = first_name
        payload = {
                    "login": self.login,
                    "password": self.password,
                    "firstName": self.first_name
        }
        self.send_create_request(payload)

    @allure.step('Установка пароля и имени нового курьера и отправка запроса')
    def register_new_random_courier_without_login(self):
        self.password = generate_random_string(10)
        self.first_name = generate_random_string(10)
        payload = {
                    "password": self.password,
                    "firstName": self.first_name
        }
        self.send_create_request(payload)

    @allure.step('Установка логина и имени нового курьера и отправка запроса')
    def register_new_random_courier_without_password(self):
        self.login = generate_random_string(10)
        self.first_name = generate_random_string(10)
        payload = {
                    "login": self.login,
                    "firstName": self.first_name
        }
        self.send_create_request(payload)

    @allure.step('Установка логина и пароля нового курьера и отправка запроса')
    def register_new_random_courier_without_name(self):
        self.login = generate_random_string(10)
        self.password = generate_random_string(10)
        payload = {
                    "login": self.login,
                    "password": self.password,
        }
        self.send_create_request(payload)

    @allure.step('Отправка запроса авторизации')
    def login_courier(self, payload):
        self.login_response = requests.post(Constants.LOGIN_COURIER_URL, data = payload)

    #относится к дополнительному заданию
    @allure.step('Отправка запроса на удаление')
    def delete_courier(self, payload):
        self.delete_response = requests.delete(Constants.DELETE_COURIER_URL.format(payload))

    @allure.step('Сохранение id курьера')
    def set_courier_id(self):
        self.courier_id = self.login_response.json()['id']
