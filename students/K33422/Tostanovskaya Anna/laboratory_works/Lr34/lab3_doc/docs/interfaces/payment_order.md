# Payment Order

Интерфейс для просмотра, добавления, изменения, удаление записей из таблицы "Платежное поручение".

Используемые методы: GET, POST, PUT, DELETE

Реализация методов:

1). получение данных о платежных поручениях;
```
async GetPaymentOrder () {
  try {
    const response = await this.axios
      .get('http://127.0.0.1:8000/ad_agency/paymentorder/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    this.paymentorders = response.data
    return response.data
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
2). добавление записи о платежных поручениях;
```
async CreatePaymentOrder () {
  try {
    const response = await this.axios
      .post('http://127.0.0.1:8000/ad_agency/paymentorder/create/', { req: this.editedItem.req, client: this.editedItem.client, invoice: this.editedItem.invoice, pay_date: this.editedItem.pay_date }, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 201) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
3). изменение записи о платежных поручениях;
```
async UpdatePaymentOrder () {
  this.editedIndex = 1
  try {
    const response = await this.axios
      .put('http://127.0.0.1:8000/ad_agency/paymentorder/' + this.editedItem.id + '/', { req: this.editedItem.req.id, client: this.editedItem.client.id, invoice: this.editedItem.invoice.id, pay_date: this.editedItem.pay_date }, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 200) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
4). удаление записи о платежных поручениях;
```
async DeletePaymentOrder () {
  this.editedIndex = 1
  this.dialogDelete = true
  try {
    const response = await this.axios
      .delete('http://127.0.0.1:8000/ad_agency/paymentorder/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

    if (response.status !== 204) {
      throw new Error(response.status)
    }
    window.location.reload()
  } catch (e) {
    console.error('AN API ERROR', e)
  }
},
```
5). получение данных о клиентах для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о платежных поручениях(Client, пункт 1);

6). получение данных о заявках для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о платежных поручениях(Request, пункт 1);

7). получение данных о счетах на оплату для последующего использования в [v-select](https://vuetifyjs.com/en/api/v-select/) при создании, изменении записи о платежных поручениях(Invoice, пункт 1).