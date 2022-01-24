# ForecastApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecastDelete**](ForecastApi.md#forecastDelete) | **DELETE** /forecast/{id} | 
[**forecastList**](ForecastApi.md#forecastList) | **GET** /forecast | 
[**forecastRead**](ForecastApi.md#forecastRead) | **GET** /forecast/{id} | 


<a name="forecastDelete"></a>
# **forecastDelete**
> forecastDelete(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Прогноз. | [default to null]

### Return type

null (empty response body)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="forecastList"></a>
# **forecastList**
> List forecastList()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/Forecast.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="forecastRead"></a>
# **forecastRead**
> Forecast forecastRead(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Прогноз. | [default to null]

### Return type

[**Forecast**](../Models/Forecast.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

