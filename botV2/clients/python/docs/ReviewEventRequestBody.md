# ReviewEventRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**event_id** | **int** | event id | 
**grade** | **int** | grade of event | 
**who_id** | **int** | reviewer id | 
**whom_id** | **int** | reviewee id | 

## Example

```python
from random_coffe_client.models.review_event_request_body import ReviewEventRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewEventRequestBody from a JSON string
review_event_request_body_instance = ReviewEventRequestBody.from_json(json)
# print the JSON string representation of the object
print(ReviewEventRequestBody.to_json())

# convert the object into a dict
review_event_request_body_dict = review_event_request_body_instance.to_dict()
# create an instance of ReviewEventRequestBody from a dict
review_event_request_body_from_dict = ReviewEventRequestBody.from_dict(review_event_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


