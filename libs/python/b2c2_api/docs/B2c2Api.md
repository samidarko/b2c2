# b2c2_api.B2c2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**b2c2_balance_get**](B2c2Api.md#b2c2_balance_get) | **GET** /balance | Get Balances
[**b2c2_instruments_get**](B2c2Api.md#b2c2_instruments_get) | **GET** /instruments | Get Tradable Instruments
[**b2c2_order_post**](B2c2Api.md#b2c2_order_post) | **POST** /order | Post an order
[**b2c2_request_for_quote_post**](B2c2Api.md#b2c2_request_for_quote_post) | **POST** /request_for_quote | API endpoint to send Request for Quotes.


# **b2c2_balance_get**
> dict(str, str) b2c2_balance_get()

Get Balances

This shows the available balances in the supported currencies.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import b2c2_api
from b2c2_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = b2c2_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with b2c2_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = b2c2_api.B2c2Api(api_client)
    
    try:
        # Get Balances
        api_response = api_instance.b2c2_balance_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling B2c2Api->b2c2_balance_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, str)**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request –- Incorrect parameters. |  -  |
**401** | Unauthorized – Wrong Token. |  -  |
**404** | Not Found – The specified endpoint could not be found. |  -  |
**405** | Method Not Allowed – You tried to access an endpoint with an invalid method. |  -  |
**406** | Not Acceptable – Incorrect request format. |  -  |
**429** | Too Many Requests – Rate limited, pause requests. |  -  |
**500** | Internal Server Error – We had a problem with our server. Try again later. |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **b2c2_instruments_get**
> list[Instrument] b2c2_instruments_get()

Get Tradable Instruments

List all your tradable instruments. Please ask your sales representative if you want access to more instruments.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import b2c2_api
from b2c2_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = b2c2_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with b2c2_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = b2c2_api.B2c2Api(api_client)
    
    try:
        # Get Tradable Instruments
        api_response = api_instance.b2c2_instruments_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling B2c2Api->b2c2_instruments_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Instrument]**](Instrument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request –- Incorrect parameters. |  -  |
**401** | Unauthorized – Wrong Token. |  -  |
**404** | Not Found – The specified endpoint could not be found. |  -  |
**405** | Method Not Allowed – You tried to access an endpoint with an invalid method. |  -  |
**406** | Not Acceptable – Incorrect request format. |  -  |
**429** | Too Many Requests – Rate limited, pause requests. |  -  |
**500** | Internal Server Error – We had a problem with our server. Try again later. |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **b2c2_order_post**
> Order b2c2_order_post(order_request)

Post an order

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import b2c2_api
from b2c2_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = b2c2_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with b2c2_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = b2c2_api.B2c2Api(api_client)
    order_request = b2c2_api.OrderRequest() # OrderRequest | 

    try:
        # Post an order
        api_response = api_instance.b2c2_order_post(order_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling B2c2Api->b2c2_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_request** | [**OrderRequest**](OrderRequest.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request –- Incorrect parameters. |  -  |
**401** | Unauthorized – Wrong Token. |  -  |
**404** | Not Found – The specified endpoint could not be found. |  -  |
**405** | Method Not Allowed – You tried to access an endpoint with an invalid method. |  -  |
**406** | Not Acceptable – Incorrect request format. |  -  |
**429** | Too Many Requests – Rate limited, pause requests. |  -  |
**500** | Internal Server Error – We had a problem with our server. Try again later. |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **b2c2_request_for_quote_post**
> Quote b2c2_request_for_quote_post(quote_request)

API endpoint to send Request for Quotes.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import b2c2_api
from b2c2_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = b2c2_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with b2c2_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = b2c2_api.B2c2Api(api_client)
    quote_request = b2c2_api.QuoteRequest() # QuoteRequest | 

    try:
        # API endpoint to send Request for Quotes.
        api_response = api_instance.b2c2_request_for_quote_post(quote_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling B2c2Api->b2c2_request_for_quote_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_request** | [**QuoteRequest**](QuoteRequest.md)|  | 

### Return type

[**Quote**](Quote.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request –- Incorrect parameters. |  -  |
**401** | Unauthorized – Wrong Token. |  -  |
**404** | Not Found – The specified endpoint could not be found. |  -  |
**405** | Method Not Allowed – You tried to access an endpoint with an invalid method. |  -  |
**406** | Not Acceptable – Incorrect request format. |  -  |
**429** | Too Many Requests – Rate limited, pause requests. |  -  |
**500** | Internal Server Error – We had a problem with our server. Try again later. |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

