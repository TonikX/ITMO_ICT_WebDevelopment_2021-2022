### Subject List

Просмотреть данные о предмете 

**URL** : `/subject/list/`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/subject/list/')
      .then((res) => {
        console.log('this.subjects', this.subjects)
        this.subjects = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```
