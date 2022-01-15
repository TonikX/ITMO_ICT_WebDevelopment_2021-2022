# Teacher Create 

Создать преподавателя и его предметы

**URL** : `/teacher/create/`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/teacher/create/', this.addForm)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
      await this.axios
        .get('http://127.0.0.1:8000/teacher/list/')
        .then((res) => {
          this.teacher_id = res.data[res.data.length - 1].id
        })
        .catch((error) => {
          console.log(error)
        })
      for (const sub of this.addSub.subject) {
        await this.axios
          .post('http://127.0.0.1:8000/subteach/create/', {
            teacher: this.teacher_id,
            subject: sub
          })
          .then((res) => {
            console.log(res)
            this.$refs.reset()
          })
          .catch((error) => {
            console.log(error)
          })
      }
    }
}
```
