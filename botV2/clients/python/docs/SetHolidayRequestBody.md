# SetHolidayRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**id** | **int** | Telegram UserID | 
**till_date** | **datetime** | When holiday ends RFC 3339 | 

## Example

```python
from random_coffe_client.models.set_holiday_request_body import SetHolidayRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SetHolidayRequestBody from a JSON string
set_holiday_request_body_instance = SetHolidayRequestBody.from_json(json)
# print the JSON string representation of the object
print(SetHolidayRequestBody.to_json())

# convert the object into a dict
set_holiday_request_body_dict = set_holiday_request_body_instance.to_dict()
# create an instance of SetHolidayRequestBody from a dict
set_holiday_request_body_from_dict = SetHolidayRequestBody.from_dict(set_holiday_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


