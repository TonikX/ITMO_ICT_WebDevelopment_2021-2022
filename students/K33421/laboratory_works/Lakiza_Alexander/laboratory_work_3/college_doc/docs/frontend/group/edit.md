# Group Edit 

Удалить / изменить группу

**URL** : `/group/:teacher_id/`

**Methods** : `PUT / DELETE`

## Success Responses

**Code** : `200 OK / 204 No Content`

**Content** : `{}`

```javascript
async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/group/${this.gr_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.push('/group')
        })
        .catch((error) => {
          console.log(error)
        })
    }
```
