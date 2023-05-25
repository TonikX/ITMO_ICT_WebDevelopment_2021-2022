# Invoice

Интерфейс для просмотра, добавления, изменения, удаление записей из таблицы "Счет на оплату".

Используемые методы: GET, POST, PUT, DELETE

Реализация методов:

1). получение данных о счетах на оплату;
```
async GetInvoice () {
  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/ad_agency/invoice/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.invoices = response.data
    return response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
2). добавление записи о счете на оплату;
```
async CreateInvoice () {
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/ad_agency/invoice/create/', JSON.stringify({ req: this.editedItem.req, client: this.editedItem.client, pay_due: this.editedItem.pay_due }), { headers: { Authorization: 'Token ' + localStorage.getItem('token'), 'Content-Type': 'application/json' } })

    if (response.status !== 201) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
3). изменение записи о счете на оплату;
```
async UpdateInvoice () {
  this.editedIndex = 1
  try {
    const response = await this.axios
      .put('http://127.0.0.1:8000/ad_agency/invoice/' + this.editedItem.id + '/', { req: this.editedItem.req.id, client: this.editedItem.client.id, pay_due: this.editedItem.pay_due }, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
4). удаление записи о счете на оплату;
```
async DeleteInvoice () {
  this.editedIndex = 1
  this.dialogDelete = true
  try {
    const response = await this.axios
      .delete('http://127.0.0.1:8000/ad_agency/invoice/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 204) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
5). получение данных о клиентах для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о счетах на оплату(Client, пункт 1);

6). получение данных о заявках для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о счетах на оплату(Request, пункт 1).