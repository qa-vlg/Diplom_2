import pytest
import allure
from helpers import UserRandomData
from methods.user_methods import UserMethods
from data import UserSignUpData, UserLoginData, ResponseCodes, ErrorMessages, ConfirmationMessage


class TestUserCreate:

    @allure.title('Gjpbnbdysq сценарий создания Пользователя')
    @allure.description('Выполняем создание Пользователя используя eybrfkmyst данные.')
    def test_create_user_true(self):
        payload = UserRandomData.create_user_data()
        status_code, response_data = UserMethods.user_create(payload)
        assert status_code == ResponseCodes.ok and response_data["success"] == True

    @allure.title('Негативный сценарий проверки создания Пользователя: existing credentials')
    @allure.description('Выполняем создание Пользователя используя данные уже существующего.')
    @pytest.mark.parametrize("payload", [UserSignUpData.existing_user_credentials])
    def test_create_existing_user_false(self, payload):
       status_code, response_data = UserMethods.user_create(payload)
       assert status_code == ResponseCodes.forbidden and response_data["message"] == ErrorMessages.existing_account

    @allure.title('Негативный сценарий проверки создания Пользователя: missing values')
    @allure.description('Выполняем создание Пользователя используя пустые вводные данные.')
    @pytest.mark.parametrize("payload", [UserSignUpData.user_credentials_empty_email,
                                         UserSignUpData.user_credentials_empty_name,
                                         UserSignUpData.user_credentials_empty_pwd])
    def test_create_user_missing_fields_false(self, payload):
       status_code, response_data = UserMethods.user_create(payload)
       assert status_code == ResponseCodes.forbidden and response_data["message"] == ErrorMessages.missing_user_info

class TestUserLogin:

    @allure.title('Позитивный сценарий проверки логина Пользователя.')
    @allure.description('Используя активный аккаунт Пользователя, выполняем логин.')
    def test_user_login_true(self):
       payload = UserLoginData.valid_user_credentials
       status_code, response_data = UserMethods.user_login(payload)
       assert status_code == ResponseCodes.ok and response_data['success'] == True

    @allure.title('Негативный сценарий проверки логина Пользователя: wrong values')
    @allure.description('Выполняем логин Пользователя используя неверные данные.')
    @pytest.mark.parametrize("payload", [UserLoginData.user_credentials_invalid_email, UserLoginData.user_credentials_invalid_pwd,
                                         UserLoginData.user_credentials_empty_email, UserLoginData.user_credentials_empty_pwd])
    def test_courier_login_wrong_credentials_false(self, payload):
       status_code, response_data = UserMethods.user_login(payload)
       assert status_code == ResponseCodes.unauthorised and response_data["message"] == ErrorMessages.login_error

class TestUserDelete:
    
    @allure.title('Позитивный сценарий удаления Пользователя.')
    @allure.description('Используя верные данные, удаляем Пользователя.')
    def test_delete_existing_user_true(self, user):
        bearer_token = user
        status_code, response_data = UserMethods.user_delete(bearer_token)
        assert status_code == ResponseCodes.accepted and response_data["message"] == ConfirmationMessage.user_removed

    @allure.title('Негативный сценарий проверки удаления Пользователя: wrong values')
    @allure.description('Выполняем удаление Пользователя используя неверные данные.')
    @pytest.mark.parametrize("bearer_token", ['013441', ''])
    def test_delete_user_invalid_data_false(self, bearer_token):
       status_code, response_data = UserMethods.user_delete(bearer_token)
       assert status_code == ResponseCodes.unauthorised and response_data["success"] == False

class TestUserInfo:

    @allure.title('Позитивный сценарий изменения информации Пользователя.')
    @allure.description('Выполняем изменения информации Пользователя используя верные данные.')
    @pytest.mark.parametrize("payload", [{"email": UserRandomData.user_email()}, {"name": UserRandomData.user_name()},
                                         {"email": UserRandomData.user_email(), "name": UserRandomData.user_name()}])
    def test_update_user_info_authorized_true(self, user, payload):
        bearer_token = user
        status_code, response_data = UserMethods.user_update_info(bearer_token, payload)
        assert status_code == ResponseCodes.ok and response_data["success"] == True

    @allure.title('Негативный сценарий изменения информации Пользователя.')
    @allure.description('Выполняем изменения информации Пользователя неавторизованным пользователем.')
    @pytest.mark.parametrize("payload", [{"email": UserRandomData.user_email()}, {"name": UserRandomData.user_name()},
                                         {"email": UserRandomData.user_email(), "name": UserRandomData.user_name()}])
    def test_update_user_info_unauthorized_false(self, payload):
        bearer_token = None
        status_code, response_data = UserMethods.user_update_info(bearer_token, payload)
        assert status_code == ResponseCodes.unauthorised and response_data["message"] == ErrorMessages.unauthorised_error
        