# Пользователь

## Регистрация

Регистрация нового пользователя.

**URL** : `/auth/users/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Request body** : 
```json
{
   "username": "gleb",
   "password": "12345678",
   "email": "gleb@gmail.com",
   "towns": [1, 2]
}
```

**Success Response**

**Code** : `200 OK`

```json
{
    "email": "gleb@gmail.com",
    "username": "gleb",
    "id": 1
}
```


## Аунтентификация

Аунтентификация пользователя и получение токена.

**URL** : `/auth/token/login/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Request body** : 
```json
{
   "username": "gleb",
   "password": "12345678"
}
```

**Success Response**

**Code** : `200 OK`

```json
{
    "auth_token": "090120266a287b7938e8b6b8fe9e8f58334a96cf"
}
```

**Failure**

**Code** : `400 Bad request`

```json
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```

## Выход

Завершение сеанса пользователя и удаление токена.

**URL** : `/auth/token/logout/`

**Method** : `POST`

**Auth required** : YES

**Headers** : 
    Authorization: Token <your_token>

**Request body** : empty

**Success Response**

**Code** : `204 No Content`

```json
{
    "auth_token": "090120266a287b7938e8b6b8fe9e8f58334a96cf"
}
```

**Failure**

**Code** : `401 Bad request`

**Body response** :
```json
{
    "detail": "Invalid token."
}
```


## Профиль пользователя

Получение информации о текущем пользователе.

**URL** : `/auth/users/me/`

**Method** : `GET`

**Auth required** : YES

**Headers** : 
    Authorization: Token <your_token>

**Request body** : empty

**Success Response**

**Code** : `200 OK`

```json
{
    "id": 1,
    "email": "gleb@gmail.com",
    "username": "gleb"
}
```

**Failure**

**Code** : `401 Unauthorized`

**Body response** :
```json
{
    "detail": "Authentication credentials were not provided."
}
```

## Информация о пользователях

Получение информации о каком-либо пользователе.

**URL** : `/user/<user_id>/`

**Method** : `GET`

**Auth required** : YES

**Headers** : 
    Authorization: Token <your_token>

**Request body** : empty

**Success Response**

**Code** : `200 OK`

```json
{
    "id": 1,
    "last_login": "2022-03-09T05:33:17.878439Z",
    "is_superuser": false,
    "username": "gleb",
    "first_name": "",
    "last_name": "",
    "email": "gleb@gmail.com",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2022-03-09T05:20:02.613644Z",
    "days_count": 3,
    "groups": [],
    "user_permissions": [],
    "towns": []
}
```

**Failure**

**Code** : `401 Unauthorized`

**Body response** :
```json
{
    "detail": "Authentication credentials were not provided."
}
```


