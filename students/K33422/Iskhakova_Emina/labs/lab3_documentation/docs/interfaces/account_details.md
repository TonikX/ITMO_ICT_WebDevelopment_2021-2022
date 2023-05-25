# Account Details

Интерфейс для просмотра и изменения данных учетной записи пользователя.

Используемые методы: GET, PATCH

Реализация методов:

1). получение данных об учетной записи пользователя;
```
async GetAccountDetails () {
  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/auth/users/me/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.AccountDetails = response.data
    this.EditedItem = response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
2). изменение дополнительных полей.
```
async ChangeAccountDetails () {
  try {
    const response = await this.axios
      .patch('http://127.0.0.1:8000/auth/users/me/', JSON.stringify(this.EditedItem), { headers: { Authorization: 'Token ' + localStorage.getItem('token'), 'Content-Type': 'application/json' } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```