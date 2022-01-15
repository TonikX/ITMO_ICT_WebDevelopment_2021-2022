# User Sign Up 

Зарегистрировать нового пользователя

**URL** : `/auth/users/`

**Methods** : `POST`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```javascript
    async signUp () {
      await this.axios
        .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
        .then((res) => {
          console.log(res)
          window.location.href = 'http://localhost:8080/signin'
        })
        .catch((error) => {
          console.log(error)
        })
    }
}
```
