# Create ReadersAttachment

Создает объект-связь между читателем и залом.

**URL** : `/library/readers_attachment/create/`

**Allow** : `POST, OPTIONS`

**HTTP 201 CREATED**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 3,
    "attach_date": "2022-02-21T21:23:00Z",
    "reader": 2,
    "hall": 2
}
```