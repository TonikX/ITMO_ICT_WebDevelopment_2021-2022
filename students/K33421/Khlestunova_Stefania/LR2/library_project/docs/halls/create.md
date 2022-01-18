# Create Hall

Создает объект-зал в таблице залов.

**URL** : `/library/halls/create/`

**Allow** : `POST, OPTIONS`

**HTTP 201 CREATED**

**Content-type** : `application/json`

**Vary** : `Accept`

```json
{
    "id": 3,
    "hall_num": 3,
    "hall_name": "МакроКниги",
    "capacity": 500
}
```