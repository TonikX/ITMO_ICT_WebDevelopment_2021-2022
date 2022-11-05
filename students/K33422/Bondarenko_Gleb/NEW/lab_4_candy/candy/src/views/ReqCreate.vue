<template>
  <div class="add">
    <div style="text-align: right;">
          <v-app-bar
      app
      color="orange"
    >
      <v-app-bar-title>
        <h3 class="text-h4 white--text">Конфетное королевство</h3>
      </v-app-bar-title>
    </v-app-bar>
      <v-btn color=accent @click='$router.go(-1)' elevation="4">Отмена</v-btn>
    </div>
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Добавить заказ</h2>
    <br>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Сласти"
            v-model="addForm.candies"
            :items="candies"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="option in rooms" :key="option.id">
              {{ option.label }}
            </option>
          </v-select>
          <v-select
            label="Клиент"
            v-model="addForm.client"
            :items="clients"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="option in clients" :key="option.id">
              {{ option.label }}
            </option>
          </v-select>
          <div>
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              no-title
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="addForm.id_req"
                  label="Айди"
                  prepend-icon="mdi-calendar"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="addForm.check_in"
                :active-picker.sync="activePicker"
                @change="save"
              ></v-date-picker>
            </v-menu>
          </div>
          <div>
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              no-title
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="addForm.req_date"
                  label="Дата заказа"
                  prepend-icon="mdi-calendar"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="addForm.req_date"
                :active-picker.sync="activePicker"
                @change="save"
              ></v-date-picker>
            </v-menu>
          </div>
          <v-btn color="secondary" @click="create">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'RequestCreate',
  data: () => ({
    candies: [],
    client: [],
    addForm: {
      candies: '',
      client: '',
      id_req: '',
      req_date: ''
    }
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/candy/clients/')
      .then((res) => {
        const data = res.data
        for (let i = 0; i < res.data.length; i++) {
          const label = `${data[i].last_name} ${data[i].first_name}`
          const id = data[i].id
          this.clients.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/candy/candies/')
      .then((res) => {
        const data = res.data
        for (let i = 0; i < res.data.length; i++) {
          const label = data[i].number
          const id = data[i].id
          this.rooms.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async create () {
      await this.axios
        .post('http://127.0.0.1:8000/candy/req/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/req')
    }
  }
}
</script>
