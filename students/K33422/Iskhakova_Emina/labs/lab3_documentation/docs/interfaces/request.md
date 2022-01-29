# Request

Интерфейс для просмотра, добавления, изменения, удаление записей из таблицы "Заявки".

Используемые методы: GET, POST, PUT, DELETE

Реализация методов:

1). получение данных о заявках;
```
async GetRequests () {
  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/ad_agency/request/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.requests = response.data
    return response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
2). добавление заявки;
```
async CreateRequest () {
  this.matchStatus()
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/ad_agency/request/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 201) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
3). изменение данных о заявке;
```
async UpdateRequest () {
  this.editedIndex = 1
  this.matchStatus() // сопоставление значения статуса и ключа
  try {
    const response = await this.axios
      .put('http://127.0.0.1:8000/ad_agency/request/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
4). удаление заявки;
```
async DeleteRequest () {
  this.editedIndex = 1
  this.dialogDelete = true
  try {
    const response = await this.axios
      .delete('http://127.0.0.1:8000/ad_agency/request/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 204) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
5). получение данных о заявках в соответствии с выбранными фильтрами;
```
async GetFiltered () {
  let filterUrl
  filterUrl = ''
  if (this.filter.status) {
    filterUrl += 'status=' + this.filter.status
  }
  if (this.filter.legal_entity) {
    if (filterUrl !== '') {
      filterUrl += '&'
    }
    filterUrl += 'legal_entity=' + this.filter.legal_entity
  }
  if (this.filter.from_date) {
    if (filterUrl !== '') {
      filterUrl += '&'
    }
    filterUrl += 'from_date=' + this.filter.from_date
  }
  if (this.filter.to_date) {
    if (filterUrl !== '') {
      filterUrl += '&'
    }
    filterUrl += 'to_date=' + this.filter.to_date
  }

  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/ad_agency/request/' + '?' + filterUrl, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.requests = response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
6). получение данных о клиентах для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о заявке(Client, пункт 1)