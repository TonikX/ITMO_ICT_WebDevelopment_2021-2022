# Sign Up

Интерфейс для регистрации в системе.

Используемые методы: POST

Реализация методов:

1). регистрация
```
async signUp () {
  if (this.signUpForm.role === 'admin') {
    this.signUpForm.role = 'ad'
  } else if (this.signUpForm.role === 'manager') {
    this.signUpForm.role = 'ma'
  } else if (this.signUpForm.role === 'accountant') {
    this.signUpForm.role = 'ac'
  }
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)

    if (response.status !== 201) {
      throw new Error(response.status)
    }
    this.$refs.signUpForm.reset()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
}
```