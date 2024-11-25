# random_coffe_client.GroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupsApi.md#create_group) | **POST** /groups | create new group
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /groups/{name} | delete group
[**get_group**](GroupsApi.md#get_group) | **GET** /groups/{name} | group by name
[**join_group**](GroupsApi.md#join_group) | **POST** /groups/join | join group
[**leave_group**](GroupsApi.md#leave_group) | **POST** /groups/leave | leave group


# **create_group**
> CreateGroup201Response create_group(create_group_request_body)

create new group

Create a new group record.

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.create_group201_response import CreateGroup201Response
from random_coffe_client.models.create_group_request_body import CreateGroupRequestBody
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
    api_instance = random_coffe_client.GroupsApi(api_client)
    create_group_request_body = random_coffe_client.CreateGroupRequestBody() # CreateGroupRequestBody | 

    try:
        # create new group
        api_response = api_instance.create_group(create_group_request_body)
        print("The response of GroupsApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_request_body** | [**CreateGroupRequestBody**](CreateGroupRequestBody.md)|  | 

### Return type

[**CreateGroup201Response**](CreateGroup201Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | IGroupUC created |  * Location - URL of the newly created group <br>  |
**400** | Invalid request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(name)

delete group

[NOT NEEDED] delete group

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
    api_instance = random_coffe_client.GroupsApi(api_client)
    name = 'MAI' # str | Group Name

    try:
        # delete group
        api_instance.delete_group(name)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Group Name | 

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
**201** | Created |  -  |
**204** | IGroupUC deleted |  -  |
**404** | IGroupUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> CreateGroup201Response get_group(name)

group by name

Get group by name.

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.create_group201_response import CreateGroup201Response
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
    api_instance = random_coffe_client.GroupsApi(api_client)
    name = 'MAI' # str | Group Name

    try:
        # group by name
        api_response = api_instance.get_group(name)
        print("The response of GroupsApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Group Name | 

### Return type

[**CreateGroup201Response**](CreateGroup201Response.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IGroupUC response |  -  |
**400** | Invalid request |  -  |
**404** | IGroupUC not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_group**
> join_group(join_leave_group_request_body)

join group

join group

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.join_leave_group_request_body import JoinLeaveGroupRequestBody
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
    api_instance = random_coffe_client.GroupsApi(api_client)
    join_leave_group_request_body = random_coffe_client.JoinLeaveGroupRequestBody() # JoinLeaveGroupRequestBody | 

    try:
        # join group
        api_instance.join_group(join_leave_group_request_body)
    except Exception as e:
        print("Exception when calling GroupsApi->join_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **join_leave_group_request_body** | [**JoinLeaveGroupRequestBody**](JoinLeaveGroupRequestBody.md)|  | 

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
**201** | joined IGroupUC |  -  |
**400** | Invalid request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_group**
> leave_group(join_leave_group_request_body)

leave group

leave group

### Example

* Bearer (JWT) Authentication (auth):

```python
import random_coffe_client
from random_coffe_client.models.join_leave_group_request_body import JoinLeaveGroupRequestBody
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
    api_instance = random_coffe_client.GroupsApi(api_client)
    join_leave_group_request_body = random_coffe_client.JoinLeaveGroupRequestBody() # JoinLeaveGroupRequestBody | 

    try:
        # leave group
        api_instance.leave_group(join_leave_group_request_body)
    except Exception as e:
        print("Exception when calling GroupsApi->leave_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **join_leave_group_request_body** | [**JoinLeaveGroupRequestBody**](JoinLeaveGroupRequestBody.md)|  | 

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
**201** | leaved IGroupUC |  -  |
**400** | Invalid request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

