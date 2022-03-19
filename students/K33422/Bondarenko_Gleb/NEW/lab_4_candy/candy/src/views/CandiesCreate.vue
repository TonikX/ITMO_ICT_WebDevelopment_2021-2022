<template>
  <div class="add">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.push("/candies")' elevation="4">Отмена</v-btn>
    </div>
              <v-app-bar
      app
      color="orange"
    >
      <v-app-bar-title>
        <h3 class="text-h4 white--text">Конфетное королевство</h3>
      </v-app-bar-title>
    </v-app-bar>
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Добавить сласть</h2>
    <br>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Айди"
            v-model="addForm.id_candy"
          />
          <v-text-field
            label="Тип"
            v-model="addForm.type"
          />
          <v-text-field
            label="Описание"
            v-model="addForm.description"
          />
          <v-text-field
            label="Цена"
            v-model="addForm.price"
          />
          <v-btn color="secondary" @click="add">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'CandiesCreate',
  data: () => ({
    addForm: {
      id_candy: '',
      type: '',
      description: '',
      price: ''
    }
  }),
  methods: {
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/candy/candies/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.push('/candies/')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>
