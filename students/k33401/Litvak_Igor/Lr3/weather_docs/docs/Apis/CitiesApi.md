# CitiesApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**citiesClosest**](CitiesApi.md#citiesClosest) | **GET** /cities/closest/ | 
[**citiesFavouriteCreate**](CitiesApi.md#citiesFavouriteCreate) | **POST** /cities/favourite/ | 
[**citiesFavouriteDelete**](CitiesApi.md#citiesFavouriteDelete) | **DELETE** /cities/favourite/{id}/ | 
[**citiesFavouriteList**](CitiesApi.md#citiesFavouriteList) | **GET** /cities/favourite/ | 
[**citiesFavouritePartialUpdate**](CitiesApi.md#citiesFavouritePartialUpdate) | **PATCH** /cities/favourite/{id}/ | 
[**citiesFavouriteRead**](CitiesApi.md#citiesFavouriteRead) | **GET** /cities/favourite/{id}/ | 
[**citiesFavouriteUpdate**](CitiesApi.md#citiesFavouriteUpdate) | **PUT** /cities/favourite/{id}/ | 
[**citiesForecast**](CitiesApi.md#citiesForecast) | **GET** /cities/{id}/forecast/ | 
[**citiesList**](CitiesApi.md#citiesList) | **GET** /cities/ | 
[**citiesRead**](CitiesApi.md#citiesRead) | **GET** /cities/{id}/ | 


<a name="citiesClosest"></a>
# **citiesClosest**
> List citiesClosest(lat, lon)



    Returns city closest to certain coordinates

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **BigDecimal**|  | [default to null]
 **lon** | **BigDecimal**|  | [default to null]

### Return type

[**List**](../Models/City.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="citiesFavouriteCreate"></a>
# **citiesFavouriteCreate**
> FavouriteCity citiesFavouriteCreate(data)



    Viewset for favourite cities

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FavouriteCity**](../Models/FavouriteCity.md)|  |

### Return type

[**FavouriteCity**](../Models/FavouriteCity.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="citiesFavouriteDelete"></a>
# **citiesFavouriteDelete**
> citiesFavouriteDelete(id)



    Viewset for favourite cities

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Favourite city. | [default to null]

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="citiesFavouriteList"></a>
# **citiesFavouriteList**
> List citiesFavouriteList()



    Viewset for favourite cities

### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/FavouriteCity.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="citiesFavouritePartialUpdate"></a>
# **citiesFavouritePartialUpdate**
> FavouriteCity citiesFavouritePartialUpdate(id, data)



    Viewset for favourite cities

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Favourite city. | [default to null]
 **data** | [**FavouriteCity**](../Models/FavouriteCity.md)|  |

### Return type

[**FavouriteCity**](../Models/FavouriteCity.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="citiesFavouriteRead"></a>
# **citiesFavouriteRead**
> FavouriteCity citiesFavouriteRead(id)



    Viewset for favourite cities

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Favourite city. | [default to null]

### Return type

[**FavouriteCity**](../Models/FavouriteCity.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="citiesFavouriteUpdate"></a>
# **citiesFavouriteUpdate**
> FavouriteCity citiesFavouriteUpdate(id, data)



    Viewset for favourite cities

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this Favourite city. | [default to null]
 **data** | [**FavouriteCity**](../Models/FavouriteCity.md)|  |

### Return type

[**FavouriteCity**](../Models/FavouriteCity.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="citiesForecast"></a>
# **citiesForecast**
> City citiesForecast(id)



    Cached wrapper around OpenWeatherMap API

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this City. | [default to null]

### Return type

[**City**](../Models/City.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="citiesList"></a>
# **citiesList**
> List citiesList()



    Viewset for cities

### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/City.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="citiesRead"></a>
# **citiesRead**
> City citiesRead(id)



    Viewset for cities

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this City. | [default to null]

### Return type

[**City**](../Models/City.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

