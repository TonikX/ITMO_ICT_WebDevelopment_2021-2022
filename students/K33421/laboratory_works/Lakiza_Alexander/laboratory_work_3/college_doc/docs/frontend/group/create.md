# Group Create 

Создать группу

**URL** : `/group/create/`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
async add () {
      await this.axios
        .post('http://127.0.0.1:8000/group/create/', this.addForm)
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
