import random
import string

class UserRandomData:

    @staticmethod
    def create_user_data():
        email = UserRandomData.user_email()
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = random.choice(range(7, 25))))
        name = UserRandomData.user_name()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload
    
    @staticmethod
    def user_email():
        domain = 'qa.com'
        prefix = ''.join(random.choices(string.ascii_letters + string.digits, k = random.choice(range(15, 25))))
        return f'{prefix}@{domain}'
    
    @staticmethod
    def user_name():
        return ''.join(random.choices(string.ascii_letters, k = random.choice(range(5, 15))))
