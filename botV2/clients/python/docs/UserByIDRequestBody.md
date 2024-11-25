# UserByIDRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**id** | **int** | UserID | 

## Example

```python
from random_coffe_client.models.user_by_id_request_body import UserByIDRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserByIDRequestBody from a JSON string
user_by_id_request_body_instance = UserByIDRequestBody.from_json(json)
# print the JSON string representation of the object
print(UserByIDRequestBody.to_json())

# convert the object into a dict
user_by_id_request_body_dict = user_by_id_request_body_instance.to_dict()
# create an instance of UserByIDRequestBody from a dict
user_by_id_request_body_from_dict = UserByIDRequestBody.from_dict(user_by_id_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


