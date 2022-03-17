# List of all users

Shows information about all users

**URL** : `/users/list/`

**Method** : `GET`


## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "username": "admin",
        "first_name": null,
        "last_name": null,
        "passport": null,
        "salary": 0,
        "cage": []
    },
    {
        "username": "nika1",
        "first_name": "Veronika",
        "last_name": "Novikova",
        "passport": "123445",
        "salary": 20000,
        "cage": [
            1,
            2
        ]
    }
]
```