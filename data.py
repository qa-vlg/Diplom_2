

class OrderData:

   valid_ingredients = [
       "61c0c5a71d1f82001bdaaa6d",
       "61c0c5a71d1f82001bdaaa6f",
       "61c0c5a71d1f82001bdaaa70",
       "61c0c5a71d1f82001bdaaa71",
       "61c0c5a71d1f82001bdaaa72",
       "61c0c5a71d1f82001bdaaa6e",
       "61c0c5a71d1f82001bdaaa73",
       "61c0c5a71d1f82001bdaaa74",
       "61c0c5a71d1f82001bdaaa6c",
       "61c0c5a71d1f82001bdaaa75",
       "61c0c5a71d1f82001bdaaa76",
       "61c0c5a71d1f82001bdaaa77",
       "61c0c5a71d1f82001bdaaa78",
       "61c0c5a71d1f82001bdaaa79",
       "61c0c5a71d1f82001bdaaa7a"
   ]
   invalid_ingredients = [
       "61c0c5a71d1f82001bdaaa6d_invalid",
       "61c0c5a71d1f82001bdaaa6f_invalid",
       "61c0c5a71d1f82001bdaaa70_invalid",
   ]

class UserLoginData:
    
    valid_user_credentials = {
        "email": "qa_vlg_test_user@yaahoo.com",
        "password": "pwd777"
    }
    user_credentials_invalid_pwd = {
        "email": "qa_vlg_test_user@yaahoo.com",
        "password": "qwerty1234"
    }
    user_credentials_invalid_email = {
        "email": "qa_322vlg_test_user@yaahoo.com",
        "password": "pwd777"
    }
    user_credentials_empty_email = {
        "email": "",
        "password": "pwd777"
    }
    user_credentials_empty_pwd = {
        "email": "qa_vlg_test_user@yaahoo.com",
        "password": ""
    }

class UserSignUpData:

    existing_user_credentials = {
        "email": "qa_vlg_test_user@yaahoo.com",
        "password": "pwd777",
        "name": "qa_vlg"
    }
    user_credentials_empty_email = {
        "email": "",
        "password": "qwerty123",
        "name": "Alexx"
    }
    user_credentials_empty_pwd = {
        "login": "some_test_data@hootmail.com",
        "password": "",
        "firstName": "Samm"
    }
    user_credentials_empty_name = {
        "login": "some_test_data@hootmail.com",
        "password": "123342s!",
        "name": ""
    }

class ErrorMessages:

    login_error = "email or password are incorrect"
    unauthorised_error = "You should be authorised"
    missing_user_info = "Email, password and name are required fields"
    existing_account = "User already exists"
    no_id = "Ingredient ids must be provided"

class ResponseCodes:
    forbidden = 403
    ok = 200
    unauthorised = 401
    accepted = 202
    server_error = 500
    bad_request = 400

class ConfirmationMessage:
    user_removed = "User successfully removed"
    