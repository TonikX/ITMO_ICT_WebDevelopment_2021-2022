# UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersProfileAvatarUpdate**](UsersApi.md#usersProfileAvatarUpdate) | **PUT** /api/users/profile/avatar | Обновить аватар текущего пользователя
[**usersProfileDestroy**](UsersApi.md#usersProfileDestroy) | **DELETE** /api/users/profile | Деактивировать аккаунт
[**usersProfilePartialUpdate**](UsersApi.md#usersProfilePartialUpdate) | **PATCH** /api/users/profile | Редактировать информацию о текущем пользователе
[**usersProfileRetrieve**](UsersApi.md#usersProfileRetrieve) | **GET** /api/users/profile | Получить информацию о текущем пользователе
[**usersProfileUpdate**](UsersApi.md#usersProfileUpdate) | **PUT** /api/users/profile | Редактировать информацию о текущем пользователе


<a name="usersProfileAvatarUpdate"></a>
# **usersProfileAvatarUpdate**
> ProfileAvatar usersProfileAvatarUpdate(avatar)

Обновить аватар текущего пользователя

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar** | **File**|  | [optional] [default to null]

### Return type

[**ProfileAvatar**](../models/ProfileAvatar.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

<a name="usersProfileDestroy"></a>
# **usersProfileDestroy**
> usersProfileDestroy()

Деактивировать аккаунт

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="usersProfilePartialUpdate"></a>
# **usersProfilePartialUpdate**
> Profile usersProfilePartialUpdate(firstName, lastName, checkScanToken)

Редактировать информацию о текущем пользователе

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstName** | **String**|  | [optional] [default to null]
 **lastName** | **String**|  | [optional] [default to null]
 **checkScanToken** | **String**|  | [optional] [default to null]

### Return type

[**Profile**](../models/Profile.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, application/json, multipart/form-data
- **Accept**: application/json

<a name="usersProfileRetrieve"></a>
# **usersProfileRetrieve**
> Profile usersProfileRetrieve()

Получить информацию о текущем пользователе

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](../models/Profile.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="usersProfileUpdate"></a>
# **usersProfileUpdate**
> Profile usersProfileUpdate(firstName, lastName, checkScanToken)

Редактировать информацию о текущем пользователе

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstName** | **String**|  | [optional] [default to null]
 **lastName** | **String**|  | [optional] [default to null]
 **checkScanToken** | **String**|  | [optional] [default to null]

### Return type

[**Profile**](../models/Profile.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, application/json, multipart/form-data
- **Accept**: application/json

