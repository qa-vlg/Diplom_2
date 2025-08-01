import requests
import allure
from endpoints import Urls

class UserMethods:

    @staticmethod
    @allure.step('Создание Пользователя')
    def user_create(payload):
        response = requests.post(Urls.USER_CREATE, json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    
    @staticmethod
    @allure.step('Логин Пользователя')
    def user_login(payload):
        response = requests.post(Urls.USER_LOGIN, json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    
    @staticmethod
    @allure.step('Изменение информации Пользователя')
    def user_update_info(bearer_token, payload):
        headers = {
            "Authorization": bearer_token
            }
        response = requests.patch(Urls.USER, json=payload, headers=headers)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response

    @staticmethod
    @allure.step('Удаление Пользователя')
    def user_delete(bearer_token):
        headers = {
            "Authorization": bearer_token
            }
        response = requests.delete(Urls.USER, headers=headers)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    