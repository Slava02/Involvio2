# BlockUserRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**who_id** | **int** | Telegram UserID of user who is blocking | 
**whom_id** | **int** | Telegram UserID of user who is being blocked | 

## Example

```python
from random_coffe_client.models.block_user_request_body import BlockUserRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BlockUserRequestBody from a JSON string
block_user_request_body_instance = BlockUserRequestBody.from_json(json)
# print the JSON string representation of the object
print(BlockUserRequestBody.to_json())

# convert the object into a dict
block_user_request_body_dict = block_user_request_body_instance.to_dict()
# create an instance of BlockUserRequestBody from a dict
block_user_request_body_from_dict = BlockUserRequestBody.from_dict(block_user_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


