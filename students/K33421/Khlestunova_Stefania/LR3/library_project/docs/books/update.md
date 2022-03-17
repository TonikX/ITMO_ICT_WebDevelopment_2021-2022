# Update Book

Просмотр/изменение/удаление данных о книге.

**URL** : `/library/book/<int:pk>/update/`

**Allow** : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 1,
    "name": "Абра Кадабра",
    "authors": "Константин Филипок",
    "publisher": "ООО Русский стандарт",
    "pub_year": "2000-01-15",
    "section": "А56",
    "instance_count": 300,
    "bk_cipher": "3728120339"
}
```