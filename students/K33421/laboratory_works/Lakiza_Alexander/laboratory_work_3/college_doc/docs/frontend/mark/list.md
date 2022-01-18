### Mark List

Просмотреть данные об оценке студента 

**URL** : `/mark/list/`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/mark/list/')
      .then((res) => {
        console.log('this.marks', this.marks)
        this.marks = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```
