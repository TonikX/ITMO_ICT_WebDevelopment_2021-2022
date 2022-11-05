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
        <h2 class="display-1 font-weight-bold mb-3">Сласти</h2>
        <br>
        <tr>
          <td><strong>Айди</strong></td>
          <td><strong>Тип</strong></td>
          <td><strong>Описание</strong></td>
          <td><strong>Цена</strong></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr v-for="elem in candies" :key="elem.id">
          <td>{{ elem.id_candy }}</td>
          <td>{{ elem.type }}</td>
          <td>{{ elem.description }}</td>
          <td>{{ elem.price }}</td>
          <td>
            <v-btn color="orange" @click='$router.push(`/candies/update/${ elem.id }/`)'>Редактировать</v-btn>
          </td>
          <td>
            <v-btn color="orange" @click="deleteElem(elem.id)">Удалить</v-btn>
          </td>
        </tr>
      </b-table>
      <br>
      <v-col>
        <v-btn color="orange" @click='$router.push("/candies/create/")'>Добавить сласть</v-btn>
      </v-col>
    </div>
  </div>
</template>

<script>

export default {
  name: 'CandiesView',
  components: {
  },
  data: () => ({
    candies: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/candy/candies/')
      .then((res) => {
        this.candies = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/candy/candies/update/${elem}/`)
        .then((res) => {
          console.log(res)
          this.$router.go(0)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
  td {
    text-align: left;
    padding: 0.8rem;
  }
</style>
