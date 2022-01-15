### Pair List

Просмотреть данные о парах

**URL** : `/pair/list/`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/pair/list/')
      .then((res) => {
        this.pairs = res.data
      })
      .catch((error) => {
        console.log(error)
      })
```
