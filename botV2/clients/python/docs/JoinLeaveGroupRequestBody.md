# JoinLeaveGroupRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**group_name** | **str** | Group UserID | 
**user_id** | **int** | Group UserID | 

## Example

```python
from random_coffe_client.models.join_leave_group_request_body import JoinLeaveGroupRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of JoinLeaveGroupRequestBody from a JSON string
join_leave_group_request_body_instance = JoinLeaveGroupRequestBody.from_json(json)
# print the JSON string representation of the object
print(JoinLeaveGroupRequestBody.to_json())

# convert the object into a dict
join_leave_group_request_body_dict = join_leave_group_request_body_instance.to_dict()
# create an instance of JoinLeaveGroupRequestBody from a dict
join_leave_group_request_body_from_dict = JoinLeaveGroupRequestBody.from_dict(join_leave_group_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


