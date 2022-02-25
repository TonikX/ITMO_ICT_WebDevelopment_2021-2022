# Documentation for CheckSplitter API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**authLoginCreate**](apis/AuthApi.md#authlogincreate) | **POST** /api/auth/login/ | Авторизация пользователя
*AuthApi* | [**authLogoutCreate**](apis/AuthApi.md#authlogoutcreate) | **POST** /api/auth/logout/ | Выход
*AuthApi* | [**authPasswordChangeCreate**](apis/AuthApi.md#authpasswordchangecreate) | **POST** /api/auth/password/change/ | Смена пароля
*AuthApi* | [**authPasswordResetConfirmCreate**](apis/AuthApi.md#authpasswordresetconfirmcreate) | **POST** /api/auth/password/reset/confirm/ | Подтверждение сброса пароля
*AuthApi* | [**authPasswordResetCreate**](apis/AuthApi.md#authpasswordresetcreate) | **POST** /api/auth/password/reset/ | Запрос на сброс пароля
*AuthApi* | [**authRegistrationCreate**](apis/AuthApi.md#authregistrationcreate) | **POST** /api/auth/registration/ | Регистрация пользователя
*AuthApi* | [**authRegistrationResendEmailCreate**](apis/AuthApi.md#authregistrationresendemailcreate) | **POST** /api/auth/registration/resend-email/ | Повторная отправка e-mail
*AuthApi* | [**authRegistrationVerifyEmailCreate**](apis/AuthApi.md#authregistrationverifyemailcreate) | **POST** /api/auth/registration/verify-email/ | Подтверждение e-mail
*AuthApi* | [**authTokenRefreshCreate**](apis/AuthApi.md#authtokenrefreshcreate) | **POST** /api/auth/token/refresh/ | Обновить JWT токен
*AuthApi* | [**authTokenVerifyCreate**](apis/AuthApi.md#authtokenverifycreate) | **POST** /api/auth/token/verify/ | Валидировать JWT токен
*ChecksApi* | [**checksItemsUpdate**](apis/ChecksApi.md#checksitemsupdate) | **PUT** /api/checks/{id}/items | Установить взаиморасчет для чека
*ChecksApi* | [**checksList**](apis/ChecksApi.md#checkslist) | **GET** /api/checks | Получить список чеков
*ChecksApi* | [**checksRetrieve**](apis/ChecksApi.md#checksretrieve) | **GET** /api/checks/{id} | Получить чек по ID
*ChecksApi* | [**checksSyncCreate**](apis/ChecksApi.md#checkssynccreate) | **POST** /api/checks/sync | Синхронизировать чеки из ЧекСкан
*UsersApi* | [**usersProfileAvatarUpdate**](apis/UsersApi.md#usersprofileavatarupdate) | **PUT** /api/users/profile/avatar | Обновить аватар текущего пользователя
*UsersApi* | [**usersProfileDestroy**](apis/UsersApi.md#usersprofiledestroy) | **DELETE** /api/users/profile | Деактивировать аккаунт
*UsersApi* | [**usersProfilePartialUpdate**](apis/UsersApi.md#usersprofilepartialupdate) | **PATCH** /api/users/profile | Редактировать информацию о текущем пользователе
*UsersApi* | [**usersProfileRetrieve**](apis/UsersApi.md#usersprofileretrieve) | **GET** /api/users/profile | Получить информацию о текущем пользователе
*UsersApi* | [**usersProfileUpdate**](apis/UsersApi.md#usersprofileupdate) | **PUT** /api/users/profile | Редактировать информацию о текущем пользователе


<a name="documentation-for-models"></a>
## Documentation for Models

 - [Check](models/Check.md)
 - [CheckItem](models/CheckItem.md)
 - [CheckItemPartRequest](models/CheckItemPartRequest.md)
 - [JWT](models/JWT.md)
 - [LoginRequest](models/LoginRequest.md)
 - [PaginatedCheckList](models/PaginatedCheckList.md)
 - [PasswordChangeRequest](models/PasswordChangeRequest.md)
 - [PasswordResetConfirmRequest](models/PasswordResetConfirmRequest.md)
 - [PasswordResetRequest](models/PasswordResetRequest.md)
 - [PatchedProfileRequest](models/PatchedProfileRequest.md)
 - [Profile](models/Profile.md)
 - [ProfileAvatar](models/ProfileAvatar.md)
 - [ProfileRequest](models/ProfileRequest.md)
 - [RegisterRequest](models/RegisterRequest.md)
 - [ResendEmailVerificationRequest](models/ResendEmailVerificationRequest.md)
 - [RestAuthDetail](models/RestAuthDetail.md)
 - [TokenRefresh](models/TokenRefresh.md)
 - [TokenRefreshRequest](models/TokenRefreshRequest.md)
 - [TokenVerifyRequest](models/TokenVerifyRequest.md)
 - [UserDetails](models/UserDetails.md)
 - [VerifyEmailRequest](models/VerifyEmailRequest.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="jwtAuth"></a>
### jwtAuth

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A

