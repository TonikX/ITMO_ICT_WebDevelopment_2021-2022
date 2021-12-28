# list Single hotel API

This API is meant to perform list operation with hotels.

**URL** : `/api/hotels/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "name": "Marina Bay Sand",
        "address": "singapore",
        "description": "marina bay sand is a good hotel",
        "owner": 4
    },
    {
        "id": 2,
        "name": "Marriot",
        "address": "Ha noi vietnam",
        "description": "marriot is the old hotel",
        "owner": 5
    }
]
```