import allure
import pytest
from helpers import UserRandomData
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods
from data import OrderData, ResponseCodes, ErrorMessages


class TestCreateOrder:

    @allure.title('Позитивный сценарий создания Заказа.')
    @allure.description('Используя верные данные, выполняем создание заказа.')
    @pytest.mark.parametrize("payload", [{"ingredients":OrderData.valid_ingredients[0]}, 
                                        {"ingredients":OrderData.valid_ingredients[1], "ingredients":OrderData.valid_ingredients[2]},
                                        {"ingredients":OrderData.valid_ingredients[3], "ingredients":OrderData.valid_ingredients[4], "ingredients":OrderData.valid_ingredients[5]}])
    def test_create_valid_order_true(self, payload):
        user_payload = UserRandomData.create_user_data()
        response = UserMethods.user_create(user_payload)
        bearer_token = response[1]["accessToken"]
        status_code, response_data = OrderMethods.order_create(bearer_token, payload)
        assert status_code == ResponseCodes.ok and response_data["success"] == True

    @allure.title('Негативный сценарий создания Заказа.')
    @allure.description('Используя неверные данные, выполняем создание заказа.')
    @pytest.mark.parametrize("payload", [{"ingredients":OrderData.invalid_ingredients[0]},
                                         {"ingredients":OrderData.valid_ingredients[1],"ingredients":OrderData.invalid_ingredients[1]}])
    def test_create_order_invalid_ingredient_false(self, payload):
        user_payload = UserRandomData.create_user_data()
        response = UserMethods.user_create(user_payload)
        bearer_token = response[1]["accessToken"]
        order_response = OrderMethods.order_create(bearer_token, payload)
        assert order_response[0] == ResponseCodes.server_error

    @allure.title('Негативный сценарий создания Заказа без ингредиента.')
    @allure.description('Выполняем создание заказа без ингредиента.')
    @pytest.mark.parametrize("payload", [{}])
    def test_create_order_no_ingredient_id_false(self, payload):
        user_payload = UserRandomData.create_user_data()
        response = UserMethods.user_create(user_payload)
        bearer_token = response[1]["accessToken"]
        status_code, response_data = OrderMethods.order_create(bearer_token, payload)
        assert status_code == ResponseCodes.bad_request and response_data["message"] == ErrorMessages.no_id

    @allure.title('Позитивный сценарий создания Заказа без авторизации.')
    @allure.description('Выполняем создание заказа без авторизации.')
    @pytest.mark.parametrize("payload", [{"ingredients":OrderData.valid_ingredients[6]}, {"ingredients":OrderData.valid_ingredients[7], "ingredients":OrderData.valid_ingredients[8]},
                                             {"ingredients":OrderData.valid_ingredients[9], "ingredients":OrderData.valid_ingredients[10], "ingredients":OrderData.valid_ingredients[11]}])
    def test_create_order_unauthorized_true(self, payload):
        bearer_token = None
        status_code, response_data = OrderMethods.order_create(bearer_token, payload)
        assert status_code == ResponseCodes.ok and response_data["success"] == True

class TestUserOrders:

    @allure.title('Позитивный сценарий получения информации о Заказе.')
    @allure.description('Выполняем получения Заказа авторизованным пользователем.')
    def test_get_user_orders_authorized_true(self, user_with_order):
        bearer_token, expected_ingredient = user_with_order
        status_code, response_data = OrderMethods.get_user_orders(bearer_token)
        assert status_code == ResponseCodes.ok and response_data["orders"][0]["ingredients"][0] == expected_ingredient

    @allure.title('Негативный сценарий получения информации о Заказе неавторизованным пользователем.')
    @allure.description('Выполняем получения неавторизованным пользователем.')
    def test_get_user_orders_unauthorized_false(self):
        bearer_token = None
        status_code, response_data = OrderMethods.get_user_orders(bearer_token)
        assert status_code == ResponseCodes.unauthorised and response_data["message"] == ErrorMessages.unauthorised_error
