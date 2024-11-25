# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthday** | **datetime** | Birthday | 
**city** | **str** | User&#39;s city | 
**full_name** | **str** | First name | 
**gender** | **str** | User&#39;s gender | 
**goal** | **str** | User&#39;s goal for the meetings | 
**groups** | [**List[Group]**](Group.md) | User&#39;s groups | 
**id** | **int** | Telegram UserID | 
**interests** | **str** | User&#39;s interests | 
**photo_url** | **str** | Photo URL | 
**position** | **str** | User&#39;s position in organization | 
**socials** | **str** | User&#39;s account | 
**user_name** | **str** | Username | 

## Example

```python
from random_coffe_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


