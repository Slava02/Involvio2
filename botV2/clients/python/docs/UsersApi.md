# random_coffe_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_user**](UsersApi.md#block_user) | **POST** /users/block | block user
[**cancel_user_holiday**](UsersApi.md#cancel_user_holiday) | **POST** /users/holiday/cancel | set or reset holiday
[**create_user**](UsersApi.md#create_user) | **POST** /users | create new user
[**get_user**](UsersApi.md#get_user) | **GET** /users/{username} | user by username
[**set_user_holiday**](UsersApi.md#set_user_holiday) | **POST** /users/holiday | set holiday
[**update_user**](UsersApi.md#update_user) | **PUT** /users | update user


# **block_user**
> block_user(block_user_request_body)

block user

block user

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.block_user_request_body import BlockUserRequestBody
from random_coffe_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = random_coffe_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): auth
configuration = random_coffe_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with random_coffe_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = random_coffe_client.UsersApi(api_client)
    block_user_request_body = random_coffe_client.BlockUserRequestBody() # BlockUserRequestBody | 

    try:
        # block user
        api_instance.block_user(block_user_request_body)
    except Exception as e:
        print("Exception when calling UsersApi->block_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_user_request_body** | [**BlockUserRequestBody**](BlockUserRequestBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User blocked |  -  |
**204** | No Content |  -  |
**400** | Invalid request |  -  |
**404** | IUserUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_user_holiday**
> cancel_user_holiday(user_by_id_request_body)

set or reset holiday

returns info about current user's holidays

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.user_by_id_request_body import UserByIDRequestBody
from random_coffe_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = random_coffe_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): auth
configuration = random_coffe_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with random_coffe_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = random_coffe_client.UsersApi(api_client)
    user_by_id_request_body = random_coffe_client.UserByIDRequestBody() # UserByIDRequestBody | 

    try:
        # set or reset holiday
        api_instance.cancel_user_holiday(user_by_id_request_body)
    except Exception as e:
        print("Exception when calling UsersApi->cancel_user_holiday: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_by_id_request_body** | [**UserByIDRequestBody**](UserByIDRequestBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Holiday canceled |  -  |
**204** | No Content |  -  |
**400** | Invalid request |  -  |
**404** | IUserUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> create_user(user_request_response_body)

create new user

Create a new user record.

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.user_request_response_body import UserRequestResponseBody
from random_coffe_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = random_coffe_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): auth
configuration = random_coffe_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with random_coffe_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = random_coffe_client.UsersApi(api_client)
    user_request_response_body = random_coffe_client.UserRequestResponseBody() # UserRequestResponseBody | 

    try:
        # create new user
        api_instance.create_user(user_request_response_body)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_request_response_body** | [**UserRequestResponseBody**](UserRequestResponseBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created |  -  |
**400** | Invalid request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UpdateUser200Response get_user(username)

user by username

Get a user by username.

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.update_user200_response import UpdateUser200Response
from random_coffe_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = random_coffe_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): auth
configuration = random_coffe_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with random_coffe_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = random_coffe_client.UsersApi(api_client)
    username = 'ivanko228' # str | Username

    try:
        # user by username
        api_response = api_instance.get_user(username)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username | 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IUserUC response |  -  |
**400** | Invalid request |  -  |
**404** | IUserUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_holiday**
> set_user_holiday(set_holiday_request_body)

set holiday

prevent bot from sending messages for a certain amount of time

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.set_holiday_request_body import SetHolidayRequestBody
from random_coffe_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = random_coffe_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): auth
configuration = random_coffe_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with random_coffe_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = random_coffe_client.UsersApi(api_client)
    set_holiday_request_body = random_coffe_client.SetHolidayRequestBody() # SetHolidayRequestBody | 

    try:
        # set holiday
        api_instance.set_user_holiday(set_holiday_request_body)
    except Exception as e:
        print("Exception when calling UsersApi->set_user_holiday: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_holiday_request_body** | [**SetHolidayRequestBody**](SetHolidayRequestBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Holiday set |  -  |
**204** | No Content |  -  |
**400** | Invalid request |  -  |
**404** | IUserUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UpdateUser200Response update_user(update_user_request_body)

update user

Update an existing user by UserID.

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.update_user200_response import UpdateUser200Response
from random_coffe_client.models.update_user_request_body import UpdateUserRequestBody
from random_coffe_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = random_coffe_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): auth
configuration = random_coffe_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with random_coffe_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = random_coffe_client.UsersApi(api_client)
    update_user_request_body = random_coffe_client.UpdateUserRequestBody() # UpdateUserRequestBody | 

    try:
        # update user
        api_response = api_instance.update_user(update_user_request_body)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_request_body** | [**UpdateUserRequestBody**](UpdateUserRequestBody.md)|  | 

### Return type

[**UpdateUser200Response**](UpdateUser200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IUserUC updated |  -  |
**400** | Invalid request |  -  |
**404** | IUserUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

