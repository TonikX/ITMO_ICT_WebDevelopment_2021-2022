### Student List

Просмотреть данные о студенте

**URL** : `/student/list/`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/student/list/')
      .then((res) => {
        console.log('this.students', this.students)
        this.marks = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```
