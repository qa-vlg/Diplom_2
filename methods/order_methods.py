import requests
import allure
from endpoints import Urls
from json import JSONDecodeError

class OrderMethods:

    @staticmethod
    @allure.step('Создание Заказа')
    def order_create(bearer_token, payload):
        headers = {
            "Authorization": bearer_token
            }
        response = requests.post(Urls.ORDER_URL, json=payload, headers=headers)
        status_code = response.status_code
        try:
            formated_response = response.json()
        except JSONDecodeError:
            formated_response = response.text
        return status_code, formated_response
    
    @staticmethod
    @allure.step('Получение информации о Заказах Пользователя')
    def get_user_orders(bearer_token):
        headers = {
            "Authorization": bearer_token
            }
        response = requests.get(Urls.ORDER_URL, headers=headers)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    