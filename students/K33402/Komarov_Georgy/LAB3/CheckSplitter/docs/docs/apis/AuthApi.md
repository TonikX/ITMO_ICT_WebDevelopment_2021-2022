# AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authLoginCreate**](AuthApi.md#authLoginCreate) | **POST** /api/auth/login/ | Авторизация пользователя
[**authLogoutCreate**](AuthApi.md#authLogoutCreate) | **POST** /api/auth/logout/ | Выход
[**authPasswordChangeCreate**](AuthApi.md#authPasswordChangeCreate) | **POST** /api/auth/password/change/ | Смена пароля
[**authPasswordResetConfirmCreate**](AuthApi.md#authPasswordResetConfirmCreate) | **POST** /api/auth/password/reset/confirm/ | Подтверждение сброса пароля
[**authPasswordResetCreate**](AuthApi.md#authPasswordResetCreate) | **POST** /api/auth/password/reset/ | Запрос на сброс пароля
[**authRegistrationCreate**](AuthApi.md#authRegistrationCreate) | **POST** /api/auth/registration/ | Регистрация пользователя
[**authRegistrationResendEmailCreate**](AuthApi.md#authRegistrationResendEmailCreate) | **POST** /api/auth/registration/resend-email/ | Повторная отправка e-mail
[**authRegistrationVerifyEmailCreate**](AuthApi.md#authRegistrationVerifyEmailCreate) | **POST** /api/auth/registration/verify-email/ | Подтверждение e-mail
[**authTokenRefreshCreate**](AuthApi.md#authTokenRefreshCreate) | **POST** /api/auth/token/refresh/ | Обновить JWT токен
[**authTokenVerifyCreate**](AuthApi.md#authTokenVerifyCreate) | **POST** /api/auth/token/verify/ | Валидировать JWT токен


<a name="authLoginCreate"></a>
# **authLoginCreate**
> JWT authLoginCreate(password, username, email)

Авторизация пользователя

    Check the credentials and return the REST Token if the credentials are valid and authenticated. Calls Django Auth login method to register User ID in Django session framework  Accept the following POST parameters: username, password Return the REST Framework Token Object&#39;s key.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **String**|  | [default to null]
 **username** | **String**|  | [optional] [default to null]
 **email** | **String**|  | [optional] [default to null]

### Return type

[**JWT**](../models/JWT.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
- **Accept**: application/json

<a name="authLogoutCreate"></a>
# **authLogoutCreate**
> RestAuthDetail authLogoutCreate()

Выход

    Calls Django logout method and delete the Token object assigned to the current User object.  Accepts/Returns nothing.

### Parameters
This endpoint does not need any parameter.

### Return type

[**RestAuthDetail**](../models/RestAuthDetail.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="authPasswordChangeCreate"></a>
# **authPasswordChangeCreate**
> RestAuthDetail authPasswordChangeCreate(old\_password, new\_password1, new\_password2)

Смена пароля

    Calls Django Auth SetPasswordForm save method.  Accepts the following POST parameters: new_password1, new_password2 Returns the success/fail message.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old\_password** | **String**|  | [default to null]
 **new\_password1** | **String**|  | [default to null]
 **new\_password2** | **String**|  | [default to null]

### Return type

[**RestAuthDetail**](../models/RestAuthDetail.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
- **Accept**: application/json

<a name="authPasswordResetConfirmCreate"></a>
# **authPasswordResetConfirmCreate**
> RestAuthDetail authPasswordResetConfirmCreate(new\_password1, new\_password2, uid, token)

Подтверждение сброса пароля

    Password reset e-mail link is confirmed, therefore this resets the user&#39;s password.  Accepts the following POST parameters: token, uid,     new_password1, new_password2 Returns the success/fail message.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new\_password1** | **String**|  | [default to null]
 **new\_password2** | **String**|  | [default to null]
 **uid** | **String**|  | [default to null]
 **token** | **String**|  | [default to null]

### Return type

[**RestAuthDetail**](../models/RestAuthDetail.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
- **Accept**: application/json

<a name="authPasswordResetCreate"></a>
# **authPasswordResetCreate**
> RestAuthDetail authPasswordResetCreate(email)

Запрос на сброс пароля

    Calls Django Auth PasswordResetForm save method.  Accepts the following POST parameters: email Returns the success/fail message.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **String**|  | [default to null]

### Return type

[**RestAuthDetail**](../models/RestAuthDetail.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
- **Accept**: application/json

<a name="authRegistrationCreate"></a>
# **authRegistrationCreate**
> JWT authRegistrationCreate(username, email, password1, password2)

Регистрация пользователя

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**|  | [default to null]
 **email** | **String**|  | [default to null]
 **password1** | **String**|  | [default to null]
 **password2** | **String**|  | [default to null]

### Return type

[**JWT**](../models/JWT.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
- **Accept**: application/json

<a name="authRegistrationResendEmailCreate"></a>
# **authRegistrationResendEmailCreate**
> RestAuthDetail authRegistrationResendEmailCreate(email)

Повторная отправка e-mail

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **String**|  | [default to null]

### Return type

[**RestAuthDetail**](../models/RestAuthDetail.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
- **Accept**: application/json

<a name="authRegistrationVerifyEmailCreate"></a>
# **authRegistrationVerifyEmailCreate**
> RestAuthDetail authRegistrationVerifyEmailCreate(key)

Подтверждение e-mail

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**|  | [default to null]

### Return type

[**RestAuthDetail**](../models/RestAuthDetail.md)

### Authorization

[jwtAuth](../index.md#jwtAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
- **Accept**: application/json

<a name="authTokenRefreshCreate"></a>
# **authTokenRefreshCreate**
> TokenRefresh authTokenRefreshCreate(refresh)

Обновить JWT токен

    Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **String**|  | [default to null]

### Return type

[**TokenRefresh**](../models/TokenRefresh.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
- **Accept**: application/json

<a name="authTokenVerifyCreate"></a>
# **authTokenVerifyCreate**
> authTokenVerifyCreate(token)

Валидировать JWT токен

    Takes a token and indicates if it is valid.  This view provides no information about a token&#39;s fitness for a particular use.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **String**|  | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
- **Accept**: Not defined

