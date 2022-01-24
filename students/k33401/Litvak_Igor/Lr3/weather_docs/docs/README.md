# Documentation for Weather API documentation

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost:8000/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**authJwtCreateCreate**](Apis/AuthApi.md#authjwtcreatecreate) | **POST** /auth/jwt/create/ | Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
*AuthApi* | [**authJwtRefreshCreate**](Apis/AuthApi.md#authjwtrefreshcreate) | **POST** /auth/jwt/refresh/ | Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
*AuthApi* | [**authJwtVerifyCreate**](Apis/AuthApi.md#authjwtverifycreate) | **POST** /auth/jwt/verify/ | Takes a token and indicates if it is valid.  This view provides no information about a token's fitness for a particular use.
*AuthApi* | [**authUsersActivation**](Apis/AuthApi.md#authusersactivation) | **POST** /auth/users/activation/ | 
*AuthApi* | [**authUsersCreate**](Apis/AuthApi.md#authuserscreate) | **POST** /auth/users/ | 
*AuthApi* | [**authUsersDelete**](Apis/AuthApi.md#authusersdelete) | **DELETE** /auth/users/{id}/ | 
*AuthApi* | [**authUsersList**](Apis/AuthApi.md#authuserslist) | **GET** /auth/users/ | 
*AuthApi* | [**authUsersMeDelete**](Apis/AuthApi.md#authusersmedelete) | **DELETE** /auth/users/me/ | 
*AuthApi* | [**authUsersMePartialUpdate**](Apis/AuthApi.md#authusersmepartialupdate) | **PATCH** /auth/users/me/ | 
*AuthApi* | [**authUsersMeRead**](Apis/AuthApi.md#authusersmeread) | **GET** /auth/users/me/ | 
*AuthApi* | [**authUsersMeUpdate**](Apis/AuthApi.md#authusersmeupdate) | **PUT** /auth/users/me/ | 
*AuthApi* | [**authUsersPartialUpdate**](Apis/AuthApi.md#authuserspartialupdate) | **PATCH** /auth/users/{id}/ | 
*AuthApi* | [**authUsersRead**](Apis/AuthApi.md#authusersread) | **GET** /auth/users/{id}/ | 
*AuthApi* | [**authUsersResendActivation**](Apis/AuthApi.md#authusersresendactivation) | **POST** /auth/users/resend_activation/ | 
*AuthApi* | [**authUsersResetPassword**](Apis/AuthApi.md#authusersresetpassword) | **POST** /auth/users/reset_password/ | 
*AuthApi* | [**authUsersResetPasswordConfirm**](Apis/AuthApi.md#authusersresetpasswordconfirm) | **POST** /auth/users/reset_password_confirm/ | 
*AuthApi* | [**authUsersResetUsername**](Apis/AuthApi.md#authusersresetusername) | **POST** /auth/users/reset_username/ | 
*AuthApi* | [**authUsersResetUsernameConfirm**](Apis/AuthApi.md#authusersresetusernameconfirm) | **POST** /auth/users/reset_username_confirm/ | 
*AuthApi* | [**authUsersSetPassword**](Apis/AuthApi.md#authuserssetpassword) | **POST** /auth/users/set_password/ | 
*AuthApi* | [**authUsersSetUsername**](Apis/AuthApi.md#authuserssetusername) | **POST** /auth/users/set_username/ | 
*AuthApi* | [**authUsersUpdate**](Apis/AuthApi.md#authusersupdate) | **PUT** /auth/users/{id}/ | 
*CitiesApi* | [**citiesClosest**](Apis/CitiesApi.md#citiesclosest) | **GET** /cities/closest/ | Returns city closest to certain coordinates
*CitiesApi* | [**citiesFavouriteCreate**](Apis/CitiesApi.md#citiesfavouritecreate) | **POST** /cities/favourite/ | Viewset for favourite cities
*CitiesApi* | [**citiesFavouriteDelete**](Apis/CitiesApi.md#citiesfavouritedelete) | **DELETE** /cities/favourite/{id}/ | Viewset for favourite cities
*CitiesApi* | [**citiesFavouriteList**](Apis/CitiesApi.md#citiesfavouritelist) | **GET** /cities/favourite/ | Viewset for favourite cities
*CitiesApi* | [**citiesFavouritePartialUpdate**](Apis/CitiesApi.md#citiesfavouritepartialupdate) | **PATCH** /cities/favourite/{id}/ | Viewset for favourite cities
*CitiesApi* | [**citiesFavouriteRead**](Apis/CitiesApi.md#citiesfavouriteread) | **GET** /cities/favourite/{id}/ | Viewset for favourite cities
*CitiesApi* | [**citiesFavouriteUpdate**](Apis/CitiesApi.md#citiesfavouriteupdate) | **PUT** /cities/favourite/{id}/ | Viewset for favourite cities
*CitiesApi* | [**citiesForecast**](Apis/CitiesApi.md#citiesforecast) | **GET** /cities/{id}/forecast/ | Cached wrapper around OpenWeatherMap API
*CitiesApi* | [**citiesList**](Apis/CitiesApi.md#citieslist) | **GET** /cities/ | Viewset for cities
*CitiesApi* | [**citiesRead**](Apis/CitiesApi.md#citiesread) | **GET** /cities/{id}/ | Viewset for cities


<a name="documentation-for-models"></a>
## Documentation for Models

 - [Activation](./Models/Activation.md)
 - [City](./Models/City.md)
 - [CustomUserCreate](./Models/CustomUserCreate.md)
 - [FavouriteCity](./Models/FavouriteCity.md)
 - [PasswordResetConfirm](./Models/PasswordResetConfirm.md)
 - [SendEmailReset](./Models/SendEmailReset.md)
 - [SetPassword](./Models/SetPassword.md)
 - [SetUsername](./Models/SetUsername.md)
 - [TokenObtainPair](./Models/TokenObtainPair.md)
 - [TokenRefresh](./Models/TokenRefresh.md)
 - [TokenVerify](./Models/TokenVerify.md)
 - [User](./Models/User.md)
 - [UsernameResetConfirm](./Models/UsernameResetConfirm.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="Basic"></a>
### Basic

- **Type**: HTTP basic authentication

