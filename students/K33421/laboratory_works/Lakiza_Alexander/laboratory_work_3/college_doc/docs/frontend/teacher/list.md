### Teacher List

Просмотреть данные о преподавателе и его предметах

**URL** : `/teacher/list/`

**Methods** : `GET`

## Success Responses

**Code** : `200 OK`

**Content** : `[{}]`

```javascript
    await this.axios
      .get('http://127.0.0.1:8000/teacher/list/')
      .then((res) => {
        console.log('this.teachers', this.teachers)
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
}
```
