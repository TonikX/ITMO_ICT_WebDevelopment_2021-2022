# ChecksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checksItemsUpdate**](ChecksApi.md#checksItemsUpdate) | **PUT** /api/checks/{id}/items | Установить взаиморасчет для чека
[**checksList**](ChecksApi.md#checksList) | **GET** /api/checks | Получить список чеков
[**checksRetrieve**](ChecksApi.md#checksRetrieve) | **GET** /api/checks/{id} | Получить чек по ID
[**checksSyncCreate**](ChecksApi.md#checksSyncCreate) | **POST** /api/checks/sync | Синхронизировать чеки из ЧекСкан


<a name="checksItemsUpdate"></a>
# **checksItemsUpdate**
> checksItemsUpdate(id, CheckItemPartRequest)

Установить взаиморасчет для чека

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique value identifying this Чек. | [default to null]
 **CheckItemPartRequest** | [**List**](../models/CheckItemPartRequest.md)|  |

### Return type

null (empty response body)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="checksList"></a>
# **checksList**
> PaginatedCheckList checksList(page)

Получить список чеков

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **Integer**| A page number within the paginated result set. | [optional] [default to null]

### Return type

[**PaginatedCheckList**](../models/PaginatedCheckList.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="checksRetrieve"></a>
# **checksRetrieve**
> Check checksRetrieve(id)

Получить чек по ID

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique value identifying this Чек. | [default to null]

### Return type

[**Check**](../models/Check.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="checksSyncCreate"></a>
# **checksSyncCreate**
> checksSyncCreate()

Синхронизировать чеки из ЧекСкан

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

