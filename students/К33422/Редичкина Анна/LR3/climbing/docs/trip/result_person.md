После завершения восхождения фиксируется
информация об успешности восхождения для определенного
альпиниста.

**URL** : `trip/<int:pk>/result_for_person`

**HTTP 201 Created**

**Allow:** `POST, OPTIONS`

**Content-Type:** `application/json`

**Vary:** `Accept`


```json
{
    "climbing": 1,
    "person": 1,
    "description": "Good"
}
```