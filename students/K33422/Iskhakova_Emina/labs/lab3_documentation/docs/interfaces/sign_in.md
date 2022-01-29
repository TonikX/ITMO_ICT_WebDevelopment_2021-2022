# Sign In

Интерфейс для авторизации в системе.

Используемые методы: POST

Реализация методов:

1). авторизация
```
async signIn () {
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/auth/token/login/', this.signInForm)

    console.log('SIGN IN RESPONSE', response)

    // if (response.status !== 200) {
    //   throw new Error(response.status)
    // }

    this.$refs.signInForm.reset()

    localStorage.setItem('token', response.data.auth_token)
    
    window.location = '/'
  } catch (e) {
    console.error('AN API ERROR', e)
  }
}
```