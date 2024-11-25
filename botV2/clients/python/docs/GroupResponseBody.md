# GroupResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from random_coffe_client.models.group_response_body import GroupResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GroupResponseBody from a JSON string
group_response_body_instance = GroupResponseBody.from_json(json)
# print the JSON string representation of the object
print(GroupResponseBody.to_json())

# convert the object into a dict
group_response_body_dict = group_response_body_instance.to_dict()
# create an instance of GroupResponseBody from a dict
group_response_body_from_dict = GroupResponseBody.from_dict(group_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


