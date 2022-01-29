# Chosen services

Интерфейс для просмотра, добавления, изменения, удаление записей из таблицы "Выбранные услуги".

Используемые методы: GET, POST, PUT, DELETE

Реализация методов:

1). получение данных о выбранных услугах;
```
async GetChosenServices () {
  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/ad_agency/chosenservices/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.chosenservices = response.data
    return response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
2). добавление записи о выбранных услугах;
```
async CreateChosenServices () {
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/ad_agency/chosenservices/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 201) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
3). изменение записи о выбранных услугах;
```
    async UpdateChosenServices () {
      this.editedIndex = 1
      try {
        const response = await this.axios
          .put('http://127.0.0.1:8000/ad_agency/chosenservices/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
```
4). удаление записи о выбранных услугах;
```
async DeleteChosenServices () {
  this.editedIndex = 1
  this.dialogDelete = true
  try {
    const response = await this.axios
      .delete('http://127.0.0.1:8000/ad_agency/chosenservices/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 204) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
5). получение данных об услугах для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о выбранных услугах(ServicesPL, пункт 1);

6). получение данных о заявках для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о выбранных услугах(Request, пункт 1).