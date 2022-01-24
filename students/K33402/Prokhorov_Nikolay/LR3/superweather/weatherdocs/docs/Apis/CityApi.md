# CityApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cityCreate**](CityApi.md#cityCreate) | **POST** /city | 
[**cityDailyList**](CityApi.md#cityDailyList) | **GET** /city/{id}/daily | 
[**cityDelete**](CityApi.md#cityDelete) | **DELETE** /city/{id} | 
[**cityForecastList**](CityApi.md#cityForecastList) | **GET** /city/{id}/forecast | 
[**cityList**](CityApi.md#cityList) | **GET** /city | 
[**cityPartialUpdate**](CityApi.md#cityPartialUpdate) | **PATCH** /city/{id} | 
[**cityRead**](CityApi.md#cityRead) | **GET** /city/{id} | 
[**cityUpdate**](CityApi.md#cityUpdate) | **PUT** /city/{id} | 


<a name="cityCreate"></a>
# **cityCreate**
> City cityCreate(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**City**](../Models/City.md)|  |

### Return type

[**City**](../Models/City.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="cityDailyList"></a>
# **cityDailyList**
> List cityDailyList(id, weekday)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Прогноз по дням. | [default to null]
 **weekday** | **BigDecimal**|  | [optional] [default to null]

### Return type

[**List**](../Models/CityDaily.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="cityDelete"></a>
# **cityDelete**
> cityDelete(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Город. | [default to null]

### Return type

null (empty response body)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="cityForecastList"></a>
# **cityForecastList**
> List cityForecastList(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Прогноз. | [default to null]

### Return type

[**List**](../Models/Forecast.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="cityList"></a>
# **cityList**
> List cityList(q)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **String**|  | [optional] [default to null]

### Return type

[**List**](../Models/City.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="cityPartialUpdate"></a>
# **cityPartialUpdate**
> City cityPartialUpdate(id, data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Город. | [default to null]
 **data** | [**City**](../Models/City.md)|  |

### Return type

[**City**](../Models/City.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="cityRead"></a>
# **cityRead**
> City cityRead(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Город. | [default to null]

### Return type

[**City**](../Models/City.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="cityUpdate"></a>
# **cityUpdate**
> City cityUpdate(id, data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Город. | [default to null]
 **data** | [**City**](../Models/City.md)|  |

### Return type

[**City**](../Models/City.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

