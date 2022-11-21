# User account

# Register

Create new account

**URL** : `/auth/users/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Request body (example)** : 
```json
{
   "username": "kust2",
   "password": "k12345678",
   "email": "kust2@gmail.com",
   "towns": [1, 3]
}
```

### Success Response

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "email": "kust2@gmail.com",
    "username": "kust2",
    "id": 89
}
```


# Token

Create new token and login

**URL** : `/auth/token/login/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Request body (example)** : 
```json
{
   "username": "kust2",
   "password": "k12345678"
}
```

### Success Response

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "auth_token": "090120266a287b7938e8b6b8fe9e8f58334a96cf"
}
```

### Failure

Check your input data. It must be in correct format.

**Code** : `400 Bad request`

**Content** : `{[]}`

```json
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```

# Logout

Force disable and delete given token

**URL** : `/auth/token/logout/`

**Method** : `POST`

**Auth required** : YES

**Headers** : 
    Authorization: Token <your_token>

**Request body** : empty

### Success Response

**Code** : `204 No Content`

```json
{
    "auth_token": "090120266a287b7938e8b6b8fe9e8f58334a96cf"
}
```

### Failure

Token is already invalid

**Code** : `401 Bad request`

**Body response** :
```json
{
    "detail": "Invalid token."
}
```


# Get current user info

Get current user info

**URL** : `/auth/users/me/`

**Method** : `POST`

**Auth required** : YES

**Headers** : 
    Authorization: Token <your_token>

**Request body** : empty

### Success Response

**Code** : `200 OK`

```json
{
    "email": "kust2@gmail.com",
    "id": 5,
    "username": "kust2"
}
```

### Failure

**Code** : `401 Unauthorized`

**Body response** :
```json
{
    "detail": "Authentication credentials were not provided."
}
```

# Get any user info

Get any user info

**URL** : `/user/<user_id>/`

**Method** : `POST`

**Auth required** : YES

**Headers** : 
    Authorization: Token <your_token>

**Request body** : empty

### Success Response

**Code** : `200 OK`

```json
{
    "id": 6,
    "last_login": "2022-03-09T05:33:17.878439Z",
    "is_superuser": false,
    "username": "kust3",
    "first_name": "",
    "last_name": "",
    "email": "kust3@gmail.com",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2022-03-09T05:20:02.613644Z",
    "days_count": 3,
    "groups": [],
    "user_permissions": [],
    "towns": []
}
```

### Failure

**Code** : `401 Unauthorized`

**Body response** :
```json
{
    "detail": "Authentication credentials were not provided."
}
```


