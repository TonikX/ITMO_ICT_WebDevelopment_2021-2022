# Documentation for SuperWeather API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost:8888*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**authTokenLoginCreate**](Apis/AuthApi.md#authtokenlogincreate) | **POST** /auth/token/login/ | Use this endpoint to obtain user authentication token.
*AuthApi* | [**authTokenLogoutCreate**](Apis/AuthApi.md#authtokenlogoutcreate) | **POST** /auth/token/logout/ | Use this endpoint to logout user (remove user authentication token).
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
*CityApi* | [**cityCreate**](Apis/CityApi.md#citycreate) | **POST** /city | 
*CityApi* | [**cityDailyList**](Apis/CityApi.md#citydailylist) | **GET** /city/{id}/daily | 
*CityApi* | [**cityDelete**](Apis/CityApi.md#citydelete) | **DELETE** /city/{id} | 
*CityApi* | [**cityForecastList**](Apis/CityApi.md#cityforecastlist) | **GET** /city/{id}/forecast | 
*CityApi* | [**cityList**](Apis/CityApi.md#citylist) | **GET** /city | 
*CityApi* | [**cityPartialUpdate**](Apis/CityApi.md#citypartialupdate) | **PATCH** /city/{id} | 
*CityApi* | [**cityRead**](Apis/CityApi.md#cityread) | **GET** /city/{id} | 
*CityApi* | [**cityUpdate**](Apis/CityApi.md#cityupdate) | **PUT** /city/{id} | 
*FavoritesApi* | [**favoritesCreate**](Apis/FavoritesApi.md#favoritescreate) | **POST** /favorites | 
*FavoritesApi* | [**favoritesDelete**](Apis/FavoritesApi.md#favoritesdelete) | **DELETE** /favorites/{id} | 
*FavoritesApi* | [**favoritesList**](Apis/FavoritesApi.md#favoriteslist) | **GET** /favorites | 
*FavoritesApi* | [**favoritesPartialUpdate**](Apis/FavoritesApi.md#favoritespartialupdate) | **PATCH** /favorites/{id} | 
*FavoritesApi* | [**favoritesRead**](Apis/FavoritesApi.md#favoritesread) | **GET** /favorites/{id} | 
*FavoritesApi* | [**favoritesUpdate**](Apis/FavoritesApi.md#favoritesupdate) | **PUT** /favorites/{id} | 
*ForecastApi* | [**forecastDelete**](Apis/ForecastApi.md#forecastdelete) | **DELETE** /forecast/{id} | 
*ForecastApi* | [**forecastList**](Apis/ForecastApi.md#forecastlist) | **GET** /forecast | 
*ForecastApi* | [**forecastRead**](Apis/ForecastApi.md#forecastread) | **GET** /forecast/{id} | 


<a name="documentation-for-models"></a>
## Documentation for Models

 - [Activation](./Models/Activation.md)
 - [City](./Models/City.md)
 - [CityDaily](./Models/CityDaily.md)
 - [FavoriteCity](./Models/FavoriteCity.md)
 - [Forecast](./Models/Forecast.md)
 - [PasswordResetConfirm](./Models/PasswordResetConfirm.md)
 - [SendEmailReset](./Models/SendEmailReset.md)
 - [SetPassword](./Models/SetPassword.md)
 - [SetUsername](./Models/SetUsername.md)
 - [TokenCreate](./Models/TokenCreate.md)
 - [User](./Models/User.md)
 - [UserCreate](./Models/UserCreate.md)
 - [UsernameResetConfirm](./Models/UsernameResetConfirm.md)
 - [WeatherCurrent](./Models/WeatherCurrent.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="Basic"></a>
### Basic

- **Type**: HTTP basic authentication

