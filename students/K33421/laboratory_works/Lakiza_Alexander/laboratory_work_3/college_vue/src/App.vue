<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <h1 class="headline">College App</h1>
        <v-col v-if='isAuth'><a @click="logout" style="color: white; text-decoration: underline">LogOut</a></v-col>
        <v-col v-if="!isAuth">
          <router-link to="/signin" style="color: white">SignIn</router-link>
        </v-col>
        <v-col v-if="!isAuth">
          <router-link to="/signup" style="color: white">SignUp</router-link>
        </v-col>
      </div>
    </v-app-bar>

    <v-main class="my-5 px-5">
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    isAuth: ''
  }),
  created () {
    this.isAuth = localStorage.getItem('token') !== null && localStorage.getItem('token') !== undefined
    if (localStorage.getItem('token')) {
      this.axios.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`
    }
    console.log(this.isAuth, localStorage.getItem('token'), this.axios.defaults.headers.common.Authorization)
  },
  methods: {
    logout () {
      console.log(localStorage.getItem('token'))
      localStorage.removeItem('token')
      console.log(localStorage.getItem('token'))
      delete this.axios.defaults.headers.common.Authorization
      window.location.href = 'http://localhost:8080/'
    }
  }
}
</script>
