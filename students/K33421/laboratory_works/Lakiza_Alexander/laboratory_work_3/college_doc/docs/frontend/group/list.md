### Group List

Просмотреть данные о группах

**URL** : `/group/list/`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/group/list/')
      .then((res) => {
        console.log('this.groups', this.groups)
        this.groups = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```
