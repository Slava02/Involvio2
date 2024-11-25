# EventResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | event time RFC 3339 | 
**description** | **str** | event description | 
**id** | **int** | event id | 
**name** | **str** | event name | 
**users** | [**List[User]**](User.md) | event members | 

## Example

```python
from random_coffe_client.models.event_response_body import EventResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponseBody from a JSON string
event_response_body_instance = EventResponseBody.from_json(json)
# print the JSON string representation of the object
print(EventResponseBody.to_json())

# convert the object into a dict
event_response_body_dict = event_response_body_instance.to_dict()
# create an instance of EventResponseBody from a dict
event_response_body_from_dict = EventResponseBody.from_dict(event_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


