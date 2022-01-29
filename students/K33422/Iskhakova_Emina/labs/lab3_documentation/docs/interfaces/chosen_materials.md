# Chosen materials

Интерфейс для просмотра, добавления, изменения, удаление записей из таблицы "Выбранные материалы".

Используемые методы: GET, POST, PUT, DELETE

Реализация методов:

1). получение данных о выбранных материалах;
```
async GetChosenMaterials () {
  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/ad_agency/chosenmaterials/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.chosenmaterials = response.data
    return response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
2). добавление записи о выбранных материалах;
```
async CreateChosenMaterials () {
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/ad_agency/chosenmaterials/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 201) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
3). изменение записи о выбранных материалах;
```
async UpdateChosenMaterials () {
  this.editedIndex = 1
  try {
    const response = await this.axios
      .put('http://127.0.0.1:8000/ad_agency/chosenmaterials/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
4). удаление записи о выбранных материалах;
```
async DeleteChosenMaterials () {
  this.editedIndex = 1
  this.dialogDelete = true
  try {
    const response = await this.axios
      .delete('http://127.0.0.1:8000/ad_agency/chosenmaterials/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 204) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
5). получение данных о материалах для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о выбранных материалах(MaterialsPL, пункт 1);

6). получение данных о заявках для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о выбранных материалах(Request, пункт 1).