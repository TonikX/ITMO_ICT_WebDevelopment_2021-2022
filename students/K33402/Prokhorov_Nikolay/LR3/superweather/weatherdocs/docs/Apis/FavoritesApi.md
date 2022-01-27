# FavoritesApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**favoritesCreate**](FavoritesApi.md#favoritesCreate) | **POST** /favorites | 
[**favoritesDelete**](FavoritesApi.md#favoritesDelete) | **DELETE** /favorites/{id} | 
[**favoritesList**](FavoritesApi.md#favoritesList) | **GET** /favorites | 
[**favoritesPartialUpdate**](FavoritesApi.md#favoritesPartialUpdate) | **PATCH** /favorites/{id} | 
[**favoritesRead**](FavoritesApi.md#favoritesRead) | **GET** /favorites/{id} | 
[**favoritesUpdate**](FavoritesApi.md#favoritesUpdate) | **PUT** /favorites/{id} | 


<a name="favoritesCreate"></a>
# **favoritesCreate**
> FavoriteCity favoritesCreate(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FavoriteCity**](../Models/FavoriteCity.md)|  |

### Return type

[**FavoriteCity**](../Models/FavoriteCity.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="favoritesDelete"></a>
# **favoritesDelete**
> favoritesDelete(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this favorite city. | [default to null]

### Return type

null (empty response body)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="favoritesList"></a>
# **favoritesList**
> List favoritesList()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/FavoriteCity.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="favoritesPartialUpdate"></a>
# **favoritesPartialUpdate**
> FavoriteCity favoritesPartialUpdate(id, data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this favorite city. | [default to null]
 **data** | [**FavoriteCity**](../Models/FavoriteCity.md)|  |

### Return type

[**FavoriteCity**](../Models/FavoriteCity.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="favoritesRead"></a>
# **favoritesRead**
> FavoriteCity favoritesRead(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this favorite city. | [default to null]

### Return type

[**FavoriteCity**](../Models/FavoriteCity.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="favoritesUpdate"></a>
# **favoritesUpdate**
> FavoriteCity favoritesUpdate(id, data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this favorite city. | [default to null]
 **data** | [**FavoriteCity**](../Models/FavoriteCity.md)|  |

### Return type

[**FavoriteCity**](../Models/FavoriteCity.md)

### Authorization

[Basic](../swagger.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

