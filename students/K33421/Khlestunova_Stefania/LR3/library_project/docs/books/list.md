# Books List

Выводит список хранящихся в библиотеке книг.

**URL** : `/library/book/list/`

**Allow** : `GET, HEAD, OPTION`

**HTTP 200 OK**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
[
    {
        "id": 1,
        "name": "Абра Кадабра",
        "authors": "Константин Филипок",
        "publisher": "ООО Русский стандарт",
        "pub_year": "2000-01-15",
        "section": "А56",
        "instance_count": 300,
        "bk_cipher": "3728120339"
    },
    {
        "id": 2,
        "name": "Константин",
        "authors": "-",
        "publisher": "DC Comics",
        "pub_year": "2013-01-01",
        "section": "B32",
        "instance_count": 30,
        "bk_cipher": "1883827276"
    },
    {
        "id": 3,
        "name": "451 градус по Фаренгейту",
        "authors": "Рей Брэдбери",
        "publisher": "Домино, Эксмо",
        "pub_year": "2013-01-01",
        "section": "B32",
        "instance_count": 9,
        "bk_cipher": "1883827276"
    },
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
]
```