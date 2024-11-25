# UserEventsResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[Event]**](Event.md) |  | 

## Example

```python
from random_coffe_client.models.user_events_response_body import UserEventsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserEventsResponseBody from a JSON string
user_events_response_body_instance = UserEventsResponseBody.from_json(json)
# print the JSON string representation of the object
print(UserEventsResponseBody.to_json())

# convert the object into a dict
user_events_response_body_dict = user_events_response_body_instance.to_dict()
# create an instance of UserEventsResponseBody from a dict
user_events_response_body_from_dict = UserEventsResponseBody.from_dict(user_events_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


