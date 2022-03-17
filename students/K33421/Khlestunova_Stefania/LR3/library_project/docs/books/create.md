# Create Book

Создает объект-книгу в таблице книги.

**URL** : `/library/book/create/`

**Allow** : `POST, OPTIONS`

**HTTP 201 CREATED**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 4,
    "name": "Jugabuga",
    "authors": "Братья Авторы, Сестры Авторы",
    "publisher": "Картошка",
    "pub_year": "1982-02-01",
    "section": "S21",
    "instance_count": 100,
    "bk_cipher": "1029323812"
}
```