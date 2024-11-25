# CreateGroupRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**name** | **str** | Group Name | 

## Example

```python
from random_coffe_client.models.create_group_request_body import CreateGroupRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupRequestBody from a JSON string
create_group_request_body_instance = CreateGroupRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateGroupRequestBody.to_json())

# convert the object into a dict
create_group_request_body_dict = create_group_request_body_instance.to_dict()
# create an instance of CreateGroupRequestBody from a dict
create_group_request_body_from_dict = CreateGroupRequestBody.from_dict(create_group_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


