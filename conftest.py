import pytest
from data import OrderData
from helpers import UserRandomData
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods


@pytest.fixture
def user():
    payload = UserRandomData.create_user_data()
    UserMethods.user_create(payload)
    response = UserMethods.user_login(payload)
    bearer_token = response[1]["accessToken"]
    yield bearer_token
    UserMethods.user_delete(bearer_token)

@pytest.fixture
def order(user):
    payload = {"ingredients":OrderData.valid_ingredients[0]}
    bearer_token = user
    response = OrderMethods.order_create(bearer_token, payload)
    return bearer_token, response

@pytest.fixture
def user_with_order(order):
    bearer_token, order_response = order
    ingredient_used = order_response[1]["order"]["ingredients"][0]["_id"]
    return bearer_token, ingredient_used
