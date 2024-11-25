# CreateEventRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**var_date** | **datetime** | event time RFC 3339 | 
**description** | **str** | event description | 
**name** | **str** | event name | 
**users** | [**List[User]**](User.md) | event members | 

## Example

```python
from random_coffe_client.models.create_event_request_body import CreateEventRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventRequestBody from a JSON string
create_event_request_body_instance = CreateEventRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateEventRequestBody.to_json())

# convert the object into a dict
create_event_request_body_dict = create_event_request_body_instance.to_dict()
# create an instance of CreateEventRequestBody from a dict
create_event_request_body_from_dict = CreateEventRequestBody.from_dict(create_event_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


