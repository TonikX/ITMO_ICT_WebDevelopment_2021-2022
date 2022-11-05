<template>
  <v-container>
     <v-app-bar
      app
      color="orange"
    >
      <v-app-bar-title>
        <h3 class="text-h4 white--text">Конфетное королевство</h3>
      </v-app-bar-title>
    </v-app-bar>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/lable.png')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>
      <v-col>
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            Добро пожаловать в магазин Конфетное королевство!<br>
          </h1>
            Чтобы продолжить, пожалуйста, зарегистрируйтесь и войдите на сайт.
        </v-col>
        <v-col>
            <v-btn color=orange @click='$router.push("/sign-in/")'>Войти</v-btn>
        </v-col>
        <v-col>
            <v-btn color=orange @click='$router.push("/sign-up/")'>Зарегистрироваться</v-btn>
        </v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'HomeView',
  data: () => ({
    isAuth: ''
  }),
  created () {
    this.isAuth = localStorage.getItem('token') !== null && localStorage.getItem('token') !== undefined
    console.log(this.isAuth, localStorage.getItem('token'), this.axios.defaults.headers.common.Authorization)
  }
}
</script>
