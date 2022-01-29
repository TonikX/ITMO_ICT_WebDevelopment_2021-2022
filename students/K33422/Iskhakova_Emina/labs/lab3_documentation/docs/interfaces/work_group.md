# Work Group

Интерфейс для просмотра, добавления, изменения, удаление записей из таблицы "Рабочие группы".

Используемые методы: GET, POST, PUT, DELETE

Реализация методов:

1). получение данных о рабочих группах;
```
async GetWorkGroup () {
  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/ad_agency/workgroup/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.workgroups = response.data
    return response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
2). добавление записи о рабочей группе;
```
async CreateWorkGroup () {
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/ad_agency/workgroup/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 201) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
3). изменение записи о рабочей группе;
```
async UpdateWorkGroup () {
  this.editedIndex = 1
  try {
    const response = await this.axios
      .put('http://127.0.0.1:8000/ad_agency/workgroup/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
4). удаление записи о рабочей группе;
```
async DeleteWorkGroup () {
  this.editedIndex = 1
  this.dialogDelete = true
  try {
    const response = await this.axios
      .delete('http://127.0.0.1:8000/ad_agency/workgroup/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 204) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
5). получение данных об исполнителях для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о рабочих группах(Executor, пункт 1);

6). получение данных о заявках для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о рабочих группах(Request, пункт 1).