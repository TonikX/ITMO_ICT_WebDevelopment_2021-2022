# Client

Интерфейс для просмотра, добавления, изменения, удаление записей из таблицы "Клиент".

Используемые методы: GET, POST, PUT, DELETE

Реализация методов:

1). получение данных о клиентах;
```
async GetClients () {
  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/ad_agency/client/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.clients = response.data
    return response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
2). добавление клиента;
```
async CreateClient () {
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/ad_agency/client/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 201) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
3). изменение данных о клиенте;
```
async UpdateClient () {
  this.editedIndex = 1 // изменение параметра для корректного отображения формы изменения данных
  try {
    const response = await this.axios
      .put('http://127.0.0.1:8000/ad_agency/client/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
4). удаление клиента;
```
async DeleteClient () {
  this.editedIndex = 1
  this.dialogDelete = true
  try {
    const response = await this.axios
      .delete('http://127.0.0.1:8000/ad_agency/client/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 204) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```