# Pair Create 

Создать пару

**URL** : `/pair/create/`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async create () {
      await this.axios
        .post('http://127.0.0.1:8000/pair/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/manager')
    }
```
