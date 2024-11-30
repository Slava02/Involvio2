from botV2.clients.python import random_coffe_client
from datetime import datetime
import os
from botV2.clients.python.random_coffe_client.models.user_request_response_body import UserRequestResponseBody
from botV2.clients.python.random_coffe_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = random_coffe_client.Configuration(
    host="http://127.0.0.1:8000"
)
user_dict = {
    "birthday": "2020-12-09T16:09:53+00:00",
    "city": "Moscow",
    "full_name": "tikhon lavrukhin",
    "gender": "male",
    "goal": "fun",
    "groups": [
        {
            "id": 1234,
            "name": "mai"
        }
    ],
    "id": 12356,
    "interests": "Programming,math",
    "photo_url": "https://photo",
    "position": "student",
    "socials": "string",
    "user_name": "tik"
}


# Enter a context with an instance of the API client
with random_coffe_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = random_coffe_client.UsersApi(api_client)
    user_request_response_body = random_coffe_client.UserRequestResponseBody.from_dict(user_dict) # UserRequestResponseBody |

    try:
        # create new user
        api_instance.create_user(user_request_response_body)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)

if __name__ == '__main__':
    dict = {'full_name': 'Тихон Лаврухин', 'gender': 'male', 'photo_url': 'AgACAgIAAxUAAWdJfxsG_8RVJj94f1LIS7iPYDhAAAKrpzEbILJILGaEbPLvHJSSAQADAgADYwADNgQ', 'city': 'Москва', 'socials': 'https://asdsd', 'position': 'Разработчик', 'interests': 'Математика, шахматы', 'birthday': datetime(2001, 4, 20, 0, 0), 'goal': '50/50', 'groups': [], 'id': 123, 'user_name':'asdasd'}
    user = UserRequestResponseBody.from_dict(dict)
    print(user)