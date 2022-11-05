<template>
  <div>
        <v-app-bar
      app
      color="orange"
    >
      <v-app-bar-title>
        <h3 class="text-h4 white--text">Конфетное королевство</h3>
      </v-app-bar-title>
    </v-app-bar>
    <br>
    <div align="center">
      <b-table>
        <h2 class="display-1 font-weight-bold mb-3">Список заказов</h2>
        <br>
        <tr>
          <td><strong>Айди</strong></td>
          <td><strong>Клиент</strong></td>
          <td><strong>Сласти</strong></td>
          <td><strong>Дата заказа</strong></td>
        </tr>
        <tr v-for="elem in request" :key="elem.id">
          <td>{{ elem.id_req }}</td>
          <td>{{ elem.client }}</td>
          <td>{{ elem.candies }}</td>
          <td>{{ elem.req_date }}</td>
        </tr>
      </b-table>
      <br>
      <v-col>
        <v-btn color="orange" @click='$router.push("/req/create/")'>Добавить заказ</v-btn>
      </v-col>
    </div>
  </div>
</template>

<script>

export default {
  name: 'ReqView',
  components: {
  },
  data: () => ({
    request: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/candy/request/')
      .then((res) => {
        this.request = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
}

</script>

<style>
  td {
    text-align: left;
    padding: 0.8rem;
  }
</style>
