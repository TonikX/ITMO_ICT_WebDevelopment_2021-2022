<template>
  <div class="home">
    <h3 v-if="!isAuth">Access is restricted! Please log in or register.</h3>
    <v-col><h3 v-if="isAuth">Welcome!</h3></v-col>
    <v-col><v-btn v-if="isAuth" @click='$router.push("/deputy")' elevation="4">Home</v-btn></v-col>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data: () => ({
    isAuth: ''
  }),
  created () {
    this.isAuth = localStorage.getItem('token') !== null && localStorage.getItem('token') !== undefined
    console.log(this.isAuth, localStorage.getItem('token'), this.axios.defaults.headers.common.Authorization)
  }
}
</script>
