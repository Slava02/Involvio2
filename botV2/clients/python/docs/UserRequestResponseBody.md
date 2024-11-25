# UserRequestResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**birthday** | **datetime** | Birthday | 
**city** | **str** | User&#39;s city | 
**full_name** | **str** | First name | 
**gender** | **str** | User&#39;s gender | 
**goal** | **str** | User&#39;s goal for the meetings | 
**groups** | [**List[Group]**](Group.md) | User&#39;s groups | 
**id** | **int** | Telegram UserID | 
**interests** | **str** | User&#39;s interests | 
**photo_url** | **str** | Photo URL | 
**position** | **str** | User&#39;s position in organization | 
**socials** | **str** | User&#39;s account | 
**user_name** | **str** | Username | 

## Example

```python
from random_coffe_client.models.user_request_response_body import UserRequestResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequestResponseBody from a JSON string
user_request_response_body_instance = UserRequestResponseBody.from_json(json)
# print the JSON string representation of the object
print(UserRequestResponseBody.to_json())

# convert the object into a dict
user_request_response_body_dict = user_request_response_body_instance.to_dict()
# create an instance of UserRequestResponseBody from a dict
user_request_response_body_from_dict = UserRequestResponseBody.from_dict(user_request_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


