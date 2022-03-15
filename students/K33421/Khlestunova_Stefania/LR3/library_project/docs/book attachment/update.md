# Update BookAttachment

Просмотр/изменение/удаление информации о записи о заимствовании книги.

**URL** : `/library/book_attachment/<int:pk>/update/`

**Allow** : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 1,
    "attach_date": "2022-01-17T20:10:52Z",
    "book": 1,
    "reader": 1
}
```