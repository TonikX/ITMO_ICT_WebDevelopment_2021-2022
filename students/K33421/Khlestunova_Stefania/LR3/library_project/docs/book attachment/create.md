# Create BookAttachment

Создает объект-связь между читателям и взятыми им книгами.

**URL** : `/library/book_attachment/create/`

**Allow** : `POST, OPTIONS`

**HTTP 201 CREATED**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 4,
    "attach_date": "2022-01-22T21:23:00Z",
    "book": 4,
    "reader": 3
}
```