Выводит информацию обо всех восхождениях

**URL** : `/trip`

**HTTP 200 OK**

**Allow:** `GET, HEAD, OPTIONS`

**Content-Type:** `application/json`

**Vary:** `Accept`


```json
 {
        "id": 1,
        "start_time": "2021-06-24T08:10:00Z",
        "finish_time": "2021-06-26T12:00:00Z",
        "peak": 1,
        "participants": [
            1,
            2
        ],
        "information": ""
    },
    {
        "id": 2,
        "start_time": "2022-01-08T16:30:48Z",
        "finish_time": "2022-01-11T16:30:55Z",
        "peak": 2,
        "participants": [
            2,
            4,
            3
        ],
        "information": ""
    },
    {
        "id": 3,
        "start_time": "2022-02-24T12:00:00Z",
        "finish_time": "2022-02-28T17:00:00Z",
        "peak": 2,
        "participants": [],
        "information": "It's going to be amazing."
    }
```