# Executor

Интерфейс для просмотра, добавления, изменения, удаление записей из таблицы "Исполнители".

Используемые методы: GET, POST, PUT, DELETE

Реализация методов:

1). получение данных об исполнителе;
```
async GetExecutors () {
  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/ad_agency/executor/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.executors = response.data
    return response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
2). добавление исполнителя;
```
async CreateExecutor () {
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/ad_agency/executor/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 201) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
3). изменение данных об исполнителе;
```
async UpdateExecutor () {
  this.editedIndex = 1
  try {
    const response = await this.axios
      .put('http://127.0.0.1:8000/ad_agency/executor/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
4). удаление исполнителя;
```
async DeleteExecutor () {
  this.editedIndex = 1
  this.dialogDelete = true
  try {
    const response = await this.axios
      .delete('http://127.0.0.1:8000/ad_agency/executor/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 204) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```