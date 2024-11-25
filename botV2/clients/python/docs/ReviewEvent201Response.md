# ReviewEvent201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | event id | 
**grade** | **int** | grade of event | 
**id** | **int** | review id | 
**who_id** | **int** | reviewer id | 
**whom_id** | **int** | reviewee id | 

## Example

```python
from random_coffe_client.models.review_event201_response import ReviewEvent201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewEvent201Response from a JSON string
review_event201_response_instance = ReviewEvent201Response.from_json(json)
# print the JSON string representation of the object
print(ReviewEvent201Response.to_json())

# convert the object into a dict
review_event201_response_dict = review_event201_response_instance.to_dict()
# create an instance of ReviewEvent201Response from a dict
review_event201_response_from_dict = ReviewEvent201Response.from_dict(review_event201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


