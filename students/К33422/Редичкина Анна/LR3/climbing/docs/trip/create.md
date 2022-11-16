Создает запись о новом восхождении

**URL** : `/trip/create`

**HTTP 201 Created**

**Allow:** `POST, OPTIONS`

**Content-Type:** `application/json`

**Vary:** `Accept`


```json
{
    "id": 3,
    "start_time": "2022-02-24T12:00:00Z",
    "finish_time": "2022-02-28T17:00:00Z",
    "peak": 2,
    "participants": [],
    "information": "It's going to be amazing."
}
```