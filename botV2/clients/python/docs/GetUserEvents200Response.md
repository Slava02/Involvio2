# GetUserEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**UserEventsResponseBody**](UserEventsResponseBody.md) |  | 

## Example

```python
from random_coffe_client.models.get_user_events200_response import GetUserEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserEvents200Response from a JSON string
get_user_events200_response_instance = GetUserEvents200Response.from_json(json)
# print the JSON string representation of the object
print(GetUserEvents200Response.to_json())

# convert the object into a dict
get_user_events200_response_dict = get_user_events200_response_instance.to_dict()
# create an instance of GetUserEvents200Response from a dict
get_user_events200_response_from_dict = GetUserEvents200Response.from_dict(get_user_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


