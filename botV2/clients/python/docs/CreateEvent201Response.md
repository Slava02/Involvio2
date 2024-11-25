# CreateEvent201Response


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
from random_coffe_client.models.create_event201_response import CreateEvent201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEvent201Response from a JSON string
create_event201_response_instance = CreateEvent201Response.from_json(json)
# print the JSON string representation of the object
print(CreateEvent201Response.to_json())

# convert the object into a dict
create_event201_response_dict = create_event201_response_instance.to_dict()
# create an instance of CreateEvent201Response from a dict
create_event201_response_from_dict = CreateEvent201Response.from_dict(create_event201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


