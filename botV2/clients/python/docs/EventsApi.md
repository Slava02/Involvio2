# random_coffe_client.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event**](EventsApi.md#create_event) | **POST** /events | create new event
[**delete_event**](EventsApi.md#delete_event) | **DELETE** /events/{id} | delete event
[**get_user_events**](EventsApi.md#get_user_events) | **GET** /events/{id} | events by user id
[**review_event**](EventsApi.md#review_event) | **POST** /events/review | review event


# **create_event**
> CreateEvent201Response create_event(create_event_request_body)

create new event

Create new event record.

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.create_event201_response import CreateEvent201Response
from random_coffe_client.models.create_event_request_body import CreateEventRequestBody
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
    api_instance = random_coffe_client.EventsApi(api_client)
    create_event_request_body = random_coffe_client.CreateEventRequestBody() # CreateEventRequestBody | 

    try:
        # create new event
        api_response = api_instance.create_event(create_event_request_body)
        print("The response of EventsApi->create_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->create_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_request_body** | [**CreateEventRequestBody**](CreateEventRequestBody.md)|  | 

### Return type

[**CreateEvent201Response**](CreateEvent201Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | IEventUC created |  -  |
**400** | Invalid request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event**
> delete_event(id)

delete event

delete event

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
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
    api_instance = random_coffe_client.EventsApi(api_client)
    id = 1 # int | event id

    try:
        # delete event
        api_instance.delete_event(id)
    except Exception as e:
        print("Exception when calling EventsApi->delete_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| event id | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | deleted IEventUC |  -  |
**400** | Invalid request |  -  |
**404** | IEventUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_events**
> GetUserEvents200Response get_user_events(id)

events by user id

Get all events users where user participated

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.get_user_events200_response import GetUserEvents200Response
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
    api_instance = random_coffe_client.EventsApi(api_client)
    id = 1 # int | event id

    try:
        # events by user id
        api_response = api_instance.get_user_events(id)
        print("The response of EventsApi->get_user_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_user_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| event id | 

### Return type

[**GetUserEvents200Response**](GetUserEvents200Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IEventUC response |  -  |
**400** | Invalid request |  -  |
**404** | IEventUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_event**
> ReviewEvent201Response review_event(review_event_request_body)

review event

leave feedback about event

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.review_event201_response import ReviewEvent201Response
from random_coffe_client.models.review_event_request_body import ReviewEventRequestBody
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
    api_instance = random_coffe_client.EventsApi(api_client)
    review_event_request_body = random_coffe_client.ReviewEventRequestBody() # ReviewEventRequestBody | 

    try:
        # review event
        api_response = api_instance.review_event(review_event_request_body)
        print("The response of EventsApi->review_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->review_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_event_request_body** | [**ReviewEventRequestBody**](ReviewEventRequestBody.md)|  | 

### Return type

[**ReviewEvent201Response**](ReviewEvent201Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | IEventUC created |  * EventID -  <br>  * Grade -  <br>  * ID -  <br>  * WhoID -  <br>  * WhomID -  <br>  |
**400** | Invalid request |  -  |
**404** | IEventUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

