<template>
<div style='text-align: center;'>
<v-app>
    <v-app-bar
      app
      color='black'
      dark
    >
    <v-btn @click="gohome()"
        text
      >
        <span class="mr-2">Home</span>
    </v-btn>
    <v-spacer></v-spacer>
    <v-btn @click="goLogout()"
        text
      >
        <span class="mr-2">Log out</span>
      </v-btn>
      </v-app-bar>
      <br><br><br><br>
  <input v-model="login" placeholder="Login"/><br>
  <input v-model="first_name" placeholder="First Name"/><br>
  <input v-model="last_name" placeholder="Last Name"/><br>
  <input v-model="tel" placeholder="Phone Number"/><br>
  <input v-model="password" type=password placeholder="Password"/><br>
  <button @click="edit">Enter</button>
  </v-app>
</div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Edit',
  data () {
    return {
      login: '',
      password: '',
      first_name: '',
      last_name: '',
      tel: ''
    }
  },
  methods: {
    goLogout () {
      sessionStorage.removeItem('auth_token')
      window.location = '/'
    },
    gohome () {
      this.$router.push({ name: 'Home' })
    },
    edit () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/me/',
        headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') },
        type: 'PATCH',
        data: {
          username: this.login,
          password: this.password,
          first_name: this.first_name,
          last_name: this.last_name,
          tel: this.tel
        },
        success: (response) => {
          alert('Your profile has been changed')
          this.$router.push({ name: 'Home' })
        },
        error: (response) => {
          alert('Something went wrong, please, try again')
          console.log(response)
        }
      })
    }
  }
}
</script>

<style>
</style>
