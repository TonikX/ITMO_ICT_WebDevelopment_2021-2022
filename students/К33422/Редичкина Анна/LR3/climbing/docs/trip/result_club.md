После завершения восхождения фиксируется
информация об успешности восхождения для группы в целом.

**URL** : `trip/<int:pk>/result_for_club`

**HTTP 201 Created**

**Allow:** `POST, OPTIONS`

**Content-Type:** `application/json`

**Vary:** `Accept`


```json
{
    "climbing": 1,
    "club": 2,
    "description": "Amazing"
}
```