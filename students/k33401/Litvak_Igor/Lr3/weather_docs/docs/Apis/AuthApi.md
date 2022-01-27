# AuthApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authJwtCreateCreate**](AuthApi.md#authJwtCreateCreate) | **POST** /auth/jwt/create/ | 
[**authJwtRefreshCreate**](AuthApi.md#authJwtRefreshCreate) | **POST** /auth/jwt/refresh/ | 
[**authJwtVerifyCreate**](AuthApi.md#authJwtVerifyCreate) | **POST** /auth/jwt/verify/ | 
[**authUsersActivation**](AuthApi.md#authUsersActivation) | **POST** /auth/users/activation/ | 
[**authUsersCreate**](AuthApi.md#authUsersCreate) | **POST** /auth/users/ | 
[**authUsersDelete**](AuthApi.md#authUsersDelete) | **DELETE** /auth/users/{id}/ | 
[**authUsersList**](AuthApi.md#authUsersList) | **GET** /auth/users/ | 
[**authUsersMeDelete**](AuthApi.md#authUsersMeDelete) | **DELETE** /auth/users/me/ | 
[**authUsersMePartialUpdate**](AuthApi.md#authUsersMePartialUpdate) | **PATCH** /auth/users/me/ | 
[**authUsersMeRead**](AuthApi.md#authUsersMeRead) | **GET** /auth/users/me/ | 
[**authUsersMeUpdate**](AuthApi.md#authUsersMeUpdate) | **PUT** /auth/users/me/ | 
[**authUsersPartialUpdate**](AuthApi.md#authUsersPartialUpdate) | **PATCH** /auth/users/{id}/ | 
[**authUsersRead**](AuthApi.md#authUsersRead) | **GET** /auth/users/{id}/ | 
[**authUsersResendActivation**](AuthApi.md#authUsersResendActivation) | **POST** /auth/users/resend_activation/ | 
[**authUsersResetPassword**](AuthApi.md#authUsersResetPassword) | **POST** /auth/users/reset_password/ | 
[**authUsersResetPasswordConfirm**](AuthApi.md#authUsersResetPasswordConfirm) | **POST** /auth/users/reset_password_confirm/ | 
[**authUsersResetUsername**](AuthApi.md#authUsersResetUsername) | **POST** /auth/users/reset_username/ | 
[**authUsersResetUsernameConfirm**](AuthApi.md#authUsersResetUsernameConfirm) | **POST** /auth/users/reset_username_confirm/ | 
[**authUsersSetPassword**](AuthApi.md#authUsersSetPassword) | **POST** /auth/users/set_password/ | 
[**authUsersSetUsername**](AuthApi.md#authUsersSetUsername) | **POST** /auth/users/set_username/ | 
[**authUsersUpdate**](AuthApi.md#authUsersUpdate) | **PUT** /auth/users/{id}/ | 


<a name="authJwtCreateCreate"></a>
# **authJwtCreateCreate**
> TokenObtainPair authJwtCreateCreate(data)



    Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenObtainPair**](../Models/TokenObtainPair.md)|  |

### Return type

[**TokenObtainPair**](../Models/TokenObtainPair.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authJwtRefreshCreate"></a>
# **authJwtRefreshCreate**
> TokenRefresh authJwtRefreshCreate(data)



    Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenRefresh**](../Models/TokenRefresh.md)|  |

### Return type

[**TokenRefresh**](../Models/TokenRefresh.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authJwtVerifyCreate"></a>
# **authJwtVerifyCreate**
> TokenVerify authJwtVerifyCreate(data)



    Takes a token and indicates if it is valid.  This view provides no information about a token&#39;s fitness for a particular use.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenVerify**](../Models/TokenVerify.md)|  |

### Return type

[**TokenVerify**](../Models/TokenVerify.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersActivation"></a>
# **authUsersActivation**
> Activation authUsersActivation(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Activation**](../Models/Activation.md)|  |

### Return type

[**Activation**](../Models/Activation.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersCreate"></a>
# **authUsersCreate**
> CustomUserCreate authUsersCreate(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CustomUserCreate**](../Models/CustomUserCreate.md)|  |

### Return type

[**CustomUserCreate**](../Models/CustomUserCreate.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersDelete"></a>
# **authUsersDelete**
> authUsersDelete(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this user. | [default to null]

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="authUsersList"></a>
# **authUsersList**
> List authUsersList()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/User.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="authUsersMeDelete"></a>
# **authUsersMeDelete**
> authUsersMeDelete()



### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="authUsersMePartialUpdate"></a>
# **authUsersMePartialUpdate**
> User authUsersMePartialUpdate(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**User**](../Models/User.md)|  |

### Return type

[**User**](../Models/User.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersMeRead"></a>
# **authUsersMeRead**
> List authUsersMeRead()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/User.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="authUsersMeUpdate"></a>
# **authUsersMeUpdate**
> User authUsersMeUpdate(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**User**](../Models/User.md)|  |

### Return type

[**User**](../Models/User.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersPartialUpdate"></a>
# **authUsersPartialUpdate**
> User authUsersPartialUpdate(id, data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this user. | [default to null]
 **data** | [**User**](../Models/User.md)|  |

### Return type

[**User**](../Models/User.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersRead"></a>
# **authUsersRead**
> User authUsersRead(id)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this user. | [default to null]

### Return type

[**User**](../Models/User.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="authUsersResendActivation"></a>
# **authUsersResendActivation**
> SendEmailReset authUsersResendActivation(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SendEmailReset**](../Models/SendEmailReset.md)|  |

### Return type

[**SendEmailReset**](../Models/SendEmailReset.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersResetPassword"></a>
# **authUsersResetPassword**
> SendEmailReset authUsersResetPassword(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SendEmailReset**](../Models/SendEmailReset.md)|  |

### Return type

[**SendEmailReset**](../Models/SendEmailReset.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersResetPasswordConfirm"></a>
# **authUsersResetPasswordConfirm**
> PasswordResetConfirm authUsersResetPasswordConfirm(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PasswordResetConfirm**](../Models/PasswordResetConfirm.md)|  |

### Return type

[**PasswordResetConfirm**](../Models/PasswordResetConfirm.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersResetUsername"></a>
# **authUsersResetUsername**
> SendEmailReset authUsersResetUsername(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SendEmailReset**](../Models/SendEmailReset.md)|  |

### Return type

[**SendEmailReset**](../Models/SendEmailReset.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersResetUsernameConfirm"></a>
# **authUsersResetUsernameConfirm**
> UsernameResetConfirm authUsersResetUsernameConfirm(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UsernameResetConfirm**](../Models/UsernameResetConfirm.md)|  |

### Return type

[**UsernameResetConfirm**](../Models/UsernameResetConfirm.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersSetPassword"></a>
# **authUsersSetPassword**
> SetPassword authUsersSetPassword(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SetPassword**](../Models/SetPassword.md)|  |

### Return type

[**SetPassword**](../Models/SetPassword.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersSetUsername"></a>
# **authUsersSetUsername**
> SetUsername authUsersSetUsername(data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SetUsername**](../Models/SetUsername.md)|  |

### Return type

[**SetUsername**](../Models/SetUsername.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="authUsersUpdate"></a>
# **authUsersUpdate**
> User authUsersUpdate(id, data)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| A unique integer value identifying this user. | [default to null]
 **data** | [**User**](../Models/User.md)|  |

### Return type

[**User**](../Models/User.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

